 #Module name File.py
#Created by Shubham Tiwary
#Date : 2020 - 7 - 3

import re
class File:
	def __init__(self,filename):
		self.file = filename
		self.__cont = []
		self.__cont_str = ""
				
	def getcont(self):
		try:
			file = open(self.file)
			self.__cont = file.readlines()
			for cont in self.__cont:
				self.__cont_str += cont			
		except:
			raise ValueError("File Not Found")
		finally:
			file.close()
	
	#Gets data from start to end lines into a list
	def getline(self,strt=0,end=""):
		 self.getcont()
		 if end == "":
		 	end = strt + 1
		 else: end +=1
		 lines = [self.__cont[line][:-1] for line in range(strt,end)]
		 return lines
	
	#Writes on a specific line on file	 		 
	def writeline(self,line,cont):
		 self.getcont()
		 newlst = list()
		 for x in range(len(self.__cont)):
		 	if not x+1 == line:
		 		newlst.append(self.__cont[x])
		 	else:
		 		newlst.append(cont+'\n')
		 		
		 newcont = ""
		 for c in newlst: newcont += c
		 f1 = open(self.file,"w")
		 f1.write(newcont); f1.close()
	
	#Gets Data from file into a dictionary	 	 
	def getdata(self,**data):
		 	self.getcont()
		 	content = self.__cont_str
		 	ptrn = r"([\w]+:[\w\d]+)"
		 	raw_dat = re.findall(ptrn,content)	
		 	for dat in raw_dat:
		 		attr = re.findall(r"([\w]+)",dat)
		 		data[attr[0]] = attr[1]
		 	return data				 					 		 							 					 		 

