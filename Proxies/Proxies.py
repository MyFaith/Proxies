# coding: utf-8

import requests, math
import gevent
from gevent.queue import Queue
from gevent import monkey; monkey.patch_all()
from pyquery import PyQuery

class Proxies():
    def __init__(self):
        self.domestic_gn_url = 'http://www.kuaidaili.com/free/inha/{0}/'
        self.domestic_pt_url = 'http://www.kuaidaili.com/free/intr/{0}/'
        self.abroad_gn_url = 'http://www.kuaidaili.com/free/outha/{0}/'
        self.abroad_pt_url = 'http://www.kuaidaili.com/free/outtr/{0}/'
        self.result_arr = []
        self.s = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
            'Referer': 'http://www.kuaidaili.com/'
        }

    def fetch_urls(self, queue, quantity):
        while not queue.empty():
            url = queue.get()
            html = self.s.get(url, headers=self.headers).text
            pq = PyQuery(html)
            size = pq.find('tbody tr').size()
            for index in range(size):
                item = pq.find('tbody tr').eq(index)
                ip = item.find('td').eq(0).text()
                port = item.find('td').eq(1).text()
                _type = item.find('td').eq(3).text()
                self.result_arr.append({
                    str(_type).lower(): '{0}://{1}:{2}'.format(str(_type).lower(), ip, port)
                })
                if len(self.result_arr) >= quantity:
                    break

    def get_proxies(self, quantity, type):
        '''
        quantity: 数量
        type: 类型
            1.国内高匿代理
            2.国内普通代理
            3.国外高匿代理
            4.国外普通代理
        '''
        url_queue = Queue()
        need_pages = math.ceil(quantity/15)
        # 判断类型
        if type == 1:
            # 国内高匿代理
            base_url = self.domestic_gn_url
        elif type == 2:
            # 国内普通代理
            base_url = self.domestic_pt_url
        elif type == 3:
            # 国外高匿代理
            base_url = self.abroad_gn_url
        elif type == 4:
            # 国外普通代理
            base_url = self.abroad_pt_url
        # 获取所需要的页面URL
        for index in range(need_pages):
            url = base_url.format(index+1)
            url_queue.put(url)
        # 处理所有URL,开启2个协程
        gevent_list = []
        for index in range(2):
            gevent_list.append(
                gevent.spawn(self.fetch_urls, url_queue, quantity)
            )
        gevent.joinall(gevent_list)

    def get_result(self):
        return self.result_arr

if __name__ == '__main__':
    p = Proxies()
    p.get_proxies(20, 1)
    result = p.get_result()
    print(result)
