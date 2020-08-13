salaries={
  "jany" : 3242,
  "maty" : 5436,
  "jeff" : 6543,
  "grogg" : 2345,
  "marroi" :436436 
}
morethan3k = []
for keys in salaries:
   if salaries[keys] >= 3000 :
      morethan3k.append("{0}: {1}".format(keys,salaries[keys]))
print(morethan3k,"\n")









