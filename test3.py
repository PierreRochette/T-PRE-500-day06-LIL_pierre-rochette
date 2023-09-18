import os, sys 

path = "/home/pierrerochette/Documents/Pré-MSC/T-PRE-500"
dirs = os.listdir(path)
for file in dirs :
    print(file)

out = os.path.basename(path)
print(out)

out2 = os.path.dirname(path)
print(out2)

out3 = os.path.isabs(path)
print(out3)

out4 = os.path.isdir(path)
print(out4)

out5 = os.path.isfile(path)
print(out5)

for root, dirs, files in os.walk(path, topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))