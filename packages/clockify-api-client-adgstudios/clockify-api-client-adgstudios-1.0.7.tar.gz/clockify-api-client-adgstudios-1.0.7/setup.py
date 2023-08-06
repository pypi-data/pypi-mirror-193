from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='clockify-api-client-adgstudios',
    version='1.0.7',
    author="Michael Bláha, Ashlin Darius Govindasamy",
    author_email="michael.blaha@eluvia.com, adg@adgstudios.co.za",
    description="Simple python API client for clockify. Inspired by https://pypi.org/project/clockify/library.",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eluvia-com/clockify-api-aclient",
    install_requires=['requests', 'factory_boy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={"dev": ["twine"]}
)
