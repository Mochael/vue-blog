---
author: Michael
catalog: true
date: 2021-05-16
header_img: /img/in-post/new_header3.jpg
header_mask: rgba(40, 57, 101, .4)
header_style: image
subtitle: No subtitle
title: How to Untrack Committed Files from Git
tree_state: 🌱
---

1. Run the command
```
git filter-branch --index-filter "git rm -rf --cached --ignore-unmatch <filepath (or folderpath)>" HEAD
```
2. Make sure the files are now in your `.gitignore` before you stage and then commit again