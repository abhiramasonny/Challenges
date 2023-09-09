class prime:
    def __init__(self, n):
        self.n = n
        print(self.check(n))
        
    def check(self, n):
        if n < 2:
            return False
        if (n % 2 == 0) and (n != 2):
            return False
        if (n % 3 == 0) and (n != 3):
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6-w # formula
        return True

p = prime(30)