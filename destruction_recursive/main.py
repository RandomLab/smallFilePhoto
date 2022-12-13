import os, pathlib
from PIL import Image

current_path = pathlib.Path().resolve()

PATH_OUT= str(current_path) + '/images/'

list_dir = os.listdir(PATH_OUT)

# compress file one time and save
def compress_img(file, val):
    print(f'process file {file} val {val} in {PATH_OUT}')
    img = Image.open(PATH_OUT + file)
    img.save(PATH_OUT + 'process_' + file, optimize=True, quality=val)

# recursively compress the same file from 100 to 0
def recursive_compression(file, quality):
    num_loop = 100 - int(quality)
    compress_img(file, 100)
    for i in reversed(range(num_loop)):
        compress_img(file, i)

if __name__ == '__main__':
    quality = 1
    for (i, file) in enumerate(list_dir):
        recursive_compression(file, quality)
    print('process end')