---
author: Michael
catalog: true
date: 2021-05-16
header_img: /img/in-post/new_header3.jpg
header_mask: rgba(40, 57, 101, .4)
header_style: image
subtitle: No subtitle
title: What is R Squared
tree_state: 🌱
---

$R^2$ is the proportion of variance explained in the independent variable by the dependent variable. It can be calculated as follows where $\bar{y} = \frac{1}{n}\sum_i^n y_i$ and $\hat{y}_i$ are the predictions of $y_i$ from the dependent variables $x_i$ :

$$R^{2}(y, \hat{y})=1-\frac{\sum_{i=1}^{n}\left(y_{i}-\hat{y}_{i}\right)^{2}}{\sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)^{2}}$$