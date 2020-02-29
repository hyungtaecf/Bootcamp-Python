import random

def guess_result(guess):
    # Generating the clues
    result = "Nope"
    if guess>=100 and guess<1000:
        if str(to_array(guess)[0]) in code or str(to_array(guess)[1]) in code or str(to_array(guess)[2]) in code:
            result="Close"
            if str(to_array(guess)[0]) == code[0] or str(to_array(guess)[1]) == code[1] or str(to_array(guess)[2]) == code[2]:
                result="Match"
                if str(to_array(guess)[0]) == code[0] and str(to_array(guess)[1]) == code[1] and str(to_array(guess)[2]) == code[2]:
                    result="That is the code!"
        return result
    return "You are supposed to guess a 3-digit number!"

def to_array(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num //= 10
    return pos_nums[::-1]

print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")

# Generating Code
digits = [str(num) for num in range(10)]
random.shuffle(digits)
code = digits[:3]
code_is_broken = False
print("Code has been generated, please guess a 3 digit number")

# Running Game Logic
while code_is_broken == False:
    # Getting guess
    guess = int(input("What is your guess? "))
    result = guess_result(guess)
    print("Here is the result of your guess: ")
    print(result)
    if result == "That is the code!":
        code_is_broken=True
