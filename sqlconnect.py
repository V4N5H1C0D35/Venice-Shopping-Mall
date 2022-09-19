def call():
    import mysql.connector as mc
    co = mc.connect(host="localhost",user="root",passwd="star",db="ShoppingMall")
    cur = co.cursor()
    my=cur.execute("Select * from user")
    myrecords=cur.fetchone()
    while myrecords is not None:
        myrecords=cur.fetchone()
    cur.execute("Select * from user")

    my2=cur.fetchall()


    d=list(my2)
    
    n=input("Enter your name")
    no=int(input("Enter Your Number  of Visits : "))
    ch="n"
    use=no
    if no==1 :
        no=1
        t=(n,no)
        data="insert into user values(%s,%s)"
        add=cur.execute(data,t)
        print("data added")
    else:
        
        update="update user set visits=%s where name=%s"
        data2=(no,n)
        cur.execute(update,data2)


    co.commit()

