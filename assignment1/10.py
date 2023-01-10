#print first, mid and last
str = "james"
x = str[0]
l = len(str)/2
y = str[int(l)]
z = str[-1]
print(x+y+z)
next
s1="hello"
s2="world"
s3="hi"
print(s1+s2+s3)


s1 = ("he{s2}llo")
print(s1.format(s2="world"))
#arrage string characters such that lowercase letters should come first
x = "HeLLOWorld"
up=[]
low=[]
for char in x:
    if char.islower():
        up.append(char)
    else:
        low.append(char)
string =''.join(low+up)
print(string)

#count all letters digits and speacial symbols from a givien string
str = "p@#$yn26at^i5ve"
digit=chara=spe=0
for char in str:
    if char.isdigit():
        digit=digit+1
    elif char.isalpha():
        chara=chara+1
    else:
        spe=spe+1
print("number of digit",'=',digit)
print("number of characters",'=',chara)
print("number of special",'=',spe)
#remove special symbols / puntuation from  a string
#ans : jon is developer music director
str = "*/jon is 2developer & music director"
x=[]
for char in str:
    if char.isalpha():
        x.append(char)
        print(end='')
print(''.join(x))