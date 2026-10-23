# ------------------------------------------------------
#        Name: (Rouan Chen)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Reading text from the user in a loop and checking the secret word "food", or the words "Dog" and "dog". If the sentence has the words, it prints corresponding message and repeats until a match is found. """
    while True:
        sentence = input("Give me a sentence:")
        if secret_word in sentence:
            print("You used the secret word!")
            break
    
        elif "dog" in sentence or "Dog" in sentence:
            print('You used the word "dog" or the word "Dog"!')
            break
        else:
            print("Try again")



# Task 2
def check_greater():
    """ Reading two integers from the user and compares them. Repeats if they are equal, otherwise prints which integer is greater."""
    while True:
        num1 = int(input("Give me a first integer: "))
        num2 = int(input("Give me a second integer: "))
        
        if num1 > num2:
            print("First is Greater")
            break
        
        elif num1 < num2:
            print("Second is Greater")
            break
        
        else:
            print("Try again")


# Task 3
def get_special_numbers():
    """ Iterates numbers from 1 to 40, discarding numbers that are even, not the multiple of 3, or the multiple of 5, and then, prints the rest."""
    for num in range(1, 41):
        if num % 2 == 0:
            continue
        
        if num % 3 != 0:
            continue
        
        if num % 5 == 0:
            continue
        
        print(num)


# Task 4.a
def my_for_loop():
    """ Asing the user for a string. Validating the length from 2 to 5, and checks for space. If it's valid, classifies each letter as a vowel or consonant. """
    user_str = input("Give me a string: ")
    if len(user_str) < 2 or len(user_str) > 5 or " " in user_str:
        print("bad word")
        return
    
    vowels = "aeiouAEIOU"
    
    for char in user_str:
        if char in vowels:
            print(f"letter {char} is a vowel")
        else:
            print(f"letter {char} is a consonant")

# Task 4.b
def my_while_loop():
    """ Show a list of chioces a, b, or c to handle loop continuation, exit, or program termination."""
    while True:
        chioce = input("Choose one option: a, b, or c: ")
        
        if chioce == 'a':
            continue
        
        elif chioce == 'b':
            print("Goodbye")
            return
        
        elif chioce == 'c':
            sys.exit()
        
        else:
            print("try again")
    
# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
