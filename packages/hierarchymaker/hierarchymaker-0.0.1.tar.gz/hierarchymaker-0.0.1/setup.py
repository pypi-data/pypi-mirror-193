from setuptools import setup, find_packages

# Setting up
setup(
    name="hierarchymaker",
    version="0.0.1",
    author="Pavan Pawar",
    author_email="pppawar124@gmail.com",
    description="Json to tree Hierarchy converter",
    long_description_content_type="text/markdown",
    long_description="A package to Plot the nodes based on type in the attached hierarchy JSON to an image so that "
                     "when humans try to look at it it will be much easier for them to debug.",
    packages=find_packages(),

    license="MIT",
    keywords=['json', 'graph', 'nodeId', 'child', 'name'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],

    python_requires=">=3.8",

)
