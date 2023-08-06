from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="azure_logging",
    version="0.0.1",
    # author="Adrian Bartsch",
    # author_email="adrian.bartsch@marxkrontal.com",
    description="Template for PyPI packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_namespace_packages(include=["azure_logging", "azure_logging.*"]),
    install_requires=[],
    classifiers=[],
    python_requires=">=3.8"
)