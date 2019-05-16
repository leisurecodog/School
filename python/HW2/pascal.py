def count(num):
# count the longest width of pascal triangle
    row = [1]

    num = int(num)

    wid = 0
    for i in range(num - 1):
        row = [l + r for l ,r in zip([0] + row , row + [0])]
        if i != num-2:
            continue
        st = ''
        for s in row:
            st += str(s) + ' '
        wid = len(st) - 1
    return wid

def print_tri(wid):
# print pascal triangle
   
    row  = [1]

    for i in range(num):
        st = ''
        for s in row:
            st += str(s) + ' '
        print(st.center(wid))
        row = [l + r for l ,r in zip([0]+row , row + [0])]

if __name__ == '__main__':
    num = input('Please enter the total levels of the pascal triangle> ')
    num = int(num)
    print_tri(count(num))
