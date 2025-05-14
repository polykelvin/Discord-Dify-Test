import os
from setuptools import setup, find_packages

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="discord-tools-dify",
    version="1.0.0",
    author="Dify Plugin Developer",
    author_email="contact@example.com",
    description="A plugin that allows users to send messages to Discord and read messages from Discord channels",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/discord-tools-dify",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    package_data={
        "discord_tools_dify": ["manifest.json"],
    },
    entry_points={
        "console_scripts": [
            "discord-tools-dify=discord_tools_dify.server:main",
        ],
    },
)