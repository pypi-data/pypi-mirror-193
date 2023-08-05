from setuptools import setup

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="reisinger_drive",
    packages=["reisingerdrive"],
    install_requires=["aiohttp>=3.0.6", "async_timeout>=3.0.0"],
    version="0.2.1",
    description="A python3 library to communicate with a Reisinger Drive System",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.5.3",
    author="sreisi",
    author_email="",
    url="https://github.com/sreisi/reisinger-drive-api",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
