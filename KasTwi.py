# coding: utf-8

import os
import os.path
import fnmatch
import subprocess
import wget 
import bs4
import urllib, urllib2

def execute(root_path):
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            if fnmatch.fnmatch(filename, u"*.pdf"):
                org_path = os.path.join(dirpath, filename)
                ppp = dirpath + "/images/"
                ppp_path = os.path.join(ppp, filename)
                png_path = ppp_path.replace(".pdf", ".png")
                print(png_path)

                print "convert {0} to {1}".format(org_path, png_path)

                if subprocess.call(["convert", "-density", "150", "-trim", org_path, png_path]) != 0:
                    print "failed: {0}".format(org_path)

def kasumi_search():
    url = "https://www.kasumi.co.jp/tenpo/kennan/technopark_sakura.html"
    ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36"
    header = {"User-Agent" : ua}
    val = {"name":"hoge","location":"huga", "language":"piyo"}
    data = urllib.urlencode(val)
    req = urllib2.Request(url, data, header)
    kasumi_soup = bs4.BeautifulSoup(urllib2.urlopen(req))
    print(kasumi_soup)


if __name__ == '__main__':
    # root_path = raw_input("target folder path> ")
    # execute(root_path)
    # url = "https://www.kasumi.co.jp/tenpo/kennan/technopark_sakura.html"
    # wget.download(url)

    kasumi_search()