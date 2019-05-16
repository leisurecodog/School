import csv
dic = dict()
name = ''
def get_data_list(file_name):
    global name
    name = dic[file_name]
    with open(file_name) as csvfile:
        read = csv.reader(csvfile)
        total = [str(r).strip('[\'').strip('\']').split(',') for r in read]
        return total[1:]

def get_monthly_averages(data_list):
    monthly_averages_list = []
    date = data_list[0][0][:7]
    clvol = 0
    sumvol = 0
    for data in data_list:
        if date != data[0][:7]:
            monthly_averages_list.append((clvol/sumvol,date))
            date = data[0][:7]
            clvol = 0
            sumvol = 0
        clvol += float(data[4][2:-1]) * float(data[5][2:-1])
        sumvol += float(data[5][2:-1])
    monthly_averages_list.append((clvol/sumvol,date))
    return monthly_averages_list
        
        
def print_info(monthly_average_list):
    worst= sorted(monthly_average_list)
    best = worst[::-1]
    print('The six best months for ' + name + '\'s stock are as follows:')
    for i in range(6):
        print("{} {:.3f}".format(best[i][1],best[i][0]))
    print('')
    print('The six worst months for ' + name + '\'s stock are as follows:')
    for i in range(6):
        print("{} {:.3f}".format(worst[i][1],worst[i][0]))
    print('')

    
if __name__ == '__main__':
    dic['google.csv'] = "Google"
    dic['cisco.csv'] = "Cisco"
    print_info(get_monthly_averages(get_data_list(
    input('Enter the name of the data file> '))))
    print_info(get_monthly_averages(get_data_list(
    input('Enter the name of the data file> '))))
    
