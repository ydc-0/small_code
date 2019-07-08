# GCC/GDB
* [GCC 编译选项](http://c.biancheng.net/view/664.html)
* gcc编译 选项：
	* `gcc -g hello.c`
	* 必须添加 `-g` 选项才能生成可供 gdb 调试的程序
* 打开gdb：
	* `gdb a.out` -> 打开 gdb 并加载可执行文件
	* 先打开 gdb，然后使用 `file a.out` (`exec-file a.out`) 加载文件

# 常用的 gdb 调试命令
* [常用gdb命令](http://man.linuxde.net/gdb)
* 运行程序：
	* `r`(`run`):
		* 执行程序
		* 后面可以直接加参数，相当于命令行传参
	* `c`(`continue`):
		* 继续执行
		* 程序暂停时可用此命令继续正常执行
	* `s`(`step`):
		* 单步执行，相当于 step-into
		* 遇到函数体会进入
	* `n`(`next`)：
		* 单步执行，相当于 step-over
		* 遇到函数体直接执行而不进入
	* `finish`:
		* step-out，执行当前函数的剩余部分，并退出当前函数

* 设置断点 `b`(`break`):
	* `b 15` -> 根据行号设置断点
	* `b hello.c:10` -> 指定文件的行号
	* `b main` -> 指定函数设置断点
	* `b hello.c:main` -> 指定文件的函数
	* `break 10 if i == 3` -> 设置条件断点
	* `break *0x4fffff` -> 固定地址设置断点（地址可通过 `info address <xxx>` 得到）
	* `info break` -> 当前设置的断点
	* `delete breakpoint 1` -> 删除指定的断点

* 查看源码 `list`:
	* `list <line_num>` 以某行为中心显示十行（默认）源代码
	* `list <function>` 以函数起始为中心显示十行代码
	* `list -/+` 显示之前/之后十行代码
	* `set listsize count` 设置每次显示的行数
	* `list <file_name>` 设置要显示的源文件
	* `list <num1>,<num2>` 设置起始，结束的行数

* 查看变量 `p`(`print`)：
	* `print <val_name>` 打印当前某个变量的值
	* `print /d <val_name>` 以十进制显示 （其他：/o/x/u/t/f/a/c/s）
	* `print *array@len` 打印动态数组
	* `print array` 打印静态数组
	* `set print elements` 设置数组显示大小
	* [参考文档](http://visualgdb.com/gdbreference/commands/print)

* 查看内存 `x`(examine memory):
    * `x /FMT <address>` 查看指定内存区域，FMT设置格式和要查看的内存大小
    * example ：`x /3uh 0x54320 ` 以双字节(h)为一个单位十六进制(u)显示3个单位
    * use `help x` for more details

* 查看信息 `i`(`info`):
	* `info args` 当前函数的参数名及其值
	* `info locals` 当前函数中所有局部变量及其值
	* `nfo break ` 断点信息
	* `info threads` 线程信息
	* `info registers` 寄存器信息
	* `info functions <regex>` 查看(名字过滤)所有函数
	* `info variables` 全部的静态和全局变量
	* `info address <symbol>` 查看某个变量/函数的位置
	* info 还有很多的用法 `help info <xxxx>`

* 查看堆栈调用`bt`(`backtrace`)：
    * 在断点处执行可查看当前函数的调用，包含参数值等
    * `frame <num>` 移动到指定序号的堆栈
    * `up` 上移一层
    * `down` 下移一层
    
* 查看线程`thread`
    * `info threads` 线程信息
    * `thread <ID>` 切换到线程
    * `thread apply <ID1> <ID2> <command>` 在线程中执行命令
    * `thread apply all bt` 显示所有线程的堆栈调用
    * TODO: 线程与设置断点

# 调试汇编
* 编译与反汇编
	* GCC 使用 -S 选项可将源码编译为汇编代码
	* GCC 可编译汇编文件为可执行文件
	* objdump 可将可执行文件反汇编为汇编代码
* gdb 调试：
	* `disassemble` 显示汇编代码
	* `stepi`,`nexti` 执行单步汇编指令
	* `print $rbp` 打印某寄存器的值
	* `info registers` 显示所有寄存器信息
	* `layout regs` 窗格形式显示当前的寄存器及代码

# 调试 Coredump
* 生成/加载 coredump 文件：
	* linux 下允许生成 core dump 文件,限制不超过指定大小的core文件
        ```
        echo "ulimit -c unlimited" >> /etc/profile
        //echo "ulimit -c 1024" >> /etc/profile
        source /etc/profile
    
        ulimit –c (unlimited/1024)
        ```
    * gdb 调试 core 文件：
        * 直接加载： `gdb <exec_file> <core_file>`
        * 打开后加载： `core_file <core_file>`
    * 常用的命令：`bt`(`backtrace`), `frame`, `up`, `down`