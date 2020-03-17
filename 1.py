'''
    python 关键字
'''
#单行注释
import keyword

print(keyword.kwlist);

'''
    行与缩进，不需要使用大括号
'''
if True:
    print("asda");
else:
    print("False");

'''
    数字类型变量
'''
var = 1;
'''
    浮点类型变量
'''
var1 = 1.0;
print(var+var1);
print(var // var1) #取整
print(var % var1)  #求余

del var1; #删除变量


'''
    字符串
'''
str1 = "susu";
str2 = 'susu';
print(str1[0]);
#倒起数
print(str1[-1]);
print(str1[-4]);
#字符串截取
print(str1[0:3])

str3 = 'hello world'
print(str3)
#查看有哪些方法
print(dir(str3))
#重复100次
print("*" * 100)
print(str3.upper())


'''
    列表
'''
list = [1,3,'ad',3.9]
print(list[2])
print(list[-1])

print(list[0:3])

list = [1,2,3,4,5,6,7,8,9,10]
print("*" * 100)
print(list[0:])
print(list[0],list[2],list[4],list[6],list[8])
print(list[0::2])
print(list[-1::-1])
print("-" * 100)

list = [1,3,5]
list.append(9)
print(list)
list[0] = 2
print(list)
del list[0]
print(list)
list.remove(5)
print(list)
list.reverse()
print("*"*100)
'''
print(help(list.remove))
print(help(list))
'''



'''
    
'''
tup = (1, 3, 'abc', 3.0)
print(tup[0])
print(tup[-1])
'''
(tup[0], tup[1], tup[2])
'''
print(tup[0: 3])
#不能修改里面的元素


print("*" * 100)


'''
    字典类似于Java的HasHMap
'''
susu = {"name":"苏苏","age":"15"}
susu["sex"] = 0;
susu[1] = 1;
print(susu);
susu["name"] = "苏酒儿"
print(susu)

del susu[1]
print(susu)

print(susu.values())
print(susu.keys())
print("*"*100)

'''
    集合类似于Java里面的HashSet
'''
set = {1,6,3,4,5,2}

set.add(0)
print(set)

set.remove(2)
print(set)

print(len(set))
set.clear();


'''
不可变数据类型
'''
#修改其内容，内存地址，也相应发生改变
a = 100
print(id(a))
a = 300
print(id(a))

print("*" * 100)

#可变数据类型
#修改其内容，内存地址不会发生改变
list = [1,3,4]
print(id(list))
list.append(5)
print(id(list))

print("函数角色--" * 100)

#不可变数据类型在函数中，不能对其内容进行修改
def changeVal(a):
    a = 100

b = 1000
changeVal(b)
print(b)

#可变数据类型，在函数中能修改其内容
def addVal(list):
    list.append(10000)

list = [1,3,4]
addVal(list)
print(list)

'''
While
'''

'''
for
'''
sites = ["susu","sujiuer","aisha"]
for site in sites:
    if site == "susu":
        print("苏苏")
        break
else:
    print("没有数据")



'''
range()
'''
print("*"*100)
print(type(range(10)))

print("*"*100)
for val in range(1,10):
    print(val)
