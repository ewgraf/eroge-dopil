# -*- coding: cp1251 -*-
import os
import re
#+---------------------------------------------------+
#|                                                   |
#|               !#########       #                  |
#|             !########!          ##!               |
#|          !########!   Union of    ###             |
#|       !##########      Soviet      ####           |
#|     ######### #####     IIchan     ######         |
#|      !###!      !####!   Republics  ######        |
#|        !           #####            ######!       |
#|                      !####!         #######       |
#|                         #####       #######       |
#|                           !####!   #######!       |
#|                              ####!########        |
#|           ##                   ##########         |
#|         ,######!          !#############          |
#|       ,#### ########################!####!        |
#|     ,####'     ##################!'    #####      |
#|   ,####'            #######              !####!   |
#|  ####'                                      ##### |
#|  ~##        ALL HAIL THE MOTHERLAND!          #~  |
#|                                                   |
#+---------------------------------------------------+
# =======
# глобали
# =======
path = os.path.dirname(os.path.abspath(__file__))
prefix		= None		# префикс
affix		= "_old"	# постфикс
extension	= ".jpg"	# расширение переименовываемых файлов

files = os.listdir(path)# все файлы в папке "path"
for file in files:
	

for file in files:
	fileName, fileExtension = os.path.splitext(file)
	#if fileExtension == ".jpg":							# селектор цикла
		#origin  = os.path.join(path, file)
		#destiny = wrap(prefix, file, affix)
		#print fileName
		#os.rename(pats + file, )
		#fullPath = origin(path, file)

def wrap(prefix, file, affix):	# укутать строку
	fileName, fileExtension = os.path.splitext(file)
	return prefix + fileName + affix + fileExtension

def match(list, pattern):
	return re.findall(pattern, list)