# n = 3
# for i in range(n, 0, -1):
#     print("*" * i)


def func(n):
    if n == 0:
        return
    func(n-1)
    print("* "*n)
    

n = 5
func(n)