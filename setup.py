from setuptools import find_packages, setup

setup(
    name='postbot',
    packages=['postbot'],
    version='0.1.0',
    description='A simple tool to make posts on Instagram programmatically',
    author='TG',
    license='MIT',
    keywords=(
        "postbot python instagram post automation \
         marketing promotion bot selenium"
    ),
    install_requires=["selenium>=3.141.0", "mysql-connector-python>=8.0.22"],
    python_requires=">=3, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    platforms=["win32", "linux", "linux2", "darwin"],
)