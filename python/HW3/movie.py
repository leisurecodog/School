def choice_a(lst):
    str1 = input('Enter movies separated by an operator> ')
    '''get operation char'''
    pos = str1.find(',')
    ch = str1[pos+7]
    ''''''
    ls = [list(map(lambda x: x.strip(' '),l))  for l in [x.split(', ') for x in str1.split(ch)]]
    total = []
    
    '''find name for each movie'''
    for L1 in ls:
        tmp_lst = []
        for L2 in lst:
            tmp = L1[0]
            if tmp.lower() in [x.lower() for x in L2]:
                tmp_lst.append(L2[0])
        total.append(tmp_lst)
    '''operation'''
    if ch == '|':
        ans = list(set(total[0]) | set(total[1]))
        if ans == []:
            print('There is no actors.')
        else:
            print('The actors: ',end='')
            print(', '.join(ans))
    elif ch == '&':
        ans = list(set(total[0]) & set(total[1]))
        if ans == []:
            print('There is no common actors.')
        else:
            print('The common actors: ',end='')
            print(', '.join(ans))
    else:
        ans = list(set(total[0]) ^ set(total[1]))
        if ans == []:
            print('There is no actors.')
        else:
            print('The xor actors: ',end='')
            print(', '.join(ans))


def choice_b(lst):
    str1 = input('Enter an actor’s name> ')
    mv_lst = []
    '''get movie list'''
    for x in lst:
        if str1 in x:
            mv_lst = x[1:len(x):2]
            break
    act_lst = []
    for mv in mv_lst:
        for L in lst:
            if mv in L:
                act_lst.append(L[0])
    print('The actors: ',end='')
    print(', '.join(list(set(act_lst) -set([str1]) ) ) )
        
            
def read_data(lst):
    with open('imdb.txt','r',encoding='utf8') as f:
        for r in f.readlines():
            r = r.replace('(',',').replace(')','').replace('\n','')
            lst.append(r.split(','))
        


if __name__ == '__main__':
    lst = []
    read_data(lst)
    lst = [list(map(lambda x: x.strip(' '),l))  for l in lst]
            
    while True:
        print('a) Use movie titles to find actors\n'
              'b) Use an actor’s name to find all the'
              'actors whom he or she has acted\n'
              'q) Quit\n')
        ch = input('Enter choice> ')
        if ch == 'a':
            choice_a(lst)
        elif ch == 'b':
            choice_b(lst)
        elif ch == 'q':
            break
        else:
            print("Invaild Choice\n")
