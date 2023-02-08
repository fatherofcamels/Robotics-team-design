import os 
import pathlib
import launch
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher, Ros2SupervisorLauncher
from webots_ros2_driver.urdf_spawner import URDFSpawner, get_webots_driver_node
from webots_ros2_driver.utils import controller_url_prefix


def get_ros2_nodes(*args):
    package_dir = get_package_share_directory('naodriver')
    robot_description = pathlib.Path(os.path.join(package_dir, 'resource', 'nao.urdf')).read_text()
    nao_description = pathlib.Path(os.path.join(package_dir, 'resource', 'nao_description.urdf')).read_text()
    #urdf Definitions
    #Name has to match up with controller name
    spawn_URDF_bobby = URDFSpawner(
        name='bobby',
        robot_description=nao_description,#This needs to be change later with a more suitable name
        relative_path_prefix=os.path.join(package_dir,'resource'),
        
    )

    bobby_driver = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        additional_env={'WEBOTS_CONTROLLER_URL': controller_url_prefix() + 'bob'},
        parameters=[
            {'robot_description': nao_description}
        ]
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            '  robot_description': nao_description
        }],
    )

    return [ 
        bobby_driver,
        spawn_URDF_bobby,
    ]




def generate_launch_description():
    package_dir = get_package_share_directory('naodriver')

    webots = WebotsLauncher(
        world=os.path.join(package_dir, 'worlds', 'world.wbt')
    )

    ros2_supervisor = Ros2SupervisorLauncher()


    return LaunchDescription([
        webots,
        
        ros2_supervisor,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())]
            )
        )
    ] + get_ros2_nodes())