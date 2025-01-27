# Software Architecture
## High Level Overview
The following flowchart shows a high-level view of the communication in-between our packages when running the system on the robot. Naming convention in our repository may vary, as we show here the underlying algorithms of our packages, instead of the packages named by our internal company convention. In case of running the HelMoRo repository as a simulation, the four lefternmost hardware nodes are replaced by a single gazebo_ros bridge, which handles communication between ROS and the gazebo simulation engine. The internal packages are briefly explained in sections [helmoro_common](#helmoro_common), [helmoro_real](#helmoro_real) and [helmoro_sim](#helmoro_sim). External Packages are explained in section [External Packages](#external-packages). 

![This image shows the high level communication between the our ROS packages](pictures/high_level_communication.drawio.svg "High Level Communication")

## helmoro_common

In the following, each package of the Helmoro ROS architecture is explained shortly.

### bringup
- manages the launch process of the HelMoRo
- manages the launch process of RVIZ

### control
- stores parameters for diff drive controller and joint state broadcaster.

### description
- stores URDF and meshes
- publishes static transforms

### state_estimation
- uses [robot_localization](http://docs.ros.org/en/melodic/api/robot_localization/html/index.html) in the background
- combines wheel odometry and IMU information with an EKF
- publishes transform between HelMoRo and odom frame

### slam
- uses [slam_toolbox](https://docs.ros.org/en/humble/p/slam_toolbox/) in the background
- combines lidar scans and odometry pose to create a map of the environment and localizes HelMoRo within
- publishes transform between map and odom frame

## helmoro_real
### bringup
- manages the launch process of packages interfacing with IMU, camera, LIDAR and motors

### motors
- ROS2 wrapper for the motor controllers
- converts motor states into wheel odometry
- converts robot velocity commands into motor commands

#### Wiring Options

|  | Checklist | |
|  |  |  |
| Wiring  |- Wire both RoboClaws to the Jetson Nano SBC via Micro-USB to Micro-USB cable. |
| Setting | - Connect one RoboClaw to PC via USB and open it with the downloaded [BasicmicroMotionStudio](https://www.basicmicro.com/downloads) <br>- Don’t set any of the two RoboClaws to USB-TTL Relay Mode <br>- Set an address for each RoboClaw in the General Settings. Note for this wiring, the addresses can be equal since ports are different (/dev/ttyACM0 and /dev/ttyACM1 in Linux) <br>- Set Baudrate you would like to use in the General Settings. <br>- [Configure the PID values](https://resources.basicmicro.com/auto-tuning-with-motion-studio) of the RoboClaws if not yet done. <br>- Don’t forget to Device &rarr; Write Settings in the top left corner before disconnecting your RoboClaw. |

#### Troubleshooting

In case you are getting errors from this package and the Roboclaw Motor Controllers are not working, go through the following quick checks:

1. Check if the port name of both Roboclaws appear when plugin in, the USB by typing `ls /dev/ttyACM*`
2. Check if you have the authority to write to this port. Otherwise type `chmod 666 <portname>` in order to add the authority.
3. Also, when using this node with two USB cables, it can happen that the portnames of the left and the right roboclaw motor controller swap (`/dev/ttyACM0` <-> `/dev/ttyACM1`). Since, to this point their USB ports are not fixed. If this happens, simply swap the two addresses for the left and the right controller specified in the param file.


## helmoro_sim
### bringup
- manages the launch process of the gazebo simulation and spawns the robot

### gazebo_tools
- contains world files
- starts the ros-gazebo bridge

## helmoro_operations
### joymanager
- interprets joystick commands from Logitech Wireless joystick F710 controller
- scales joystick commands to desired linear and angular velocities
- publishes of velocity commands

### navigation
- uses [navigation2](https://docs.nav2.org/) in the background
- launches nodes for local and global costmap generation
- launches nodes for recovery behaviour, planning and trajectory following


## External Packages

### Camera
The [OrbbecSDK ROS2 Wrapper](https://github.com/Helbling-Technik/HelMoRo_OrbbecSDK_ROS2) provides integration of Orbbec cameras with ROS 2 environment. It supports ROS2 Foxy, Humble, and Jazzy distributions. Helmoro's camera, the Astra Pro Plus, is EoL. We created our own fork to fix a bug caused by non-existing intrinsic parameters.

### IMU
The [bno055](https://github.com/flynneva/bno055.git) package is a community created packages for interfacing with the IMU Bosch BNO055 IMU.

### LIDAR
The [rplidar_ros](https://github.com/Slamtec/rplidar_ros) packages is provided by the LIDAR manufacturer Slamtec. It supports ROS1 and ROS2.
