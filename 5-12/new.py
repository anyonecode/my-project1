# d = int(input('eneter the range'))
# a = [1,2,3,4,5]
# b = a[:d]
#
# a.append(b)
# print(a)
# a = 6
# b=2
# c = a%b
# print(c)
# a = [1,2,3,4]
# for i in a:
#     print(i)
# a = 13.45
# i = int(a//1)
# print(i)
def match(word_1, a, word_2, b):
#     if len(word_2) == b:
#         return len(word_1) == a
#     if len(word_1) == a:
#         for i in range(b, len(word_2)):
#             if word_2[i] != "*":
#                 return False
#         return True
#     if word_2[b] == "?" or word_2[b] == word_1[a]:
#         return match(word_1, a + 1, word_2, b + 1)
#     if word_2[b] == "*":
#         return match(word_1, a + 1, word_2, b) or match(word_1, a, word_2, b + 1)
#
#
# def matching(word_1,word_2):
#     return match(word_1, 0, word_2, 0)
#
# print(matching('XYXZZXY', 'X***Y'))
str1 = str(input('enter a string'))
str2 = str(input('enter a string'))
spe = ('*', "?", "[]", '!', '#')
if len(str1) == len(str2):
    for i in str1:
        for j in str2:
            for k in spe:
                if str1[0] == str2[0] and str1[-1] == str2[-1] or i == k:
                    print('true')
                else:
                    print('false')
