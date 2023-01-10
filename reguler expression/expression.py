'''Character 	Description 	Example 	Try it
1.[] 	A set of characters 	"[a-m]"
2.\ 	Signals a special sequence (can also be used to escape special characters) 	"\d"
3.. 	Any character (except newline character) 	"he..o"
4.^ 	Starts with 	"^hello"
5.$ 	Ends with 	"planet$"
6.* 	Zero or more occurrences 	"he.*o"
7.+ 	One or more occurrences 	"he.+o"
8.? 	Zero or one occurrences 	"he.?o"
9.{} 	Exactly the specified number of occurrences 	"he.{2}o"
10.| 	Either or 	"falls|stays"
11.() 	Capture and group'''
#1
import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

#2
import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)

#3
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

#4
import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

#5
import re

txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
#6
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)

#7
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x)

#8
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

#9
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)

#10
import re

txt = "The rain in Spain fall mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("fall|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#11
