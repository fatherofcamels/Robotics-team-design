import os
from setuptools import setup
from glob import glob


package_name = 'naodriver'
data_files = [
    ('share/ament_index/resource_index/packages',['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    (os.path.join("share", package_name), glob('launch/*launch.py')),
    (os.path.join("share", package_name), glob('worlds/*.wbt'))
]
data_files.append(('share/' + package_name + '/worlds', [
    'worlds/world.wbt',]))


for (path, _, sub_folder) in os.walk('resource'):
    for filename in sub_folder:
        if filename != package_name:  # do not add the empty 'package_name' file
            data_files.append((os.path.join('share', package_name, path), [os.path.join(path, filename)]))


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,   
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='abubakar',
    maintainer_email='ayusuf13@hotmail.co.uk',
    description='NaoDriver',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension':['launch_ros = launch_ros'],
        'console_scripts':[
            'my_robot_driver = naodriver.my_robot_driver:main'
        ]

    }
)
