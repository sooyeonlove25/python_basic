a = [1, 2, 3, ['a', 'b', 'c']]
print(a)
print(type(a))
print(a[0])
print(a[3][1])

a = [1, 2, 3, ['a', 'b', [1,3,5],'c']]
print(a[0])
print(a[3][1])
print(a[3][2][1:])

jumin = '000212-41111111'
print(jumin.split())

jumin = '000212 41111111'
print(jumin.split())

jumin = '000212 41111111'
print(jumin.split())
print(len(jumin))
print(len(a))
print(len(a[3]))

a = [1, 2, 3, ['abbb', 'b', [1,3,5],'c']]
print(len(a[3][0]))

a = [1, 2, 3, ['abbb', 'b', [1,3,5],'c']]
a[3][0] = 'hi'
print(a)

a = [1, 2, 3, ['abbb', 'b', [1,3,5],'c']]
del a[3]
# print(a)

a = [1, 2, 3, ['abbb', 'b', [1,3,5],'c']]
del a
# print(a)

a = [1,2,3]
a.append('qqq')
print(a)
a.insert(0,'aaa')
print(a)
a = [1, 4, 3, 2]
a.sort(reverse=True)
print(a)

#  첫 번째로 나오는 x를 삭제하는 함수 -> remove(x)
a = [1, 4, 3, 2]
a.reverse()
print(a)

a = ['a', 'b', 'c']
a.remove('b')
print(a)

a = ['a', 'b', 'c','b']
print(a.remove('b'))
print(a)

a = ['a', 'b', 'c', 'b']
print(a.pop(a.index('b')))
print(a)

t1 = (1, 2, 'a', 'b')
t1[0] = 0
del t1[0]