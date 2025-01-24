# Detailed Usage

In the following, it is explained how to use the Helmoro ROS architecture. Under `helmoro_description/launch/` you will find several launch files:

- helmoro.launch: Default launch file for Helmoro
- gmapping_helmoro.launch: Used for [gmapping](#slam-using-gmapping)
- nav_helmoro.launch: Used for the [Navigation Stack](#autonomous-navigation-using-the-navigation-stack)
- explore_helmoro.launch: Used for [explore_lite](#autonomous-slam-using-explore_lite)
- showcase_helmoro.launch: Used for the [showcase](#showcase)

In the following, only the usage on the main launch file, **helmoro.launch**, on which all other launch files depend on, is explained. However using the other launch files works analogously. Head to the linked sections to discover more about the purpose and usage of the other launch files.

## Run  

The main launch file to run all the required nodes of the Helmoro ROS architecture is **helmoro.launch** in the package **helmoro_description**.


In order to run Helmoro form a remote PC, you can use ssh as described in the following command.

```sh
ssh <username>@<IP-address>
```

Thereby, type in the username and instead of "IP" type in the IP-address of your Helmoro. Using this command, you can remotely log into the terminal of the Helmoro SBC and thus launch helmoro.launch from your remote device.

Once connected to helmoro via ssh, run the launch file with the following commands:

```sh
roslaunch helmoro_description helmoro.launch
```

### Running ROS across Multiple Machines

In some cases, you want to run ROS across multiple machines for example to visualize the published data of Helmoro externally on RViZ. To do so, you can open up two windows in the terminal of one of your machines and connect one of your terminals via ssh to the other machine. Select one machine to run your master on. In our case, this would be the Helmoro. This is where you would start your roscore or a launch file such as helmoro.launch.

A common problem, that occurs is that the machines cannot resolve each others hostname into an IP-address. Check if the IP-address of each machine is visible by typing:

```sh
echo $ROS_IP
```

If there is no IP-address showing up, you can set ROS_IP in each machine environment before starting a node by typing:

```sh
export $<Your_IP>
```

You can also use the following script in each terminal, after you filled in the required values

```sh
#!/bin/bash

source /opt/ros/noetic/setup.bash

# select workspace
source /home/$USER/<Your catkin workspace>/devel/setup.bash

# set IP of localhost, ethernet or wifi for using remote roscore
ip_temp=$(hostname -I)
#my_ip = localhost
my_ip=${ip_temp% }

# set IP of roscore
roscore_ip=$my_ip

export ROS_IP=$my_ip
export ROS_HOSTNAME=$my_ip
export ROS_MASTER_URI=http://$roscore_ip:11311

```

Then, enter the following commands in both terminals:

```sh
export ROS_MASTER_URI=http://<IP_of_Master>:11311
```

Thereby, type in the IP-address of your master-machine instead of <IP_of_Master>.

For further testing, you can use the [rostopic](http://wiki.ros.org/rostopic) tool on all machines that are connected to the master. Using the command
`rostopic list` you should get a list of all available topics. In wireless networks, which our Helmoro uses, it is sometimes necessary to check if there is a connection and messages still come.
You can do so by echoing a published topic.

```sh
rostopic echo /topic_name
```

If you are in the HTKZ lab network you can look for Helmoro's IP [here](http://intranet/grpit/DHCP_HTKZ-Labor.asp)

For further reference head to [ROS MultipleMachines](http://wiki.ros.org/ROS/Tutorials/MultipleMachines) and [ROS NetworkSetup](http://wiki.ros.org/ROS/NetworkSetup).

### Run RViZ with a config file

In order to run RViZ as a standalone directly with the custom config file, type in:

```sh
rosrun rviz rviz -d `rospack find helmoro_description`/rviz/rviz_config.rviz
```

## Arguments

You can pass several arguments to the **helmoro.launch** and other launch files, when running it using:

```sh
roslaunch helmoro_description helmoro.launch arg_name:=value
```

### Usage Arguments

The most important arguments for usage are depicted in the following table.

| Parameter       | Default    | Definition                                                       |
| --------------- | ---------- | ---------------------------------------------------------------- |
| is_real_robot   | true       | Switch to use real robot or gazebo simulation                    |
| use_rviz        | false      | Switch to use rviz for visualization also activates the joystick |
| use_joystick    | = use_rviz | Switch to use joystick                                           |
| use_lidar       | true       | Switch to use lidar                                              |
| use_rgbd_camera | true       | Switch to use rgbd camera                                        |

### RVIZ Arguments

| Parameter        | Default          | Definition               |
| ---------------- | ---------------- | ------------------------ |
| rviz_config_file | rviz_config.rviz | Default rviz config file |

### Gazebo Arguments

| Parameter    | Default                                          | Definition                                                          |
| ------------ | ------------------------------------------------ | ------------------------------------------------------------------- |
| paused       | false                                            | Switch if gazebo is started running or in paused mode               |
| use_sim_time | true                                             | Switch if simulated gazebo time or real time is used for simulation |
| gui          | false                                            | Switch if gui of gazebo is displayed                                |
| world        | helmoro_gazebo_plugin/worlds/helmoro_wohnung_mob | Default testing world that is loaded for gazebo simulation          |

### Common commands

To run Helmoro in simulation (in Gazebo) you can call this command on your local computer:

```sh
roslaunch helmoro_description showcase_helmoro.launch is_real_robot:=false use_rviz:=true use_gui:=true
```

You then can add a box into the environment and let Helmoro pick it up. Be reminded that in simulation helmoro does not have a fork (but he can push around objects) and that the odometry is better then in reality.

To run the required nodes for the showcase on Helmoro you can run:

```sh
roslaunch helmoro_description showcase_helmoro.launch
```

Additionally, the above written command to call rviz on your local computer

```sh
rosrun rviz rviz -d `rospack find helmoro_description`/rviz/rviz_config.rviz
```

You then also need to start the joystick node (on your computer) with:

```sh
 roslaunch helmoro_joymanager joymanager.launch
```

Make sure to connect the joystick to your computer

#### Advanced usage or tuning

If you want to tune the parameters of amcl or the navigation stack, while Helmoro is running you can open the dynamic reconfigure plugin after running:

```sh
rosrun rqt_gui rqt_gui
```