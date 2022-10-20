




class Deque:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def push_back(self, value):
        if self.head == self.tail:
            self.head = -1 % self.max_n
        if self.size != self.max_n:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            return print('error')

    def push_front(self, value):
        if self.size != self.max_n:
            if self.tail == self.head == 0:
                self.tail = 1
            self.queue[self.head] = value
            self.head = (self.head - 1) % self.max_n
            self.size += 1
        else:
            return print('error')

    def pop_front(self):
        if self.is_empty():
           return print('error')
        if self.head == self.max_n-1:
            self.head = 0 % self.max_n
            x = self.queue[self.head]
            self.queue[self.head] = None
        else:
            x = self.queue[self.head+1]
            self.queue[self.head+1] = None
            self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return print(x)

    def pop_back(self):
        if self.is_empty():
           return print('error')
        x = self.queue[self.tail-1]
        self.queue[self.tail-1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return print(x)


def main():
 ran = int(input())
 n = int(input())
 d = Deque(n)
 for i in range(ran):
    input_arr = input().split()
    if input_arr[0] == 'pop_front':
        d.pop_front()
        print(d.queue)
        print('head:', d.head, 'tail:', d.tail)
    if input_arr[0] == 'pop_back':
        d.pop_back()
        print(d.queue)
        print('head:', d.head, 'tail:', d.tail)

    if input_arr[0] == 'push_front':
        d.push_front(int(input_arr[1]))
        print(d.queue)
        print('head:', d.head, 'tail:', d.tail)

    if input_arr[0] == 'push_back':
        d.push_back(int(input_arr[1]))
        print(d.queue)
        print('head:', d.head, 'tail:', d.tail)


if __name__ == '__main__':
    main()
