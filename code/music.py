import threading
import time
import tkinter as tk
import os
from lxml import etree
import requests
import webbrowser
import re
import json
class Spider(object):
	starname = 'AJonnyCool'
	# url = 'http://king.junyuewl.com/api.php?callback=jQuery111307253625129728498_1563796139283'
	# url_ku_gou = 'http://king.junyuewl.com/api.php?callback=jQuery111307253625129728498_1563797077768'
	url_ku_gou = 'http://king.junyuewl.com/api.php?'
	data = {'types': 'search', 'count': '666', 'source': 'kugou', 'pages': '1', 'name': starname}
	header = {'Host':'king.junyuewl.com','Referer':'https://y.qq.com/portal/search.html','Content-Type':'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0'}
	music_info =[]
	def index_request(self):

		str = input()
		self.starname = str
		self.data['name'] = str
		response=requests.post(self.url_ku_gou,data=self.data,headers=self.header)
		# print(response.text)
		# jsonres=re.findall(r'jQuery111307253625129728498_1563797077768\((.*)\)',response.text,re.S)
		# res = json.loads(''.join(jsonres))
		res = json.loads(response.text)
		self.music_info =[]
		self.music_info = res
		# print(res)
		for i in res:
			try:
				self.download_music(i)
			except Exception as e:
				print(e)
				
			# time.sleep(1)
	def download_music(self,music):
		music_url='http://king.junyuewl.com/api.php?'
		data = {'types':'url','id':music['id'],'source':'kugou'}
		response=requests.post(music_url,data=data,headers=self.header)
		res=json.loads(response.text)
		# print(music['name'])
		# print(res['url']
		# print(response.text)
		if len(res['url'])>0:
			# print(res['url'])
			path = 'F:/python/音乐下载/'+self.starname
			ispath=os.path.exists(path)
			if not ispath:
				os.mkdir(path)
			name = 'F:/python/音乐下载/'+self.starname+'/'+music['name']+'.mp3'
			isname=os.path.exists(name)
			# 如果不存在，才下载
			if not isname:
				res = requests.get(res['url'])
				with open(name,'wb') as fw:
					fw.write(res.content)
					fw.close()
					print(music['name']+'.mp3'+'下载完成！！！')
			else:
				print(name+'  已经存在-----')
	def getmusicnum(self):
		return len(self.music_info)
	
if  __name__== '__main__':
	spider=Spider()
	spider.index_request()
	print('---一共%d首歌曲---'%spider.getmusicnum())