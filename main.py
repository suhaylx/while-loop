
i = 0 
while i <= 50:
  print(i)
  i +=1
  break
#else:
# print("when it will executed")
print (i)


q = 0
while q < 50:
  print(q)
  break




#################################################################################
#using while and for 

my_list = list(range(1,100))
item = 0

while item < len(my_list):
  print(my_list[item])
  item +=1


for items in my_list:
  print(items)


###while true situations that asking for some action or process

while True:
  response = input("Say something : ")
  if(response == 'byee'):
    print ("Okay byee")
    break