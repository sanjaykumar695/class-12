#Global Lists
n1=[]
p1=[]
n2=[]
p2=[]
ttl=0
ch_no=[]
ilist=[]
qlist=[]
plist=[]
tlist=[]

item_price={"Chocolate Cake":70,"Strawberry Cake":75,"Vennila Cake":60,"Watermelon Cake":75,"Honey Cake":65,"Sponge Cake":60,"Plum Cake":50,"Pineapple Cake":70,"Egg-less Cake":50,"Apple Cake":85,"Mango Cake":75,"Red Velvet":85,"Black Forest":90,"White Forest":90,"Rainbow Cake":95,"Berry Cake":90,"Veg Puffs":15,"Egg Puffs":20,"Mushroom Puffs":25,"Chicken Puffs":45,"Mutton Puffs":55,"Paneer Puffs":40,"Potato Chips":25,"Onion Rings":30,"Lolipop":5,"Lays":10,"Bingo":10,"chetos":15,"Kurkure":10,"Muruku":20,"Thattu Vadai":25,"Samosa":15,"Pakoda":30,"Coco-cola":45,"Bovonta":60,"Fanta":40,"7-Up":45,"Mountain Dew":40,"Pepsi":45,"Red Bull":50,"Tea":10,"Coffee":15,"Badam Milk":15,"Rose Milk":20,"Green Tea":30,"Bread":25,"Rusk":30,"Bun":5,"Mini-Bun":20,"Coconut Bun":30}

item_order={1:"Chocolate Cake",2:"Strawberry Cake",3:"Vennila Cake",4:"Watermelon Cake",5:"Honey Cake",6:"Sponge Cake",7:"Plum Cake",8:"Pineapple Cake",9:"Egg-less Cake",10:"Apple Cake",11:"Mango Cake",12:"Red Velvet",13:"Black Forest",14:"White Forest",15:"Rainbow Cake",16:"Berry Cake",17:"Veg Puffs",18:"Egg Puffs",19:"Mushroom Puffs",20:"Chicken Puffs",21:"Mutton Puffs",22:"Paneer Puffs",23:"Potato Chips",24:"Onion Rings",25:"Lolipop",26:"Lays",27:"Bingo",28:"chetos",29:"Kurkure",30:"Muruku",31:"Thattu Vadai",32:"Samosa",33:"Pakoda",34:"Coco-cola",35:"Bovonta",36:"Fanta",37:"7-Up",38:"Mountain Dew",39:"Pepsi",40:"Red Bull",41:"Tea",42:"Coffee",43:"Badam Milk",44:"Rose Milk",45:"Green Tea",46:"Bread",47:"Rusk",48:"Bun",49:"Mini-Bun",50:"Coconut Bun"}

#Main
def home():
    print("-"*55)
    print("\tWELCOME TO GANAPATHI IYER BAKERY")
    home_123()

def home_123():
    print("-"*55)
    print("\t\t1.Create Account")
    print("\t\t2.Log-in")
    print("-"*55)
    ch1=int(input("Enter your choice: "))
    if ch1==1:
        create_acc()
    elif ch1==2:
        log_in()
    else:
        print("Invalid Number")
        home_123()

def create_acc():
    global n1
    global p1
    import mysql.connector as sql
    sqldb=sql.connect(host="localhost",user="root",passwd="sanjay@2005",database="bakery")
    sqlcursor=sqldb.cursor()
    print("-"*55)
    name=input("Enter your Name: ")
    pin=int(input("Create your password(4):"))
    if name != "" and pin !="":
        n1.append(name)
        p1.append(pin)
    else:
        print("Please Enter the Details")
    print("-"*55)
    print("Account Created Successfully")
    print("-"*55)
    data=(str(name),str(pin))
    q1="insert into uinfo values(%s,%s)"
    sqlcursor.execute(q1,data)
    sqldb.commit()
    home_123()
    
def log_in():
    global n2
    global p2
    import mysql.connector as sql
    sqldb=sql.connect(host="localhost",user="root",passwd="sanjay@2005",database="bakery")
    sqlcursor=sqldb.cursor()
    name=input("Enter your Name: ")
    pin=int(input("Enter your Password: "))
    rec=[name,pin]
    if name != "" and pin !="":
        n2.append(name)
        p2.append(pin)
    else:
        print("Please Enter the Details")
    sqlcursor.execute("select * from uinfo")
    l=[]
    for x in sqlcursor:
        y=list(x)
        l.append(y)
    for i in l:
        if i == rec:
            log_in_123()
            break
        
