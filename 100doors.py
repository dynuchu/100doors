#Creating the list for the doors
doors = [False]*100

#defining the door alternating function
def doors_open():
    global doors
    for i in range(100): 
        for j in range(i, 100, i+1):
            if doors[j] == True:
                doors[j] = False
            else:
                doors[j] = True         
    for i in range(0,100):   
        if doors[i] == True:
            if i<99:
                print("%i," % (i+1), end=" ") 
            else:
                print("%i" % (i+1), end=" ")       

print("The following doors are opened: ", end=" ")
doors_open()
print("\n")



