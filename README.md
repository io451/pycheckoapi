![изображение](https://github.com/user-attachments/assets/0fa9b735-d9c1-4047-a2e1-43efb20965d4)



# Python Checko API
Full implementation of [checko.ru](https://checko.ru/) API functions in Python

This is a site where you can find any information about Russian legal entities and individual entrepreneurs.

## Features

- Easy to use
- Inculdes All API functions
- Useful for OSINT scripts

### Requirements

- Python 3.10+

- API-key of [checko.ru](https://checko.ru)

- [Requests library](https://docs.python-requests.org/en/latest/index.html)



## Installation

Install pycheckoapi with pip

```bash
  pip install pycheckoapi
```

Install pycheckoapi with git

```bash
git clone https://github.com/webcartel-https/pycheckoapi
cd pycheckoapi
python setup.py
```


## Usage

Simple example of pycheckoapi usage

```Python
from pycheckoapi import Checko

c = Checko(method="company",api_key=*API-KEY*,parameters="ogrn",id="1046300330317")
request_ = c.request()
c.default_parse(request_)
```

[Documentation](https://github.com/webcartel-https/pycheckoapi/wiki/%D0%94%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D1%8F)


## Roadmap

### Version 0.2 roadmap
- Add "search" method (search by name)
- Add finances method

