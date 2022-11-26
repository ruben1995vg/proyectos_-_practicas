
paragraph = input('\ntexto ').replace(',', '')
paragraph = paragraph.replace(',', '')

words= paragraph.split()

set_1=set(words)

set_2=list(set_1)

print('\n')
# print(set_1)
print(len(set_1))
print('\n')
dic={}

# def counter(s, p):
#     for i in s:
#         increment=0
#         for x in p:
#             if x == i:
#                 increment+=1
#         dic.setdefault(i,increment)
#     print(dic)
    
            

# counter(set_2, words)

print({c: words.count(c) for c in set_2 if c in words})

