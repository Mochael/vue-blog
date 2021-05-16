---
author: Michael
catalog: true
date: 2021-05-16
header_img: /img/in-post/new_header3.jpg
header_mask: rgba(40, 57, 101, .4)
header_style: image
subtitle: No subtitle
title: How to Write Output to Text File
tree_state: 🌱
---

`SomeCommand > SomeFile.txt` overwrites `SomeFile.txt` with the output from `SomeCommand`

`SomeCommand >> SomeFile.txt` appends the output from `SomeCommand` to the text file

`SomeCommand &> SomeFile.txt` overwrites the output as well as the `stderr` output from `SomeCommand` to the text file