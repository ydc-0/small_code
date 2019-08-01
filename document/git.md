# Git 实战教程
    * https://www.shiyanlou.com/courses/4
    * 内容取自实验楼，完整内容如上链接

# 基本用法
## 二、Git 的初始化
* 在使用 Git进行代码管理之前，我们首先要对 Git 进行初始化配置。
    * 使用 Git 的第一件事就是设置你的名字和 email，这些就是你在提交 commit 时的签名，每次提交记录里都会包含这些信息。使用 git config 命令进行配置：
        ```
        $ git config --global user.name "Scott Chacon"
        $ git config --global user.email "schacon@gmail.com"
        ```
    * 执行了上面的命令后，会在家目录（/home/shiyanlou）下建立一个叫 .gitconfig 的文件（该文件为隐藏文件，需要使用 ls -al 查看到）. 内容一般像下面这样，可以使用 vim 或 cat 查看文件内容:
        ```
        $ cat ~/.gitconfig
        [user]
                email = schacon@gmail.com
                name = Scott Chacon
        ```
    * 上面的配置文件就是 Git 全局配置的文件，一般配置方法是 git config --global <配置名称> <配置的值>。
    * 如果你想使项目里的某个值与前面的全局设置有区别（例如把私人邮箱地址改为工作邮箱），你可以在项目中使用 git config 命令不带 --global 选项来设置. 这会在你当前的项目目录下创建 .git/config，从而使用针对当前项目的配置。

## 4.3 使用 git commit 提交修改
    * 我们当前的仓库是使用 git init 初始化的本地仓库，所以我们需要将本地仓库与远程仓库关联，使用如下命令（需要修改下面的远程仓库地址为自己的仓库地址）：
        ```
        $ git remote add origin https://github.com/kinglion580/shiyanlou.git
        ```
    * 对于上述命令而言，git remote add 命令用于添加远程主机，origin 是主机名，此处我们可以自定义，不一定非要使用 origin，而 https://github.com/kinglion580/shiyanlou.git，是我自己的远程仓库，此处 需要替换为自己的远程仓库地址

# 中级技能（上）
## 六、储藏
* 1.储藏
    * 当你正在做一项复杂的工作时， 发现了一个和当前工作不相关但是又很讨厌的 bug. 你这时想先修复 bug 再做手头的工作， 那么就可以用 `git stash` 来保存当前的工作状态， 等你修复完 bug 后，执行反储藏（unstash）操作就可以回到之前的工作里。
        ```
        $ git stash save "work in progress for foo feature"
        ```
    * 上面这条命令会保存你的本地修改到储藏（stash）中， 然后将你的工作目录和索引里的内容全部重置， 回到你当前所在分支的上次提交时的状态。
    * 好了， 你现在就可以开始你的修复工作了。
        ```
        $ git commit -a -m "blorpl: typofix"
        ```
    *当你修复完bug后， 你可以用 `git stash apply` 来回复到以前的工作状态。
        ```
        $ git stash apply
        ```
* 2.储藏队列
    * 你也可多次使用 git stash 命令，　每执行一次就会把针对当前修改的储藏（stash）添加到储藏队列中. 用 `git stash list `命令可以查看你保存的储藏（stashes）:
        ```
        $ git stash list
        ```
    * 可以用类似 `git stash apply stash@{1}` 的命令来使用在队列中的任意一个储藏（stashes）. `git stash clear` 则是用来清空这个队列。

## 七、Git 树名
* 1. Git 树名
    * 不用 40 个字节长的 SHA 串来表示一个提交（commit）或是其它 git 对象，有很多种名字表示方法。在 Git 里，这些名字就叫树名（treeish）。
* 2. Sha 短名
    * 如果你的一个提交（commit）的 sha 名字是 980e3ccdaac54a0d4de358f3fe5d718027d96aae， git会把下面的串视为等价的:
        ```
        980e3ccdaac54a0d4de358f3fe5d718027d96aae
        980e3ccdaac54a0d4
        980e3cc
        ```
    * 只要你的sha短名（Partial Sha）是不重复的（unique），它就不会和其它名字冲突（如果你使用了5个字节以上那是很难重复的），Git 也会把sha短名（Partial Sha）自动补全。
