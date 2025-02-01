from setuptools import setup

package_name = 'turtlebot3_go_to_point'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='said',
    maintainer_email='said@rover.com',
    description='A simple node to move TurtleBot3 to a goal position',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Komut adı = 'python dosyası içindeki fonksiyon'
            'go_to_point = turtlebot3_go_to_point.go_to_point:main',
        ],
    },
)

