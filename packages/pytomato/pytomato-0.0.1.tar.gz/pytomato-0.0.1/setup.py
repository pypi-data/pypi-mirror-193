# encoding:utf-8
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = '0.0.1'

setuptools.setup(
    name="pytomato",
    version=version,
    author="sunlulu.tomato",
    author_email="sunlulu.tomato@bytedance.com",
    description="python tools to accelerate development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sunlulu427/tomato",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)