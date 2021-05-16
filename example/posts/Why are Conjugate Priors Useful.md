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
title: Why are Conjugate Priors Useful
tree_state: 🌱
---

Suppose our prior follows a beta distribution $$p(\theta) \sim Beta(\alpha,\beta)$$ and we have a binomial likelihood $$p(x\mid\theta)$$.
$$
p(\theta \mid x) = p(x \mid \theta) p(\theta)
$$
Since the beta is a conjugate prior for the binomial likelihood, we can show that $$p(\theta \mid x) \sim Beta(k+\alpha,n-k+\beta)$$.

- We don't need to actually calculate this $$p(\theta \mid x)$$ with the computer since it just follows a known distribution and the MAP estimate for this distribution will be of the same form as the optimal estimate of $$p(\theta)$$, just with the adjusted $$k+\alpha, \ n-k+\beta$$ values.