from EasyPyQt import VERSION

from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = VERSION
DESCRIPTION = "A package for PyQt template&example codes"
LONG_DESCRIPTION = "A package to generate PyQt code from .ui files, and also provide some examples such as 'Loading UI', 'Overlay UI' ... etc"

# Setting up
setup(
    name="EasyPyQt",
    version=VERSION,
    author="LeeFuuChang",
    author_email="leefuuchang@gmail.com",
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    packages=find_packages(include=("EasyPyQt", "EasyPyQt.*")),
    license="LICENSE.md",
    readme="README.md",
    keywords=["python", "PyQt5"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": [
            "epyqt = EasyPyQt.__main__:main"
        ]
    },
    python_requires=">=3.0",
    install_requires=["PySide2", "PyQt5", "pyqt5-tools"],
)