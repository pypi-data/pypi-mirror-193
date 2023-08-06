from setuptools import setup, find_packages
from startwork.constants.__version__ import __version__

VERSION = __version__
DESCRIPTION = 'Fast change between projects'

setup(
    name="startwork",
    version=VERSION,
	entry_points={
        'console_scripts': [
            'work=startwork.main:main'
        ]
    },
    author="JorbFreire",
    author_email="",
    description=DESCRIPTION,
    include_package_data=True,
    packages=find_packages(),
    install_requires=["inquirer==3.1.2"],
    keywords=['python', 'inquirer'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ]
)
