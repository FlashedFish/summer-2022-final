# summer-2022-final
final project for lis 4930
Problem description: Cryptography is a very old and essential discipline for privately sharing information. for my final i have decided to write a program that ciphers any text input using the Caesar Cipher one of the oldest cipher methods in the world. the Caesar cipher works by taking each character and shifting its position on the alphabet by a key value, looping over the whole alphabet at z and starting again at a. creating this program requires using many different python methods in conjunction with good mathematics.

 The technical approach is to take each letter in string ignoring non character values and to get their ascii values then to increment those values by the key values given by the user. using the modulo operator of 26 ( the length of the English alphabet) plus the ascii value for a (65 upper case 97 lower case) you then get an incremented and looped value of the character. which you then convert back into a string



example     input : text "abcz" key: 1

                    output: "bcda"

explanation : all of the characters were incremented up the alphabet by one the letter z looped around back to a.
