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
title: How to Set Up Python Aliasing In the Command Line
tree_state: 🌱
---

In your .zshrc file you need to put the lines:

`alias python=/usr/local/bin/python3`
- sets the command `python` to be the same thing as running the command ``/usr/local/bin/python3`

`alias pip=pip3`
- sets the command `pip` to be the same thing as running the command `pip3`