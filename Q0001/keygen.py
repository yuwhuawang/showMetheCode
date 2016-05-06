#coding:utf-8

import random,string

def keygen(len):
	"""
	随机生成给定长度的字符和数据混合字符串激活码,区分大小写

	"""
	CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"


	activationKey = string.join(random.sample(CHARACTERS,len)).replace(" ","")

	return activationKey

if __name__=="__main__":

	for i in range(1,201):
		print i,keygen(10)
