# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/11 8:38
# @Author  : layman
import requests

url = "https://www.pearvideo.com/video_1734741"
cont_Id = url.split("_")[1]
# video_status=f"https://video.pearvideo.com/mp4/adshort/20210710/cont-{cont_Id}-15715772_adpkg-ad_hd.mp4"
video_status = f"https://www.pearvideo.com/videoStatus.jsp?contId={cont_Id}&mrd=0.83569543577246"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Referer": url}
resp = requests.get(video_status, headers=headers)
dic = resp.json()
src_url = dic["videoInfo"]["videos"]["srcUrl"]
system_time = dic["systemTime"]
# https://video.pearvideo.com/mp4/adshort/20210710/cont-1734741-15715772_adpkg-ad_hd.mp4
# https://video.pearvideo.com/mp4/adshort/20210710/1625964243946-15715772_adpkg-ad_hd.mp4
src_url = src_url.replace(system_time, f"cont-{cont_Id}")
print(src_url)
