<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
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


<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Better Banner Registration</h3>

  <p align="center">
    A simple tool to optimize the speed of course registration on Self-Service Banner (SSB).
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Banner registration is a stressful time for many college students. With limited seats in popular classes and a large number of students trying to register at the same time, the process can be slow and frustrating. Better Banner Registration is a tool designed to optimize the speed of course registration on Self-Service Banner (SSB) by automating the process and reducing the time it takes to register for classes.

Just collect your course registration numbers (CRNs) and Better Banner Registration will make it as fast as possible to register for your classes when registration opens. With Better Banner Registration, you can increase your chances of getting into the classes you want and reduce the stress of registration day.

Tired of spamming copy and paste for each class like everyone else? With Better Banner Registration you navigate the registration form, the tool handles the CRN input, preventing the waste of precious seconds spent highlight, copying then clicking back into the banner registration form. This tool allows you to register for classes in a fraction of the time it would take to do it manually, giving you a competitive edge in securing your spot in the classes you need. For a standard 5-course (15-credit) schedule, Better Banner Registration can bring the registration time down to well under 15 seconds, but speeds such as these are not guaranteed depending on outside factors such as internet connectivity, pre-script navigation of the registration system, class availability, and user error. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![uv][uv]][uv-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* uv - [Installation Instructions](https://github.com/astral-sh/uv#installation)

### Installation

1. Get your CRNs ready. You can find these on your institution's course catalog or registration page. They are typically 5-digit numbers that uniquely identify each course section.
2. Clone the repo
   ```sh
   git clone https://github.com/lefkovitzj/BetterBannerRegistration.git
   ```
3. Install dependencies with uv
   ```sh
   uv sync
   ```
4. Duplicate the `.env.example` file and enter your list of CRNs in `.env`
   ```sh
   cp .env.example .env
   # open .env and add your CRNs to the CRN_LIST variable, then save and close the file
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

After completing the installation steps, you can run the tool with the following command:

```sh
uv run main.py
```

While the program is running, pressing the 'F8' key will begin the automated registration process. The tool will automatically insert the CRNs you provided in the `.env` file into the registration form, allowing you to register for your classes much faster than doing it manually. All you have to do is open the page, switch to the "Enter CRN s" tab, press F8 and then submit the form after your CRNs have been entered. The tool will handle the rest, allowing you to quickly register for your classes and increase your chances of getting into the classes you want.

The program will continue to run until you choose to exit the program by pressing `CTRL+C` in the terminal window where you ran the `uv run main.py` command.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Joseph Lefkovitz - [@lefkovitzj](https://github.com/lefkovitzj) - contact@lefkovitzj.com

Project Link: [https://github.com/lefkovitzj/BetterBannerRegistration](https://github.com/lefkovitzj/BetterBannerRegistration)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/lefkovitzj/BetterBannerRegistration.svg?style=for-the-badge
[contributors-url]: https://github.com/lefkovitzj/BetterBannerRegistration/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/lefkovitzj/BetterBannerRegistration.svg?style=for-the-badge
[forks-url]: https://github.com/lefkovitzj/BetterBannerRegistration/network/members
[stars-shield]: https://img.shields.io/github/stars/lefkovitzj/BetterBannerRegistration.svg?style=for-the-badge
[stars-url]: https://github.com/lefkovitzj/BetterBannerRegistration/stargazers
[issues-shield]: https://img.shields.io/github/issues/lefkovitzj/BetterBannerRegistration.svg?style=for-the-badge
[issues-url]: https://github.com/lefkovitzj/BetterBannerRegistration/issues
[license-shield]: https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge
[license-url]: https://github.com/lefkovitzj/BetterBannerRegistration/blob/main/LICENSE.txt
[product-screenshot]: images/screenshot.png
<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[uv]: https://img.shields.io/badge/uv-000000?style=for-the-badge&logo=uv&logoColor=white
[uv-url]: https://github.com/astral-sh/uv
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/