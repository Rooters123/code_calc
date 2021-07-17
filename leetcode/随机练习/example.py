# flag = 1
# while flag:
#   # 输入第一个矩形x与y轴的坐标数值
#   x1,x2,y1,y2 = input("<<<").split(",")
#   x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)
#
#   # 输入第二个矩形x与y轴的坐标数值
#   new_x1,new_x2,new_y1,new_y2 = input("<<<").split(",")
#   new_x1,new_x2,new_y1,new_y2 = int(new_x1),int(new_x2),int(new_y1),int(new_y2)
#
#   if (x2 <= new_x1 or new_x2 <= new_x1) and (y2 <= new_y1 or new_y2 <= new_y2):
#     print("矩形不重合，请重新输入矩形数组！")
#   else:
#     flag = 0
#
# # 构建x轴的列表和y轴的列表
# xlist = [x1,x2,new_x1,new_x2]
# ylist = [y1,y2,new_y1,new_y2]
#
# # 对xlist和ylist进行排序，寻找里面xlist和ylist里面第二大和第三大的值，分别相减进行计算
# xlist.sort()
# ylist.sort()
#
# print(abs(xlist[1] - xlist[2]) * abs(ylist[1] - ylist[2]))
import copy
a = [1,2,[3,4]]
b = copy.copy(a)
c = copy.deepcopy(a)
print(id(a),id(b),id(c))
print(id(a[2]),id(b[2]),id(c[2]))

import timeit
print(timeit.timeit("[]",number=10**5))
print(timeit.timeit("list()",number=10**5))

from dis import dis
print(dis('[]'))

