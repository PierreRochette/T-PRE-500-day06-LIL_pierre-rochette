import os 

path = "/home/pierrerochette/Documents/Pré-MSC/T-PRE-500"

for root, dirs, files in os.walk(path, topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

# Le module os.walk() fait déjà appel à la récursivité