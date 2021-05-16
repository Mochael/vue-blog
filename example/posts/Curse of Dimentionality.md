---
author: Michael
catalog: true
date: 2021-05-16
header_img: /img/in-post/new_header1.jpg
header_mask: rgba(40, 57, 101, .4)
header_style: image
subtitle: No subtitle
title: Curse of Dimentionality
tree_state: 🌱
---

Let's say you have $p$ features and $n$ samples. Think of a $p$ dimensional cube/rectangle, where each edge contains the set of values that can be drawn from a specific feature (this is a simplification because hypothetically people with specific values of certain features have different probabilities of getting other features. For example, someone whose 100 years old is much more likely to have gray hair than an 11 year old). So, the volume of the cube is the scope of possible samples that could be drawn from the domain. As the number of features increases, the volume of the domain increases exponentially. So, we require more samples $n$ to get enough coverage of the domain to build an effective model.