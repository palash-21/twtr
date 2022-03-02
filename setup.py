from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="twtr",
    version="0.0.1",
    author="palash",
    author_email="palashpathak.21@gmail.com",
    description="Twitter data processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/palash-21/twtr",
    project_urls={
        "Bug Tracker": "https://github.com/palash-21/twtr/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=('tests')),
    python_requires=">=3.6",
)