The point of this coding exercise was to check and make sure that the elements of a list are either palindromes or that they are not. To understand this exercise, the programmer must first understand what a palindrome is, what the purpose of the while loop is and why we ran a for loop in the main().

A palindrome is a word, where it is a mirror reflection of each letter of the word between the first half of the word and the latter half of the word. It has to be halved in order to measure the elements of letter of the word. An simple example of a palindrome is the word racecar:

                rac e car
        So rac spelled backwards is car and the word
        is seperated by e. It is still a palindrome as
        word halved will split between e. 

        Here is another clear example:
                Abba  (Yes, the band. Just roll with it.)
                Ab ba
        The word is evenly halved without a letter seperator. 

The way this is expressed in the program, is via the nested for loop, where we take the range of the length of the word is then individually halved in the list:

                    for w in range(len(word)//2)
                    
To note, if this is not done, then the result is either all of the words in the list are palindromes or all are not, which is why the words need to be halved by their length. Another purpose of the list, is to append to the list, as to then provide the program with a way to check the values.

The use of the while loop, was the most practical approach to appending to the list. The program utilizes the input function (input()) to enter the word. The word then got appended to the list and then another variable, that stores a question asking to see if the programmer would input anymore word. A conditional logic of no, would break the loop. 

Once the list is complete, then a nested for loop would access the elements of an individual word. To break it down, the main outer loop, accesses the list of words. The inner loop then breaks the list, by accessing the letters of each word, one word at a time. 

        words =  ['anna', 'racecar', 'control', 'kayak', 'tenet', 'buy']
                
                for word in words:
                    for w in range(len(word)//2):
                        if word[w] == word[len(word)-w-1]:
                            palindrome = True
                
Let's break it down here:
               1. for word in words:
                    accesses the list called words as an
                    iterable. 
                    for 
               2.    for w in range(len(word)//2)
                        Here is where the loop is doing the
                        work, that the program was inteneded
                        for. This loop is accessing the individaul word and its letters.
               3.       if word[w] == word[len(word) - w -1]:
                            palindrome = True
                            The conditional logic, is the way that, when the word gets halved in the inner loop, that it will check each letter against the latter half. Then a boolean would kick in as a truthy or falsy statement. 
                            
                            Even though, a boolean is illustrated here, it is to simplify, that this conditional statement would be true, if the condition of the loop is met. It is implied to be false, if the condition is not met. In the program, the conditional logic is explicitly truthy or falsy.  