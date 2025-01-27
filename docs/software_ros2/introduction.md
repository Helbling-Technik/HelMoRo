# Introduction

This section aims to explain and document the code necessary to run HelMoRo. All the relevant computation, that allows Helmoro to navigate autonomously, happens on board using ROS 2.

Helmoro is equipped with the following electronic parts:

- 4 DC-Motors and 4 angular encoders
- 4 2 [Roboclaw Motor Controllers](https://www.basicmicro.com/Roboclaw-2x7A-Motor-Controller_p_55.html) to control their motion.
- 1 Lidar ([RPLidar Slamtec](https://www.slamtec.com/en/Lidar/A2))
- 1 RGB-D camera ([Orbbec Astra Pro](https://orbbec3d.com/product-astra-pro/))
- 1 IMU ([Adafruit BNO055 Absolut Orientation](https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor))
- 1 [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) with [Ubuntu 22.04](https://ubuntu.com/download/raspberry-pi)

![helmoro_intro](pictures/helmoro_intro.png)

The following capabilites have been tested within simulation and on the physical robot:

- Video, map and position streaming to local computer
- Remote joystick control
- Autonomous Navigation to set goal positions
- Remote controlled mapping
- Autonomous mapping
