pal_list = ["anna", "racecar", "control", "kayak"]
palindrome = True

def is_palindrome(pal_list,palindrome):
    while palindrome:
        in_word = str(input("Enter a word: "))
        pal_list.append(in_word.lower())
        print(pal_list)
        ask_word = input("Would you like to enter another word: 'yes' or 'no'")
        if ask_word == 'no':
            break
    return pal_list

def main(palindrome):    
    for pal in is_palindrome(pal_list,palindrome):
        for p in range(len(pal)):
            if pal[p] != pal[len(pal)-p-1]:
                palindrome = False
        if palindrome == True:
            print(f'{pal} is a palindrome.')
        else:
            print(f'{pal} is not a palidrome.')

if __name__ == "__main__":
    main(palindrome)

'''
for pal in pal_list:
            for p in range(len(pal)//2):
                if pal[p] != pal[len(pal) - p -1]:
                    palindrome = False
                    print(f"{pal} is not a palidrome.")
                else:
                    print(f"{pal} is a palindrome.")
'''