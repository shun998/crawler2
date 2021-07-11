# -*- coding: utf-8 -*-
# TODO  网易云评论
# @Date    : 2021/7/11 9:19
# @Author  : layman
# window.asrsea 加密
# encSecKey "7612fd451a00df413951efd00430b64558df17f7208042b1ed12546d10dac63b2707b06f45a58dc3c1d87ec62c9e08e4ec49f5ef11341a66fa9d1dd1f091ea5f72b19a98fed333a4e5cdc4f797ccfbfdebeb185e900187dd79273e06cf1b90532aa85e5b0c42f1693c58d38819db22542dc21566e5b9bfe32dad1bea821c4706"
# encText   "QBXUUyvh7kExGKuMYpQk9VO1XuBxTwyGaWJLSuK+2Ew6Qrdd2jpC3xXK+za2eiPazr7pTNwSLg545AnAmuTl6wa6C3ZD5B6gMGVu/pPa9XzwxGsTO8s9ETLhu3LPHCwZNWi3zsk00uyCSQSnLI050YTJzFRqgQ2fwW68IfwCZ/4GmGnWRPfcu99/xLvnMxlbwUmjBPDKBDks8/2O5eLUB5JY61/d879Y9FjkkOb3cDMJ/sZeo4AyzhG6yuyUH5EAYFXkzzACiFlBlB5UVk+FS2Fkq8BSIOgOpgbYrfHwOEc="
# data "rid=R_SO_4_1847256510&threadId=R_SO_4_1847256510&pageNo=1&pageSize=20&cursor=-1&offset=0&orderType=1"
# csrf_token: ""
# cursor: "-1"
# offset: "0"
# orderType: "1"
# pageNo: "1"
# pageSize: "20"
# rid: "R_SO_4_1847256510"
# threadId: "R_SO_4_1847256510"
import json

import requests
from Crypto.Cipher import AES
from base64 import b64encode


# 处理加密过程
"""
 function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c  # 16个随机字符串
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) { d:数据 e:定值 f:定值 g:定值
        var h = {}
          , i = a(16); # # 16个随机字符串
        return h.encText = b(d, g), 
        h.encText = b(h.encText, i),#params
        h.encSecKey = c(i, e, f), # encSecKey
        h
        """
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "IkbLnhK8zaKjPq5I"
encSeckey = "8e83a731c7d1bbfbebc2830a339eb2f471b731e856890756948337160f77af64b2d67bc447bac2b1a1781927ecf7ad499bbf8fd804a777033cf723da4eea253713412ace8fca9e26d6e1a2f3af5eacc4b319904732f0f354332c32c2343c1f7e1194d6bf316c63e32457fce1964aca0b790724f64c8a65754e867262581372ed"
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
data = {"csrf_token": "",
        "cursor": "-1",
        "offset": "0",
        "orderType": "1",
        "pageNo": "1",
        "pageSize": "20",
        "rid": "R_SO_4_1847256510",
        "threadId": "R_SO_4_1847256510"}

def get_encSecKey():
    return encSeckey


def get_params(data):
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second


def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def enc_params(data, key):
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode("utf-8"))  # 加密
    return str(b64encode(bs), "utf-8")

headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
resp = requests.post(url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
},headers=headers)
print(resp.text)
