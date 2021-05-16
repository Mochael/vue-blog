---
author: Michael
catalog: true
date: 2021-05-16
header_img: /img/in-post/new_header2.jpg
header_mask: rgba(40, 57, 101, .4)
header_style: image
subtitle: No subtitle
tags:
- notes
title: How to Store and Access SQL Queries in Databricks
tree_state: 🌱
---

1. Create the SQL query and define `table_name` as the name where you store the queried table.
```
%sql
CREATE OR REPLACE TEMPORARY VIEW <table_name> AS 

'''SQL query here'''
SELECT * FROM <data_table>
```

2. Create a spark dataframe for the queried table
```
spark_dataframe_of_table = spark.table('table_name')
```