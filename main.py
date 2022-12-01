import random

def text():
    f = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    r = ['0','1','2','3','4','5','6','7','8','9']
    res = ''
    for i in range(11):
        res += random.choice(f+r)
    return res


x = text()
print(x)
