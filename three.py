#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.


#Sample String: 'w3resource'
#Expected Result: 'w3ce'

String = "w3resource"
i = String[0]
j = String[1]
k = String[len(String)-2]
l =String[len(String)-1]

print(i+j+k+l)

#Sample String: 'w3'
#Expected Result: 'w3w3'

string = "w3"
i = string[0]
j= string[1]

print(2*(i+j))

#Sample String: ' w'
#Expected Result: Empty String

string = "w"

if len(string)<2:
   print("")
else:
   print(string[0]+string[1])
