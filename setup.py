import setuptools
import animeX

packages = [
    'animeX'
]

with open("README", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="animeX",  # Replace with your own username
    version=animeX.__version__,
    author="Samuel Abada",
    author_email="abadasamuelosp@gmail.com",
    description="A simple, yet versatile package for downloading " \
                "anime.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mastersam07/animeX-pack",
    packages=setuptools.find_packages(),
    install_requires=[  # I get to this in a second
        "wget==3.2",
        "requests==2.21.0",
        "beautifulsoup4==4.9.0",
    ],
    scripts=['animeX/animeX.py'],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
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
