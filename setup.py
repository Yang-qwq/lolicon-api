# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="lolicon-api",
    version="1.0.0",
    author="Yang",
    author_email="yang_qwq@qq.com",
    description="A API library that allow you requests lolicon api easier",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Yang-qwq/lolicon-api",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=[
        "requests>=2.32.4",
    ],
)