* 3. 分支， Remote 或 标签
    * 你可以使用分支，remote 或标签名来代替 SHA 串名， 它们只是指向某个对象的指针。假设你的master 分支目前在提交（commit）:980e3 上， 现在把它推送（push）到 origin 上并把它命名为标签 v1.0， 那么下面的串都会被 git 视为等价的:
        ```
        980e3ccdaac54a0d4de358f3fe5d718027d96aae
        origin/master
        refs/remotes/origin/master
        master
        refs/heads/master
        v1.0
        refs/tags/v1.0
        ```
    * 这意味着你执行下面的两条命令会有同样的输出:
        ```
        $ git log master
        $ git log refs/tags/v1.0
        ```
* 4. 日期标识符
    * Git 的引用日志（Ref Log）可以让你做一些 相对 查询操作：
        ```
        master@{yesterday}
        master@{1 month ago}:
        ```
    * 上面的第一条命令是：master 分支的昨天状态（head）的缩写。注意: 即使在两个有相同 master 分支指向的仓库上执行这条命令，但是如果这个两个仓库在不同机器上，那么执行结果也很可能会不一样。

* 5. 顺序标识符
    * 这种格式用来表达某点前面的第 N 个提交（ref）。
        ```
        master@{5}
        ```
    * 上面的表达式代表着 master 前面的第 5 个提交（ref）。
* 6. 多个父对象
    * 这能告诉你某个提交的第 N 个直接父提交（parent）。这种格式在合并提交（merge commits）时特别有用，这样就可以使提交对象（commit object）有多于一个直接父对象（direct parent）:
        ```
        master^2
        ```
* 7. 波浪号
    * 波浪号用来标识一个提交对象（commit object）的第 N 级嫡（祖）父对象（Nth grandparent），例如:
        ```
        master~2
        ```
    * 就代表 master 所指向的提交对象的第一个父对象的第一个父对象（译者：你可以理解成是嫡系爷爷）。 它和下面的这个表达式是等价的:
        ```
        master^^
        ```
    * 你也可以把这些标识符叠加起来， 下面这个3个表达式都是指向同一个提交（commit）:
        ```
        master^^^^^^
        master~3^~2
        master~6
        ```
* 8. 树对象指针
    * 如果大家对之前的 Git 对象模型还有印象的话， 就记得提交对象（commit object）是指向一个树对象（tree object）的。假如你要得到一个提交对象（commit object）指向的树对象（tree object）的 sha 串名， 你就可以在 ‘树名' 的后面加上 {tree} 来得到它:
        ```
        master^{tree}
        ```
* 9. 二进制标识符
    * 如果你要某个二进制对象（blob）的 sha 串名，你可以在树名（treeish）后添加二进制对象（blob）对应的文件路径来得到它：
        ```
        master:/path/to/file
        ```
* 10. 区间
    * 最后，你可以用 .. 来指两个提交（commit）之间的区间. 下面的命令会给出你在 7b593b5 和 51bea1 之间除了 7b593b5 外的所有提交（commit）（注意：51bea1是最近的提交）：
        ```
        7b593b5..51bea1
        ```
    * 这会包括所有从 7b593b 开始的提交（commit）。译者注：相当于 7b593b..HEAD：
        ```
        7b593b.. 
        ```

