import os
import renpy

for dir in renpy.config.searchpath:
    ext_list = []
    # Crawl the directories
    for root, dirs, files in os.walk(os.path.join(dir, 'extensions')):
        for fn in files:
            if fn.lower().endswith(".rpe"):
                ext_list.append(os.path.join(root, fn))
    # Load sorted file list
    for fn in sorted(ext_list):
        renpy.main.load_rpe(fn)
