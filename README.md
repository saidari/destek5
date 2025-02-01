# TurtleBot3 Go To Point
Bu paket TurtleBot3 robotunun Gazebo üzerinde belirlenen bir hedefe gitmesini sağlayan bir ROS2 Python düğümü içerir.

# Kurulum

1) ROS2 Humble ve TurtleBot3 paketlerinin kurulu olduğundan emin olun. Gazebo'nun kurulu olduğundan emin olun.

2) Bir ROS2 çalışma alanında bu dosyaları kullanın.

3) Çalışma alanınızı derleyin

cd ~/ros2_ws
colcon build --packages-select turtlebot3_go_to_point
source install/setup.bash

# Kullanım

1) Gazebo Ortamını TurtleBot3 ile Başlatın

ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

2) Ayrı bir terminalde düğümü çalıştırın

source ~/ros2_ws/install/setup.bash
ros2 run turtlebot3_go_to_point go_to_point

# Notlar

Robot, go_to_point.py içinde belirlenen target_x ve target_y konumuna doğru ilerleyecek ve yeterince yaklaştığında duracaktır.

TurtleBot3 modelini (burger, waffle vb.) ayarlamak için:

echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc









