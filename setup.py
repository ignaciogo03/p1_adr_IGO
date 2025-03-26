from setuptools import find_packages, setup

<<<<<<< HEAD
package_name = 'prueba2_py'
=======
package_name = 'prueba_py'
>>>>>>> 337fcb21265e2fd43ce492e0a672553bd23c683a

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
    maintainer='iganan',
    maintainer_email='iganan@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
<<<<<<< HEAD
            'service = prueba2_py.service_member_function:main',
            'client = prueba2_py.client_member_function:main',
=======
                'talker = prueba_py.publisher_member_function:main',
                'listener = prueba_py.subscriber_member_function:main',
>>>>>>> 337fcb21265e2fd43ce492e0a672553bd23c683a
        ],
    },
)
