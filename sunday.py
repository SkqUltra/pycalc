#!/usr/bin/python
#-*- coding: UTF-8 -*- 

def get_next(str2):
	next = {}
	for i in range(len(str2)):
		if next.has_key(str2[i]) == False:
			next[str2[i]] = i
	return next

def sunday():
	str1 = raw_input("请输入1：")
	str2 = raw_input("请输入2：")
	next = get_next(str2)
	i = 0
	j = 0
	while(i < len(str1) and j < len(str2)):
		if str1[i] == str2[j]:
			i += 1 
			j += 1
		else:
			if i - j + len(str2) >= len(str1):
				j = 0
				i = len(str1)
			elif next.has_key(str1[i - j + len(str2)]) == False:
				i = i - j + len(str2) + 1
				j = 0
			else:
				i = i - j + len(str2) - next[str1[i - j + len(str2)]]
				j = 0
	if j == len(str2):
		return i-j
	else:
		return -1


if __name__ == '__main__':
	print sunday()