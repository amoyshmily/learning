from urllib import request
import urllib
from urllib import parse
import time

# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
my_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/65.0.3325.146 Safari/537.36'}


def crawl_page(page_url):
    print('...crawling')
    req = request.Request(page_url, headers=my_header)
    res = request.urlopen(req).read()

    return res


def save_page(html, file_name):
    print('...saving to'+file_name)
    with open(file_name, 'wb') as file:
        file.write(html)

    print('------------------------------------')


def tieba_spider(tieba_name, begin_page_num, end_page_num):

    url_base = 'http://tieba.baidu.com/f?{}'
    encoded_tieba_name = urllib.parse.urlencode({'kw': tieba_name})
    url_prefix = url_base.format(encoded_tieba_name)

    for page_num in range(begin_page_num, end_page_num+1):
        page_url = url_prefix+'&ie=utf-8&pn={}'.format(str((page_num-1)*50))
        file_name = '../download/'+tieba_name+'第'+str(page_num)+'页.html'

        html = crawl_page(page_url)
        save_page(html, file_name)

        time.sleep(3)


if __name__ == '__main__':
    tieba_spider('python', 1, 3)
