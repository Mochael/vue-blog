---
author: Michael
catalog: true
date: 2021-05-16
header_img: /img/in-post/new_header1.jpg
header_mask: rgba(40, 57, 101, .4)
header_style: image
subtitle: No subtitle
tags:
- notes
title: How to Add to Your System Path Variable for Mac
tree_state: 🌱
---

Put the following command in your .zshrc file in your root directory
`export PATH=/usr/local/bin:$PATH`

- The first **PATH** contains all the directories that we want to source from the terminal
- **/usr/local/bin** is the path that we want to add to be sourced
- **:$PATH** references the current value **PATH**, so everything that is already sourced in the .zshrc file
- So, the variable path looks something like this with a colon between each path:
  - PATH= /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games