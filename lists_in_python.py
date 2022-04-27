# a=['foo','bar','baz','qux']
# b=['baz','qux','bar','foo']
# print(id(a),id(b))
# l1=[1,2,3,4]
# l2=[3,4,1,2]
# print(id(l1),id(l2))
# print(l1 is l2)
# print([1,2,3,4]==[1,2,3,4])
# a=['foo','bar','baz','qux','quux','corge']
# print(a[4],a[-2])
# print(a[1],a[-5])
# print(a[-1])
# print(a[0])
# print(a[2:5])
# print(a[1:4])
# print(a[-5:-2])
# print(a[:4],a[0:4])
# print(a[3:],a[3:6])
# print(a[:4]+a[4:])
# print(a[:3]+a[3:])
# print(a[::])
# print(a[:])
# print(a[:3]+a[3:]==a)
# l=['a','b','c','d','e','f','g','h','i']
# print(l[2:7:2])
# print(l[2::2])
# print(l[2:7:3])
# 3step slicing
# a=['foo','bar','baz','qux','quux','corge']
# print(a[0:7:2])
# print(a[::2])
# print(a[0:6:2])
# print(a[2::2])
# print(a[::-1])
# print(a[0::])
# print(a[::-3])
# print(a[6:0:-2])
# print(a[6:0]
# print(a[4:4])
# a=['foo','bar','baz','qux','quux','corge',0.5,40,4+5j,True,[1,2,3,4],(6,7,8),0.5,'foo',random,func,simpleclass]
# print(a)
# def func():
#     pass
# class simpleclass:
#     import random
#     pass
# a=['foo','bar','baz','qux','quux','corge',0.5,40,4+5j,True,[1,2,3,4],(6,7,8),0.5,'foo','random','func','simpleclass']
# print(a)
# a=['foo','bar','baz','qux','quux','corge']
# a[0]="madhu"
# print(a)
# print('bar' in a)
# print('qux' not in a)

# x=['a',['bb',['ccc','ddd'],'ee','ff'],'g',['hh','ii'],'j']
# print(x[1])
# print(x[1][0])
# print(x[1][1])
# print(x[1][1][0])
# print(x[3][0])
# print(x[1][3])
# print(x[4])
# print(x[-1])
# print(x[1][2])
# print('ddd' in x)
# print('ddd' in x[1])
# print('ddd' in x[1][1])

a=['foo','bar','baz','qux','quux','corge']
print(a)
# del a[3]
# print(a)
# del a[1:5]
# print(a)
# a+=['madhu','python']
# print(a)
# l=['madhu']
# print(l*3)
# print(l*-3)
l1=['madhu','python']
l2=['python','hello']
# print(l1-l2)
print(['madhu','python']+a)
a.append("python")
print(a)
a.append({'python','hello'})
print(a)
x=a.append({'a':'python','b':'hello'})
print(a)


