#Functions for More Functionaliry Over Strings and Chars

from string import in_str

#CHARCTERS
class char:
   def __init__(self, ch):
      if len(ch) == 0:
         self.ch = "";
      else:
         self.ch = ch[0];  
      self.lower = "abcdefghijklmnopqrstuvwxyz";
      self.upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
   
   def to_upper(self):
      small_char = in_str(self.ch,self.lower);
      if small_char != "null":
         self.ch = self.upper[small_char];

   def to_lower(self):
      large_char = in_str(self.ch,self.upper);
      if large_char != "null":
         self.ch = self.lower[large_char];
   
   def __add__(self,other):
      return self.ch + other.ch;





