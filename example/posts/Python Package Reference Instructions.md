---
author: Michael
catalog: true
date: 2021-05-16
header_img: /img/in-post/new_header2.jpg
header_mask: rgba(40, 57, 101, .4)
header_style: image
subtitle: No subtitle
tags:
- notes
title: Python Package Reference Instructions
tree_state: 🌱
---

## How to Install Python Libraries Inside Jupyter Notebook
```
import sys
!{sys.executable} -m pip install <package_name>
```

## How to check version of a specific package
```
pip freeze | grep ipywidgets
```

## How to Upgrade a Specific Python Package
```
pip install --upgrade matplotlib
```