
def foo(n):
    if n==0:
        return
    foo(n-1)
    print(n, end=" ")

foo(10)
print()

def foo2(n):
    if(n==0):
        return
    print(n, end=" ")
    foo2(n-1)

foo2(10)