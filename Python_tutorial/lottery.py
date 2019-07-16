#!/usr/bin/env python
# coding: utf-8

# In[6]:


from random import randint


def generate_numbers():
    num_list = list()
    while len(num_list)<6:
        random_num = randint(1,45)
        if random_num not in num_list:
            num_list.append(random_num)
    return num_list
def draw_winning_numbers():
    lotto_list = sorted(generate_numbers())
    bonus_num = randint(1,45)
    while len(lotto_list) <7:
        if bonus_num not in lotto_list:
            lotto_list.append(bonus_num)
    return lotto_list
    

def count_matching_numbers(list1,list2):
    count = 0    
    for number in list1:
        if number in list2[:6]:
            count +=1
    
    return count
    

def check(numbers, winning_numbers):
    user_number_list = sorted(numbers)
    winning_list = winning_numbers
    winning_count = count_matching_numbers(user_number_list,winning_list)

    bonus_count = 0
    if winning_count > 5 or (winning_count>4 and bonus_count >0) :
        print(winning_count)
    if winning_list[-1] in user_number_list:
        bonus_count += 1
    if winning_count == 6:
        return 1000000000
    elif winning_count == 5 and bonus_count == 1:
        return 50000000
    elif winning_count == 5 and bonus_count == 0:
        return 1000000
    elif winning_count == 4 and bonus_count == 0:
        return 50000
    elif winning_count == 3 and bonus_count == 0:
        return 5000
    else:
        return 0
    
    
    





