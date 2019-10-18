# pip install beautifulsoup4
# conda install lxml
# 教学： https://www.cnblogs.com/Albert-Lee/p/6232745.html
# bs4 文档： https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup

html_doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

# soup = BeautifulSoup(html_doc, 'lxml')  # 声明BeautifulSoup对象
soup = BeautifulSoup(html_doc, 'html.parser')  # 声明BeautifulSoup对象
find = soup.find('p')  # 使用find方法查到第一个p标签
# 输出返回值类型 <class 'bs4.element.Tag'>
print("title: ", soup.head.title)
print("find's return type is ", type(find))
print("find's content is", find)  # 输出find获取的值
print("find's Tag Name is ", find.name)  # 输出标签的名字
print("find's Attribute(class) is ", find['class'])  # 输出标签的class属性值
print("find's Attribute(class) is ", find.get_text())
# find_previous_siblings, find_previous_sibling
# find_next_siblings() and find_next_sibling()
# find_parents() and find_parent()
last_link = soup.find("a", id="link3")
a1 = last_link.find_previous_siblings("a")
print(a1)
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
a1 = last_link.find_parent()
print(a1)
# <p class="story">Once upon a time there were three little sisters; and their names were
# ...... of a well.</p>


# CSS 选择器：
# https://www.runoob.com/jquery/jquery-selectors.html
# Find the siblings of tags: 兄弟节点
select = soup.select("#link1 ~ a.sister")
select = soup.select("#link1 + a.sister")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
print(select)
# Find tags () beneath other tags: 在…下面
select = soup.select("html title")
select = soup.select("html > head > title")
print(select)