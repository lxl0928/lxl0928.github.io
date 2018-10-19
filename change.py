# coding: utf-8

import os

base_dir = "/Users/sensoro/hexoBlog/source/_posts"
all_files_path = os.listdir(base_dir)

all_files = [os.path.join(base_dir, item_path) for item_path in all_files_path]

for item in all_files:
    with open(item, 'r+') as fp:
        old_data = fp.read()

    if "7xorah.com1.z0.glb.clouddn.com" in old_data:
        print(item)
        new_data = old_data.replace("7xorah.com1.z0.glb.clouddn.com", "timilong.com")
        with open(item, 'w+') as fp:
            fp.write(new_data)