# 中级技能（下）
## 三、使用 Git Grep 进行搜索
* 用 git grep 命令查找 Git 库里面的某段文字是很方便的。当然，你也可以用 Linux 下的 grep 命令进行搜索，但是 git grep 命令能让你不用 签出（checkout）历史文件，就能查找它们。

    * 例如，你要看仓库里每个使用 xmmap 函数的地方，你可以运行下面的命令:
        ```
        $ git grep xmmap
        ```
    * 如果你要显示行号，你可以添加 -n选项:
        ```
        $ git grep -n xmmap
        ```
    * 如果我们想只显示文件名，我们可以使用 --name-only 选项:
        ```
        $ git grep --name-only xmmap
        ```
    * 我们用 -c 选项可以查看每个文件里有多少行 匹配内容（line matches）:
        ```
        $ git grep -c xmmap
        ```
    * 现在， 如果我们要查找 git 仓库里某个特定版本里的内容， 我们可以像下面一样在命令行末尾加上标签名（tag reference）:
        ```
        $ git grep xmmap v1.5.0
        ```
    * 我们也可以组合一些搜索条件，下面的命令就是查找我们在仓库的哪个地方定义了 SORT_DIRENT：
        ```
        $ git grep -e '#define' --and -e SORT_DIRENT
        ```
    * 我不但可以进行与（both）条件搜索操作，也可以进行或（either）条件搜索操作：
        ```
        $ git grep --all-match -e '#define' -e SORT_DIRENT
        ```
    * 我们也可以查找出符合一个条件（term）且符合两个条件（terms）之一的文件行，例如我们要找出名字中含有 PATH 或是 MAX 的常量定义:
        ```
        $ git grep -e '#define' --and \（ -e PATH -e MAX \） 
        ```

## 五、维护Git
* 1. 保证良好的性能
    * 在大的仓库中， git 靠压缩历史信息来节约磁盘和内存空间。
    * 压缩操作并不是自动进行的，你需要手动执行 `git gc`：
        ```
        $ git gc
        ```
    * 压缩操作比较耗时，你运行 `git gc` 命令最好是在你没有其它工作的时候。

* 2. 保持可靠性
    * `git fsck` 运行一些仓库的一致性检查，如果有任何问题就会报告。这项操作也有点耗时，通常报的警告就是 `悬空对象`（dangling objects）。
        ```
        $ git fsck
        ```
    * `悬空对象`（dangling objects）并不是问题，最坏的情况它们只是多占了一些磁盘空间，但有时候它们是找回丢失的工作的最后一丝希望.

## 六、建立一个公共仓库
* 1. 建立一个公共仓库
    * 假设你个人的仓库在目录 `~/proj`，我们先克隆一个新的“裸仓库“，并且创建一个标志文件告诉 git-daemon 这是个公共仓库：
        ```
        $ git clone --bare ~/proj proj.git
        $ touch proj.git/git-daemon-export-ok
        ```
    * 上面的命令创建了一个 `proj.git` 目录， 这个目录里有一个 `裸 git 仓库` —— 即只有 .git 目录里的内容，没有任何签出（checkout）的文件。
    * 下一步就是你把这个 `proj.git` 目录拷到你打算用来托管公共仓库的主机上，你可以用 `scp`， `rsync` 或其它任何方式。

* 2. 通过 git 协议导出 git 仓库
    * 用 Git 协议导出 Git 仓库， 这是推荐的方法。
    * 如果这台服务器上有管理员，他会告诉你把仓库放在哪一个目录中，并且告诉你仓库的地址 `git://URL` 是什么。
    * 服务器上需要启动 `git daemon`，它默认监听在 `9418` 端口，默认情况下它会允许你访问所有的 Git 目录（看目录中是否有 `git-daemon-export-ok` 文件）。可以配置 `git daemon` 的启动参数来让 `git-daemon` 限制用户通过 Git 协议只能访问哪些目录。

* 3. 通过 http 协议导出 git 仓库
    * Git 协议有不错的性能和可靠性，但是如果主机上已经配好了一台 web 服务器，使用 http 协议（git over http）可能会更容易配置一些。
    * 你需要把新建的 `裸仓库` 放到 `Web 服务器` 的 `可访问目录` 里， 同时做一些调整，以便让 web 客户端获得它们所需的额外信息：
        ```
        $ mv proj.git /var/www/html/proj.git
        $ cd proj.git
        $ git --bare update-server-info
        $ chmod a+x hooks/post-update
        ```
    * 克隆的时候可以使用下面的命令进行克隆：
        ```
        $ git clone http://服务器地址/proj.git
        ```
