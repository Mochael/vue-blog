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
title: What are Makefiles
tree_state: 🌱
---

When you are within a certain directory that has a file named `Makefile` running the command `make` in the terminal followed by a specific command you defined in `Makefile` will call those specific operations in the terminal.

Structure of defining a command (referred to as a rule) in the make file:
```
target: prerequisites
	recipe
```

When `make` is asked to evaluate a rule, it begins by finding the files indicated by the prerequisites and target. If any of the prerequisites has an associated rule, `make` attempts to run those first.

- Putting `-` before an instruction will ignore the errors from running the command
- Putting `@` before an instruction will stop it from printing


Example makefile:

```
all: say_hello generate  
  
say_hello:
	@echo "Hello World"  
  
generate:
	@echo "Creating empty text files..."  
	touch file-{1..10}.txt  
  
clean:
	@echo "Cleaning up..."  
	rm \*.txt
 ```