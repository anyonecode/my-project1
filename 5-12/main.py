a='sreehari'
b = set(a)
print(b)
test_str = str(input('enter a string'))
all_freq={}
# b=[]
# c=[]
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
        # b.append(all_freq)

    else:
        all_freq[i] = 1
print(all_freq)