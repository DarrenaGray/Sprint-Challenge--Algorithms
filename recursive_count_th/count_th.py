'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

str = "The kids play in the park every fourth day of the week"
str_th = "th"
count = 0


def count_th(word):

    global count
    count = 0
    # Check to see if "th" is in string("word")
    # If "th" is in the string

    if str_th in word:
        # Return the "th" count
        count = word.count(str_th)

        print(f"({count}, {str_th})")

    # Else if "th" is not in the string
    else:
        # Return initial count of 0
        count
        print(f"({count}, {str_th})")

    return count

    # global count
    # count = 0
    # # Check to see if "th" is in string("word")
    # # If "th" is in the string

    # if str_th in word:
    #     # Return the "th" count
    #     count = word.count(str_th)

    #     print(f"({count}, {str_th})")
    #     return count

    # # Else if "th" is not in the string
    # elif str == "":
    #     # Return initial count of 0
    #     print(f"({count}, {str_th})")
    #     return count_th(word)


print(count_th(str))
