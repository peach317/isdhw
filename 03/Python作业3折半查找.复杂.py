
def f(a,i):
    b=[]
    c=False
    low=0
    high=len(a)-1
    while(low<(high-1)):
        mid=int((low+high)/2)
        if(a[high]==i):
            m=high
            while(a[high]==i and high>=0):
                b.append(high)
                high=high-1
            high=m+1
            while( high<=(len(a)-1) and a[high]==i):
                b.append(high)
                high=high+1
            c=True
            break
        if(a[low]==i):
            m=low
            while(a[low]==i and low>=0):
                b.append(low)
                low=low-1
            low=m+1
            while(a[low]==i and low<=(len(a)-1)):
                b.append(low)
                low=low+1
            c=True
            break
        if(a[mid]==i):
            m=mid
            while(a[mid]==i and mid>=0):
                b.append(mid)
                mid=mid-1
            mid=m+1
            while(a[mid]==i and mid<=(len(a)-1)):
                b.append(mid)
                mid=mid+1
            c=True
            break
        elif(a[mid]>i):
            high=mid
        elif(a[mid]<i):
            low=mid
    if(c):
        return(sorted(b))

    else:
        return(0)
stu=input("请输入要被查找的序列，并以逗号隔开，例如 1,2,3,4 可以不按照大小顺序：")
stu1=eval(stu)#将stu的值返回到元组stu1中
stu2=list(stu1)#将stu1强行转化为列表stu2
a=sorted(stu2)#将stu2从小到大排序返回a
print("重新排序过的序列:",a)
i=int(input("请输入你要查找到数："))
b=f(a,i)
if b==0:
    print('没有找到')
else:
    for i in range(0,len(b)):
        print("经过重新从小到大排序，你要找的数在列表中的第{0}个位置".format(b[i]))
    
