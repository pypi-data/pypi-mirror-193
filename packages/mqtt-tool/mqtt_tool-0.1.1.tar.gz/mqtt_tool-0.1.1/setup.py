from setuptools import setup, find_packages

setup(
    name='mqtt_tool',
    version='0.1.1',
    packages=find_packages(),
    url='https://your_package_url.com',
    license='LICENSE.txt',
    author='Leo',
    author_email='52guhaha@gmail.com',
    description='a simple mqtt tool',
    long_description=open('README.md').read(),
    install_requires=[
        'paho-mqtt',
    ],
)
