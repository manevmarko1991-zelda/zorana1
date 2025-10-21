
spaces=9
limit =9
i=0 #spacenumber
z=0 # free spaces
free_count = 0
occupied = [0, 1, 0, 0, 0, 0, 0, 1, 0]
i += 1
while i < spaces:
    if occupied[i] ==0:
        free_count +=1
        print("spot",i+1,"is free")
    else:
        free_count -=1
        print("spot",i+1,"is occupied")
        if free_count > spaces * limit/10:
            print ("full")
        else:
            print("free!")
