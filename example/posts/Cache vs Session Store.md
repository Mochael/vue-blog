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
title: Cache vs Session Store
tree_state: 🌱
---

Cache is stored at an application level, not a user level. So, content in the cache is shared between users.

In session storage, the app stores all session-related data from a specific user like their profile information, messages, personalized data and themes, recommendations, targeted promotions and discounts, etc. So, content in session storage must be separated user to user.

More info is here:
https://redislabs.com/blog/cache-vs-session-store/