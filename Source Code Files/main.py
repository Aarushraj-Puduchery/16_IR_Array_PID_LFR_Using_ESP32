#Simple Line Following Code using PID

from machine import Pin,PWM,I2C,ADC
from utime import sleep,sleep_ms,ticks_ms
import machine
import sh1106
import framebuf
import bitmap
machine.freq(240000000)

# Define pin numbers connected to buttons
UP = 35  # Up Button
DP = 34  # Down B
LP = 32  # Left B
RP = 39  # Right Button
SP = 33  # Select Button
BP = 13  # Back Button

UB = Pin(UP,Pin.IN)
DB = Pin(DP,Pin.IN)
LB = Pin(LP,Pin.IN)
RB = Pin(RP,Pin.IN)
SB = Pin(SP,Pin.IN)
BB = Pin(BP,Pin.IN)

count1,count2,count3 = 0,0,0
pr1 = 0
pr2,pr3 = 0,0
detime = 0
detime2 = 0
UBv,DBv,LBv,RBv,SBv,BBv = 0,0,0,0,0,0

def callback(pin):
    global count1,count2,count3,pr1,pr2,pr3,detime,detime2,UBv,DBv,LBv,RBv,SBv,BBv
    if str(pin) == "Pin(35)" and (ticks_ms() - detime > 300):
        count1 = count1 + 1
        UBv = 1
        print("UB")
        detime = ticks_ms()
    
    elif str(pin) == "Pin(34)" and (ticks_ms() - detime > 300):
        count1 = count1 - 1
        DBv = 1
        print("DB")
        detime = ticks_ms()

    elif str(pin) == "Pin(32)" and (ticks_ms() - detime > 300):
        count2 = count2 + 1
        LBv = 1
        print("LB")
        detime = ticks_ms()
        
    elif str(pin) == "Pin(39)" and (ticks_ms() - detime > 300):
        count2 = count2 - 1
        RBv = 1
        print("RB")
        detime = ticks_ms()
        
    elif str(pin) == "Pin(33)" and (ticks_ms() - detime2 > 300):
        count3 = count3 + 1
        SBv = 1
        print("SB")
        detime2 = ticks_ms()
        
    elif str(pin) == "Pin(13)" and (ticks_ms() - detime > 300):
        count3 = count3 - 1
        BBv = 1
        print("BB")
        detime = ticks_ms()


UB.irq(trigger=Pin.IRQ_FALLING, handler=callback)
DB.irq(trigger=Pin.IRQ_FALLING, handler=callback)
LB.irq(trigger=Pin.IRQ_FALLING, handler=callback)
RB.irq(trigger=Pin.IRQ_FALLING, handler=callback)
SB.irq(trigger=Pin.IRQ_FALLING, handler=callback)
BB.irq(trigger=Pin.IRQ_FALLING, handler=callback)

#Oled Display
sda=Pin(21)
scl=Pin(22)
i2c = I2C(0, scl=scl, sda=sda, freq=400000)
oled = sh1106.SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)
oled.sleep(False)



#Motors
MAF = Pin(17,Pin.OUT)
MAR = Pin(16,Pin.OUT)
MBF = Pin(5,Pin.OUT)
MBR = Pin(18,Pin.OUT)
MAC = PWM(Pin(4))
MBC = PWM(Pin(19))

MAC.freq(1000)
MBC.freq(1000)

# Define pins for multiplexer control
sensor_value = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
s0 = Pin(25, Pin.OUT)
s1 = Pin(26, Pin.OUT)
s2 = Pin(27, Pin.OUT)
s3 = Pin(14, Pin.OUT)

# Define analog input pin
analog_pin = Pin(12)


maxvalue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
minvalue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
threshold = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sensor_val = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sensor_arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ir_val = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
mode = -1

isBlackLine = 1
P, D, I, PIDvalue = 0,0,0,0
PreviousError = 0
error = 0.0
sensorWeight = [ 9, 7, 5, 4, 3, 2, 1, 0, 0, -1, -2, -3, -4, -5, -7, -9 ]
lfSpeed = 36000
currentSpeed = 35000
activeSensors = 0
op = 0

KpFile = open("kpfile.csv","r")
Kp = float(KpFile.read())
KdFile = open("kdfile.csv","r")
Kd = float(KdFile.read())
KpFile.close()
KdFile.close()
Ki = 0

def read_ir_sensor(channel):
    s0.value(channel & 0x01)
    s1.value((channel >> 1) & 0x01)
    s2.value((channel >> 2) & 0x01)
    s3.value((channel >> 3) & 0x01)
    sleep_ms(1)  # Wait for the channel to settle
    adc = ADC(analog_pin)
    adc.atten(ADC.ATTN_11DB)
    return adc.read()

