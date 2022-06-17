"""
Name(s):Wazz Oppenheiwmew
Name of Project:Count
"""

#Write the main part of your program here. Use of the other pages is optional.

num = int(input("Count up from 1 to 100:"))
if num == 1 :
  num += 1
  num2 = int(input("Good continue:"))
  while num2 == num :
    num2 = int(input("Good continue:"))
    num += 1
    if num == 100:
      print("Congratulations you did it!")
  if num2 == 420:
    print("Ha Ha. Start over")
  elif num2 == 715: 
    print("Beanis Wenis")
  else :
    print ("Nice try, start over though.")
else:
  print("wow...you messed up already")