def persistence(n):
    def persists(n,count=1):
        if n < 10:
            return 0
        mult = 1
        while n:
            mult *= n % 10
            n /= 10
        if(mult >= 10):
            return persists(mult,count+1)
        else:
            return count
    return persists(n)
