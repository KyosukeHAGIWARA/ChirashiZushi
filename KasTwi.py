# coding: utf-8

import os
import fnmatch
import subprocess
import wget 
import bs4
import urllib, urllib2
import re
from time import sleep
from datetime import datetime

now = datetime.now().strftime("%s")
print(now)
os.makedirs("data/"+now)

def chirashi_search():
    dat = open("./data/kasumi_sakura.html", "r").read()
    kasumi_soup = bs4.BeautifulSoup(dat, "lxml")
    chirashis = []
    for chirashi in kasumi_soup.select("#chirashiList1")[0].children:
        c_id = chirashi.get("id")
        c_scheme = chirashi.select(".shufoo-scheme")[0].contents[0]
        c_url = chirashi.select(".shufoo-pdf")[0].a.get("href")
        c_data = (c_id, c_scheme, c_url)
        chirashis.append(c_data)
    return chirashis


def gen_chirashi_pdf(c_data):
    target = c_data[2]
    red = urllib2.urlopen(target).read()
    red_soup = bs4.BeautifulSoup(red, "lxml")
    url = red_soup.meta.get("content").lstrip("0;URL=")
    path = "./data/" + now + "/" + re.findall(r"[0-9]+", c_data[0])[0] + ".pdf"
    if subprocess.call(["python", "-m", "wget", "-o", path, url]) != 0:
                    print "failed: {0}".format(url)
    return path


def pdf_to_png(root_path):
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            if fnmatch.fnmatch(filename, u"*.pdf"):
                org_path = os.path.join(dirpath, filename)
                ppp = dirpath
                ppp_path = os.path.join(ppp, filename)
                png_path = ppp_path.replace(".pdf", ".png")
                print(png_path)

                print "convert {0} to {1}".format(org_path, png_path)

                if subprocess.call(["convert", "-density", "150", "-trim", org_path, png_path]) != 0:
                    print "failed: {0}".format(org_path)


if __name__ == '__main__':
    # root_path = raw_input("target folder path> ")
    # execute(root_path)
    # url = "http://ipqcache2.shufoo.net/c/2016/05/12/c/3715862491748/index/img/chirashi.pdf?shopId=116936&amp;chirashiId=3715862491748"
    # wget.download(url, out="./hhhhh.pdf")

    chirashis = chirashi_search()
    for chirashi in chirashis:
        path = gen_chirashi_pdf(chirashi)
        sleep(5)
        pdf_to_png("./data/")
