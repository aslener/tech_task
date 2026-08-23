import random
target = random.randint(0,100)
while True:
    try:
        guessed_num = int(input("guess anumber between 0 and 100:"))
        if guessed_num<0 or guessed_num>100:
            print("Enter a valid number between 0 and 100")
        else:
            if guessed_num==target:
                print("You have guessed correctly")
                break
            elif guessed_num<target:
                print("the number guessed is less than target number")
            else:
                print("the number guessed is greater than target number")
    except Exception:
        print("Your input is not valid")
    