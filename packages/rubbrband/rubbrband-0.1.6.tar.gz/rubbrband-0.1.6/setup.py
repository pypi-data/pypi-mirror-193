from setuptools import setup

setup(
    name="rubbrband",
    install_requires=[
        "click",
        "docker==6.0.1",
        "yaspin",
    ],
    include_package_data=True,
)
