class Fibonacci():
    def __init__(self, data):
        self.data = data
        self.lst = [0, 1]
        self.init = 0
        for x in range(2, data):
            self.lst.append(self.lst[x-1] + self.lst[x-2])

    def __str__(self):
        return ('The first ' + str(self.data) + ' Fibonacci numbers '
                'are ' + str(self.lst[:self.data]))

    def __iter__(self):
        return self

    def __next__(self):
        if self.init == self.data:
            raise StopIteration
        else:
            tmp = self.lst[self.init]
            self.init += 1
            return tmp

    def get_nums(self):
        return self.lst


class fibonacci_gen():
    def __init__(self, data=-1):
        self.data = data
        self.init = 0
        self.x = 0
        self.y = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.data == -1:
            tmp = self.x
            self.x, self.y = self.y, self.x + self.y
            return tmp
        else:
            if self.init == self.data:
                raise StopIteration
            else:
                tmp = self.x
                self.x, self.y = self.y, self.x + self.y
                self.init += 1
                return tmp
