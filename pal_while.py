pal_list = ["Anna", "Racecar", "control", "Kayak"]
palindrome = True

def is_palindrome(pal_list, palindrome):
    while True:
        in_word = str(input("Enter a word: "))
        pal_list.append(in_word.lower())
        print(pal_list)
        for pal in pal_list:
            for p in range(len(pal)//2):
                if pal[p] != pal[len(pal) - p -1]:
                    palindrome = False
                    print(f"{pal} is not a palidrome.")
                else:
                    print(f"{pal} is a palindrome.")
        ask_word = input("Would you like to enter another word: 'yes' or 'no'")
        if ask_word == 'no':
            break
        
is_palindrome(pal_list, palindrome)