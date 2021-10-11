from input import initialStack
import utils

initial_stack = initialStack()
# initial_node = [initial_stack, [0,0,0,4,4], 0]
stackSuccessor = []

# def initial_state():
#   return initial_node

def successors(stack):
    print(stack)
    for i in range (6):
        for j in range (6):
            if i != j and not utils.hasNothing(stack[i]):
                # for k in range (4):
                    if utils.isnotX(stack[i][0] ):
                        if utils.hasNothing(stack[j]):
                            stackSuccessor.append([i,j])
                            # stack[j].remove('X')
                            # stack[j].append(stack[i][k])
                            # stack[i].remove(stack[i][k])
                            # stack[i].insert(0,'X')
                        # # print(stack)
                        # else:
                        #     if space[j]!=0 and not hasNothing(stack[j]):
                        #         if stack[i][0]==stack[j][space[j]]:
                        #             print(i, j,space[j]-1)
                    
   


                # for k in range (4):
                #     if stack[i][k] is
    print(stackSuccessor)

def is_goal(stack):
    checker = 0
    for i in range(6):
        for j in range(4):
            if (stack[i][0] == stack[i][j] and utils.isnotX(stack[i][0])):
                checker+=1/4
    if checker == 4:
        print("Goal_State")
    else:
        successors(stack)
            

# is_goal(initial_stack)
# print(hasNothing(initial_stack[5]))





  
  


    