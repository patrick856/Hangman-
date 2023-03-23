#!/usr/bin/env python
# coding: utf-8

# In[13]:


import random

with open('english_words.txt') as file:
    words = file.readlines()

random_word = random.choice(words).strip()
hidden_word = "_"

for i in range(1,len(random_word)):
    hidden_word += "_"

lives_left = 5
while lives_left > 0:
    print(hidden_word)
    user_input = input("Please enter a character:         " + str(lives_left) + " lives left\n")

    if user_input in random_word:
        list1 = list(hidden_word)
        for i in range(len(random_word)):
            if random_word[i] == user_input:
                list1[i] = random_word[i]
        hidden_word =  "".join(list1)
        print("- Right -")
        if hidden_word == random_word:
            print(random_word)
            print("-- You win --")
            break
    else:
        print("- Wrong -")
        lives_left -= 1
        if lives_left == 0:
            print("-- You lost --")
            print("The word was - " + random_word + " -")

