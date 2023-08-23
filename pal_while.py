pal_list = ["anna", "racecar", "control", "kayak"]

def is_palindrome(pal_list):
    while True:
        in_word = str(input("Enter a word: "))
        pal_list.append(in_word.lower())
        print(pal_list)
        ask_word = str(input("Would you like to enter another word? 'yes' or 'no': "))
        if ask_word == 'no':
            break
    return pal_list

def main():    
    for pal in is_palindrome(pal_list):
        for p in range(len(pal)//2):
            if pal[p] == pal[len(pal)-p-1]:
                palindrome = f"{pal} is a palindrome."
            elif pal[0] != pal[-1]:
                palindrome = f"close, but {pal} is not a palindrome."
            else:
                palindrome = f"{pal} is not a palindrome."
        print(palindrome)

if __name__ == "__main__":
    main()