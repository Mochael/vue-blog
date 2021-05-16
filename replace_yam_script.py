import os
import sys
import random
import frontmatter
# import io
from io import BytesIO
from datetime import date


today = date.today()
my_date = today.strftime("%Y-%m-%d")

dir_path = '/Users/michaelkronovet/Desktop/vuepress-blog/example/.vuepress/public/img/in-post'
img_list = []
for filename in os.listdir(dir_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_list.append(os.path.join("/img/in-post", filename))


global_date = None
global_tags = None
with open("/Users/michaelkronovet/Desktop/vuepress-blog/example/posts/5G and WiFi.md", "r") as file:
    post = frontmatter.load(file)
    global_date = post['date']
    global_tags = post['tags']


directory = '/Users/michaelkronovet/Desktop/vuepress-blog/example/posts'
for filename in os.listdir(directory):
    print(filename)
    # if filename.endswith(".md"):
    file_dir = os.path.join(directory, filename)
    if file_dir.endswith('.md'):
        with open(file_dir, "r") as file:
            post = frontmatter.load(file)
            post['title'] = post['title']
            post['tree_state'] = post['tree_state']
            post['date'] = global_date
            post['subtitle'] = 'No subtitle'
            post['author'] = 'Michael'
            post['header_style'] = 'image'
            post['header_img'] = random.choice(img_list)
            post['header_mask'] = 'rgba(40, 57, 101, .4)'
            post['catalog'] = True
            post['tags'] = global_tags
            f = BytesIO()
            frontmatter.dump(post, f)
            with open(file_dir, "wb") as outfile:
            # Copy the BytesIO stream to the output file
                outfile.write(f.getvalue())
                outfile.close()
# post = frontmatter.load('/Users/michaelkronovet/Desktop/digital_garden/_notes/Bayesian Average.md')