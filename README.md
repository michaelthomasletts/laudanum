![laudanum](https://raw.githubusercontent.com/michaelthomasletts/laudanum/refs/heads/main/docs/laudanum.png)

[![PyPI Download](https://img.shields.io/pypi/v/laudanum?logo=pypis.svg)](https://pypi.org/project/laudanum/)
![Python Version](https://img.shields.io/pypi/pyversions/laudanum?style=pypi)
![PyPI Downloads (Total)](https://static.pepy.tech/badge/laudanum)

## What it is

A simple Python package and CLI tool for creating logos with [ASCII art](https://www.ascii-art.site/FontList.html).

## How to use it
##### Python

```python

from laudanum import Logo


Logo("fancypants").create()
```

##### CLI

```bash

laudanum --text fancypants --font ghost --filename holyguacamole.png
```

## Where to get it

```bash

pip install laudanum
```

## Where to learn more

- [Documentation](https://michaelthomasletts.github.io/laudanum/index.html)
- [Source Code](https://github.com/michaelthomasletts/laudanum)
- [PyPI](https://pypi.org/project/laudanum/)