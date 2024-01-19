import mysql.connector as mycon
cn = mycon.connect(host='127.0.0.1',user='root',password="root",database="saumyen")
cur = cn.cursor()
def showAll():
    
    global cn
    global cur
    
    try:
        query="select * from chelsea"
        cur.execute(query)
        results = cur.fetchall()
        print("**************************************************")
        print('%5s'%"KIT NO",'%15s'%'NAME','%12s'%'POSITION', '%10s'%'SALARY')
        print("**************************************************")
        count=0
        for row in results:
            print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
            count+=1
        print("*************** TOTAL RECORD : ",count,"**********")
    except:
        print("error")
def addEmp():
    global cn,cur
    print("*******************ADD NEW PLAYER**************************")
    kn = int(input("Enter Kit Number :"))
    pn = input("Enter Player Name :")
    ps = input("Enter Position :")
    sl = int(input("Enter Salary :"))
    query="insert into CHELSEA values("+str(kn)+",'"+pn+"','"+ps+"',"+str(sl)+")"
    cur.execute(query)
    cn.commit()
    #print(query)
    print("\n ## RECORD ADDED SUCCESSFULLY!")
def searchEmp():
    global cn,cur
    print("*******************SEARCH PLAYER FORM **************************")
    kn = int(input("Enter Employee number to search :"))
    query="select * from CHELSEA where Kit_No="+str(kn)
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
    else:
       
        print("**************************************************")
        print('%5s'%"KITNO",'%15s'%'NAME','%12s'%'POSITION','%10s'%'SALARY')
        print("**************************************************")
        for row in results:
            print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
    print("-"*50)
def editEmp():
    global cn,cur
    print("*******************EDIT PLAYER FORM **************************")
    kn = int(input("Enter Kit number to edit :"))
    query="select * from CHELSEA where Kit_No="+str(kn)
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
    else:
       
        print("**************************************************")
        print('%5s'%"KITNO",'%15s'%'NAME','%12s'%'POSITION','%10s'%'SALARY')
        print("**************************************************")
        for row in results:
            print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
    print("-"*50)
    ans = input("Are you sure to update ? (y/n)")
    if ans=="y" or ans=="Y":
        p = input("Enter new position to update (enter old value if not to update) :")
        s = int(input("Enter new salary to update (enter old value if not to update) :"))
        query="update CHELSEA set Position='"+p+"',salary="+str(s) + " where Kit_No="+str(kn)
        cur.execute(query)
        cn.commit()
        print("\n## RECORD UPDATED  ##")
                
def delEmp():
    global cn,cur
    print("*******************DELETE PLAYER FORM **************************")
    kn = int(input("Enter Kit number to delete :"))
    query="select * from CHELSEA where Kit_No="+str(kn)
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
    else:
       
        print("**************************************************")
        print('%5s'%"KITNO",'%15s'%'NAME','%12s'%'POSITION','%10s'%'SALARY')
        print("**************************************************")
        for row in results:
            print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
    print("-"*50)
    ans = input("Are you sure to delete ? (y/n)")
    if ans=="y" or ans=="Y":
        query="delete from emp where empno="+str(en)
        cur.execute(query)
        cn.commit()
        print("\n## RECORD DELETED  ##")
def clear():
      for i in range(1,50):
          print()
          
def generateSlip():

    global cn,cur
    print("*******************SALARY SLIP **************************")
    kn = int(input("Enter Kit number to print salary slip :"))
    query="select * from CHELSEA where Kit_No="+str(kn)
    cur.execute(query)
    results = cur.fetchone()
    if cur.rowcount<=0:
        print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
    else:
        clear()
        print("Kit_No :",results[0]," "*20,"NAME :",results[1])
        print("Position:",results[2])
        print("*"*50)
        s = int(results[3])
        LBonus = s * 15/100
        LSBonus = 1000
        SEBonus = (s+LBonus)*10/100
        gross = s+LBonus+SEBonus
        ded = LSBonus + SEBonus
        net = gross - ded
        tded= LSBonus+ SEBonus
        print("%19s"%"EARNING","%27s"%"DEDUCTION")
        print("-------------------------------------------------")
        print("%20s"%"Basic  :"+str(s),"%22s"%"INC. TAX :"+str(LSBonus))
        print("%20s"%"Loyalty Bonus  :"+str(LBonus))
        print("%20s"%"Season Ending Bonus :"+str(SEBonus))
        print("-"*50)
        print(" Gross :",gross," NET SALARY :",net,"  TOTAL DED :",tded)
    print("-"*50)
    print("=== PRESS ANY KEY ===")
    input()
        
while True:
    print("1. SHOW PLAYER LIST ")
    print("2. ADD NEW PLAYER")
    print("3. SEARCH  PLAYER ")
    print("4. EDIT PLAYER ")
    print("5. DELETE PLAYER ")
    print("6. GENERATE PAY SLIP ")
    print("7. CONTACT US")
    print("0. EXIT")
    ans = int(input("Enter your choice :"))
    if ans==1:
        showAll()
    elif ans==2:
        addEmp()
    elif ans==3:
        searchEmp()
    elif ans==4:
        editEmp()
    elif ans==5:
        delEmp()
    elif ans==6:
        generateSlip()
    elif ans==7:
        print("*"*60)
        print(" "*20,"AUTHOR : Saumyen Prateek Deka ")
        print(" "*20,"EMAIL  : saumyen18@gmail.com")
        print("*"*60)
    elif ans==0:
        print("\nBye!!")
        cn.close()
        break
