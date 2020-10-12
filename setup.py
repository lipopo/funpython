#!/bin/python

from setuptools import setup, find_packages

version = "1.0"

require_packages = [
    "opencv-python",
    "click",
]

setup(
    name = "funpython",
    author = "lipo",
    install_requires = require_packages,
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            "paint_img=funypy.a_paint.aPaint:cli",
            "code_dot=funypy.code_dot.code_dot:main"
        ]
    }
)
