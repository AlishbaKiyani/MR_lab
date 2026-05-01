from setuptools import find_packages, setup

package_name = 'lab5_slam'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alishbakiyani',
    maintainer_email='alishbakiyani75@gmail.com',
    description='Lab 5 SLAM tasks',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'cmd_pub = lab5_slam.cmd_vel_publisher:main',
            'odom_sub = lab5_slam.odom_subscriber:main',
        ],
    },
)
