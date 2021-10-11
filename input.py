A=[]
B=[]
C=[]
D=[]
E=['X','X','X','X']
F=['X','X','X','X']
list = [A,B,C,D,E,F]

def initialStack():
  with open('input/input1.in') as f:
      lines = f.readlines()
  input=lines

  

#   initlist = [A,B,C,D]
#   rand= [0,2,4,6]
#   for i in range (4):
#           for j in range (rand[i],8,8):
#               initlist[i].append(input[i][j])
#   return list
  
  for i in range (4):
    for j in range (0,8,8):
      A.append(input[i][j])
  for i in range (4):
    for j in range (2,8,8):
      B.append(input[i][j])
  for i in range (4):
    for j in range (4,8,8):
      C.append(input[i][j])
  for i in range (4):
    for j in range (6,8,8):
      D.append(input[i][j])
  return list

  
# initialStack()
# print(list)
