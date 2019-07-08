# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:22:10 2019

@author: Adam
"""
abcd = ['nintendo','Spain', 1, 2, 3]

print(abcd)

# Ex1 - Select the third element of the list and print it
abcd[2]





# Ex2 - Type a nested list with the follwing list elements inside list abcd mentioned above and print it

newlist = [54,76]

superlist = abcd+newlist
abcd.append(newlist)


# Ex3 - Print the 1 and the 4 position element in the following list

nestedlist = ["shail", [11,8, 4, 6], ['toronto'],abcd, "abcd"]
print(nestedlist[0])
print(nestedlist[3])


# Ex4  - add the fllowing 2 lists and create list3 and print new list where
#company and orange is not there

list1= [10, 20, 'company', 40, 50, 100]

list2 = [100, 200, 300, 'orange', 400, 500,1000]

list3 = list1+list2
list3.remove('company')
list3.remove('orange')
print(list3)

# Ex 5 - print the lenght of the list3

print(len(list3))
#11


# Ex 6 Add 320 to list 1 and print

list1.append(320)
print(list1)

#Ex 7 - Add parts of list1 & 2 by tking first 4 elements from list1 and last 2 elements from list2
list1[0:4] + list2[5:]


#ex 8 check if 99 is in list 1 
99 in list1
#false

#ex 9 check if 99 is not in list 1 
99 not in list1
#True




# concatenation (+) and replication (*) operators
#ex 10 - CONCATENANTE  list 1 and ['cool', 1990]
list1 + ['cool', 1990]

# Ex 11 -  triplicate the list 1
list1*3

# ex 12 - find min & max of list2
list2.remove('orange')
min(list2)
#100
max(list2)
#1000


# append & del
# Ex 13 append 'training' to list 1
list1.append('training')

# Ex 14 delete 2nd position element from list 2
del list2[1]

# Ex 15 - iterate over list1 and print all elements by adding 10 to each element

list1= [10, 65,20, 30,93,  40, 50, 100]

for x in list1:
    print(x+10)
    


#Ex 16 sorting

#sort list1 by ascending order
list1.sort()



#sort list1 by reverse order
list1.sort(reverse=True)

#ran code
#runfile('C:/Users/adn6m/answers.py', wdir='C:/Users/adn6m')
#['nintendo', 'Spain', 1, 2, 3]
#shail
#['nintendo', 'Spain', 1, 2, 3, [54, 76]]
#[10, 20, 40, 50, 100, 100, 200, 300, 400, 500, 1000]
#11
#[10, 20, 'company', 40, 50, 100, 320]
#20
#75
#30
#40
#103
#50
#60
#110