def log_in_123():
    print("-"*55)
    print("\t1.View previous Record")
    print("\t2.Place An Order")
    print("\t3.Delete A Record")
    print("\t4.Quit")
    print("-"*55)
    ch2=int(input("Enter your Choice: "))
    if ch2==1:
        old_rec()
    elif ch2==2:
        items()
    elif ch2==3:
        del_rec()
    elif ch2==4:
        tq()
    else:
        print("Invalid Number")
        log_in_123()
        
def tq():
    
    print("\tTHANKS FOR VISITING")
    print("-"*55)

def old_rec():
    import mysql.connector as sql
    sqldb=sql.connect(host="localhost",user="root",passwd="sanjay@2005",database="bakery")
    sqlcursor=sqldb.cursor()
    global n2
    
    name=input("Enter your Name: ")
    n=tuple(name)
    q="select * from oinfo values{}".format(n)
    sqlcursor.execute(q)
    result=sqlcursor.fetchall()
    for i in result:
        print(i,"\n")
    log_in_123()
    
    
def del_rec():
    import mysql.connector as sql
    sqldb=sql.connect(host="localhost",user="root",passwd="sanjay@2005",database="bakery")
    sqlcursor=sqldb.cursor()
    c=int(input("Enter item code to Delete:"))
    q="delete from oinfo where icode = {}".format(c)
    sqlcursor.execute(q)
    log_in_123()

def items():

    print("-"*55)
    print("List of Items")
    print("-"*55)
    print("           CAKE")
    print("    1. Chocolate cake  70/500g")
    print("    2. Strawberry cake 75/500g")
    print("    3. Vennila cake    60/500gm")
    print("    4. Watermelon cake 75/500gm")
    print("    5. Honey cake      65/500gm")
    print("    6. Sponge cake     60/500gm")
    print("    7. Plum cake       50/500gm")
    print("    8. Pineapple cake  70/500gm")
    print("    9. Egg less cake   50/500gm")
    print("   10. Apple cake      85/500gm")
    print("   11. Mango cake      75/500gm")
    print("-"*55)
    print("         ICE CAKES")
    print("   12. Red Velvet      85/500gm")
    print("   13. Black Forest    90/500gm")
    print("   14. White Forest    90/500gm")
    print("   15. Rainbow Cake    95/500gm")
    print("   16. Berry Cake      90/500gm")
    print("-"*55)
    print("         PUFFS")
    print("   17. Veg Puffs       15/pic")
    print("   18. Egg Puffs       20/pic")
    print("   19. Mushroom Puffs  25/pic")
    print("   20. Chicken Puffs   45/pic")
    print("   21. Mutton Puffs    55/pic")
    print("   22. Paneer Puffs    40/pic")
    print("-"*55)
    print("         SNACKS")
    print("   23. Potato chips    25/100gm")
    print("   24. Onion rings     30/100gm")
    print("   25. Lolipop         5/pic")
    print("   26. Lays            10/pic")
    print("   27. Bingo           10/pic")
    print("   28. Chetos          15/pic")
    print("   29. Kurkure         10/pic")
    print("   30. Muruku          20/pac")
    print("   31. Thattu Vadai    25/pac")
    print("   32. Samosa          15/pic")
    print("   33. Pakoda          30/100gm")
    print("-"*55)
    print("        DRINKS")
    print("   34. coco-cola       45/li")
    print("   35. Bovonto         60/li")
    print("   36. Fanta           40/li")
    print("   37. 7-UP            45/li")
    print("   38. Mountain Dew    40/li")
    print("   39. Pepsi           45/li")
    print("   40. Red-Bull        50/li")
    print("   41. Tea             10/glass")
    print("   42. Coffee          15/glass")
    print("   43. Badam Milk      15/glass")
    print("   44. Rose Milk       20/glass")
    print("   45. Green Tea       30/glass")
    print("-"*55)
    print("         BAKES")
    print("   46. Bread           25/pac")
    print("   47. Rusk            30/pac")
    print("   48. Bun             5/pic")
    print("   49. Mini-Bun        20/pac")
    print("   50. Coconut Bun     30/pic")
    print("-"*55)
    print("Press 0 to complete order")
    order_f()

