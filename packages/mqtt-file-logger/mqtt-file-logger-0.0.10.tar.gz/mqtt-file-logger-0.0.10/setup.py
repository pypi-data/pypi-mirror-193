from setuptools import setup, find_packages

VERSION = '0.0.10'
DESCRIPTION = 'MQTT Logger'
LONG_DESCRIPTION = 'A package that allows to log IOT devices data on MQTT message received event'

# Setting up
setup(
    name="mqtt-file-logger",
    version=VERSION,
    author="Shaif Azad",
    author_email="<saiforahi@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'mqtt', 'iot', 'file logger'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)