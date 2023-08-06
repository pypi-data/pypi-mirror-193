from setuptools import setup, find_packages
from pathlib import Path

with open("README.md") as f:
    long_description = f.read()

setup(
    name="pytorch-basic-frame",
    version="0.0.3",
    author="TaoChenyue",
    author_email="3038816978@qq.com",
    description="A frame for training in pytorch",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url="https://github.com/TaoChenyue/pytorch-basic-frame",
    python_requires=">=3.8",
    packages=find_packages(exclude=["src"]),
    # py_modules=[],
    install_requires=[],
    dependency_links=[],
)
