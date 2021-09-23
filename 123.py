# class Air:
#     _brand = ''
#     _price = 0
#     _time = 0
#     def setBrand(self,brand):
#        self._brand = brand
#     def getBrand(self):
#         return self._brand
#     def setPrice(self,price):
#         if price <=0:
#             print("价格不能为零")
#         else:
#             self._price = int(price)
#     def getPrice(self):
#         return self._price
#     def setTime(self,time):
#         if time < 0:
#             print("时间不能为负")
#         else:
#              self._time = int(time)
#     def power_on(self):
#         print("空调开机")
#     def shut_down(self):
#         print("空调将在",self._time,"分钟后关机")
# p= Air()
# p.power_on()
# p.setBrand (input("空调品牌"))
# p.setPrice(int(input("价格")))
# p.setTime(int(input("分钟后关机")))
class student:
    __name =''
    __age =0
    def setName(self,name):
        self.__name = name
    def getsetName(self):
        return self.__name


    def setage(self,age):
        if age>120 or age<0:
            print('年龄输入非法')
        else:
            self.__age=age
    def getage(self):
        return self.__age

    def showme(self):
        print('大家好我是：',self.__name,'我今年',self.__age,)
    def compare(self,student):
        if self.__age > student.getage():
            print('我比我同桌大',(self.__age-student.getage()),'岁')
        elif self.__age < student.getage():
            print('我比他小',(student.getage() - self.__age),'岁')
        else:
            print('一样大')
s=student()
s.setName('第一')
s.setage(33)
s1=student()
s1.setName("都是")
s1.setage(33)
s.compare(s1)
s1.compare(s)
s.showme()
s1.showme()






