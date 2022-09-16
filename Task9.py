#getting values
value1 = int(input())
value2 = int(input())
value3 = int(input())

#evaluating which one is larger
if value1 < value2 < value3:
  print(value1,value2,value3)
  
elif value1 < value3 < value2:
  print(value1,value3,value2)
  
elif value2 < value1 < value3:
  print(value2,value1,value3)
  
elif value2 < value3 < value1:
  print(value2,value3,value1)
  
elif value3 < value1 < value2:
  print(value3,value1,value2)
  
elif value3 < value2 < value1:
  print(value3,value2,value1)
