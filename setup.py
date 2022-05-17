from setuptools import setup, find_packages

setup(
    name="sb-unfurl",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["requests", "sanic"],
)