def motor1run(motorSpeed):
    if (motorSpeed > 0):
        MAF.value(1)
        MAR.value(0)
        MAC.duty_u16(int(motorSpeed))
    elif(motorSpeed < 0):
        MAF.value(0)
        MAR.value(1)
        MAC.duty_u16(abs(int(motorSpeed)))
    else:
        MAF.value(1)
        MAR.value(1)
        MAC.duty_u16(0)

def motor2run(motorSpeed):
    if (motorSpeed > 0):
        MBF.value(1)
        MBR.value(0)
        MBC.duty_u16(int(motorSpeed))
    elif(motorSpeed < 0):
        MBF.value(0)
        MBR.value(1)
        MBC.duty_u16(abs(int(motorSpeed)))
    else:
        MBF.value(1)
        MBR.value(1)
        MBC.duty_u16(0)

def calibrate():
    motor1run(0)
    motor2run(0)
    fbuf = framebuf.FrameBuffer(bitmap.calibrate_text, 128, 64, framebuf.MONO_HLSB)
    oled.fill(0)
    oled.blit(fbuf, 0, 0, 0)          
    oled.show()
    #step 1: fill the min and max list with current values
    for i in range(16):
        minvalue[i] = read_ir_sensor(i)
        maxvalue[i] = read_ir_sensor(i)

    #step 2: sort the max and min values of all sensors by moving the bot left and right
    for j in range(80):
        motor1run(27000)
        motor2run(-27000)
        for i in range(16):
            if(read_ir_sensor(i) < minvalue[i]):
                minvalue[i] = read_ir_sensor(i)
            if(read_ir_sensor(i) > maxvalue[i]):
                maxvalue[i] = read_ir_sensor(i)

    #step 3: calculate the threshold values
    print("threshold")
    for i in range(16):
        threshold[i] = (minvalue[i] + maxvalue[i])/2
        print(threshold[i],end=" ")
    motor1run(0)
    motor2run(0)

def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    
def readline():
    global onLine,isBlackLine,minvalue,maxvalue
    onLine = 0
    for i in range(16):
        if(isBlackLine):
            sensor_val[i] = convert(read_ir_sensor(i), minvalue[i], maxvalue[i], 0, 1000)
        else:
            sensor_val[i] = convert(read_ir_sensor(i), minvalue[i], maxvalue[i], 1000, 0)
        
        sensor_val[i] = min(max(sensor_val[i], 0), 1000)
        sensor_arr[i] = sensor_val[i] < 450
        if(sensor_arr[i]):
            onLine = 1
            
        if(isBlackLine == 1 and sensor_arr[i]):
            onLine = 1
        if(isBlackLine == 0 and not(sensor_arr[i])):
            onLine = 1

def linefollow():
    global error,activeSensors,P,I,D,PIDvalue,PreviousError,lsp,Kp,Ki,Kd,rsp
    error=0
    activeSensors = 0
    for i in range(16):
        error = error + (sensorWeight[i] * sensor_arr[i] * (1000 - sensor_val[i]))
        activeSensors += sensor_arr[i]
    
    error = error/activeSensors
    
    P = error
    I = I + error
    D = error - PreviousError
    
    PIDvalue = (Kp * P) + (Ki * I) + (Kd * D)
    PreviousError = error
    
    lsp = currentSpeed - PIDvalue
    rsp = currentSpeed + PIDvalue
    
    fbuf = framebuf.FrameBuffer(bitmap.letgo_text, 128, 64, framebuf.MONO_HLSB)
    oled.fill(0)
    oled.blit(fbuf, 0, 0, 0)
    oled.text("lsp = ",0,40)
    oled.text("rsp = ",0,50)
    oled.text(str(lsp),45,40)
    oled.text(str(rsp),45,50)
    oled.show()
    
    if(lsp > 65535):
        lsp = 65535
    if(lsp < 0):
        lsp = 0
    if(rsp > 65535):
        rsp = 65535
    if(rsp < 0):
        rsp = 0
    motor1run(lsp);
    motor2run(rsp);
    
def ir_show():
    global ir_val
    for i in range(1,17):
        if (i <= 8):
            oled.text(str(i),((8*(i-1))-1),55)
        else:
            oled.text(str(17 - i),(8*(i-1)-1),55)
        oled.show()
    while True:
        oled.fill_rect(0,0,128,45,0)
        for i in range(16):
            ir_val[i] = convert(read_ir_sensor(i), minvalue[i], maxvalue[i], 1, 45)
            ir_val[i] = min(max(ir_val[i],1),45)
        for i in range(16):
            oled.fill_rect((i)*8,0,6,45,1)
            oled.fill_rect((i)*8,0,6,45 - ir_val[i],0)
        oled.show()
        if SBv == 1:
            break

    
