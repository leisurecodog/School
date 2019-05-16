def wordgame(str1):
    strfind = ''
    maxlen = 0
    with open('dictionary.txt','r') as file:
        can = True
        for x in file:
            can = True
            for i in range(len(str1)):
                if x.find(str1[i]) == -1:
                    can = False
                    break
            if can:
               if len(x) > maxlen:
                    maxlen = len(x)
                    strfind = x
        if strfind:
            print('The word is ' + strfind.rstrip() + '.')
        else:
            print('There are no words that fit this criteria.')
            
                


if __name__ == '__main__':
    
    letter = input('Please enter the letters to include> ')
    letter = letter.lower()
    wordgame(letter)
    while(1):
        check = input('Do you like to continue (y/n)? ')
        if check == 'y' or check == 'Y':
            letter = input('Please enter the letters to include> ')
            letter = letter.lower()
            wordgame(letter)
        elif check == 'n' or check == 'N':
            print('Thank you for playing.')
            break
        else:
            print('Incorrect choice. Please try again.')
