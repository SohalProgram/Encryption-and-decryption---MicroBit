# Encryption-and-decryption---MicroBit
In this project I built encryption and decryption using a special method, in addition and attached is a code of two micro bit controllers that one sends the other an encrypted message and the other decrypts it.

The way the encryption works is like this: first turn the string into a list of numbers using the command ord then check the The value of the next character in the string - let's imagine that it is the letter "b" that you entered Its ASCII is 98 and determine the mathematical operation that must be done, what is the previous value "a=="97 To reach this value, that is, you must add 1, then you must add a character that marks a connection operation and a character of The digit 1 then subtract 65 from the first number and turn its digits into a string then turn all the numbers into strings and concatenate them into one string:  

final = "32@1*1"
