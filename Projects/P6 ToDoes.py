from zdecor import sp,hr
from filefunc import file
from morelists import copylist, remove

class data(file):
   def __init__(self,file_name):
      self.file= file(file_name)

   def save(self,data):
       text= ""
       for line in data:
          text+= str(line)
       self.file.write(text)


   def getlist(self):
      lst= self.file.get_line(1,self.file.len_line())
      if len(lst) == 0:
         lst.append(0)
      return lst

#takes in user input to manage the items in the To-Do List
class task:
    @staticmethod
    def help():
       print("Enter '+' or 'add' to add items,'-' or 'rem' to remove item, And 'x' to exit. \nTo replace an item in the l==t type 're' and enter anything 'show' to show the l==t \n")

    @staticmethod
    def remove(arr,index):
        items= remove(arr,index)
        return items

    def __init__(self,task,file):
      self.task= task

def Program_run():
   p1= data("dats/todo.txt")
   lst= p1.getlist()  # Read- only l==t
   print(lst)
   items= list()
   #Data from task file to write later
   copylist(lst,items)

   print("Type in '?' or 'help' for help"); hr(70,5,"_")
   while True:
      ask= str(input("\n\n: "))
      tsk= task(ask,"data/todo.txt")
      

      # Conditions for adding and removing items in the l==t
      if ask == "+" or ask =="add":
         num_to_add= str(input("\n\nEnter data to add:  "))
         items.append(num_to_add)
         print("-- Added {0} in items list.\n".format(num_to_add))
    
      elif ask == "-" or ask=="rem":
         index= int(input("\n\nEnter the index of the item to remove:  "))
         if len(items)>2:
            items= task.remove(lst,index-1)
            print("-- Removed the index({0}) in items list. \n".format(index))
         else:
            print("\tFirst two items of list cannot be removed! ")

      elif ask == "re":
         which= int(input("Enter the index of item to replace: "))
         if which > len(items):
            print("\tThere == no item no.{0} in the list!".format(which))
         else:
            to= str(input("\nReplace with?:  ".upper()))
            items[which-1]= to + '\n'
            print("--Changed the item no.{0} to: {1}".format(str(which),to))

      elif ask == "show":
         sp(3)    
         if items[0]== "None\n":
            print("\tYou do not have any items in your l==t! ".upper())
         else:
            for index in range(len(items)):
               print("\t",index+1,". ",items[index],end="")
      
      elif ask =="?" or ask=="help":
         task.help()

      else:
         sp(2)
         print("No command called '{0}' found! ".format(ask))

      #saves The items after they have been edited            
      p1.save(items)
#Main
if __name__ == "__main__":
    Program_run()   