import random
target = random.randint(0,100)
print(target)
while True:
    try:
        guessed_num = float(input("guess a number between 0 and 100:"))
        if guessed_num<0 or guessed_num>100:
            print("Enter a valid number between 0 and 100")
        else:
            if round(guessed_num) in range(target-5,target+6):
                print("You have guessed correctly")
                break
            elif guessed_num<target:
                print("the number guessed is less than target number")
            else:
                print("the number guessed is greater than target number")
        print(guessed_num)
    except Exception as e:
        print("Your input is not valid",e)
    