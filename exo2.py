import re
import numpy as np

s = 'I refer to https://google.com and I never refer http://www.baidu.com if I have to search anything'
s1 = 'Office of Research Administration: (734) 647-6333 | 4325 North Quad Office of Budget and Financial Administration: (734) 647-8044 | 309 Maynard, Suite 205 Health Informatics Program: (734) 763-2285 | 333 Maynard, Suite 500 Office of the Dean: (734) 647-3576 | 4322 North Quad UMSI Engagement Center: (734) 763-1251 | 777 North University Faculty Adminstrative Support Staff: (734) 764-9376 | 4322 North Quad'

text=r'''Everyone has the following fundamental freedoms:
(a) freedom of conscience and religion;
(b) freedom of thought, belief, opinion and expression, including freedom of the press and other media of communication;
(c) freedom of peaceful assembly; and
(d) freedom of association.
'''

s3 = 'ACAABAACAAAB'
s4 = 'ACBCAC'

old = np.array([[1, 1, 1], [1, 1, 1]])
new = old
new[0, :2] = 0

string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
result0 = re.findall('b[ao]t', string)
print('Q1: ', result0)



print('-----------------------------------------')
print('Q4: ', old)


print('Q6----------------------------------------------')
print(re.findall('^AC', s4))
print('Q7------------------------------------------------')

result2 = re.findall('A{1,2}', s3)
L = len(result2)
print(L)
print('Q8------------------------------------------------')

pattern = '\(.\)'
#Affichage de nombre de fois que pattern exite dans le text

print(len(re.findall(pattern,text)))
print('------------------------------------------------')

result = re.findall('(?<=[https]:\/\/)([A-Za-z0-9.]*)', s)
result1 = re.findall('[(]\d{3}[)]\s\d{3}[-]\d{4}', s1)

print(result)
print('-------------------------------------------------')
print(result1)