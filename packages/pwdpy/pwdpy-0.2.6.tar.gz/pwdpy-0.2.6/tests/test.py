import pwdpy
import string
import math
import passgen

print(pwdpy.generate(quantity=1,
    length=15,
    punctuation=True,
    digits=True,
    letters=True,
    l_upper=True,
    l_lower=True
    ))

# def test(pwd):
#     lc = False
#     up = False
#     d = False
#     p = False
#     pool_size = 0
#     for l in pwd:
#         if l in string.ascii_lowercase:
#             lc = True
#         elif l in string.ascii_uppercase:
#             up = True
#         elif l in string.digits:
#             d = True
#         elif l in string.punctuation:
#             p = True
#         else:
#             print
        
#     if lc:
#         pool_size += len(string.ascii_lowercase)
#     if up:
#         pool_size += len(string.ascii_uppercase)
#     if d:
#         pool_size += len(string.digits)
#     if p:
#         pool_size += len(string.punctuation)
#     tam = len(pwd)
#     log = math.log(pool_size, 2)
            
#     return tam * log

# print(test("1n|9//e^1'/th4"))