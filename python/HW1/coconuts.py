def ask_user():
    user_ans = input('How many many ounces of birds are carrying'
                     'the coconuts? ')
    user_ans = float(user_ans)

    coconuts = input('How many pounds of coconuts are there? ')

    coconuts = float(coconuts)

    if user_ans / coconuts >= 5.5:
        print('Yes! Carrying the coconuts is possible.')
    else:
        print('No. Carrying the coconuts is impossible.')


if __name__ == '__main__':
    ask_user()
