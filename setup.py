import codecs
import os

import setuptools
import animeX.utils as utils

packages = [
    'animeX'
]


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


setuptools.setup(
    name="animeX",  # Replace with your own username
    version=utils.get_version(),
    author="Samuel Abada",
    author_email="abadasamuelosp@gmail.com",
    description="A simple, yet versatile package for downloading " \
                "anime.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/mastersam07/animeX-pack",
    packages=setuptools.find_packages(),
    install_requires=[  # I get to this in a second
        "wget==3.2",
        "requests==2.21.0",
        "beautifulsoup4==4.9.0",
    ],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Multimedia :: Video"
    ],
    python_requires='>=3.6',
    keywords=["anime", "download", "video", ],
)
