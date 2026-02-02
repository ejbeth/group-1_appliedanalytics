def OutputNumber():
    stop="no"
    num = 0

    while (stop!= "yes"):   
        print(num)
        num =num + 1
        stop = input("Do you want to stop? Yes/No: ")
    print("You have exited the loop.")
    
OutputNumber()
