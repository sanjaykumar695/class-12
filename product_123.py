import mysql.connector as ms
msdb=ms.connect(host="localhost",user="root",passwd="sanjay@2005",database="bakery")
msc=msdb.cursor()
p1="insert into product values(1,'Chocolate cake',1,70)"
msc.execute(p1)
msdb.commit()
print("p1 success")
p2="insert into product values(2,'Strawberry cake',1,75)"
msc.execute(p2)
msdb.commit()
print("p2 success")
p3="insert into product values(3,'Vennila cake',1,60)"
msc.execute(p3)
msdb.commit()
print("p3 success")
p4="insert into product values(4,'Watermelon cake',1,75)"
msc.execute(p4)
msdb.commit()
print("p4 success")
p5="insert into product values(5,'Honey cake',1,65)"
msc.execute(p5)
msdb.commit()
print("p5 success")
p6="insert into product values(6,'Sponge cake',1,60)"
msc.execute(p6)
msdb.commit()
print("p6 success")
p7="insert into product values(7,'Plum cake',1,50)"
msc.execute(p7)
msdb.commit()
print("p7 success")
p8="insert into product values(8,'Pineapple cake',1,70)"
msc.execute(p8)
msdb.commit()
print("p8 success")
p9="insert into product values(9,'Egg less cake',1,50)"
msc.execute(p9)
msdb.commit()
print("p9 success")
p10="insert into product values(10,'Apple cake',1,85)"
msc.execute(p10)
msdb.commit()
print("p10 success")
p11="insert into product values(11,'Mango cake',1,75)"
msc.execute(p11)
msdb.commit()
print("p11 success")
p12="insert into product values(12,'Red Velvet',1,85)"
msc.execute(p12)
msdb.commit()
print("p12 success")
p13="insert into product values(13,'Black Forest',1,90)"
msc.execute(p13)
msdb.commit()
print("p13 success")
p14="insert into product values(14,'White Forest',1,90)"
msc.execute(p14)
msdb.commit()
print("p14 success")
p15="insert into product values(15,'Rainbow Cake',1,95)"
msc.execute(p15)
msdb.commit()
print("p15 success")
p16="insert into product values(16,'Berry Cake',1,90)"
msc.execute(p16)
msdb.commit()
print("p16 success")
p17="insert into product values(17,'Veg Puffs',1,15)"
msc.execute(p17)
msdb.commit()
print("p17 success")
p18="insert into product values(18,'Egg Puffs',1,20)"
msc.execute(p18)
msdb.commit()
print("p18 success")
p19="insert into product values(19,'Mushroom Puffs',1,25)"
msc.execute(p19)
msdb.commit()
print("p19 success")
p20="insert into product values(20,'Chicken Puffs',1,45)"
msc.execute(p20)
msdb.commit()
print("p20 success")
p21="insert into product values(21,'Mutton Puffs',1,55)"
msc.execute(p21)
msdb.commit()
print("p21 success")
p22="insert into product values(22,'Paneer Puffs',1,40)"
msc.execute(p22)
msdb.commit()
print("p22 success")
p23="insert into product values(23,'Potato chips',1,25)"
msc.execute(p23)
msdb.commit()
print("p23 success")
p24="insert into product values(24,'Onion rings',1,30)"
msc.execute(p24)
msdb.commit()
print("p24 success")
p25="insert into product values(25,'Lolipop',1,5)"
msc.execute(p25)
msdb.commit()
print("p25 success")
p26="insert into product values(26,'Lays',1,10)"
msc.execute(p26)
msdb.commit()
print("p26 success")
p27="insert into product values(27,'Bingo',1,10)"
msc.execute(p27)
msdb.commit()
print("p27 success")
p28="insert into product values(28,'Chetos',1,15)"
msc.execute(p28)
msdb.commit()
print("p28 success")
p29="insert into product values(29,'Kurkure',1,10)"
msc.execute(p29)
msdb.commit()
print("p29 success")
p30="insert into product values(30,'Muruku',1,20)"
msc.execute(p30)
msdb.commit()
print("p30 success")
p31="insert into product values(31,'Thattu Vadai',1,25)"
msc.execute(p31)
msdb.commit()
print("p31 success")
p32="insert into product values(32,'Samosa',1,15)"
msc.execute(p32)
msdb.commit()
print("p32 success")
p33="insert into product values(33,'Pakoda',1,30)"
msc.execute(p33)
msdb.commit()
print("p33 success")
p34="insert into product values(34,'coco-cola',1,45)"
msc.execute(p34)
msdb.commit()
print("p34 success")
p35="insert into product values(35,'Bovonto',1,60)"
msc.execute(p35)
msdb.commit()
print("p35 success")
p36="insert into product values(36,'Fanta',1,40)"
msc.execute(p36)
msdb.commit()
print("p36 success")
p37="insert into product values(37,'7-UP',1,45)"
msc.execute(p37)
msdb.commit()
print("p37 success")
p38="insert into product values(38,'Mountain Dew',1,40)"
msc.execute(p38)
msdb.commit()
print("p38 success")
p39="insert into product values(39,'Pepsi',1,45)"
msc.execute(p39)
msdb.commit()
print("p39 success")
p40="insert into product values(40,'Red-Bull',1,50)"
msc.execute(p40)
msdb.commit()
print("p40 success")
p41="insert into product values(41,'Tea',1,10)"
msc.execute(p41)
msdb.commit()
print("p41 success")
p42="insert into product values(42,'Coffee',1,15)"
msc.execute(p42)
msdb.commit()
print("p42 success")
p43="insert into product values(43,'Badam Milk',1,15)"
msc.execute(p43)
msdb.commit()
print("p43 success")
p44="insert into product values(44,'Rose Milk',1,20)"
msc.execute(p44)
msdb.commit()
print("p44 success")
p45="insert into product values(45,'Green Tea',1,30)"
msc.execute(p45)
msdb.commit()
print("p45 success")
p46="insert into product values(46,'Bread',1,25)"
msc.execute(p46)
msdb.commit()
print("p46 success")
p47="insert into product values(47,'Rusk',1,30)"
msc.execute(p47)
msdb.commit()
print("p47 success")
p48="insert into product values(48,'Bun',1,5)"
msc.execute(p48)
msdb.commit()
print("p48 success")
p49="insert into product values(49,'Mini-Bun',1,20)"
msc.execute(p49)
msdb.commit()
print("p49 success")
p50="insert into product values(50,'Coconut Bun',1,30)"
msc.execute(p50)
msdb.commit()
print("p50 success")






