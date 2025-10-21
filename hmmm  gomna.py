while True:
    a=float(input("enter value:"))
    i=0
    a=a*0.38
    while a < 6:
         if a<5:
            a=a+1.2
            print("value increased to ",a)
            i=i+1
         else:
            a=a-0.3
            print ("value decrieased to ",a)
            if i > 10:
                print ("loop stopped automaticlly" )
                break
    print ("final value",a)
    print ("total steps:",i)
    again=input("do u want to run again? (yes/no):").lower()
    if again != "yes":
        print("program ended.")
    breakpoint
