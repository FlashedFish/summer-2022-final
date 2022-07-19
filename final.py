print("Welcome to Ceasar Cypher-er")
text = input("Enter text to be Cyphered : non letters will not be ciphered; lower or upper case accepted\n")
key= input("now enter a number between 1 and 25 to be the 'key' to the cypher \n")
print("Original text is : '" + text + "' key is : " + key)
cipher = ""
#loop through input
for element in text:
    #convert character in string to ascii
    char=ord(element)
    #compute value based on capital or not
    if char >= 65 and char <= 90:
        char = ((int(char) +(int(key)-65))%26) +65
    if char >= 97 and char <= 122:
        char = ((int(char) +(int(key)-97))%26) +97
    #conver shifted ascii value back to a character and append to a string
    cipher+=chr(char)
print("ciphered text : '"+cipher+"'")
