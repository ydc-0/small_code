
from urllib import request
from bs4 import BeautifulSoup
import re
import os

# 解析图片地址 -> 下载图片
# http://desk.zol.com.cn/bizhi/2269_28950_2.html
# 目标：爬取小编精选的图片 https://pixabay.com/zh/editors_choice/?media_type=photo&pagi=1


class DownloadImg(object):
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self.req = None
        self.img_urls = []
        self.http_pattern = re.compile(r'https:[\S]+')
        super().__init__()

    @staticmethod
    def open_url(url):
        head = {
            "user-agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        # get 403 if head is not added
        r = request.Request(url, headers=head)
        return request.urlopen(r)


    def get_home_page(self):
        self.req = self.open_url(self.url)

    def get_url_from_img(self, img):
        if img.has_attr('srcset'):
            img_url = self.http_pattern.findall(img['srcset'])[-1]
        else:
            img_url = self.http_pattern.findall(img['data-lazy-srcset'])[-1]
        # 下载高清图片需要登录或验证码
        # href = img.find_parent()['href']
        # sub_url = "https://pixabay.com" + href
        # req = self.open_url(sub_url)
        # context = req.read()
        # # print(context)
        # soup = BeautifulSoup(context, 'html.parser')
        # down_menu = soup.select_one("div.download_menu")
        # max_img = down_menu.select_one("tr.no_default > td")
        # # max_size = max_img.get_text()
        # img_url = max_img['value']
        # img_url = 'https://pixabay.com/zh/images/download/' + max_img['value'] + '?attachment&modal'
        return img_url

    def parse_img_urls(self, max_num=None):
        context = self.req.read()
        # print(context)
        soup = BeautifulSoup(context, 'html.parser')
        div = soup.find('div',{'class':'flex_grid credits'})
        # print(div)
        for img in div.find_all('img'):
            try:
                url = self.get_url_from_img(img)
                if img.has_attr('title'):
                    title = img['title'].split(', ')
                    title = title[0] + "_" + title[1] + url[url.rfind('.'):]
                else:
                    title = url[url.rfind('/')+1:]
                # print(url, title)
                self.img_urls.append((url, title))
            except KeyError as e:
                print("KeyError:", e, "\nimg:", img)
                pass


    def save_img(self, url, file_name):
        req = self.open_url(url)
        data = req.read()
        with open(file_name,'wb') as f:
            f.write(data)

    def down_all_img(self, max_num=None):
        self.get_home_page()
        self.parse_img_urls(max_num)
        for url,name in self.img_urls:
            file_name = os.path.join(self.path, name)
            self.save_img(url, file_name)
        pass


URL = "https://pixabay.com/zh/editors_choice/?media_type=photo&pagi=1"
PATH = "E:/test"
d_img = DownloadImg(URL, PATH)
d_img.down_all_img(100)
