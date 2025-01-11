from setuptools import find_packages, setup

package_name = 'pyqt_ros'

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
    maintainer='ynu',
    maintainer_email='kb2002091437@gmail.com',
    description='ROS2 package with PyQt button GUI',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = pyqt_ros.gui_publisher:main',
            'stop_publisher = pyqt_ros.gui_stop_publisher:main',
        ],
    },
)
