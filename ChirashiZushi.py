#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import fnmatch
import subprocess
from bs4 import BeautifulSoup
import urllib2
from time import sleep
from datetime import datetime
from tweepy.auth import OAuthHandler
from tweepy.api import API
import ConfigParser


now = datetime.now().strftime("%s")
parent = "./data/" + now

shop_name = {
    "kasumi": "カスミ テクノパーク桜店",
    "marumo": "マルモ学園店",
    "aeon": "イオンつくば駅前店",
}


# scrape HP and get chirashi url,scheme
def get_chirashi_data(shop):
    chirashis = []
    
    if shop == "kasumi":
        html = open("./data/kasumi_sakura.html", "r").read()
        soup = BeautifulSoup(html, "lxml")
        for chirashi in soup.select("#chirashiList1")[0].children:
            c_id = chirashi.get("id")
            c_scheme = chirashi.select(".shufoo-scheme")[0].contents[0]
            before_url = chirashi.select(".shufoo-pdf")[0].a.get("href")
            second_html = urllib2.urlopen(before_url).read()
            second_soup = BeautifulSoup(second_html, "lxml")
            c_url = second_soup.meta.get("content").lstrip("0;URL=")
            c_data = {
                "url": c_url,
                "scheme": c_scheme.encode("utf-8"),
                "id": c_id,
            }
            chirashis.append(c_data)

    elif shop == "marumo":
        pass
    elif shop == "aeon":
        pass
    return chirashis


# generate pdf data from redirect URL
def gen_chirashi_pdf(url, dirpath, outname):
    path = dirpath + "/" + outname
    print("pathpath " + url)
    if subprocess.call(["python", "-m", "wget", "-o", path, url]) != 0:
                    print("pdf_error " + url)
                    tweet_error("@Rawashi_coins pdf_error " + url)


# convert Chirashi pdf to png
def pdf_to_png(root_path):
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            if fnmatch.fnmatch(filename, u"*.pdf"):
                org_path = os.path.join(dirpath, filename)
                ppp = dirpath
                ppp_path = os.path.join(ppp, filename)
                png_path = ppp_path.replace(".pdf", ".png")
                print("convert " + org_path +  " to " + png_path)
                if subprocess.call(["convert", "-density", "130", "-trim", org_path, png_path]) != 0:
                    print("failed: " + org_path)
                    tweet_error("@Rawashi_coins png_error " + org_path)


# tweet Chirashi images
def chirath(root_path, shop, scheme):
    api = API(get_oauth())
    reply_id = None
    text = "[" + shop_name[shop] + "] " + scheme + "のチラシ情報です"  
    for dirpath, _, filenames in os.walk(root_path):
        filenames.sort()
        filenames.reverse()
        for filename in filenames:
            if fnmatch.fnmatch(filename, "*.png"):
                st = api.update_with_media(filename=(root_path + "/" + filename), status="[testing] " + text, in_reply_to_status_id=reply_id)
                reply_id = st.id
                text = "(続き) " + text
                sleep(5)
        else:
            reply_id = None


# return twitter oath
def get_oauth():
    conf = ConfigParser.SafeConfigParser()
    conf.read("./twitter.ini")
    auth = OAuthHandler(conf.get("Twitter", "CK"), conf.get("Twitter", "CS"))
    auth.set_access_token(conf.get("Twitter", "AT"), conf.get("Twitter", "AS"))
    return auth


def tweet_error(text):
    auth = get_oauth()
    api = API(auth)
    api.update_status(status=text)


if __name__ == '__main__':
    os.makedirs(parent)
    for shop in shop_name.keys():
        shopdir = parent + "/" + shop
        os.makedirs(shopdir)
        chirashis = get_chirashi_data(shop)
        for i, chirashi in enumerate(chirashis):
            currentdir = shopdir + "/" + shop + str(i)
            os.makedirs(currentdir)
            outname = shop + str(i) + ".pdf"
            gen_chirashi_pdf(chirashi["url"], currentdir, outname)
            sleep(5)
            pdf_to_png(currentdir)
            sleep(10)
            chirath(currentdir, shop, chirashi["scheme"])
