#!/usr/bin/env python
# coding=UTF-8
__author__ = 'Konstantin Maleev <simplevolk@gmail.com>'
import vkontakte
import requests
import os
import subprocess
import shlex
import pynotify

# инициализация приложения
def Init():
	vk=vkontakte.API('##id##','###token####')
	return vk
def IsOnline(uid):  #берем ID нужного пользователя
	online=vk.get('getProfiles',uids=uid,fileds='online')
	user=online[0]
	return user
def GetApiVK(): # не используется
	r = requests.get('https://api.vkontakte.ru/method/getProfiles?uid=40485295&fields=first_name,nickname,timezone,rate,contacts,online,counters')
	return r
#################
def Notification(user2): # вывод уведомления на экран.Внимание!Если в поле Title (1-е поле) оставить пустым,то выпадает с ошибкой
	if user2==1:
		print "Online"
		pynotify.Notification("1", "1").show()
	
	else:
		print "Offline"	
		pynotify.Notification("0", "0").show()
#################



##################
vk=Init()
user=IsOnline('1') # вводим ID нужного пользователя ВКонтакте.
Notification(user)


