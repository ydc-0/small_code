# https://unsplash.com/
# 该网站已将图片修改为动态加载，无法直接用

from urllib import request  #导入requests 模块 (py3)
from bs4 import BeautifulSoup  #导入BeautifulSoup 模块

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}  #给请求指定一个请求头来模拟chrome浏览器
# web_url = 'https://unsplash.com'
# r = request.Request(web_url, headers=headers) #像目标url地址发送get请求，返回一个response对象
# r = request.urlopen(r)
# # http.client.HTTPResponse
# text = r.read()
# all_a = BeautifulSoup(text, 'lxml').find_all('a', class_='_2Mc8_')  #获取网页中的class为cV68d的所有a标签
# for a in all_a:
#     div = a.find('div')

text = '''
<img class="mimg" style="color: rgb(8, 7, 25);" height="160" width="286" src="https://tse2-mm.cn.bing.net/th?id=OIP.z5R0wso4AxKuwe1PerMVGQHaEK&amp;w=286&amp;h=160&amp;c=7&amp;o=5&amp;pid=1.7" alt="Image result for 动漫壁纸" data-bm="23">
'''

soup = BeautifulSoup(text, 'lxml')
img = soup.find('img')
img_url = img['src']
print(img_url)


# 简单的下载一张图片
url = 'https://c-ssl.duitang.com/uploads/item/201704/03/20170403005223_hGfyT.thumb.700_0.png'
req = request.Request(url)
data = request.urlopen(url).read()
with open("D:/test.png",'wb') as f:
    f.write(data)
