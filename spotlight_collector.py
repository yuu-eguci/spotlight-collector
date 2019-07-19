
"""spotlight_collector

https://support.microsoft.com/en-us/help/18827/places-landscapes-wallpaper
You don't really like Windows though, its rock screen looks great, doesn't it?
You want them, don't you?
Let's do it.
"""

from spotlight_dic import spotlight_dic
import requests
import os
import tqdm

# Directory to store images.
IMAGE_DIR = 'images'
if not os.path.exists(IMAGE_DIR):
    os.mkdir(IMAGE_DIR)

# Download image.
def dl_jpg(key, name):
    res = requests.get(f'https://kbdevstorage1.blob.core.windows.net/asset-blobs/{key}_en_1')
    if res.status_code != 200:
        return
    with open(f'{IMAGE_DIR}/{name}.jpg', 'wb') as fout:
        fout.write(res.content)

# Run program with progress bar.
with tqdm.tqdm(total=len(spotlight_dic), ascii=True, desc='Spotlight collecting') as bar:
    for key,name in spotlight_dic.items():
        dl_jpg(key, name)
        bar.update(1)
