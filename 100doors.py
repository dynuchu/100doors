doors = [False]*100

def doors_close():
    global doors

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
            print(i+1,end=", ")            
    print("\n")

print("The following doors are opened: ")
doors_close()
doors_open()



#for i in doors[1:]:
#   doors[i]=False
#    if doors[i] == True:
#        print(i, end=", ")

#for j in doors[1:]:
#    doors[j] = False


#for i in doors[1:]:
#    j = not j:
#    if j == True:
#        print(i, end=", ")






