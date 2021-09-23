class people:
    __name=''#姓名
    __sex=''#性别
    __age=0#年龄
    __sy=0#剩余话费
    __pp=''#品牌
    __rl=0#手机电池容积
    __size=0#屏幕尺寸
    __time=0#待机时长
    __jifen=0#拥有积分
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setsex(self,sex):
        self.__sex=sex
    def getsex(self):
        return self.__sex
    def setage(self,age):
        if age<=0 or age>120:
            print('输入非法')
        else:
            self.__age=int(age)
    def getage(self):
        return self.__age
    def setSy(self,sy):
        self.__sy=sy
    def getsy(self):
        return self.__sy
    def setpp(self,pp):
        self.__pp=pp
    def getpp(self):
        return self.__pp
    def setRl(self,rl):
        if rl < 0:
            print('不能为负')
        else:
             self.__rl=float(rl)
    def getrl(self):
        return self.__rl
    def setsize(self,size):
        if size<0:
            print('输入非法')
        else:
            self.__size=int(size)
    def setime(self,time):
        self.__time=time
    def gettime(self):
        return self.__time
    def setjifen(self,jifen):
        if jifen<=0:
            print('积分不能为零')
        else:
            self.__jifen=int(jifen)
    def getjifen(self):
        return self.__jifen
    def showme(self):
        print('姓名', self.__name,
              '\n性别', self.__sex,
              '\n年龄', self.__age,
              '\n所拥有的手机剩余话费',self.__sy, '元！'
                '\n手机品牌', self.__pp
              ,'\n手机电池容量', self.__rl, '%\n屏幕大小',self.__size,
              '寸\n最大待机时长',self.__time,
              '分钟\n所拥有积分：', self.__jifen)
p=people()
p.setName(input('输入年龄'))
p.setsex(input('输入性别'))
p.setage(int(input('输入年龄')))
p.setSy(float(input('剩余话费')))
p.setpp(input('手机品牌'))
p.setRl(float(input('容积')))
p.setsize(int(input('尺寸')))
p.setime(int(input('待机时间')))
p.setjifen(int(input('积分')))
p.showme()
a=p.getsy()
b=p.getjifen()
while True:
    a=int(input('电话按1，短信按2：'))
    if a==2:
        a_2=int(input('输入内容'))
        print('内容:\n',a_2)
    elif a==1:
        a_2=int(input('电话号'))
        a_1=int(input('时间'))
        if a_2==None:print('不能为零')
        elif a_2<=1:print('话费不够')
        else:
            print('已拨通')
        if a_2>0 and a_2<10:
            if b>=a_1*15:
                b-=a_1*15
            else:
                a-=a_1*1
        elif a_1>10 and a_1<=20:
            if b>=a_1*39:
                b-=a_1*39
            else:
                a-=a_1*0.8
        else :
            if b>=a_1*48:
                b-=a_1*48
            else:
                a-=a_1*0.65
        print('s剩余话费：',a)
        print('剩余积分：',b)











