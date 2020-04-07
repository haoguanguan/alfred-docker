#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import os
import sys

class Items(object):
    def __init__(self):
        self.items = list()

    def append(self, url):
        self.items.append(url.get_map())

    def construct_str(self):
        return json.dumps({"items":self.items})

    def __repr__(self):
        return self.construct_str()

class Url(object):
    """
    define a chrome bookmarks
    """
    def __init__(self, key_word, url, folder_name):
        self._article_key_word = key_word
        self._url = url
        self._folder_name = folder_name

    def __repr__(self):
        return str([self._article_key_word, self._url, self._folder_name])

    def get_list(self):
        """
        transfer inner variable into list
        """
        return [self._article_key_word, self._url, self._folder_name]

    def contain_key_word(self, key_word):
        """
        judge whether container pointer key word
        """
        st_word = self._article_key_word.upper()
        key_word = key_word.decode('utf-8').upper()
        return st_word.find(key_word) != -1

    def get_map(self):
        return {
            "title":self._article_key_word,
            "subtitle":self._url,
            "arg":self._url,
        }


def handle_json(json):
    res = []
    if json["type"] == "folder":
        for j in json["children"]:
            res.extend(handle_json(j))
    elif json["type"] == "url":
        item = Url(json['name'], json['url'], json['name'])
        res.append(item)

    return res

def parse_file(filename):
    """
    Get all bookmarks
    """
    data = None
    result = list()

    try:
        with open(filename) as json_fd:
            data = json.load(json_fd)
    except Exception as _:
        data = ""

    if data:
        # parse data
        try:
            targets = ["bookmark_bar", "other", "synced"]
            for d in targets:
                result.extend(handle_json(data["roots"][d]))
        except Exception as e:
            result = list()
    return result

def find(articles, key_word):
    """
    find all articles which containers key_word
    """
    res = list()
    for article in articles:
        if article.contain_key_word(key_word):
            res.append(article)

    return res

def main():
    """
    main entry
    """
    bookmarks = '/root/chrome_bookmarks'
    search_word = sys.argv[1]
    articles = parse_file(bookmarks)
    alternative = find(articles, search_word)

    items = Items()
    if alternative:
        for item in alternative:
            items.append(item)
    else:
        items.append(Url('Sorry', 'http://www.baidu.com', 'linux'))

    print items.construct_str()

if __name__ == "__main__":
    main()
