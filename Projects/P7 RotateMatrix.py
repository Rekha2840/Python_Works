
try:
   import numpy as np
   def rotate(times,dir="right"):
      np_dir= np.empty(9)
      np_matrix= np.arange(1,10)
      np_changer= np.arange(1,10)
      #EX: right(-2) == left(+2)
      if times < 0:
         times= abs(times)
         if dir == "right": dir = "left"
         elif dir == "left": dir = "right"
      if dir=="right":
         np_dir= np.array([3,0,1,6,4,2,7,8,5])
      elif dir=="left":
         np_dir= np.array([1,2,5,0,4,8,3,6,7])
      #Iterating the indexes and overwriting the values
      for time in range(times):
         for index in range(9):
            np_changer[index]= np_matrix[np_dir[index]]
         np_matrix = np_changer
         np_changer= np.arange(1,10)
      return np_matrix

   def RotateMatrix():
      dirn= str(input("\nMove to which Direction( l or r): "))
      #First priority : right if nothing else is true
      dirn= "left" if dirn.startswith("l") or dirn.startswith("L") else "right"
      times= int(input("Rotate to {0} by how many times: ".format(dirn)))
      array= rotate(times,dirn)
      matrix= array.reshape(1,3,3)
      # Go one dimn down
      matrix= matrix[0]
      print("After rotating {0} times to the {1}, the matrix will look like: \n\n".format(str(times),dirn))
      for x in range(len(matrix)):
         for y in range(3):
            print("\t",matrix[x][y],end=" ")
         print("")

   if __name__ == "__main__":
      RotateMatrix()


except ImportError:
   def rotate(times,dir="right"):
      dir_index= list()
      matrix= list(range(1,10))
      changer= list(range(1,10))

      #EX: right(-2) == left(+2)
      if times < 0:
         times= abs(times)
         if dir == "right": dir = "left"
         elif dir == "left": dir = "right"
      if dir=="right":
         dir_index= [3,0,1,6,4,2,7,8,5]
      elif dir=="left":
         dir_index= [1,2,5,0,4,8,3,6,7]

      #Iterating the indexes and overwriting the values
      for time in range(times):
         for index in range(9):
            changer[index]= matrix[dir_index[index]]
         matrix = changer
         changer= list(range(1,10))
      return matrix


   def RotateMatrix():
      dirn= str(input("\nMove to which Direction(l or r [Default: r]): "))
      dirn= "left" if dirn.startswith("l") or dirn.startswith("L") else "right"
      times= int(input("Enter how many times you want to rotate the matrix to the {0}: ".format(dirn)))
      array= rotate(times,dirn)

      print("After moving {0} times to the {1}, the matrix will look like: \n\n".format(str(times),dirn))
      for num in range(1,10):
         print("\t",array[num-1],end=" ")
         if num%3==0:
               print("")


   if __name__ == "__main__":
      RotateMatrix()
