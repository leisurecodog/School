def ask_user():

    user_ans = input('Please enter a word> ')

    sum = 0  # record

    i = 1   # triangle sequence for loop

    step = 2

    yes = 0  # a flag for checking triangle words

    user_ans = user_ans.lower()  # unify to lowercase

    user_ans = user_ans.strip()  # remove space

    for ch in user_ans:  # calculate is a triangle word or not

        sum += ord(ch) - ord('a') + 1

    while(sum >= i):
        if sum == i:
            yes = 1
            break
        i += step
        step += 1
    if yes:
        print(user_ans + ' is a triangle word')
    else:
        print(user_ans + ' is not a triangle word')

if __name__ == '__main__':
    ask_user()
