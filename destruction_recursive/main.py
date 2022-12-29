import os, pathlib, argparse
from PIL import Image

current_path = pathlib.Path().resolve()

PATH_OUT= str(current_path) + '/out/'

list_dir = os.listdir(PATH_OUT)

parser = argparse.ArgumentParser(description='A jpg recursive compression program')

parser.add_argument("first_val_recursion", help="Prints the first recursive loop val argument.")
parser.add_argument("second_val_recursion", help="Prints the second recursive loop val argument.")

args = parser.parse_args()


# compress file one time and save
def compress_img(file, val):
    print(f'process file {file} val {val} in {PATH_OUT}')
    img = Image.open(PATH_OUT + file)
    img.save(PATH_OUT + file, optimize=True, quality=val)

# recursively compress the same file from 100 to 0 > x times
def recursive_compression(file):
    one = int(args.first_val_recursion)
    second = int(args.second_val_recursion)

    for i in reversed(range(one)):
        compress_img(file, i)
        for j in reversed(range(second)):
            compress_img(file, j)
            print('loop 1', i, 'loop 2', j, 'total', one * second) 


if __name__ == '__main__':
    for (i, file) in enumerate(list_dir):
        recursive_compression(file)
    print('process end')
