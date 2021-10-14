def get_host(url):
    """ 返回域名，如：https://www.baidu.com """
    ul = urlparse(url)
    return ul.scheme + '://' + ul.hostname


def add_host(url, path):
    return get_host(url) + path


def get_Html(url, headers, cookies=None, params=None):
    """ 返回网页内容 """
    if cookies:
        r = requests.get(url=url, headers=headers, cookies=cookies)
    else:
        r = requests.get(url=url, headers=headers)
    r.encoding = "utf-8"
    return etree.HTML(r.text)


def get_list(html, xpath):
    """ 返回指定位置的列表 """
    return html.xpath(xpath)


def save_list_B(filename, list):
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(json.dumps(list,ensure_ascii=False))
