#print("-------------------m1 creating dict------------"
#
# deck = [str(x)+y for x in range(1,14) for y in ["S","H","C","D"]]
# val=[]
# for i in range(2,15):
#     for j in range(0,4):
#         val.append(i)
# print(val)
#
# deck_cards = {}                            
# # COnvert to dictionary
# for key in deck:
#    for value in val:
#       deck_cards[key] = value
#       val.remove(value)
#       break
# print("Dictionary from lists :\n ",deck_cards)
#print("-------------------------m1end---------------------------")


# print("--------------m2 creating dict ")
# self.card_list={}
# def construct_deck(self):
#     for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
#         for v in [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King','Ace']:
#             self.card_list.append(Card(v, s))
#
# print(self.card_list)
# print('-------------------m2 end')


#shuffling dict
# print("---------------shuffle1---------")
# import random
#
# student_dict = {'Eric': 80, 'Scott': 75, 'Jessa': 95, 'Mike': 66}
# print("Dictionary Before Shuffling")
# print(student_dict)
# keys = list(student_dict.keys())
# random.shuffle(keys)
#
# ShuffledStudentDict = dict()
# for key in keys:
#     ShuffledStudentDict.update({key: student_dict[key]})
#
# print("\nDictionary after Shuffling")
# print(ShuffledStudentDict)
# print("shuffle end--------------")

# print("----------------shuffle2------------------------")
# # To Shuffle two List at once with the same order
# mapIndexPosition = list(zip(employees, salary))
# random.shuffle(mapIndexPosition)
# # make list separate
# list1_names, list2_salary = zip(*mapIndexPosition)
# print(-------------shuffle 2---------------------)

print("tom got:")
for i in range(5):
   print(Shuffled_deck_cards[i][0])


"""""""""""""""""""""""""""not possible"""
# #using even or odd method
# even_dict = {k: v for (k, v) in Shuffled_deck_cards.items() if v % 2 == 0}
# print(len(even_dict))
# odd_dict = {k: v for (k, v) in Shuffled_deck_cards.items() if v % 2 == 1}
# print(len(odd_dict))
# ''''''''''''''''''''''''''not possible evenor odd method'''


'''''''''''''''''''''''''' check this to extract the range

'even=[]
for i in range(0:52:2):
   print(i)
'''



#distributing keys
keys=list(Shuffled_deck_cards.keys())
odd_keys = keys[0:26]
even_keys=keys[26:52]
print(len(odd_keys),len(even_keys),len(keys))

even_dict = {k: v for (k, v) in Shuffled_deck_cards.items() if odd_keys==0}
print(even_dict)
