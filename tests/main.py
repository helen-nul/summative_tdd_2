def palindrome(word):
   word = word.lower()
   return word == word[::-1]
