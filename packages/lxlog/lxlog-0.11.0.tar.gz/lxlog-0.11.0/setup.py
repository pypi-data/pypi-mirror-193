import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="lxlog",
    version="0.11.0",
    author="selvaguru",
    author_email="your_email@example.com",
    long_description=long_description,
    description="A package for analyzing system log files",
    long_description_content_type="text/markdown",
    url="https://selvaguru-s.web.app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

