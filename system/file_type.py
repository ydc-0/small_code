import filetype
import sys
import os

# https://blog.csdn.net/bruce135lee/article/details/80354956
FILE_TYPE_DICT = {
    bytes([66,77]): "BMP",
    bytes([255,216]): "JPG"
}

FILE = sys.path[0]
FILE = os.path.join(FILE, "_static/file_type.txt")
# FILE = os.path.join(FILE, "_static/file_rw.txt")

# 通过文件名获取 路径，拓展名
(filepath, fullfilename) = os.path.split(FILE)
print(filepath, fullfilename)
(filename, extension) = os.path.splitext(fullfilename)
# file_type .txt
print(filename, extension)
# basename: file_type.txt
# dir name: same with filepath
print("basename:", os.path.basename(FILE))
print("basename:", os.path.dirname(FILE))


# 通过读文件前两个字节获取文件类型
with open(FILE, "rb") as f:
    type_id = f.read(2)
    try:
        print("real file type maybe :", FILE_TYPE_DICT[type_id])
    except KeyError as e:
        print("failed to guess the real file type!")
        pass

# 使用 filetype： 原理也是读文件的前几个字节（不一定是两个）
kind = filetype.guess(FILE)
if kind:
    print("File extension: ", kind.extension)
    print('File MIME type: ', kind.mime)
else:
    print("failed to guess the real file type!")
    pass

