import csv
import math
def football(str1):
    with open(str1) as fb:
        name = ''
        minest = 99999
        f = open('result.csv','w',newline='')
        result = csv.writer(f)
        result.writerow(['Team','Goal Difference'])
        for x in csv.DictReader(fb):
            eachmin = abs(int(x['Goals']) - int(x['Goals Allowed']))
            result.writerow([x['Team'],eachmin])
            if eachmin < minest:
                name = x['Team']
                minest = eachmin
        f.close()
        print(name + ' has a minimum goal difference of ' + str(minest))

if __name__ == '__main__':
    limit = 5
    while(limit):
        str1 = input('Please enter a filename> ')
        if str1 != 'football.csv':
            limit -= 1
            print('Error opening file: ' + str1)
        else:
            football(str1)
            break
    if limit == 0:
        print('Too much input error!')
