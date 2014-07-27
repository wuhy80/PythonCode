#! /usr/bin/env python
#coding=utf-8
#coding=utf-8
import os
import sys
import re
import urllib

class MySpider:
    URL_REG = re.compile(r'(http://[^/\\]+)', re.I)
    IMG_REG = re.compile(r'<img[^>]*?src=([\'"])([^\1]*?)\1', re.I)

    def __init__(self, dir):
        self.base_dir = dir
        self.store_dir = self.base_dir
        self.ensure_dir(dir)

    def extract_img_links(self, url):
        # 获取html,提取图片url
        html = urllib.urlopen(url).read()
        imgs = [item[1].lower() for item in self.IMG_REG.findall(html)]
        f = lambda path: path if path.startswith('http://') else \
        host + path if path.startswith('/') else url + '/' + path
        imgs = list(set(map(f, imgs)))

        print '[Info]Find %d images.' % len(imgs)
        return imgs

    def ensure_dir(self, dir):
        if not os.path.isdir(dir):
            os.mkdir(dir)

    def download_img(self, store_dir, img_link):
        name = img_link.split('/')[-1]
        path = os.path.join(store_dir, name)
        try:
            print '[Info]Download: %s'% (img_link)
            urllib.urlretrieve(img_link, path)
        except:
            print "[Error]Cant't download: %s" % (img_link)

    def download_pages_img(self, url):
        '''下载网页中的图片

            @dir 保存到本地的路径
            @url 网页url
        '''
        m = self.URL_REG.match(url)
        if not m:
            print '[Error]Invalid URL: ', url
            return
        host = m.group(1)

        imgs = self.extract_img_links(url)

        # 下载图片
        for idx, img in enumerate(imgs):
            if -1 != img.find("gif"):
                self.download_img(os.path.join(self.base_dir, ""), img)

def main():
    if len(sys.argv) != 3:
        print 'Invalid argument count.'
    return
    dir, url = sys.argv[1:]
    download(dir, url)

if __name__ == '__main__':
    # download('D:\\Imgs', 'http://www.163.com')
    spyder = MySpider("d:\imgs")
    spyder.download_pages_img("http://www.yyp6.com/read.php?tid=1502926")
