# Robotics-team-design
### Github Repository for ENG5325(2023): Robocup Challenge

### Run Simulation in WeBots

1. Open WeBots
	```sh
	webots
	```
2. Go to File -> Open World ...
3. Go to Basic__1 -> worlds , and open test_world.wbt


### Install Webots ROS 2 Driver

```sh
	sudo apt-get install ros-$ROS_DISTRO-webots-ros2
	```

### Launch Package
1. change to package folder
from repository directory
```sh
	cd ros2_ws/src/nao_driver
	```
2. Source package

```sh
	source install/local_setup.bash
	```

3. Launch Package
```sh
	ros2 launch naodriver robot_launch.py
	```
