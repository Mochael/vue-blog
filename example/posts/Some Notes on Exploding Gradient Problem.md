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
title: Some Notes on Exploding Gradient Problem
tree_state: 🌱
---

Most datasets have some number of mistakes in the $y$ labels. It can be harmful to maximize $\log p(y | \bf{x})$ when $y$ is a mistake. One way to prevent this is to explicitly model the noise on the labels. For example, we can assume that for some small constant $\epsilon,$ the training set label $y$ is correct with probability $1-\epsilon,$ and otherwise any of the other possible labels might be correct. This assumption is easy to incorporate into the cost function analytically, rather than by explicitly drawing noise samples. For example, label smoothing regularizes a model based on a softmax with $k$ output values by replacing the hard 0 and 1 classification targets with targets of $\frac{\epsilon}{k-1}$ and $1-\epsilon,$ respectively. The standard cross-entropy loss may then be used with these soft targets. Maximum likelihood learning with a softmax classifier and hard targets may actually never converge- -the softmax can never predict a probability of exactly 0 or exactly $1,$ so it will continue to learn larger and larger weights, making more extreme predictions forever. It is possible to prevent this scenario using other regularization strategies like weight decay. Label smoothing has the advantage of preventing the pursuit of hard probabilities without discouraging correct classification. This strategy has been used since the 1980s