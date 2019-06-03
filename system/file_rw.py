import sys
import os

# the full path-name of this python file (include file name)
# ......./system/file_rw.py
FILE_PATH_NAME = sys.argv[0]

# the path of this python file (exclude file name)
# ......./system
FILE_PATH = sys.path[0]
FILE_PATH = os.path.join(FILE_PATH, "_static/file_rw.txt")
print("\nFILE_PATH: %s\n" % FILE_PATH)

# 模式  可做操作  若文件不存在  是否覆盖
#  r      只能读     报错          -
#  r+    可读可写    报错         是
#  w      只能写     创建         是
#  w+    可读可写    创建         是
#  a      只能写     创建      否，追加写
#  a+    可读可写    创建      否，追加写
if os.path.exists(FILE_PATH):
    os.remove(FILE_PATH)
    # 如果要删除目录，请使用os.rmdir().
    # 递归删除目录， os.removedirs()

with open(FILE_PATH, "w") as f:
    f.write("this is the first line.\n")
with open(FILE_PATH, "ab+") as f:
    f.write(bytes("Add to the end of the file\n", "utf-8"))

print("FILE:")
with open(FILE_PATH, "r") as f:
    print(f.read())

print("SEEK:")
with open(FILE_PATH, "r+") as f:
    print(f.tell())
    f.readline()
    print(f.tell())
    offset = f.tell()
    remain_context = f.read()
    # notice: seek & write , f.read could clear the seek
    f.seek(offset)
    # truncate could clear remain context in file, if
    f.truncate()
    f.write("Insert into the file\n" + remain_context)
    print(f.tell())

# use open - close
f1 = open(FILE_PATH, "r")
try:
    print("\nFILE:")
    print(f1.read())
finally:
    f1.close()
