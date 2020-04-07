import os
from pathlib import Path
import datetime

# script to generate photo gallery markdown page
f = open("content/photography.md", "w")
f.write("""---
title: "Photography"\n""")
f.write("date: " + datetime.datetime.now().astimezone().isoformat() + "\n")
f.write("""---\n\n""")

base_path = Path('.') / 'static'
path_to_directory = base_path / 'images' / 'photography'
image_path_list = sorted(path_to_directory.glob('*.jpg'))

for current_path in reversed(image_path_list):
    f.write("![" + str(current_path.stem) + "](/" + str(current_path.relative_to(base_path).as_posix()) + ")\n\n")
f.close()
