#
## Installation on the PC
1. Install [ROS Humble](https://docs.ros.org/en/humble/Installation.html)

2. Create a workspace and clone our repository. For better readability we created the workspace in this guide within the home directory and named the workspace ros2_ws. But feel free to choose another directory and workspace name.

    ```sh
    mkdir ~/ros2_ws/src
    cd ~ros2_ws/src
    git clone https://github.com/Helbling-Technik/HelMoRo-software-ROS2.git
    ```

3. Install dependencies

    ```sh
    cd ~/ros2_ws
    sudo apt-get update
    rosdep install --from-path src -yi
    ```

4. Source ROS and build the HelMoRo software package

    ```sh
    source /opt/ros/humble/setup.bash
    cd ~/ros2_ws
    colcon build --symlink-install
    ```

5. Your folder structure should now look like this
    ```sh
    ~/ros2_ws
    ├── build
    ├── install
    ├── log
    └── src
        └── HelMoRo-software-ROS2
    ```

## Installation on the robot
1. Install [ROS Humble](https://docs.ros.org/en/humble/How-To-Guides/Installing-on-Raspberry-Pi.html)

2. Create a workspace and clone our repository. For better readability we created the workspace in this guide within the home directory and named the workspace ros2_ws. But feel free to choose another directory and workspace name.

    ```sh
    mkdir ~/ros2_ws/src
    cd ~ros2_ws/src
    git clone https://github.com/Helbling-Technik/HelMoRo-software-ROS2.git
    ```

3. Clone the repo for communication with the lidar, IMU and camera

    ```sh
    git clone https://github.com/flynneva/bno055.git
    git clone -b ros2 https://github.com/Slamtec/rplidar_ros.git
    git clone https://github.com/Helbling-Technik/HelMoRo_OrbbecSDK_ROS2.git
    ```

4. Install dependencies

    ```sh
    cd ~/ros2_ws
    sudo apt-get update
    rosdep install --from-path src -yi
    ```

5. Your folder structure should now look like this
    ```sh
    ~/ros2_ws
    ├── build
    ├── install
    ├── log
    └── src
        ├── bno055
        ├── HelMoRo_OrbbecSDK_ROS2
        ├── HelMoRo-software-ROS2
        └── rplidar_ros
    ```
