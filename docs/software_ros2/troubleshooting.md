### Network 
In case you can't receive or send messages over your network, go through these checks:

1. Do your robot and computer have the same [ROS_DOMAIN_ID](https://docs.ros.org/en/foxy/Concepts/About-Domain-ID.html)?
2. Does your firewall block communication? Maybe you need to open ports?
    ```sh
    sudo ufw allow in proto udp to 224.0.0.0/4
    sudo ufw allow in proto udp from 224.0.0.0/4
    ```
3. Is multicasting enabled in your network interfaces? Is multicasting enabled in your router? Check by using the [multicast](https://index.ros.org/p/ros2multicast/) package.


### Motors

In case you are getting errors from the helmoro_motor_controls and the Roboclaw Motor Controllers are not working, go through the following quick checks:

1. Check if the port name of both Roboclaws appear when plugin in, the USB by typing `ls /dev/ttyACM*`
2. Check if you have the authority to write to this port. Otherwise type `chmod 666 <portname>` in order to add the authority.
3. Also, when connecting the motors with two USB cables, it can happen that the portnames of the left and the right roboclaw motor controller swap (`/dev/ttyACM0` <-> `/dev/ttyACM1`). Since, to this point their USB ports are not fixed. If this happens, simply swap the two addresses for the left and the right controller specified in the param file.