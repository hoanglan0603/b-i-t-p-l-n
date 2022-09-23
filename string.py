# username = 'mark'
# password = 'alo'
# newpass = 'abc'
# newString = "{0} is user and {1} is newpass".format(newpass,newpass)
# print(newString)

#{0} is replaced by the 1st format() argument. {1} is replaced by the 2nd.
 


# import humansize
# # si_suffixes = humansize.SUFFIXES[1000]
# # print(si_suffixes)
# # swap = '1000{0[0]} = 1{0[1]}'.format(si_suffixes)
# # print(swap)
# import sys
# a = '1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}'.format(sys)
# print(a)



s = '''Hello abc
sult of Years
is are cvv
Experience of years.'''
slist = s.splitlines()
print(slist)
# print(s.lower())
print(s.lower().count('l'))