def setup_val():
    global count1,count2,count3,Kp,Kd,UBv,DBv,LBv,RBv,SBv,BBv,mode,op
    menu = [bitmap.start_menu, bitmap.setting_menu]
    fbuf = framebuf.FrameBuffer(menu[count1], 128, 64, framebuf.MONO_HLSB)
    oled.blit(fbuf, 0, 0, 0)          
    oled.show()
    oled.fill(0)
    if BBv == 1:
        fbuf = framebuf.FrameBuffer(menu[count1], 128, 64, framebuf.MONO_HLSB)
        oled.blit(fbuf, 0, 0, 0)    
        oled.show()
        BBv = 0
        
    if (UBv == 1) or (DBv == 1):
        count1 = (count1) % len(menu)
        oled.fill(0)
        fbuf = framebuf.FrameBuffer(menu[count1], 128, 64, framebuf.MONO_HLSB)
        oled.blit(fbuf, 0, 0, 0)
        oled.show()
        UBv, DBv = 0,0
    if count1 == 0 and SBv == 1:
        mode = 1
    if count1 == 1 and SBv == 1:
        count1 = 0
        SBv = 0
        oled.fill(0)
        oled.show()
        while True:
            setting = [bitmap.Kp_menu,bitmap.Kd_menu]
            settingfile = ["kp","kd"]
            fbuf = framebuf.FrameBuffer(setting[count1], 128, 64, framebuf.MONO_HLSB)
            oled.fill(0)
            oled.blit(fbuf, 0, 0, 0)          
            oled.show()
            if (UBv == 1) or (DBv == 1):
                count1 = (count1) % len(setting)
                fbuf = framebuf.FrameBuffer(setting[count1], 128, 64, framebuf.MONO_HLSB)
                oled.fill(0)
                oled.blit(fbuf, 0, 0, 0)          
                oled.show()
                UBv, DBv = 0,0
                op = count1
            
            if SBv == 1:
                count1 = 0
                oled.fill(0)
                BBv = 0
                while True:
                    SBv = 0
                    if UBv == 1 or DBv == 1:
                        count1 = max(-3,min(count1,4))
                        UBv, DBv = 0,0
                        oled.fill(0)
                    oled.text(str(10**(-1*count1)),55,40)
                    oled.show()
                    KpFile = open(settingfile[op]+"file.csv","r")
                    Kp = float(KpFile.read())
                    KpText = str(Kp)
                    oled.text(KpText, 35, 18)
                    oled.show()
                    KpFile.close()
                    if LBv == 1:
                        Kp = (Kp - (1*pow(10,-1*count1)))
                        KpFile = open(settingfile[op]+"file.csv","r+")
                        KpFile.seek(0)
                        KpText = str(Kp)
                        KpFile.write(KpText)
                        KpFile.close()
                        oled.text(KpText, 35, 18)
                        oled.show()
                        oled.fill(0)
                        LBv = 0
                    if RBv == 1:
                        Kp = (Kp + (1*pow(10,-1*count1)))
                        KpFile = open(settingfile[op]+"file.csv","r+")
                        KpFile.seek(0)
                        KpText = str(Kp)
                        KpFile.write(KpText)
                        KpFile.close()
                        oled.text(KpText, 35, 18)
                        oled.show()
                        oled.fill(0)
                        RBv = 0
                    if BBv == 1:
                        oled.fill(0)
                        oled.text(settingfile[count1], 0, 0)
                        oled.show()
                        BBv = 0
                        break      
            if BBv == 1:
                BBv = 0
                break
       

while True:
    setup_val()
    if mode == 1:
        mode = 0
        break

oled.fill(0)
KpFile = open("kpfile.csv","r")
KpT = float(KpFile.read())
KpText = str(KpT)
KdFile = open("kdfile.csv","r")
KdT = float(KdFile.read())
KdText = str(KdT)
oled.text("Kp", 50, 0)
oled.text((KpText), 22, 20)
oled.text("Kd", 50, 35)
oled.text((KdText), 22, 55)
oled.show()
KpFile.close()
KdFile.close()
SBv = 0
while SBv == 0:
    pass
calibrate()
SBv = 0
BBv = 0
while SBv == 0:
    ir_show()
    motor1run(0)
    motor2run(0)

SBv = 0
fbuf = framebuf.FrameBuffer(bitmap.letgo_text, 128, 64, framebuf.MONO_HLSB)
oled.fill(0)
oled.blit(fbuf, 0, 0, 0)          
oled.show()
while True:
    readline()
#     if (currentSpeed < lfSpeed):
#         currentSpeed = currentSpeed + 4
    if (onLine == 1):
        linefollow()
    else:
        if error > 0:
            motor1run(-40000)
            motor2run(lsp)
        else:
            motor1run(rsp)
            motor2run(-40000)



