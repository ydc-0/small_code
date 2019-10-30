# 基础命令

- 查看帮助文档
  - `<cmd> --help`
  - `man <cmd>`

## 常用快捷键

- `CTRL+C` 强制结束当前正在运行的程序（KeyboardInterrupt）
- `CTRL+Z` 挂起当前正在运行的程序（fg/bg 恢复/后台恢复），vi 常用
- `CTRL+D` 退出（相当于 EOF & exit）
- `CTRL+S` 中断控制台输出，使用 `CTRL+Q` 恢复（**非保存，vi 初学者常误用**）
- `CTRL+L` 清屏，相当于 `clear` （可以上翻找到原来的输出）
- `CTRL+ALT+T` 新窗口打开一个终端， `CTRL+SHIFT+T` 新标签页打开终端
- Ubuntu 长按 Super（win）键可以显示部分窗口操作的快捷键
- `Tab` 自动补全 命令、目录、git 分支 等

## 目录相关

- Note：
  - `.` 当前目录，`..` 上一层目录， `~` 用户 home 目录， `/` 根目录
  - 目录中有某些字符时需要转义, 有时还需要 -- 来传参
  - 例：
    ```bash
    $ mkdir \[\]
    $ mkdir -- ---
    $ cd -- ---
    $ rm -r \[\]
    ```

### ls

- 显示目录中的所有文件
- 也可以使用 `dir`
- `tree` (需安装) 显示目录树
- `ll` aliased to `ls -lh` 更详细的目录信息 （`which ll`）

### cd

- 进入一个目录 `cd <dir>`
- `cd -` 可以返回上一次所在的目录，连续使用可在两个目录中来回切换

### mkdir

- 创建目录

### rm

- 删除目录
- 可以带有多个参数删除多个文件
- 要删除文件夹需要带参数 `-r`

### cp

- 复制文件

### mv

- 移动文件， 重命名文件

### touch

- 新建文件 & 更新文件的最后修改时间

### find

- `find <path> -name "*.c"` 常用的查找文件的命令
  - 可用 `*` 通配符
  - 递归查找，当前目录和其子目录

## 显示/查看/打印

### echo

- 控制台输出
- 其他的控制台打印命令 [print 与 printf](#print)

### cat

### head & tail

### diff

### grep

### vi

## 系统相关

- 很多时候我们会直接查看或修改一些系统文件
  - `cat /proc/version` 查看系统版本 （内核版本）

### 查看系统版本

- `cat /proc/version` 查看内核版本（包含系统版本）
- `uname -a` 查看内核版本 （信息不如上一个命令多）
- `lsb_release -a` 显示系统版本信息
- `cat /etc/issue` 只显示主版本号

### ifconfig

### sudo

- `sudo <cmd>` 以 root 权限运行命令
- `sudo su` 进入 root 账号
- `visudo` (需要 root 权限) 编辑 `/etc/sudoers` 文件

### apt-get

- `apt-get install` 常用的安装软件命令

### whereis

### which

# 进阶

## 玩转命令行 x 文本处理

- [grep 进阶](#grep_ex)
- [管道`|` 和 xargs **(常用)**](#管道)
- [print & printf](#print)
- test
- awk
- sed

### grep_ex

### 管道

- 可以用 `|` 符号连接多条命令，同时执行多条命令，后一条命令使用前面的输出
- `xargs` 可以将前一个命令的输出作为后一个命令的参数
- 例：
  ```bash
  $> ll | grep sh
  # 只显示文件名中包含 sh 的文件
  $> ps -aux | grep python
  # 显示正在运行的 包含python字段的程序 (grep python 本身也会被算进去)
  $> ps -ef | grep <program_name> | awk '{print $2}' | xargs kill -9
  # linux 下一行命令结束指定的进程
  # `-A -e` 可以显示所有的进程
  $> ls *.log | xargs rm
  # 删除当前目录下所有的 .log 文件
  ```

### print

- print 与 printf 区别

  - print 是 ksh 的内置命令，而 printf 是 bash 的内置命令
  - print 中不能使用%s ,%d 或%c
  - print 自动换行，printf 没有自动换行
  - printf 可以自定义输出格式 `printf format-string [arguments...]`
  - printf 的 format 格式与 C 语言基本相同

- 使用： 常使用于 awk 或脚本中

  ```text
  # test.txt
  1
  2
  3
  ```

  - \$ `awk '{print "X"$1, $1}' test.txt`

  ```sh
  X1 1
  X2 1
  X3 1
  ```

  - \$ `awk '{printf "X"$1}' test.txt`

  ```sh
  X1X2X3
  # 本机测试打印出有多余后缀 X1X2X3%
  ```

  - \$ `awk '{printf "X%s\n",$1}' test.txt`

  ```sh
  X1
  X2
  X3
  ```

## 远程操作 & 控制

- ssh
- scp

# shell 脚本

## 常用语法

- for
- if
- while
- sleep
