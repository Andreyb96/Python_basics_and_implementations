class Buffer:
    def __init__(self):
        self.buf = []

    def add(self, *a):
        for i in a:
            self.buf.append(i)
        while len(self.buf) >= 5:
            sum = 0
            for i in range(5):
                sum += self.buf.pop(0)
                i += 1
            print(sum)

    def get_current_part(self):
        return(self.buf)