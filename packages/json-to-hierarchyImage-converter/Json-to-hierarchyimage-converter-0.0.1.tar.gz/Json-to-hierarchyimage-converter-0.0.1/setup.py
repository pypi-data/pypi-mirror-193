from setuptools import setup, find_packages
import codecs
import os


# Setting up
setup(
    name="Json-to-hierarchyimage-converter",
    version="0.0.1",
    author="Pavan",
    author_email="pppawar124@gmail.com",
    description="Json to tree Hierarchy converter",
    long_description_content_type="text/markdown",
    long_description="A package to perform arithmetic operations",
    packages=find_packages(),
    install_requires=["graphviz","json"],
    keywords=['json', 'graph', 'nodeId', 'child', 'name'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
