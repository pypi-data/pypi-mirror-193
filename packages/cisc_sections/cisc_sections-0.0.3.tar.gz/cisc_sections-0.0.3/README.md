<!--- Heading --->
<div align="center">
  <img src="assets/banner.png" alt="banner" width="auto" height="auto" />
  <p>
    Python library to lookup structural steel sections from CISC manual. 
  </p>
<h4>
    <a href="https://github.com/rpakishore/steelsections-cisc/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/steelsections-cisc">Documentation</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/steelsections-cisc/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/steelsections-cisc/issues/">Request Feature</a>
  </h4>
</div>
<br />

<!-- Badges -->
[![tests](https://github.com/rpakishore/steelsections-cisc/actions/workflows/tests.yml/badge.svg)](https://github.com/rpakishore/steelsections-cisc/actions/workflows/tests.yml)

<!-- Table of Contents -->
<h2>Table of Contents</h2>

- [1. About the Project](#1-about-the-project)
  - [1.1. Screenshots](#11-screenshots)
  - [1.2. Features](#12-features)
- [2. Getting Started](#2-getting-started)
  - [2.1. Prerequisites](#21-prerequisites)
  - [2.2. Dependencies](#22-dependencies)
  - [2.3. Installation](#23-installation)
- [3. Usage](#3-usage)
- [4. Other Functions](#4-other-functions)
  - [4.1. update\_requirements.py](#41-update_requirementspy)
- [5. Modules](#5-modules)
  - [5.1. requests\_package.py](#51-requests_packagepy)
- [6. Roadmap](#6-roadmap)
- [7. FAQ](#7-faq)
- [8. License](#8-license)
- [9. Contact](#9-contact)
- [10. Acknowledgements](#10-acknowledgements)
  - [10.1. Documentation](#101-documentation)

<!-- About the Project -->
## 1. About the Project
<!-- Screenshots -->
### 1.1. Screenshots

<div align="center"> 
  <img src="https://placehold.co/600x400?text=Your+Screenshot+here" alt="screenshot" />
</div>

<!-- Features -->
### 1.2. Features

- Can lookup section properties of W, HSS, C, L and much more based on canadian CISC manual.
- Uses [forallpeople](https://github.com/connorferster/forallpeople) to return units-aware results.
- Prelim. filters to narrow down the sections returned.

<!-- Getting Started -->
## 2. Getting Started

<!-- Prerequisites -->
### 2.1. Prerequisites

### 2.2. Dependencies
The project uses the following dependencies
```
pandas>=1.5.2
forallpeople>=2.6.3
```

<!-- Installation -->
### 2.3. Installation

Install from pip as below   
```bash
pip install cisc_sections
```

Alternatively, you can compile it locally using the flit
```bash
git clone https://github.com/rpakishore/steelsections-cisc.git
cd steelsections-cisc
python -m pip install --upgrade pip
python -m pip install flit
flit install
```
<!-- Usage -->
## 3. Usage

The most basic use is just to import the library:

```python
import cisc_sections as steel
```
## 4. Other Functions
### 4.1. update_requirements.py
```bash
python update_requirements.py
```
! Be sure to run this command outside of the virtual environment

The way this script works is as follows:
- deletes the existing virtual environment
- Opens all `.py` files and checks for pip requirements
- If found, compiles the pip commands together
- Creates a new virtual env in the same directory and runs all the compiled pip commands

Inorder to ensure that all the `pip` commands are found. ensure that every time a non standard library is imported, add a line with the following in code
> #pip import XXXX

## 5. Modules
### 5.1. requests_package.py
Includes frequently used requests packages, functions, classes and defaults
The following functions are defined in the `req` class 

|Function Name| Purpose|
|-------------|--------|
|`randomize_header`|Randomize request headers by updating both referer and useragent|
|`change_useragent`|Change request useragent to random one|
|`change_referer`|Randomly set google.com as referer|
|`get_from_list`|Complete requests to a list of urls and return the list of responses|
|`get`|URL request with header randomization, timeout, proxy and retries builtin|
|`proxy_get_from_list`|Complete requests to a list of urls and return the list of responses using proxy ips|
|`proxy_get`|completes `get` request using proxies|
|`create_session`|Generate sessions object with adequate headers and adapters|



<!-- Roadmap -->
## 6. Roadmap

* [x] Set up a skeletal framework
* [ ] Todo 2

<!-- FAQ -->
## 7. FAQ
- Question 1
  + Answer 1

- Question 2
  + Answer 2

<!-- License -->
## 8. License
Distributed under the no License. See LICENSE.txt for more information.

<!-- Contact -->
## 9. Contact

Arun Kishore - [@rpakishore](mailto:rpakishore@gmail.com)

Project Link: [https://github.com/rpakishore/](https://github.com/rpakishore/)


<!-- Acknowledgments -->
## 10. Acknowledgements

### 10.1. Documentation
 - [Awesome README Template](https://github.com/Louis3797/awesome-readme-template/blob/main/README-WITHOUT-EMOJI.md)
 - [Banner Maker](https://banner.godori.dev/)
 - [Shields.io](https://shields.io/)
 - [Carbon](https://carbon.now.sh/)