---
author: Michael
catalog: true
date: 2021-05-16
header_img: /img/in-post/new_header1.jpg
header_mask: rgba(40, 57, 101, .4)
header_style: image
subtitle: No subtitle
title: How Does Version Naming Work
tree_state: 🌱
---

Things are versioned with names like `3.4.13`

This follows the structure of: `Major.minor.patch`

`patch`: don't change API at all
- Everything from before still works the same pretty much for a user

`Minor`: backwards patable
- just adding things so existing stuff still works

`Major`: very large changes that aren't necessarily backwards compatible
- previous API calls won't work the same way