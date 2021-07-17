import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="oxfordpy",
    version="1.0.0",
    description="Oxford dictionary python library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/spacesudo/oxfordpy",
    author="Chidera",
    author_email="chiderankem2@gmail.com",
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=["oxfordpy"],
    include_package_data=True,
    install_requires=["requests"],
    keywords='Oxford, dictionary, development',

    python_requires='>=3.6, <4',
    
)