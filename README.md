<div align="center">
  <p align="center">
	  <a href="https://pypi.org/project/animeX/"><img src="https://img.shields.io/pypi/v/animeX?color=blue" alt="version"></a>
	  <a href="https://pypi.python.org/pypi/animeX/"><img src="https://img.shields.io/pypi/pyversions/animeX.svg"  alt="pyversions"/></a>
	  <a href='https://animex-pack.readthedocs.io/en/latest/?badge=latest'><img src='https://readthedocs.org/projects/animex-pack/badge/?version=latest' alt='Documentation Status' />
</a>
  </p>
</div>

# animeX-pack

A lightweight Python library (and command-line utility) for downloading anime.

## Table of Contents
* [Installation](#installation)
* [Quick start](#quick-start)
* [Features](#features)
* [Usage](#usage)
* [Command-line interface](#command-line-interface)
* [Development](#development)
* [GUIs and other libraries](#guis-and-other-libraries)

## Installation

Download using pip via pypi.

```bash
$ pip install animeX
```
(Mac/homebrew users may need to use ``pip3``)

## Quick start
```sh
 py -m animeX --version
 py -m animeX --name AnimeName
```
A GUI frontend for animeX is not yet available.
A Windows executable for animeX is available at [AnimeX](https://github.com/LordGhostX/animeX-v2)

## Features
* Ability to Capture Thumbnail URL.
* Extensively Documented Source Code
* No Third-Party Dependencies
* Saves video to local device

## Usage

Let's begin with showing how easy it is to download a video with animeX:

```sh
 py -m animeX -h
 py -m animeX --version
```
This example will download boruto, its highest quality available.

```sh
 py -m animeX --name boruto
```

## Command-line interface

animeX ships with a simple CLI interface for downloading anime.

The complete set of flags are:

```sh
usage: animeX [-h] [--version] [--name AnimeName]

Command line application to download anime.

positional arguments:
  --name AnimeName      The name of the anime you want to download

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
```

## Development

<a href="https://app.codacy.com/manual/Mastersam07/animeX-pack?utm_source=github.com&utm_medium=referral&utm_content=Mastersam07/animeX-pack&utm_campaign=Badge_Grade_Dashboard"><img src="https://api.codacy.com/project/badge/Grade/7278736b380645a3ae47bc0e5953ee90"/></a>
<a href="https://github.com/ambv/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" /></a>

<p>Pull requests are welcome. For major changes and feature request, please consider going <a href="https://github.com/LordGhostX/animeX-v2">here</a> and open an issue first to discuss what you would like to change.</p>
<p>For bug fixes to the command line application or enhancements, open an issue first to discuss what you would like to change.</p>

To run code checking before a PR use ``make test``

### Virtual environment

Virtual environment is setup with [pipenv](https://pipenv-fork.readthedocs.io/en/latest/) and can be automatically activated with [direnv](https://direnv.net/docs/installation.html)

#### Code Formatting

This project is linted with [pyflakes](https://github.com/PyCQA/pyflakes), formatted with [black](https://github.com/ambv/black), and typed with [mypy](https://mypy.readthedocs.io/en/latest/introduction.html)

#### Code of Conduct

Treat other people with helpfulness, gratitude, and consideration! See the [Python Community Code of Conduct](https://www.python.org/psf/codeofconduct/).

## GUIs and other libraries