def order_f():
    import mysql.connector as sql
    sqldb=sql.connect(host="localhost",user="root",passwd="sanjay@2005",database="bakery")
    sqlcursor=sqldb.cursor()
    global ilist
    global qlist
    global plist
    global tlist
    global order
    global ttl
    global n2
    y1=1
    while(y1 != 0):
        ch3=int(input("->"))
        if ch3 == 0:
            bill_123()
            y1=0
        if ch3 > 50:
            print("Invalid Number")
            order_f()
        if ch3 in item_order.keys():
            ch_no.append(ch3)
            qty=int(input("Enter quantity : "))
            ilist.append(item_order[ch3])
            qlist.append(qty)
            plist.append(item_price[item_order[ch3]])
            tlist.append(qty*item_price[item_order[ch3]])
            ttl=ttl+(qty*item_price[item_order[ch3]])
            rec=(str(ch3),str(item_order[ch3]),str(qty),str(item_price[item_order[ch3]]),str(n2))
            q="insert into oinfo values(%s,%s,%s,%s,%s)"
            sqlcursor.execute(q,rec)
            sqldb.commit()

def bill_123():
    n=int(input("Enter 1 to Bill: "))
    if n==1:
        bill()
    else:
        print("Invalid Number")
        bill_123()
        
def bill():
    global order
    global ttl
    global n2

    print("")
    print("-"*55)
    print("                  GANAPATHI IYER BAKERY")
    print("               no.13, Kaamachi Amman street,")
    print("             Kumbakonam, Thanjavur,  Tamil Nadu.")
    print("                      ph:9790938616")
    print("-"*55)
    print("Name : ",str(n2))
    print("-"*55)
    print(" S.no       Item          Prize    quantity    total")
    for i in range(len(ch_no)):
        if len(ilist[i]) ==3:
            print(" ",i+1,"     ",ilist[i]," "*13,plist[i],"      ",qlist[i],"     ",tlist[i])
        elif len(ilist[i]) ==4:  
            print(" ",i+1,"     ",ilist[i]," "*12,plist[i],"      ",qlist[i],"     ",tlist[i])
        elif len(ilist[i]) ==5:  
            print(" ",i+1,"     ",ilist[i]," "*11,plist[i],"      ",qlist[i],"     ",tlist[i])
        elif len(ilist[i]) ==6:  
            print(" ",i+1,"     ",ilist[i]," "*10,plist[i],"      ",qlist[i],"     ",tlist[i])
        elif len(ilist[i]) ==7:  
            print(" ",i+1,"     ",ilist[i]," "*9,plist[i],"      ",qlist[i],"     ",tlist[i])
        elif len(ilist[i]) ==8:  
            print(" ",i+1,"     ",ilist[i]," "*8,plist[i],"      ",qlist[i],"     ",tlist[i])
        elif len(ilist[i]) ==9:  
            print(" ",i+1,"     ",ilist[i]," "*7,plist[i],"      ",qlist[i],"     ",tlist[i])
        elif len(ilist[i]) ==10:  
            print(" ",i+1,"     ",ilist[i]," "*6,plist[i],"      ",qlist[i],"     ",tlist[i])
        elif len(ilist[i]) ==11:  
            print(" ",i+1,"     ",ilist[i]," "*5,plist[i],"      ",qlist[i],"     ",tlist[i])
        elif len(ilist[i]) ==12:  
            print(" ",i+1,"     ",ilist[i]," "*4,plist[i],"      ",qlist[i],"     ",tlist[i])
        elif len(ilist[i]) ==13:  
            print(" ",i+1,"     ",ilist[i]," "*3,plist[i],"      ",qlist[i],"     ",tlist[i])
        elif len(ilist[i]) ==14:  
            print(" ",i+1,"     ",ilist[i]," "*2,plist[i],"      ",qlist[i],"     ",tlist[i])
        elif len(ilist[i]) ==15:  
            print(" ",i+1,"     ",ilist[i]," "*1,plist[i],"      ",qlist[i],"     ",tlist[i])

    print("-"*55)
    print("Total amount : ",ttl)
    print("-"*55)
    print(" "*20,"THANK YOU",str(n2))
    print(" "*24,"VISIT AGAIN")
    print("-"*55)                
           

home()

    
