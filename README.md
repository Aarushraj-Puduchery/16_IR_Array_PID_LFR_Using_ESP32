# 16_IR_Array_PID_LFR_Using_ESP32

This is my Second Attempt to make a Line Follower Bot, I tried to correct the mistakes I made in my first LFR and here we go This is my new 16 IR Sensor Line Follower Bot using ESP32.

Why ESP32 because it has a High Clock Speed.

A line follower bot is a type of autonomous robotic vehicle designed to follow a predefined path or track marked with contrasting lines, typically black on a light-coloured surface or vice versa. These robots employ a combination of sensors, such as infrared or optical sensors, to detect the contrast between the line and the surrounding area. By continuously analyzing the sensor data, the bot makes real-time decisions on how to adjust its wheels or propulsion system to stay centred on the line.

Line follower bots are popular in robotics competitions and educational settings, as they provide an engaging way to introduce students and enthusiasts to basic robotics principles, sensor technology, and programming. They serve as a fundamental example of closed-loop control systems and can be customized with various features, like obstacle avoidance and speed adjustments, to make them more versatile and adaptable to different scenarios. Line follower bots can be a great starting point for those interested in exploring the world of robotics and automation.

A PID Line Follower Bot using an ESP32 Microcontroller is a small autonomous robot that uses infrared sensors to follow a designated path. It employs a PID (Proportional-Integral-Derivative) control algorithm to continuously adjust its motor speeds based on sensor feedback, maintaining alignment with the path. The Pico microcontroller processes the sensor data and sends control signals to the motors, allowing the bot to track lines, it is a popular choice for educational robotics projects and competitions.

## LFR Images

|![Top View](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/4624c483-891d-458d-989e-ea01030e3924)|![Bottom View](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/5f545651-995a-4b07-9590-7b90890e553b)|
|---|---|
|![Left view](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/477f90f3-51c8-4de5-b0b8-dcf42f1aa284)|![Right View](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/40b418bb-8b40-4596-b7e4-01b5e652d84b)|

## Schematic Diagram

![Schematic_New-16-ir-array-PID-LFR](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/344165c8-0f2f-4e1e-8dd3-d19a2d06db26)

## Chassis Design

|![Components Placement](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/5c989853-6f5d-4ec2-aad2-74fcdeb39957)|![LFR Chassic](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/d56f45e6-06ae-4b1b-80c6-f39473f7865e)|
|---|---|

## Wheels Design

|![image](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/5f4f8897-9e08-4237-aa2d-c794d512c211)|![image](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/ededa547-ae68-4a39-9364-f201fa81f4df)|
|---|---|
|![image](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/74f2307e-fbc9-46b6-be2f-e7825873b10a)|![image](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/b13db7ee-9d44-4180-9c50-1c8a47e61c2c)|

>[!NOTE]
>Wheels Design Files are Uploaded and Can be 3D Printed Directly.

## Menu Graphic

|![Start](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/4846a1b8-f431-4558-b08a-dfa423befb6e)|![Settings](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/96eae412-999c-4ceb-a8cf-7e0800f1fc22)|![Kp](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/44a41a0b-8cfa-48e9-987d-21ffa6e8dc9d)|
|---|---|---|
|![Kd](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/e53380b4-74c8-43b0-bfbd-a85b8ec86bf7)|![Calibrate](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/38b9aeda-b972-4bf8-89bc-53f35eba7cb1)|![Sensor Values](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/5f8b2d97-d66c-4411-b7ee-69568664586b)|
|![Run](https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/55dc97ee-4e88-4dc0-b00d-3ac03a3de556)|

## Dry Run Video

https://github.com/Aarushraj-Puduchery/16_IR_Array_PID_LFR_Using_ESP32/assets/97360295/b0accbfe-f4fa-431e-92e3-81439fa5fb1b

