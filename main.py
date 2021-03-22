import random


my_intlist = [1, 2, 3, 4, 5]
my_charlist2 = ['Mother', 'Father', 'Suyash', 'Sanjna']
my_daylist = ['Monday', 'Tudesday', 'Wednesday', 'Thursday', 'Friday']

for e in my_intlist:
  print(e)

for name in my_charlist2:
  print(name)

  for day in my_daylist:
    print (day)

my_list = []
for i in range(10):
  my_intlist.append(random.randint(1,100))
  
print(my_intlist)