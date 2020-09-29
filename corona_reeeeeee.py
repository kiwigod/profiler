#!/usr/bin/env python

PERSON_LIMIT = 6

def ask_number_of_friends():
    n_friends = input("This is the corona bot reee, how many friends do you want to invite? ")
    if (n_friends.isnumeric()):
        n_friends = int(n_friends)
    else:
        print("you donkey")
        return 0

    if (n_friends > PERSON_LIMIT):
        print("ill eagle")
        print("too many people, not corona proof")
        return 0

    return n_friends

def ask_their_names(n):
    friends = input("State their names (seperated by space): ").split(' ')

    if (len(friends) > n):
        print("FBI open up")
        exit()

    for friend in friends:
        print(f'{friend} has been invited!')

n_friends = ask_number_of_friends()
if (n_friends):
    ask_their_names(n_friends)

# n_friends = input("This is the corona bot reee, how many friends do you want to invite? ")
# if (n_friends.isnumeric()):
#     n_friends = int(n_friends)
# else:
#     print("you donkey")
#     exit()

# if (n_friends > PERSON_LIMIT):
#     print("ill eagle")
#     print("too many people, not corona proof")
#     exit()

# friends = input("State their names (seperated by space): ").split(' ')

# if (len(friends) > PERSON_LIMIT):
#     print("FBI open up")
#     exit()

# for friend in friends:
#     print(f'{friend} has been invited!')
