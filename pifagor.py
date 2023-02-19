import random 
from itertools import permutations, product
import operator
import os

player1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
player2 = player1.copy()

def roll_dice():
    digits = []
    for i in range(3):
        digits.append(random.randint(1, 6))
        print("Kube number ", digits[i])
    return digits

def check_number(num, digits):
    """
    Check if given number can be calculated from provided 2 or 3 digits
    """
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    if len(digits) == 3:
        for a, b, c in permutations(digits, 3):
            for op1 in ops.keys():
                for op2 in ops.keys():
                    try:
                        res = ops[op1](int(a), int(b))
                        res = ops[op2](res, int(c))
                        if res == num:
                            return True                        
                    except ZeroDivisionError:
                        pass
                    except:
                        pass
    elif len(digits) == 2:
        for a, b in permutations(digits, 2):
            for op1 in ops.keys():
                    try:
                        res = ops[op1](int(a), int(b))
                        if res == num:
                            return True                        
                    except ZeroDivisionError:
                        pass
                    except:
                        pass

    return False

#check_number(18, [3, 6, 2])
#check_number(7, [2, 3, 1])

def get_and_process_user_input(left_numbers):
    dices_result=roll_dice()
    #print("Your current numbers:")
    #print(left_numbers)
    user_digits = input("Enter up to 3 digits, separated by space: ")
    digit_list = [int(i) for i in user_digits.split()]

    if len(digit_list) == 3:
        #print(digit_list[0], digit_list[1], digit_list[2])
        for user_digit in digit_list:
            for left_number in left_numbers:
                if user_digit == left_number:
                    if user_digit not in dices_result:
                        print("Sorry there was no ",user_digit," in the dices")
                        continue
                    else:
                        try:
                            left_numbers.remove(user_digit)
                        except ValueError:
                            pass
    
    
    elif len(digit_list) == 2:  
        for user_digit in digit_list:
            if user_digit in dices_result:
                try:
                    left_numbers.remove(user_digit)
                    dices_result.remove(user_digit)
                    #digit_list.remove(user_digit)
                    print("removed ",user_digit)
                except ValueError:
                    pass
            elif check_number(user_digit, dices_result):
                try:
                    left_numbers.remove(user_digit)
                    print("removed ",user_digit)
                except ValueError:
                    pass

    elif len(digit_list) == 1:
        if digit_list[0] in dices_result:
            try:
                left_numbers.remove(digit_list[0])
            except ValueError:
                    pass
        elif check_number(digit_list[0], dices_result):
            try:
                left_numbers.remove(digit_list[0])
            except ValueError:
                    pass
        elif check_number(digit_list[0], [dices_result[0], dices_result[1]]) or check_number(digit_list[0], [dices_result[0], dices_result[2]]) or check_number(digit_list[0], [dices_result[1], dices_result[2]]):
            try:
                left_numbers.remove(digit_list[0])
            except ValueError:
                    pass
    #print("result",left_numbers)    
    return left_numbers

def game_start(player1, player2):
    while player1 and player2:
        print("Player1 ", player1)
        print("Player2 ", player2)
        print("Player1 your turn")
        get_and_process_user_input(player1)
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("Player1 ", player1)
        print("Player2 ", player2)
        print("Player2 your turn")
        get_and_process_user_input(player2)
        #os.system('cls' if os.name == 'nt' else 'clear')
    if len(player1) == 0:
        print("Player1 is a winner!")
    else:
        print("Player2 is a winner!")


game_start(player1, player2)
