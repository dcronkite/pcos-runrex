





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div>
  <p>
    <a href="https://github.com/kpwhri/pcos-runrex">
      <img src="images/logo.png" alt="Logo">
    </a>
  </p>

  <h3 align="center">PCOS-Runrex</h3>

  <p>
    Feature extraction for developing algorithm to identify PCOS-related cases.
    Additional steps will require use of these variables to build a predictive algorithm.
  </p>
</div>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.8+
* runrex package: https://github.com/kpwhri/runrex

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/kpwhri/pcos-runrex.git
```
2. Install requirements
```sh
pip install -r requirements.txt -r requirements-dev.txt
```
3. Run tests.
```sh
set/export PYTHONPATH=src
pytest tests
```


<!-- USAGE EXAMPLES -->
## Usage

* Build a configuration file as defined in [runrex](https://github.com/kpwhri/runrex)
    - Full details defined in that project's [schema.py](https://github.com/kpwhri/runrex/blob/master/src/runrex/schema.py)
* `python run.py runrex.conf.(py|json|yaml)`


## Variables Identified

Variables (called 'algorithms') are broken down into various 'categories'. Either can be used in building features.

|Algorithm|Category|Description|
|---|---|---|
|pcom|-|Rotterdam criteria|
|menarche|-|age at menarche|
|hyperandrogenism|-|evidence of hyperandrogenism|


## Output Format

Recommended format is `jsonl`. For more details, see [runrex](https://github.com/kpwhri/runrex).


## Versions

<!-- Uses [SEMVER](https://semver.org/). -->

Updates/changes are not expected, and each version will be related to a date/time of usage. Versioning is based on `YYYYmmm`. See https://github.com/kpwhri/pcos-runrex/releases.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/kpwhri/pcos-runrex/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` or https://kpwhri.mit-license.org for more information.



<!-- CONTACT -->
## Contact

Please use the [issue tracker](https://github.com/kpwhri/pcos-runrex/issues). 


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* This work has been funded by Bayer.





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kpwhri/pcos-runrex.svg?style=flat-square
[contributors-url]: https://github.com/kpwhri/pcos-runrex/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kpwhri/pcos-runrex.svg?style=flat-square
[forks-url]: https://github.com/kpwhri/pcos-runrex/network/members
[stars-shield]: https://img.shields.io/github/stars/kpwhri/pcos-runrex.svg?style=flat-square
[stars-url]: https://github.com/kpwhri/pcos-runrex/stargazers
[issues-shield]: https://img.shields.io/github/issues/kpwhri/pcos-runrex.svg?style=flat-square
[issues-url]: https://github.com/kpwhri/pcos-runrex/issues
[license-shield]: https://img.shields.io/github/license/kpwhri/pcos-runrex.svg?style=flat-square
[license-url]: https://kpwhri.mit-license.org/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/kaiser-permanente-washington
<!-- [product-screenshot]: images/screenshot.png -->