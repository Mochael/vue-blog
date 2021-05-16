---
author: Michael
catalog: true
date: 2021-05-16
header_img: /img/in-post/new_header3.jpg
header_mask: rgba(40, 57, 101, .4)
header_style: image
subtitle: No subtitle
tags:
- notes
title: What is Integration Really
tree_state: 🌱
---

$$\int_a^b f(x) dx = \lim_{\Delta x \to 0}  \sum_{x=a}^b f(x) \Delta x$$

$$\int_{a}^{b} f \left( x \right) dx = \mathop {\lim }\limits_{n \to \infty } \sum\limits_{i = 1}^n f \left( {x_i^*} \right)\Delta x \hspace{0.25in}\hspace{0.25in}\hspace{0.25in} \text{where } \Delta x = \frac{b - a}{n}$$

Integration is just summing the area under a curve. You take the value of the curve at a point (height) and then multiply it by an infinitesimally small increment in the input value (width) and then sum over all these increments.