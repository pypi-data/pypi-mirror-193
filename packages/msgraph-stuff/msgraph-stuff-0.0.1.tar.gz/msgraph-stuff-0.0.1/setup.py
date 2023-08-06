from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = 'Package that adds a range of functionality for working with microsoft graph api - under constant development'

with open("README.md", "r") as fh:
    long_description = fh.read()

# Setting up
setup(
    name="msgraph-stuff",
    url="https://github.com/george-oconnor/msgraph-stuff",
    version=VERSION,
    author="george.oconnor (George O' Connor)",
    author_email="<george@georgestools.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["msgraph_stuff"],
    package_dir={'': 'src'},
    install_requires=["requests"],
    keywords=['python', 'sharepoint', 'ms', 'microsoft graph', 'msgraph', 'graph', 'api', 'microsoft', 'microsoft365', 'azure', 'graph api'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ]
)