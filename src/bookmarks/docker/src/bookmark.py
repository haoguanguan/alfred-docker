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
            bookmark_bar = data['roots']['bookmark_bar']['children']
            # for each list
            for folder in bookmark_bar:
                folder_name = folder['name']
                marks = folder['children']

                # for each marks
                for article in marks:
                    item = Url(article['name'], article['url'], folder_name)
                    result.append(item)

            bookmark_bar = data['roots']['other']["children"]
            for  d in bookmark_bar:
                folder_name = "other"

                item = Url(d['name'], d['url'], folder_name)
                result.append(item)
        except Exception as e:
            print e
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
