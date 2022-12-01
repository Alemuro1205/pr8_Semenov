import random

def text():
    f = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    res = ''
    for i in range(11):
        res += random.choice(f)
    return res


x = text()
print(x)
