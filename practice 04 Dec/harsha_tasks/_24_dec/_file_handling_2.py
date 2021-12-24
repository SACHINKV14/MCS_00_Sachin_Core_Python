with open('frame.txt','w') as wf:
    wf.write('dog is dog and cat is cat')   # creating afile and writing
    wf.write('\nthese are domestic animals')
    lines=['\nanimals are two types','\tone type is carinivorus and other is herbivorous','\nthird type also exists'
         '\tit is omnivorus']
    wf.writelines(lines)

#with open('frame.txt','r') as rf:
   #  print(rf.read())    #  reading the created file
   # print(rf.readline())  #  read the first line in file
   # print(rf.readline())  #  read the second line in file
   # data = rf.read()
   # for x in data:
    #  print(x,end='')

with open('frame.txt','r') as rft:
   print(rft.read(6))                 # reads upto 6th character in the text in file
   print(rft.read(7))                 # reads after 6th character upto 7th character

#with open('text.txt', 'w') as rft:
  #   rft.write(data)
  #   rft.write('\ndomestic animals are pets')

#import os
#if os.path.exists('texxt.txt'):            # checking if the file exists or not
#     print('yes this file exist')
#else:
#    print('not exist')