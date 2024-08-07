pos = 0
flag = False
def search(ls,find):
   global pos, flag
   while pos < len(ls):
      if ls[pos] == find:
        flag = True
        print(f"The {find} Is At {pos+1}")
      else:
         flag = False
      pos += 1
    
mlist = [10,20,25,30,65]
search(mlist,25)
      

    

