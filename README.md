# Created a simple password cracker to understand how it works

1. We take an input of only lowercase characters
2. We then have a character array that hold every letter in the alphabet and start a timer as well
3. We also create a guess array that hold each guessed combination of letters
4. The first for loop find every possible combination of words that are max 9 characters long. The first list comprehension creates a list of all possible 1-letter words
5. The second for loop loops the amount of value which is the amount of values in the list
6. The second list comprehension reloops through each character in chars and then loops through each existing character in the 'a' list and appends each character to a_new. For example, if the first letter in chars is 'a' and a[0] is also 'a', a[0] gets appended to i.  
7. We then add the new and updated 'a' list to guess adn then we see if the password typed by the user is in the 'guess' list; and if it is, we break out of the loop and stop the clock timer. 
