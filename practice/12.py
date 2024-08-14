# def word_lenghts(a): 
#     return [*map(len,a.split())]

# print(word_lenghts('How long are the words in this pharse'))

# from functools import reduce
# def digits_to_num(a):
#     return reduce(lambda x,y : (x*10)+y ,a) 

# print(digits_to_num([1,2,3]))
# print(digits_to_num([3,4,3,2,1]))

# def filter_words(lst,letter):
#     return [*filter(lambda x : x[0]==letter.lower(),lst)]

# l=['hello','are','cat','dog','ham','hi','go','to','heart']
# print(filter_words(l,'h'))

# def concatenate(l1,l2,connector):
#     return [f'{a}{connector}{b}' for a,b in zip(l1,l2)]

# print(concatenate(['A','B'],['a','b'],'-'))

# def d_list(l):
#     a=dict(enumerate(l))
#     return dict([*zip(a.values(),a)])

# def d_list(l):
#     return {b:a for a,b in enumerate(l)}

# print(d_list(['a','b','c']))

# def count_match_index(l):
#     count=0
#     for a,b in enumerate(l):
#         if a==b:
#             count+=1
#     return count

# def count_match_index(l):
#     return len([b for a,b in enumerate(l) if a==b])

# print(count_match_index([0,2,2,1,5,5,6,10]))