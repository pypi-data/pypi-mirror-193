import setuptools

import os

try:
    with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''



setuptools.setup(
    name="lxlog",
    version="0.7.0",
    author="selvaguru",
    author_email="your_email@example.com",
    description="This Package to see system log with Date Range and Process",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://selvaguru-s.web.app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

