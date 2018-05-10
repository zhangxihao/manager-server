# -*-coding:utf-8-*-
import requests

__author__ = "chenjian"

import time,json
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import http.cookiejar
from . import common


"""
POST
"""
def post(url,parms,headers):
    try:
        data = urllib.parse.urlencode(parms)
    except:
        data = parms
    if headers == '':
        req = urllib.request.Request(url, data)
    else:
        req = urllib.request.Request(url, data,headers)
    try:
        response = urllib.request.urlopen(req)
        code = response.code
        responsedata = response.read()
        responsedata = json.loads(responsedata)
        return responsedata,code
    except Exception as e:
        print(e)
        return None,e.code


"""
POST and save cookie
"""
def post_and_save_cookie(url,parms,headers):
    fp = common.createFile('cookie')
    c = http.cookiejar.LWPCookieJar(fp)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(c))
    try:
        data = urllib.parse.urlencode(parms)
    except:
        data = parms
    if headers == '':
        req = urllib.request.Request(url, data)
    else:
        req = urllib.request.Request(url, data,headers)

    try:
        response = opener.open(req)
        code = response.code
        responsedata = response.read()
        responsedata = json.loads(responsedata)
        c.save(ignore_expires=True, ignore_discard=True)
        time.sleep(3)
        return responsedata,code

    except Exception as e:
        print(e)
        return None,e.code

"""
POST with cookie , make sure has the cookie first.
"""
def post_with_cookie(url,parms,headers):
    cookiefile = common.loadFilePath('cookie')
    assert cookiefile != None
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load(cookiefile, ignore_discard=True, ignore_expires=True)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    try:
        data = urllib.parse.urlencode(parms)
    except:
        data = parms
    if headers == '':
        req = urllib.request.Request(url, data)
    else:
        req = urllib.request.Request(url, data,headers)


    try:
        response = opener.open(req)
        code = response.code
        responsedata = response.read()
        responsedata = json.loads(responsedata)
        return responsedata,code

    except Exception as e:
        print(e)
        return None,e.code

"""
GET
"""
def get(url,parms,headers):
    try:
        data = urllib.parse.urlencode(parms)
    except:
        data = parms
    req = urllib.request.Request(url,data)
    try:
        response = urllib.request.urlopen(req)
        code = response.code
        responsedata = response.read()
        responsedata = json.loads(responsedata)
        return responsedata,code
    except Exception as e:
        print(e)
        return None,e.code


"""
post file
"""
def post_file(url,files):
    try:
        response = requests.post(url, files=files)
        code = response.code
        _response = response.content
        responsedata = json.loads(_response)
        return responsedata,code
    except Exception as e:
        print(e)
        return None,e.code
