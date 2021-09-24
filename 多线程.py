from threading import Thread
import time
egg=0
cur=2

class cooker(Thread):
    cookername=''
    def run(self)-> None:
        global egg,cur
        while True:
            if egg<500:
                egg = egg + 1
                print("%s做了一个蛋挞，现在又%s个"%(self.cookername,egg))
            else  :
                if cur>0:
                    print("篮子已满",cur)
                    time.sleep(0.01)
                else:
                    print("没顾客了 !")
                    break

class god(Thread):
    name=''
    money=3000
    num=0
    def run(self) -> None:
        global egg,cur
        while True:
            if self.money>=10:
                if egg>0:
                    egg=egg-1
                    self.money=self.money-10
                    print("%s买了一个蛋挞，还剩%s个蛋挞，还有%s￥"%(self.name,egg,self.money))
                else :
                    print('没蛋挞了')
                    time.sleep(0.02)
            else :
                cur = cur - 1
                print("meiqianle")
                break







c1=cooker()
c1.cookername ="1"

c2=cooker()
c2.cookername="2"

c3=cooker()
c3.cookername="3"

d1=god()
d1.name='11'

d2=god()
d2.name='22'
c1.start()
c2.start()
c3.start()

d1.start()
d2.start()




