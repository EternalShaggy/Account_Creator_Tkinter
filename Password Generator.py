import random

def ran_char(list, count): #Create's a new random list with a certain number of elements 
    out_list = []
    for i in range(count):
        a = random.choice(list)
        out_list.append(a)
    return out_list
        

def password_genrator(letter_count=4, number_count=3, symbol_count=1, pass_length=8): #

    letter_list = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") 
    number_list = list("0124356789") 
    symbol_list = list("!”#$%&'()*+,-./:;<=>?@[]^_`{|}~") 
    extra_char = pass_length - letter_count - number_count - symbol_count
    l = []

    l.extend(ran_char(letter_list, letter_count)) #Creates random lists within the arguement's parameters then adds them to the empty list l
    l.extend(ran_char(number_list, number_count)) #| 
    l.extend(ran_char(symbol_list, symbol_count)) #| 

    if extra_char > 0: #Checks if the there's any extra space to fill the password length requirements. If so it will fill the space with randomly generated characters. 
        for i in range(extra_char):
            choice = random.randint(1,3)
            if choice == 1:
                l.extend(ran_char(letter_list, 1))
            if choice == 2:
                l.extend(ran_char(number_list, 1))
            if choice == 3:
                l.extend(ran_char(symbol_list, 1))
    
    random.shuffle(l) #Shuffles the list one more time for good measure :D
    password = "".join(l) #Turns it into a usable string

    return password

print(password_genrator(4,4,4,20))