## Components List
|S.No|  Name  | Cost | Quantity | Total Cost | Link |
|---| --- | --- | --- | --- | --- |
|1| ESP32 38 pin Development Board | ₹463.00 | 1 | ₹463.00 | https://robu.in/product/esp32-38pin-development-board-wifibluetooth-ultra-low-power-consumption-dual-core/ |
|2| TCRT5000 - Reflective Infrared Optical Sensor | ₹14.00 | 16 | ₹84.00 | https://www.electronicscomp.com/tcrt-5000-reflective-infrared-optical-sensor?gad_source=1&gclid=CjwKCAjw8diwBhAbEiwA7i_sJXOqHk0dZvL_GnIE0G32WTJIGomgZAWdONYpeRQPgrdWhnDTaYYXDxoCjcIQAvD_BwE |
|3| CD74HC4067 16 Channel Multiplexer | ₹47.00 | 1 | ₹47.00 | https://www.electronicscomp.com/cd74hc4067-16-channel-multiplexer-breakout-board-module-india?gad_source=1&gclid=CjwKCAjw8diwBhAbEiwA7i_sJbTI_0htwSTLoZ-y8TKZmN8GVIqDA2loj_VPuERGRcLqPaKO2KgiRhoCEmwQAvD_BwE |
|4| N20-12V-1000 Rpm Micro Metal Gear Motor DC Encoder | ₹448.00 | 2 | ₹1792.00 | https://robokits.co.in/motors/n20-metal-gear-micro-motors/n20-metal-gear-encoder-motor/ga12-n20-12v-1000-rpm-all-metal-gear-micro-dc-encoder-motor-with-precious-metal-brush |
|5| TB6612FNG Dual Channel Motor Driver | ₹349.00 | 1 | ₹349.00 | https://www.robojunkies.com/products/tb6612fng-dual-channel-motor-driver-breakout |
|6| Mounting Bracket for N20 Micro Gear motors | ₹29.00 | 2 | ₹58.00 | https://robu.in/product/mounting-bracket-n20-micro-gear-motors/?gclid=CjwKCAjwv-2pBhB-EiwAtsQZFMyVAIrgacEo3SnLeiZb_c0rmLDukQiCUuQzv2EGzwINDnRaVgi07hoCHJsQAvD_BwE |
|7| Mini MP1584 DC-DC 3A Adjustable Buck module | ₹48.00 | 1 | ₹48.00 | https://robu.in/product/mini-mp1584-dc-dc-adjustable-buck-module-3a/ |
|8| N20 mini-vacuum steel-ball caster wheel | ₹75.00 | 1 | ₹75.00 | https://robu.in/product/ball-castors/?gclid=CjwKCAjwv-2pBhB-EiwAtsQZFJapkUm2pvyraM-fcvEbIFXAwsW7BcBFXMhT8CuGdiMnjmRCqo3y5RoCfbwQAvD_BwE |
|9| Orange 850mah 3S 30C/60C (11.1V) Lithium Polymer Battery Pack | ₹999.00 | 1 | ₹999.00 | https://robu.in/product/orange-850mah-3s-30c-60c-lithium-polymer-battery-pack-lipo/ |
|10| Nylon XT60 Connectors Male/Female (1 pairs) | ₹69.00 | 1 | ₹69.00 | https://robu.in/product/amass-nylon-xt60-connectors-male-female-pair/ |
|11| Cricket Bat Grip | ₹100.00 | 1 | ₹100.00 | Local Shop |
|12| 1.3 inch 128×64 White OLED Display | ₹359.00 | 1 | ₹359.00 | https://robu.in/product/1-3-inch-i2c-iic-oled-lcd-module-4pin-with-vcc-gnd-white/ |
|13| 5 x 7 cm Universal PCB Prototype Board Single-Sided 2.54mm Hole Pitch | ₹33.00 | 2 | ₹66.00 | https://robu.in/product/5-x-7-cm-universal-pcb-prototype-board-single-sided-2-54mm-hole-pitch/?gclid=CjwKCAjwv-2pBhB-EiwAtsQZFE5b9qHKxeqy_LWVFsEkEtWvAuZyjGFokjC_KK8nJEzkA3N0C3TE_xoCRrgQAvD_BwE | 
|14| 3 Pin SPDT Toggle switch | ₹70.00 | 1 | ₹70.00 | https://robu.in/product/5a-3-pin-spdt-toggle-switch/ |
|15| Tactile Push Button | ₹5.00 | 6 | ₹30.00 | https://robu.in/product/12x12x7-3mm-tactile-push-button-switch-round/ |
|16| Female Header pins | ₹20.00 | 5 | ₹100.00 | https://robu.in/product/2-54mm-1x40-pin-female-single-row-header-strip-pack-of-10/?gclid=CjwKCAjwv-2pBhB-EiwAtsQZFAtwQ3ul10GUEYZ4OoZSfY7DK1FfVSDdqT6manq-n7lpXNj7vYUe9xoCQpQQAvD_BwE |
|17| Laser Cutting For Chassis | ₹205.00 | 1 | ₹205.00 | https://robu.in/product/online-laser-cutting-service/?utm_source=website&utm_medium=header&utm_campaign=laser-cutting-service&utm_id=free_promotion |
|18| 4mm SPDT 1P2T Slide Switch | ₹5.00 | 2 | ₹10.00 | https://robu.in/product/4mm-spdt-1p2t-slide-switch-pack-of-10/?gad_source=1&gclid=CjwKCAjw8diwBhAbEiwA7i_sJdteHYWvkgwv5K-RXt2dMcR4QeJUNp-5dkLhoCquk7IZ7fX7WUhKhxoC30YQAvD_BwE |
|19| 10k resistor 1/4W | ₹0.50 | 22 | ₹11.00 | https://robu.in/product/10k-ohm-0-25w-metal-film-resistor-pack-of-100/ |
|20| 220 resistor 1/4W | ₹0.50 | 16 | ₹8.00 | https://robu.in/product/220-ohm-resistor-0-25w-metal-film-pack-of-100/ |

> [!NOTE]
> Components price may vary.

## Source Code
1. `main.py` file which contains the basic setup and Run.
2. `bitmap.py` file contains all the menu graphics.
3. `KpValue.csv` and `KdValue.csv` are the files which store the kp and kd values.
4. `ssd1106.py` file is the library used for Oled display.
5. `framebuf.py` file is the library used for displaying graphics on Oled display.

>[!IMPORTANT]
>All the Files must be saved on the ESP32 Memory.

