"""
  Module name: filefuc
  Supports advance file manipulations
  v2.0: added urllib.request to allow http files reading ( for now only reading )
  
"""

import re
import string
import urllib.request


class file: 
      def __init__(self,file_path,type="r"):
         self.file_name= file_path; 
         self.file= open(file_path,type)
      def close(self):
         self.file.close();   

      def openc(self,dfile= "defl"): #counter file open function for readlines()
         if dfile is "defl": dfile= self.file_name;
         cfile= open(dfile,"r")
         lines= cfile.readlines();
         return lines

      def find_ltr(self,letter):
         lines_with_ltr= [];
         for line in self.file:
            line= line.rstrip();
            scan= re.findall(r"{0}".format(letter),line)
            if len(scan) > 0:
               lines_with_ltr.append(line)
         return lines_with_ltr;


      def len_ltr(self,letter):
         return len(self.find_ltr(letter))

      def len_line(self): #how many lines are there in the file
         return len(self.find_ltr(""));


      def get_nums(self):
         arr= []; rsl= []; num= "";
         for line in self.file:
            line= line.rstrip();
            nums= re.findall(r'[0-9]+',line)
            if len(nums) > 0:
               arr.append(nums);
         print("The numbers from {0} are: ".format(self.file_name))            
         for c in range(len(arr)):
            for x in arr[c]:
               num= "";
               num+= x;      
            num= int(num);   
            rsl.append(num)
         return rsl;   


      def get_line(self,strt,end="strt"):
            if end is "strt": end = strt;
            rsl= [];  count= 0;   
            self.lines= self.openc();
            if strt > len(self.lines) or end>len(self.lines):
              return list()
            for x in range(strt-1,end):
              rsl.append(self.lines[x]) 
            if len(rsl) is 1: return rsl[0]
            return rsl

      def words(self):
         counts = dict()
         for line in self.file:
            line = line.translate(str.maketrans('','',string.punctuation))
            line = line.lower()
            words = line.split()
            for word in words:
               if word not in counts:
                  counts[word] = 1
               else:
                  counts[word] += 1
         # Sort the dictionary by value
         lst = list()
         for key, val in list(counts.items()):
            lst.append((val, key))
         lst.sort()   
         return lst

      def lwords(self,max_num_words):
         file_words= self.words(); lst= list()
         for x, y in file_words[::-1][0:max_num_words]:
            lst.append((x,y))
         return lst

      # writing into file functions     
      def insert(self,line,text):
         try:
            data= ""; lines= self.openc();
            lines[line-1]= str(text)+'\n';
            for line in lines:
               data+= line;
            conn= open(self.file_name,"w")   
            conn.write(data)
            conn.close()
         except IndexError:
            print ("Argument1 exceed no of lines in file {0} i.e: {1} !!".format(self.file_name,self.len_line()))  

      def write(self,text):
          conn= open(self.file_name,"w")
          conn.write(text)
          conn.close();        

      def copy_file(self,file2,ctype= "from"): #default = from
         if ctype is "from":    #file2: write; file1 read;
            file1= file2;
            file2= self.file_name; 
         else:
            file1= self.file_name; 
         data= ""; lines= self.openc(file1);
         for line in lines:
            data+= line;
         conn= open(file2,"w");
         conn.write(data);
         conn.close();

      def clear(self,file_name="self"):
         if file_name is "self": file_name= self.file_name;
         conn= open(file_name,"w");
         conn.write(" ")
         conn.close();

      def cut_file(self,file2,ctype= "from"):
         self.copy_file(file2,ctype)
         self.clear(file2);



class http_file:
    def __init__(self,file_path):
       self.hfile_name= file_path;
       self.hfile= urllib.request.urlopen(file_path)

    def get_lines(self):
       cfile= urllib.request.urlopen(self.hfile_name)
       try:
          lines= cfile.readlines()
          return lines
       finally:
          cfile.close();

    def len_line(self):
        return len(self.get_lines())


    def download_file(self,url,file):
        urllib.request.urlretrieve(url,file)


