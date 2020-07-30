#Sheina Lussato 336089891
#Herold Tahar 342611274
import lxml.html
import requests


pending = {}    # url => priority
visited = {}    # url => (priority, [urls])
url_prior = dict()


def getNextUrl():
    max = None
    url = None
    i = 0
    for k, v in url_prior.items():
        if i == 0 or v > max:
            max = v
            url = k
        i = i + 1
    return url


def crawl(url, xpaths):
    if len(visited) == 100:
        return []
    if url not in url_prior:
        url_prior[url] = 1
    url_priority = url_prior[url]
    if pending.get(url) is not None:
        pending.pop(url)
    visited[url] = (url_priority, [])
    res = requests.get(url)
    doc = lxml.html.fromstring(res.content)
    children = {}   # make sure we don't process the same child url twice.
    for xpath in xpaths:
        for t in doc.xpath(xpath):
            try:
                found_url = t.attrib['href']
            except:
                found_url = t if "https://en.wikipedia.org" in t else "https://en.wikipedia.org" + t
            if found_url == url:
                continue
            if children.get(found_url):
                continue
            if found_url not in url_prior:
                url_prior[found_url] = 1
            else:
                url_prior[found_url] = url_prior[found_url] + 1
            children[found_url] = True
    visited[url] = (url_prior[url], children.keys())
    relations = []
    for child in children.keys():
        relations.append([url, child])
    try:
        url_prior.pop(url)
        return relations + [x for x in crawl(getNextUrl(), xpaths) if x not in relations]
    except:
        return []
