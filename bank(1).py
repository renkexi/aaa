import random
import pymysql
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank='第四十银行'
money = 0
con=pymysql.connect(host="localhost", user='root',password='',database='银行')
cursor=con.cursor()
def bank_adduser():
    spl="select count(*) from kaihu"
    cursor.execute(spl)
    data = cursor.fetchall()
    if len(data) >=100:
        print("已满")

    account = random.randint(10000000,99999999)
    spl1 = "select * from kaihu where account = %s"
    param = [account]
    cursor.execute(spl1,param)
    data = cursor.fetchall()

    if len(data) !=0:
        print("失败，重复")
    else:
        username = input("请输入您的用户名")
        password = input("请输入您的密码")
        print("请输入您的地址")
        country = input("\t\t请输入您的国家")
        province = input("\t\t请输入您的省份")
        street = input("\t\t请输入您的街道")
        door = input("\t\t请输入您的门牌号")
        sql2: str = "insert into kaihu vaiues(%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
        param = [account,username,country,province,street,door,money,bank]
        cursor.execute(sql2,param)
        con.commit()


        info='''
                ----------个人信息---------
                       用户名:%s        
                       密码：*****       
                       地址：%s          
                       余额：%s          
                       开户行名称：%s     
                --------------------------
                开户成功
        '''
        print(info % (username, account, country, province, street, door, money, bank))
def addmoney():
    a1 = int(input("请输入您的账号"))
    sql3 = "select * from kaihu where account = %s"
    param = [a1]
    cursor.execute(sql3, param)
    data = cursor.fetchall()
    if len(data) == 1:
         money1 = float(input("请输入您需要存入的金额："))
         money2 = data[0][7] + money1
         sql4 = "update kaihu set money = %s + money where account = %s"
         param1 = [money2, a1]
         cursor.execute(sql4, param1)
         con.commit()
         info = '''
                        ------------个人信息------------
                        用户名:%s
                        账号：%s
                        余额：%s
                        开户行名称：%s
                    '''
            # 每个元素都可传入%
         print(info % (data[0][1], data[0][0], money2, data[0][8]))
    else:
         print("您的账户输入错误")
def remoney():
    while True:
        username = input('请输入用户名:')
        password = input('请输入密码：')
        if username not in bank:
            print('你还没有开户，请先开户')
            break
        else:
            while bank[username]['password'] != password:
                password = input("密码错误,请重新输入密码")

            print('您现在账户%s元'%(bank[username]['money']))
            a=input('请输入取款金额：')
            if a.isdigit():
                if int(a)<= bank[username]['money']:
                    bank[username]['money']-=int(a)
                    print('尊敬的%s,存钱已完成，您现在账户余额：%s'%(username,bank[username]['money']))
                    break
                else :
                    print("输入错误")
            else:
                 print('你输入得什么')


# 定义转账方法
def zhuanzhang():
    while True:
        username = input('请输入用户名:')
        password = input('请输入密码：')
        if username not in bank:
            print('你还没有开户，请先开户')
            break
        else:
            while bank[username]['password'] != password:
                password = input("密码错误,请重新输入密码")

            gousername=input('请输入要转给的用户名：')
            while gousername not in bank:
                gousername=input('你要转给的用户不存在，请重新输入：')
            if username==gousername:
                print("自己转自己好玩是吧？")
                continue
            print('您现在账户%s元' % (bank[username]['money']))
            gomoney=input('请输入转账金额')
            if gomoney.isdigit():
                if int(gomoney)<= bank[username]['money']:
                    bank[username]['money']-=int(gomoney)
                    bank[gousername]['money'] += int(gomoney)
                    print('尊敬的%s,转账已完成，您现在账户余额：%s'%(username,bank[username]['money']))
                    break
                else :
                    print("你在想屁吃")
            else:
                 print('你输入得什么玩意')
def chaxun():
    while True:
        username = input('请输入用户名:')
        password = input('请输入密码：')
        while username not in bank:
            username=input('你要查询的用户不存在，请重新输入要查询的用户')

        while bank[username]['password'] != password:
            password = input("密码错误,请重新输入密码")
        info = '''
                ----------个人信息---------
                       用户名:%s        
                       密码：*****       
                       地址：%s          
                       余额：%s          
                       开户行名称：%s     
                --------------------------
                '''
        print(info % (username, bank[username]['address'], bank[username]['money'], bank_name))
while True:
    print('''
    ---------------欢迎来银行---------------
    -------------------------------------------
    ----------1.开户            ----------------
    ----------2.存钱            ----------------
    ----------3.取钱            ----------------
    ----------4.转账            ----------------
    ----------5.查询            ----------------
    ----------6.Bye            ----------------
    -------------------------------------------
    ''')
    chose = input('你好，请输入操作项')
    if chose=='1':
        bank_adduser()
    elif chose=='2':
        addmoney()
    elif chose=='3':
        remoney()
    elif chose=='4':
        zhuanzhang()
    elif chose=='5':
        chaxun()
    else:
        print('欢迎下次光临')
        cursor.close()
        con.close()
        break