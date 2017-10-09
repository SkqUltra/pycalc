#!/usr/bin/python
# -*- coding: UTF-8 -*- 

def get_next1(str1):
	next = [-1]
	k = -1
	j = 0
	while j < len(str1) - 1:
		if k == -1 or str1[k] == str1[j]:
			k += 1
			j += 1
			next.append(k)
		else:
			k = next[k]
	return next

def get_next2(str1):
	next = [-1]
	k = -1
	j = 0
	while j < len(str1) - 1:
		if k == -1 or str1[k] == str1[j]:
			k += 1
			j += 1
			if str1[k] == str1[j]:
				next.append(next[k])
			else:
				next.append(k)
		else:
			k = next[k]
	return next

def kmp():
	str1 = raw_input("请输入1：")
	str2 = raw_input("请输入2：")
	next = get_next1(str2)
	print next
	i = 0
	j = 0
	while (i < len(str1) - 1 and j < len(str2) - 1):
		if j == -1 or str1[i] == str2[j]:
			i += 1
			j += 1
		else:
			j = next[j]
	if j == len(str2) - 1:
		return i - j
	return -1

	# str str1 = input("input str1:");
	# str str2 = input("input str2:");

if __name__ == '__main__':
	print kmp()