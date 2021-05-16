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
title: What is the Naive Bayes algorithm
tree_state: 🌱
---

The single core assumption with Naive Bayes is:
$$P(X_1,...,X_n \mid Y) = \prod_{i=1}^n P(X_i \mid Y)$$
- Assume $Y$ represents a specific class/label and $X_1,...,X_n$ are the observed data points

This assumption is essentially saying that if we are given the class for each datapoint, the datapoints are completely independent from one another. So if we use this assumption along with Baye's rule we can predict the probability of data points belonging to a specific class:

$$P(Y=k \mid X) = \frac{P(X \mid Y=k)P(Y=k)}{\sum_j P(X_i \mid Y=j)P(Y=j)} = \frac{P(Y=k) \prod_{i=1}^n P(X_i \mid Y=k)}{\sum_j P(Y=j) \prod_{i=1}^n P(X_i \mid Y=j)}$$