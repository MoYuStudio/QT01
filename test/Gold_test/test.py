# -*- coding: UTF-8 -*-
# 本模块从上海黄金交易所官网下载历史交易数据
# https://www.sge.com.cn/sjzx/mrhqsj

import os
import time
from Lib.Web import get_Html, get_list, get_List_xpath, add_host
from Lib.os import save_list, save_list_A, save_list_B, makdir, BASE_PATH

headers = {
    'Referer': 'https://www.sge.com.cn/sjzx/mrhqsj',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}


def get_table(title, url, headers):
    table_xpath = '//div[@class="content"]/table/tbody/tr/td[1]/text()'
    html = get_Html(url, headers)
    doc = get_list(html, table_xpath)
    tab = []
    had = []
    n = len(doc)
    for r in range(1, n+1):
        table_xpath = '//div[@class="content"]/table/tbody/tr[%d]/td/text()' % r
        d = get_list(html, table_xpath)
        if r == 1:
            for i in d:
                had.append(str(i).replace('\t', '').replace(
                    '\n', '').replace('\r', ''))
        else:
            row = {}
            row['交易日期'] = title
            try:
                for i in range(len(d)):
                    row[had[i]] = str(d[i]).replace(
                        '\t', '').replace('\n', '').replace('\r', '')
            except Exception as e:
                pass
            tab.append(row)
    return tab


if __name__ == "__main__":

    # 获得下载链接
    for r in range(1, 201):
        url = 'https://www.sge.com.cn/sjzx/mrhqsj?p=%d' % r
        filename = 'list_%d.txt' % r
        cache_dir = "goldlist"

        html = get_Html(url, headers)

        if not os.path.exists(os.path.join(BASE_PATH, cache_dir)):
            makdir(os.path.join(BASE_PATH, cache_dir))

        filename = os.path.join(BASE_PATH, cache_dir, filename)
        if os.path.exists(filename):
            print("跳过：%s" % filename)
            continue

        a = '/html/body/div[6]/div/div[2]/div[2]/div[2]/ul/li/a/span[2]/text()'
        b = '/html/body/div[6]/div/div[2]/div[2]/div[2]/ul/li/a/@href'
        lst = get_List_xpath(html, a, b)
        for item in lst:
            lst[item] = add_host(url, lst[item])

        save_list_A(filename, lst)

        print('获取历史行情第%d页' % r)

        time.sleep(3)

    # 下载行情数据
    for r in range(1, 201):
        url = 'https://www.sge.com.cn/sjzx/mrhqsj?p=%d' % r
        filename = 'list_%d.txt' % r
        cache_dir = "goldlist"
        filename = os.path.join(BASE_PATH, cache_dir, filename)
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                line = f.readline()
                item, url = line.split('\t')
                filename = os.path.join(BASE_PATH, cache_dir, "%s.txt" % item)

                if os.path.exists(filename):
                    print("跳过：%s" % filename)
                    continue

                doc = get_table(item, str(url).replace('\n', ''), headers)
                save_list_B(filename, doc)

                print("保存：%s" % filename)

                time.sleep(3)