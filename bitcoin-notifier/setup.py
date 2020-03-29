from setuptools import setup


# function to open & read the README.md file
def readme():
    with open('README.md') as f:
        README = f.read()
    return README


# this part contains details of the package/module like which license, version of python, libraries, etc
# that are needed for running  the package also info about the author
setup(
    name="bitcoin-notifier",
    version="0.0.3",
    description="A Python package to get bitcoin updates and predictions",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/anik-ghosh-au7/bitcoin_notifier",
    author="Anik Ghosh",
    author_email="tech.anikghosh@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["bitcoin_notifier"],
    include_package_data=True,
    install_requires=["requests", "datetime"],
    entry_points={
        "console_scripts": [
            "bitcoin-notifier=bitcoin_notifier.cli:main",
        ]
    },
)
