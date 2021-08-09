from setuptools import setup

setup(
    name="dmc",
    version="0.1",
    author="alfredo.leon",
    description="This is the second project for Udacity's Data Engineering Nanodegree.",
    install_requires=[
        "pandas",
        "jupyter",
        "cassandra-driver",
        "tqdm"
    ]
)