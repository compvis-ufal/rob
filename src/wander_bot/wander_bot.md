# wander_bot

## Setup environment variables
export TURTLEBOT_GAZEBO_WORLD_FILE=/opt/ros/melodic/share/turtlebot3_gazebo/worlds/turtlebot3_world.world
export TURTLEBOT3_MODEL=waffle_pi

## Start framework
roscore
roslaunch turtlebot3_gazebo turtlebot3_world.launch
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping

## Run Python scripts
./red_light_green_light.py
rostopic list
rostopic echo /cmd_vel

## Read Laser Scan

- Directly from terminal
rostopic echo scan

- Using a script (play around with the robot and check the updated measurement, check lower and upper bounds [0.2, inf])
./range_ahead.py

