####问题描述
####小偷去偷k个房屋，偷相邻的两个房屋会出发警报，每个房屋中的价值是已知的，求解小偷能获取的最大利益

import numpy as np
##递归求解
A=[1,4,1,2,5,6,3]
# def f(A):
#     k=len(A)-1
#     if k==0:
#         sum=A[0]
#     elif k==1:
#         sum=max(A[0],A[1])
#     else:
#         m1=A[0:k]
#         m2=A[0:k-1]
#         sum=max(f(m1),f(m2)+A[k])
#     return sum
# print(f(A))

#####动态规划求解
# def f_dp(A):
#     k=len(A)-1  #得到列表A的长度，因为是从0开始，所以这里减去1
#     if k==0:
#         sum=A[0]    #如果A只有一个数，则输出这个数
#     elif k==1:
#         sum=max(A[0],A[1])  #如果A有两个数，则输出这两个数中最大的那个
#     else:
#         ff=[0]*(k+1)     #创建一个全为0的列表，长度为A的长度，用来存储在K个房屋中，获取的最大的利益
#         ff[0]=A[0]       #k=0时，表示A中只有一个元素，此时ff[0]等于A[0]
#         ff[1]=max(A[0],A[1])  #k=1时，表示A中有两个元素，值为两者中最大的那个
#         for i in range(2,k+1): #循环遍历，求解所有的ff
#             ff[i]=max(ff[i-1],ff[i-2]+A[i])
#         sum=ff[k]   #输出最后一个ff的值，就是我们想要的答案
#     return sum
# print(f_dp(A))

#########输出偷取房屋的编号

def f_dp(A):
    k=len(A)-1  #得到列表A的长度，因为是从0开始，所以这里减去1
    if k==0:
        sum=A[0]    #如果A只有一个数，则输出这个数
    elif k==1:
        sum=max(A[0],A[1])  #如果A有两个数，则输出这两个数中最大的那个
    else:
        ff=[0]*(k+1)     #创建一个全为0的列表，长度为A的长度，用来存储在K个房屋中，获取的最大的利益
        ff[0]=A[0]       #k=0时，表示A中只有一个元素，此时ff[0]等于A[0]
        ff[1]=max(A[0],A[1])  #k=1时，表示A中有两个元素，值为两者中最大的那个
        for i in range(2,k+1): #循环遍历，求解所有的ff
            ff[i]=max(ff[i-1],ff[i-2]+A[i])
        sum=ff[k]   #输出最后一个ff的值，就是我们想要的答案

    #编号可以通过ff列表推算出来
    IND=[]
    ind=ff.index(max(ff))
    IND.append(ind)
    while ff[ind]>A[ind]:
        ind=ff.index(ff[ind]-A[ind])
        IND.append(ind)
    IND.reverse()
    return sum,IND
print(f_dp(A))

