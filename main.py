import random

def text():
    f = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
<<<<<<< HEAD
    f1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    res = ''
    for i in range(11):
        res += random.choice(f+f1)
=======
    r = ['0','1','2','3','4','5','6','7','8','9']
    res = ''
    for i in range(11):
        res += random.choice(f+r)
>>>>>>> dev
    return res
    
x = text()
print(x)
