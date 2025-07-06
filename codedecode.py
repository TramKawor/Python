#make a code language 1. 


#coding
#if the word contains atleast 3 character, remove the first leter and append it in the end
#now append three random characters at the starting and the end
#else
#simply reverse the string

#decoding 
#if the word contains less than 3 characters, reverse it
#else
#remove 3 random characters from start and end. Now remove the last letter and append it in begining 



Question = input("Wanna encrypt or decrypt: \n")
if Question == "encrypt":
    word = str(input("Enter your word:"))
# Encryption
    if len(word) > 3:
        word1 = word[1:]
        word2 = word1.__add__(word[0])
        import random
        import string
        s = string.ascii_lowercase
        random_string = ''.join(random.sample(s,3))
        random_string1 = ''.join(random.sample(s,3))
        word3 =f'{random_string}{word2}{random_string1}'
        print(f"The encrypted value is '{word3}'")
    else:
        b=word[::-1]
        print(f"The encrypted value is {b}")
        
    
#decryption
elif Question == "decrypt":
    d_Word = str(input("Enter word you want to decrypt:\n"))
    if len(d_Word) < 3:
        print(f"The decrypted value is {d_Word[::-1]}")
    else:
      
         d4_Word = d_Word[3:-3]
         d5_Word = d4_Word[:-1]
         d6_Word = d4_Word[-1]
         deCrypt = f"{d6_Word}{d5_Word}"
         print(f"The decrypted value is {deCrypt}")
       
#What I searched :::
# import random
# import string

# s = string.ascii_lowercase + string.digits
# random_string = ''.join(random.sample(s, 10))
# print(random_string)  # Output: 'jw72qidagk'