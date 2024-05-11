
####################################################



def is_palindrom(word): 

    reversed_word = ''
    
    for i in range(len(word) - 1, -1, -1):
        reversed_word = reversed_word + word[i]
    
    print(reversed_word == word)


is_palindrom("gio")


###################################################


def remove_spaces(word):
   word_without_space = ''
    
   for char in word:
        if char != " ":
            word_without_space = word_without_space + char
    
        print(word_without_space)

remove_spaces("giorgi qartvelishvili")



##################################################


def my_replace(word,char1,char2):
    replaced_word = ''
    
    for i in word:
        if i == char1:
            replaced_word = replaced_word + char2 
        else:
            replaced_word = replaced_word + i
    
    print(replaced_word)

my_replace("giorgi qartvelishvili", "k", "i")


##################################################


def func(number_list):
    sum = 0
    quantity = 0
    
    for num in number_list:
        if num >= 0:
            sum = sum + num
        else:
            quantity = quantity + 1
    
    print(sum,quantity)

func([1,2,3,-1,-2,-3])


