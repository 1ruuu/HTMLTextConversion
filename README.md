
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/1ruuu/HTMLTextConversion/">
    <img src="image/logo.png" alt="Logo" width="512" height="256">
  </a>

  <h3 align="center">HTMLTextConversion--A tool for converting HTML text.</h3>
  <p align="center">This is an unofficial Python package that uses OpenCC to convert text within HTML content. Currently, it only supports converting from Simplified Chinese to Traditional Chinese (updates for other languages are coming soon...)
    <br />
    <a href="https://github.com/1ruuu/HTMLTextConversion/"><strong>docs » »</strong></a>
    <br />
    <a href="https://github.com/1ruuu/HTMLTextConversion/issues/new">Report Bug</a>
    ·
    <a href="https://github.com/1ruuu/HTMLTextConversion/issues/new">Request Feature</a>
  </p>

</p>


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
        <li><a href="#Installation">Installation</a></li>
        <li><a href="#Quick Start">Quick Start</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project
### Built With
[![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Please follow the instructions to install and set up the environment for this project.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/1ruuu/HTMLTextConversion.git
   ```
2. Move to the project
   ```sh
   cd ./HTMLTextConversion
   ```
3. Build environment
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Quick Start
You can follow the [sample code](https://github.com/1ruuu/HTMLTextConversion/blob/main/sample_code.ipynb) to get the sample usage of this package.

<!-- USAGE EXAMPLES -->
## Usage
### Setup
#### How to use this package in your own project?
You can directly copy the folder pyopenverse to your project, here is an example structure design:

```
.
└── your-project/
    ├── your_custom_module/
    │   ├── your_function_1.py
    │   └── your_function_2.py
    ├── HTMLTextConversion/   <--- Copy & Paste the entire Conversion folder here.
    │   ├── conversion.py
    │   └── engine.py
    └── your_main.py
```
### Create a HTMLTextConversion Engine
```sh
# import packages and create a Conversion engine
from Conversion.engine import Tools

tool = Tools()
```

### Simplified to Traditional
Now we can use this engine to convert Simplified Chinese in HTML to Traditional Chinese.
```sh
file_path = "src/sample.html" # Please change the file_path into what you wanna convert
tool.chinese_conversion(file_path=file_path) # This will creat a '_conversion.html' in origin html path
```

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


<!-- CONTACT -->
## Contact

E-Mail: irene45666@gmail.com

Project Link: [https://github.com/1ruuu/HTMLTextConversion/](https://github.com/1ruuu/HTMLTextConversion/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/1ruuu/HTMLTextConversion.svg?style=for-the-badge
[license-url]: https://github.com/1ruuu/HTMLTextConversion/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/yiruke
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/pypi/pyversions/numpy
[Python-url]: https://numpy.org/
