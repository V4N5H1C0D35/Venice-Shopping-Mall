# *****PYTHON PROJECT-VENICE SHOPPING MALL*****
# *****COMBINED EFFORTS BY- VANSHIKA ALANG*****
# Dictionaries use for billing..
caswearwo={1:"Jeans",2:"T-Shirt",3:"Lowers",4:"Night Suits",5:"Track Suits"}
partywearwo={1:"Tunics",2:"Midi",3:"Lehenga",4:"Gown",5:"Suit"}
formwearwo={1:"Shirt",2:"Pent",3:"Coat"}
caswearmen={1:"Jeans",2:"T-Shirt",3:"Lowers",4:"Night Suits",5:"Track Suits"}
partywearmen={1:"Men's Suit",2:"Sherwani"}
formwearmen={1:"Shirt",2:"Pent",3:"Coat"}
kidswear={1:"Overalls",2:"Mittens",3:"Beanie",4:"Baby Apron",5:".Socks",6:"Diapers",7:"Singlet",8:"Shoes"}
chairs={1:"Wooden Chairs",2:"Plastic Chairs"}
tables={1:"Wooden Tables",2:"Dinning Table"}
sofas={1:"Cotton Fabric Sofa Set",2:"Rexine Sofa Set",3:"Leather Sofa Set"}
ironingboard={1:"Freestanding Ironing Board",2:"Compact Ironing Board",3:"Built Ironing Boards"}
wardrobes={1:"Moisture Resistant Wardrobes",2:"Boiling Water Resistant Wardrobes"}
desk={1:"Office Desk",2:"Standing Desk",3:"Student Desk",4:"Typewriter Desk"}
woodgrandclock={1:"Black Woodgrandclock",2:"Brown Woodgrandclock"}
drawerchest={1:"Drawerchest",2:"Drawerchest",3:"Drawerchest",4:"Drawerchest"}
curtainrods={1:"Coventional Curtain Rods",2:"Tension Curtain Rods",3:"Traverse Curtain Rods"}
sleepingbed={1:"Book Sleeping Bed",2:"Twin Sleeping Bed",3:"Single Sleeping Bed"}
fruits={1:"Apple",2:"Banana",3:"Mango",4:"Litchi",5:"Pomegranate",6:"Melon",7:"Watermelon",8:"Papaya",9:"Guava",10:"Strawberries",11:"Plums",12:"Grapes",13:"Kiwi",14:"Dragonfruit"}
vegetables={1:"Onion",2:"Tomatoes",3:"Potatoes",4:"Brinjle",5:"Cucumbers",6:"Ladyfinger",7:"Chillies",8:"Bitter Gourd",9:"Bottle Gourd",10:"Pumpkin",11:"Cauliflower",12:"Brocoli"}
packfooditem={1:"Flour",2:"Refined Flour",3:"Sugar",4:"Kellog's",5:"Chips",6:"Biscuit",7:"Custard Powder",8:"Fruit Cake"}
pulses={1:"Green Gram",2:"Lentil",3:"Red Gram",4:"Black Lentil",5:"Chickpeas",6:"Cowpeas",7:"Kidney Beans",8:"Turkish Gram",9:"Sago"}
spices={1:"Asafoetida",2:"Bay Leaves",3:"Cardamom",4:"Salt",5:"Red Chilli Powder",6:"Turmeric",7:"Black Pepper",8:"Black Salt",9:"Cloves",10:"Corriander Seeds",11:"Fenugreek Seeds",17:"Flax Seeds",18:"Ginger-Garlic Paste"}
electronics={1:"Television",2:"Refrigerator",3:"Air Conditioner",4:"Summer Cooler",5:"Fan",6:"Water Purifiers",7:"Headphones",8:"Earpods",9:"Smart Watches",10:"Smartphones",11:"Laptops",12:"Computers",13:"Tabs",14:"Tubelight",15:"LED Bulbs"}
#all values are fictious
caswearwo1={1:1750,2:2250,3:1500,4:1750,5:2500}
partywearwo1={1:5000,2:5500,3:10000,4:8000,5:3500}
formwearwo1={1:2500,2:1770,3:6575}
caswearmen1={1:1800,2:2300,3:1000,4:2500,5:3600}
partywearmen1={1:10000,2:13000}
formwearmen1={1:2500,2:2000,3:7600}
kidswear1={1:1600,2:1300,3:2000,4:900,5:200,6:200,7:600,8:1000}
chairs1={1:4000,2:5000}
tables1={1:6000,2:7000}
sofas1={1:25000,2:30000,3:36000}
ironingboard1={1:2700,2:2600,3:2700}
wardrobes1={1:15000,2:20000}
desk1={1:10000,2:8500,3:12000,4:13000}
woodgrandclock1={1:35000,2:49990}
drawerchest1={1:4000,2:6000,3:4000,4:5000}
curtainrods1={1:1500,2:2000,3:2500}
sleepingbed1={1:10000,2:15000,3:20000}
fruits1={1:150,2:50,3:90,4:150,5:200,6:100,7:60,8:60,9:150,10:90,11:200,12:150,13:300,14:400}
vegetables1={1:50,2:50,3:40,4:60,5:40,6:100,7:60,8:100,9:40,10:40,11:50,12:90}
packfooditem1={1:40,2:30,3:50,4:160,5:50,6:90,7:170,8:90}
pulses1={1:150,2:100,3:150,4:80,5:100,6:200,7:150,8:100,9:60}
spices1={1:200,2:150,3:1000,4:50,5:300,6:150,7:600,8:60,9:800,10:250,11:100}
electronics1={1:30000,2:45000,3:25000,4:10000,5:5000,6:15000,7:12000,8:3000,9:15000,10:30000,11:60000,12:50000,13:10000,14:50000,15:300}

g=open("bill.txt","r")
import csv
f=open("Book1.csv","a")
writer = csv.writer(f)

import sys
import datetime
import sqlconnect 
import tkinter
from tkinter import *
root=Tk()
root.title("Welcome")
root.geometry("4000x4000")
root.configure(bg="black")
background_image=PhotoImage(file="ooopen.png")
background_label=Label(root,image=background_image)
background_label.place(x=2,y=2,relwidth=1,relheight=1)
root.after(3000,root.destroy)
root.mainloop()

l=[]
products={}       
print("*"*99)
print("\t\t\t\t\tVENICE SHOPPING MALL")
print('*'*45, "WELCOME", "*"*45)
w="\t\t^^^^^^^^^^^^^Oops that wasn't a valid input^^^^^^^^^^^^\n\t\t\tTo continue from this section again choose 'y'"
x=True
def main():
    global l
    global x
    def back_menu(c):
        global x
        x=True
        if c=='n' or c=='N':
            x=False
        else:
            pass

    while x==True:
        print("\nDIFFERENT TYPES OF PRODUCTS AVAILABLE:")
        print("1.Clothing")
        print("2.Furniture")
        print("3.Groceries")
        print("4.Electronics")
        
        choice1=int(input("From which section do you want to buy?"))

        
        if choice1==1:
            root=Tk()
            root.title("Welcome")
            root.geometry("4000x4000")
            root.configure(bg="black")
            background_image=PhotoImage(file="clothing.png")
            background_label=Label(root,image=background_image)
            background_label.place(x=2,y=2,relwidth=1,relheight=1)
            root.after(2000,root.destroy)
            root.mainloop()
            
            print("")
            print('*'*35, "WELCOME TO CLOTHING SECTION", "*"*35)
            while x==True:
                print("\nCATEGORIES:")
                print("1.Women(Including Teenagers)")
                print("2.Men(Including Teenagers)")
                print("3.Kids(0-5 years)")
                choice2=int(input("For whom you want to buy?"))
                try:
                    p=choice2>3
                    if p==True:
                        raise ValueError(" More Value")
                except ValueError:
                    sys.stderr.write(w)
                    print()
                if choice2==1:
                    print("\nTYPES:-")
                    print("1.Casual Wear")
                    print("2.Party Wear")
                    print("3.Formal Wear")
                    try:
                        choice3=int(input("Which type do you want?"))
                        p=choice3>3
                        if p==True:
                            raise ValueError(" More Value")
                    except ValueError:
                        sys.stderr.write(w)
                        print()
                    else:
                        pass
                    
                    if choice3==1:
                        while x==True:
                            print("\nTYPES OF CASUALWEAR AVAILABLE:-")
                            print("1.Jeans")
                            print("2.T-shirt")
                            print("3.Lowers")
                            print("4.Night Suits")
                            print("5.Track Suits")
                            try:
                                choice4=int(input("What do you want to buy?"))
                                p=choice4>5
                                if p==True:
                                    raise ValueError(" More Value")
                            except ValueError:
                                sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                                continue
                            print("\nCOLOURS AVAILABLE:-")                            
                            print("1.Black")
                            print("2.White")
                            print("3.Blue")
                            print("4.Pink")
                            print("5.Red")
                            if p==0:
                                a=caswearwo1[choice4]
                            else:
                                pass
                            choice5=int(input("Which colour do you want?"))
                            try:
                                p=choice5>5
                                if p==True:
                                    raise ValueError(" More Value")
                            except ValueError:
                                sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                                continue
                            choice6=int(input("How many products do you want to buy?"))
                            l.append(a*choice6)
                            m=list(caswearwo.values())
                            n=list(caswearwo1.values())                
                            k1=m[choice4 -1]
                            k2=n[choice4 -1]
                            p=(k2,choice6,a*choice6)
                            products[k1]=p   
                            c=input("Do you want to buy anything else from here(y/n)?")
                            back_menu(c)
                            
                    if choice3==2:
                        while x==True:
                            print("\nTYPES OF PARTYWEAR AVAILABLE:-")
                            print("1.Tunics")
                            print("2.Midi")
                            print("3.Lehenga")
                            print("4.Gown")
                            print("5.Suit")
                            choice4=int(input("What do you want to buy?"))
                            try:
                                p=choice4>5
                                if p==True:
                                    raise ValueError(" More Value")
                            except ValueError:
                                    sys.stderr.write(w)
                                    print()
                                    continue
                            a=partywearwo1[choice4]
                            print("\nCOLOURS AVAILABLE:-")
                            print("1.Black")
                            print("2.White")
                            print("3.Blue")
                            print("4.Pink")
                            print("5.Red")
                            print("6.Green")
                            try:
                                choice5=int(input("Which colour do you want?"))
                                p=choice4>6
                                if p==True:
                                    raise ValueError(" More Value")
                            except ValueError:
                                    sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                                    continue
                            choice6=int(input(" how many products do you want to buy?"))
                            l.append(a*choice6)
                            m=list(partywearwo.values())
                            n=list(partywearwo1.values())                
                            k1=m[choice4-1]
                            k2=n[choice4 -1]
                            p=(k2,choice6,a*choice6)
                            products[k1]=p   
                            c=input("Do you want to buy anything else from here(y/n)?")
                            back_menu(c)

                        
                    if choice3==3:
                        while x==True:
                            print("TYPES OF FORMAL WEAR AVAILABLE:-")
                            print("1.Shirt")
                            print("2.Pent")
                            print("3.Coat")
                            choice4=int(input("What do you want to buy?"))
                            try:
                                p=choice4>3
                                if p==True:
                                    raise ValueError(" More Value")
                            except ValueError:
                                    sys.stderr.write(w)
                                    print()
                                    continue
                            a=formwearwo1[choice4]
                            print("\nCOLOURS AVAILABLES:-")
                            print("1.Black")
                            print("2.White")
                            try:
                                choice5=int(input("Which colour do you want?"))
                                p=choice5>2
                                if p==True:
                                    raise ValueError(" More Value")
                            except ValueError:
                                sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                                continue
                            choice6=int(input(" how many products do you want to buy?"))
                            l.append(a*choice6)
                            m=list(partywearwo.values())
                            n=list(partywearwo1.values())                
                            k1=m[choice4-1]
                            k2=n[choice4 -1]
                            p=(k2,choice6,a*choice6)
                            products[k1]=p   
                            c=input("Do you want to buy anything else from here(y/n)?")
                            back_menu(c)

                     
                if choice2==2:
                    print("\nTYPES:-")
                    print("1.Casual Wear")
                    print("2.Party Wear")
                    print("3.Formal Wear")
                    choice3=int(input("Which type do you want?"))
                    try:
                        p=choice3>3
                        if p==True:
                            raise ValueError(" More Value")
                    except ValueError:
                            sys.stderr.write(w)
                            print()
                    if choice3==1:
                        while x==True:
                            print("\nTYPES OF CASUALWEAR AVAILABLE:-")
                            print("1.Jeans")
                            print("2.T-shirt")
                            print("3.Lowers")
                            print("4.Night Suits")
                            print("5.Track Suits")
                            
                            try:
                                choice4=int(input("What do you want to buy?"))
                                p=choice4>5
                                if p==True:
                                    raise ValueError(" More Value")
                            except ValueError:
                                sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                                continue
                            print("\nCOLOURS AVAILABLE:-")                            
                            print("1.Black")
                            print("2.White")
                            print("3.Blue")
                            print("4.Pink")
                            print("5.Red")
                            if p==0:
                                a=caswearmen1[choice4]
                            else:
                                pass
                            choice5=int(input("Which colour do you want?"))
                            try:
                                p=choice5>5
                                if p==True:
                                    raise ValueError(" More Value")
                            except ValueError:
                                sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                                continue
                            choice6=int(input("how many pieces do you want to buy?  "))
                            l.append(a*choice6)
                            m=list(caswearmen.values())
                            n=list(caswearmen1.values())                
                            k1=m[choice4 -1]
                            k2=n[choice4 -1]
                            p=(k2,choice6,a*choice6)
                            products[k1]=p   
                            c=input("Do you want to buy anything else from here(y/n)?")
                            back_menu(c)

   
                        
                    if choice3==2:
                        while x==True:
                            print("\nTYPES OF PARTYWEAR AVAILABLE:-")
                            print("1.Men's suit")
                            print("2.Sherwani")
                            choice4=int(input("What do you want to buy?"))
                            try:
                                p=choice4>2
                                if p==True:
                                    raise ValueError(" More Value")
                            except ValueError:
                                sys.stderr.write(w)
                                print()
                                    
                            a=partywearmen1[choice4]
                            print("\nCOLORS AVAILABLE:-")
                            print("1.Black")
                            print("2.White")
                            print("3.Golden")
                            choice5=int(input("Which colour do you want?"))
                            try:
                                p=choice3>8
                                if p==True:
                                    raise ValueError(" More Value")
                            except ValueError:
                                sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                                continue
                            choice6=int(input("how many pieces do you want to buy?  "))
                            l.append(a*choice6)
                            m=list(partywearmen.values())
                            n=list(partywearmen1.values())                
                            k1=m[choice4 -1]
                            k2=n[choice4 -1]
                            p=(k2,choice6,a*choice6)
                            products[k1]=p   
                            c=input("Do you want to buy anything else from here(y/n)?")
                            back_menu(c)

                        
                    if choice3==3:
                        while x==True:
                            print("\nTYPES OF FORMALWEAR AVAILABLE:-")
                            print("1.Shirt")
                            print("2.Pent")
                            print("3.Coat")
                            choice4=int(input("What do you want to buy?"))
                            try:
                                p=choice4>3
                                if p==True:
                                    raise ValueError(" More Value")
                            except ValueError:
                                    sys.stderr.write(w)
                                    print()
                            a=formwearmen1[choice4]
                            print("\nCOLOURS AVAILABLE:-")
                            print("1.Black")
                            print("2.White")
                            choice5=int(input("Which colour do you want?"))
                            try:
                                p=choice3>2
                                if p==True:
                                    raise ValueError(" More Value")
                            except ValueError:
                                sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                                continue
                            choice6=int(input("how many pieces do you want to buy?  "))
                            l.append(a*choice6)
                            m=list(formwearmen.values())
                            n=list(formwearmen1.values())                
                            k1=m[choice4 -1]
                            k2=n[choice4 -1]
                            p=(k2,choice6,a*choice6)
                            products[k1]=p   
                            c=input("Do you want to buy anything else from here(y/n)?")
                            back_menu(c)

                        
                if choice2==3:
                    while x==True:
                        print("\nTYPES OF CLOTHES:-")
                        print("1.Overalls")
                        print("2.Mittens")
                        print("3.Beanie")
                        print("4.Baby Apron")
                        print("5.Socks")
                        print("6.Diapers")
                        print("7.Singlet")
                        print("8.Shoes")
                        choice4=int(input("What do you want to buy?"))
                        try:
                            p=choice4>8
                            if p==True:
                                raise ValueError(" More Value")
                        except ValueError:
                            sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                            continue
                        a=kidswear1[choice4]
                        print("\nCOLOURS AVAILABLE:-")
                        print("1.Black")
                        print("2.White")
                        print("3.Blue")
                        print("4.Pink")
                        print("5.Red")
                        print("6.Green")
                        choice5=int(input("Which colour do you want?"))
                        try:
                            p=choice5>6
                            if p==True:
                                raise ValueError(" More Value")
                        except ValueError:
                            sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                            continue
                        choice6=int(input("how many pieces do you want to buy?  "))                            
                        l.append(a*choice6)
                        m=list(kidswear.values())
                        n=list(kidswear1.values())                
                        k1=m[choice4 -1]
                        k2=n[choice4 -1]
                        p=(k2,choice6,a*choice6)
                        products[k1]=p   
                        c=input("Do you want to buy anything else from here(y/n)?")
                        back_menu(c)
                     

                c=input("Do you want to buy anything else from this section(y/n)?")         
                back_menu(c)       


        if choice1==2:

            while x==True:
                root=Tk()
                root.title("Welcome to Furniture Section")
                root.geometry("4000x4000")
                root.configure(bg="black")
                background_image=PhotoImage(file="furniture.png")
                background_label=Label(root,image=background_image)
                background_label.place(x=2,y=2,relwidth=1,relheight=1)
                root.after(2000,root.destroy)
                root.mainloop()

                
                print('*'*34, "WELCOME TO FURNITURES SECTION", "*"*34)
                print("\nITEMS AVAILABLE IN FURNITURE SECTION:-")
                print("1.Chairs")
                print("2.Tables")
                print("3.Couch")
                print("4.Ironing Board")
                print("5.Wardrobes")
                print("6.Desk")
                print("7.Wooden Grandfather Clock")
                print("8.Drawing Chest")
                print("9.Curtain Rods")
                print("10.Sleeping Beds")
                Ch=int(input("Select the product you want to buy"))
                try:
                    p=Ch>10
                    if p==True:
                        raise ValueError(" More Value")
                except ValueError:
                    sys.stderr.write(w)
                    print()
                if(Ch==1):
                       while x==True:
                           print("\nTYPES OF CHAIRS AVAILABLE IN STORE:-")
                           print("1.Wooden Chairs")
                           print("2.Plastic Chairs")
                           choice3=int(input("What type of chair do you want to buy?"))
                           try:
                               p=choice3>2
                               if p==True:
                                   raise ValueError(" More Value")
                           except ValueError:
                                sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                                continue
                           a=chairs1[choice3]                           
                           choice4=int(input("How many chairs you want to buy?"))
                           l.append(a*choice4)
                           m=list(chairs.values())
                           n=list(chairs1.values())                
                           k1=m[choice3 -1]
                           k2=n[choice3 -1]
                           p=(k2,choice4,a*choice4)
                           products[k1]=p   
                           c=input("Do you want to buy anything else from here(y/n)?")
                           back_menu(c)
                        
                
                
                if(Ch==2):
                       while x==True:
                           print("\nTYPES OF TABLES AVAILABLE IN STORE:- ")
                           print("1.Wooden Tables")
                           print("2.Dinning Table")
                           choice3=int(input("What  type of table do you want to buy?"))
                           try:
                               p=choice3>2
                               if p==True:
                                   raise ValueError(" More Value")
                           except ValueError:
                               sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                               continue
                           a=tables1[choice3]                           
                           choice4=int(input("How many tables do you want to buy?"))
                           l.append(a*choice4)
                           m=list(tables.values())
                           n=list(tables1.values())                
                           k1=m[choice3 -1]
                           k2=n[choice3 -1]
                           p=(k2,choice4,a*choice4)
                           products[k1]=p   
                           c=input("Do you want to buy anything else from here(y/n)?")
                           back_menu(c)
                  
                if(Ch==3):
                       while x==True:
                           print("\nTYPES OF SOFAS (SOAF FABRICS) AVAILABLE IN STORE:- ")
                           print("1.Cotton Fabric Sofa Set")
                           print("2.Rexine Sofa Set")
                           print("3.Leather Sofa Set")
                           choice3=int(input("What type of sofa set do you want to buy?"))
                           try:
                               p=choice3>3
                               if p==True:
                                    raise ValueError(" More Value")
                           except ValueError:
                               sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                               continue
                           a=sofas1[choice3]                           
                           choice4=int(input("How many sofa sets you want to buy?"))
                           l.append(a*choice4)
                           m=list(sofas.values())
                           n=list(sofas1.values())                
                           k1=m[choice3 -1]
                           k2=n[choice3 -1]
                           p=(k2,choice4,a*choice4)
                           products[k1]=p   
                           c=input("Do you want to buy anything else from here(y/n)?")
                           back_menu(c)

                       
                if(Ch==4):
                       while x==True:
                           print("\n ")
                           print("1.Freestanding Ironing Board")
                           print("2.Compact Ironing Board")
                           print("3.Built Ironing Boards")
                           choice3=int(input("What type of ironing board do you want to buy?"))
                           try:
                               p=choice3>3
                               if p==True:
                                   raise ValueError(" More Value")
                           except ValueError:
                               sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                               continue
                           a=ironingboard1[choice3]                           
                           choice4=int(input("How many ironing boards do you want to buy?"))
                           l.append(a*choice4)
                           m=list(ironingboard.values())
                           n=list(ironingboard1.values())                
                           k1=m[choice3 -1]
                           k2=n[choice3 -1]
                           p=(k2,choice4,a*choice4)
                           products[k1]=p   
                           c=input("Do you want to buy anything else from here(y/n)?")
                           back_menu(c)
                        
                 
                if(Ch==5):
                       while x==True:
                           print("\nTypes of wardrobes available in store ")
                           print("1.Moisture Resistant Wardrobes")
                           print("2.Boiling Water Resistant Wardrobes")
                           choice3=int(input("What type of wardrobe do you want to buy?"))
                           try:
                               p=choice3>2
                               if p==True:
                                   raise ValueError(" More Value")
                           except ValueError:
                               sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                               continue
                           a=wardrobes1[choice3]                           
                           choice4=int(input("How many wardrobes do you want to buy?"))
                           l.append(a*choice4)
                           m=list(wardrobes.values())
                           n=list(wardrobes1.values())                
                           k1=m[choice3 -1]
                           k2=n[choice3 -1]
                           p=(k2,choice4,a*choice4)
                           products[k1]=p   
                           c=input("Do you want to buy anything else from here(y/n)?")
                           back_menu(c)                    
                if(Ch==6):
                       while x==True:
                           print("\nTypes of desks available in store ")
                           print("1.Office Desk")
                           print("2.Standing Desk")
                           print("3.Student Desk")
                           print("4.Typewriter Desk")
                           choice3=int(input("What type of desk do you want to buy?"))
                           try:
                               p=choice3>4
                               if p==True:
                                   raise ValueError(" More Value")
                           except ValueError:
                               sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                               continue
                           a=desk1[choice3]
                           choice4=int(input("How many desks do you want to buy?"))
                           l.append(a*choice4)
                           m=list(desk.values())
                           n=list(desk1.values())                
                           k1=m[choice3 -1]
                           k2=n[choice3 -1]
                           p=(k2,choice4,a*choice4)
                           products[k1]=p   
                           c=input("Do you want to buy anything else from here(y/n)?")
                           back_menu(c)

                        
                if(Ch==7):
                    
                       while x==True:
                           print("\nAvailable colours for wooden grandfather clock")
                           print("1.Black")
                           print("2.Brown")
                           choice3=int(input("Which colour  wooden grandfather clock do you want to buy?"))
                           try:
                               p=choice3>2
                               if p==True:
                                   raise ValueError(" More Value")
                           except ValueError:
                               sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                               continue
                           choice4=int(input("How many wooden grandfather clock do you want to buy?"))
                           a=woodgrandclock1[choice3]  
                           l.append(a*choice4)
                           m=list(woodgrandclock.values())
                           n=list(woodgrandclock1.values())                
                           k1=m[choice3 -1]
                           k2=n[choice3 -1]
                           p=(k2,choice4,a*choice4)
                           products[k1]=p     
                           c=input("Do you want to buy anything else from here(y/n)?")
                           back_menu(c)


                if(Ch==8):
                       while x==True:
                           print("\nAvailable colours for drawer chest in store ")
                           print("1.White")
                           print("2.Brown")
                           print("3.Black")
                           print("4.Cream")
                           choice3=int(input("What type of do you want to buy?"))
                           try:
                               p=choice3>4
                               if p==True:
                                   raise ValueError(" More Value")
                           except ValueError:
                               sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                               continue
                           choice4=int(input("How many do you want to buy?"))
                           a=drawerchest1[choice3]  
                           l.append(a*choice4)
                           m=list(drawerchest.values())
                           n=list(drawerchest1.values())                
                           k1=m[choice3 -1]
                           k2=n[choice3 -1]
                           p=(k2,choice4,a*choice4)
                           products[k1]=p     
                           c=input("Do you want to buy anything else from here(y/n)?")
                           back_menu(c)


                       
                if(Ch==9):
                       while x==True:
                           print("Types of curtain rods available in store ")
                           print("1.Coventional Curtain Rods")
                           print("2.Tension Curtain Rods")
                           print("3.Traverse Curtain Rods")
                           choice3=int(input("What type of curtain rod do you want to buy?"))
                           try:
                               p=choice3>3
                               if p==True:
                                   raise ValueError(" More Value")
                           except ValueError:
                               sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                               continue
                           choice4=int(input("How many curtain rods do you want to buy?"))
                           a=curtainrods1[choice3]  
                           l.append(a*choice4)
                           m=list(curtainrods.values())
                           n=list(curtainrods1.values())                
                           k1=m[choice3 -1]
                           k2=n[choice3 -1]
                           products[k1]=[k2]     
                           c=input("Do you want to buy anything else from here(y/n)?")
                           back_menu(c)


                if(Ch==10):
                       while x==True:
                           print("Types of sleeping beds available in store ")
                           print("1.Book Sleeping Bed")
                           print("2.Twin Sleeping Bed")
                           print("3.Single Sleeping Bed")
                           choice3=int(input("What type of sleeping bed do you want to buy?"))
                           try:
                               p=choice3>3
                               if p==True:
                                   raise ValueError(" More Value")
                           except ValueError:
                               sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                               continue
                           choice4=int(input("How many sleeping beds do you want to buy?"))
                           a=sleepingbed1[choice3]
                           l.append(a*choice4)
                           m=list(sleepingbed.values())
                           n=list(sleepingbed1.values())                
                           k1=m[choice3 -1]
                           k2=n[choice3 -1]
                           p=(k2,choice4,a*choice4)
                           products[k1]=p     
                           c=input("Do you want to buy anything else from here(y/n)?")
                           back_menu(c)

                             
                c=input("Do you want to buy anything else from this section(y/n)?")
                back_menu(c)                  
                    
        if choice1==3:
            root=Tk()
            root.title("Welcome To Groceries Section")
            root.geometry("4000x4000")
            root.configure(bg="black")
            background_image=PhotoImage(file="groceries.png")
            background_label=Label(root,image=background_image)
            background_label.place(x=2,y=2,relwidth=1,relheight=1)
            root.after(2000,root.destroy)
            root.mainloop()

            print('*'*34, "WELCOME TO GROCERIES SECTION", "*"*35)
            while x==True:
                print("\nITEMS AVAILABLE:-")
                print("1.Fruits")
                print("2.Vegetables")
                print("3.Packaged Food Items")
                print("4.Spices")
                print("5.Pulses")
                choice2=int(input("From which section you want to buy?"))
                try:
                    p=choice2>5
                    if p==True:
                        raise ValueError(" More Value")
                except ValueError:
                    sys.stderr.write(w)
                    print()
                if choice2==1:
                    while x==True:
                        print("\nFRUITS AVAILABLE")
                        print("1.Apple")
                        print("2.Banana")
                        print("3.Mango")
                        print("4.Litchi")
                        print("5.Pomegranate")
                        print("6.Melon")
                        print("7.Watermelon")
                        print("8.Papaya") 
                        print("9.Guava")
                        print("10.Strawberries")
                        print("11.Plums")
                        print("12.Grapes")
                        print("13.Kiwi")
                        print("14.Dragonfruit")
                        choice3=int(input("What do you want to buy?"))
                        try:
                            p=choice3>14
                            if p==True:
                                raise ValueError(" More Value")
                        except ValueError:
                            sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                            continue
                        choice4=int(input("How much quantity you want to buy(in kg)?"))
                        a=fruits1[choice3]  
                        l.append(a*choice4)
                        m=list(fruits.values())
                        n=list(fruits1.values())                
                        k1=m[choice3 -1]
                        k2=n[choice3 -1]
                        p=(k2,choice4,a*choice4)
                        products[k1]=p     
                        c=input("Do you want to buy anything else from here(y/n)?")
                        back_menu(c)

                       
                if choice2==2:
                    while x==True:
                        print("\nVEGETABLES AVAILABLE: ")
                        print("1.Onion")
                        print("2.Tomatoes")
                        print("3.Potatoes")
                        print("4.Brinjal")
                        print("5.Cucumber")
                        print("6.Ladyfinger")
                        print("7.Chillies")
                        print("8.Bitter Gourd")
                        print("9.Bottle Gourd")
                        print("10.Pumpkin")
                        print("11.Cauliflower")
                        print("12.Brocoli")
                        choice3=int(input("What do you want to buy?"))
                        try:
                            p=choice3>12
                            if p==True:
                                raise ValueError(" More Value")
                        except ValueError:

                            sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                            continue
                        choice4=int(input("How much quantity you want to buy(in kg)?"))
                        a=vegetables1[choice3]  
                        l.append(a*choice4)
                        m=list(vegetables.values())
                        n=list(vegetables1.values())                
                        k1=m[choice3 -1]
                        k2=n[choice3 -1]
                        p=(k2,choice4,a*choice4)
                        products[k1]=p     
                        c=input("Do you want to buy anything else from here(y/n)?")                        
                        back_menu(c)
                    
                if choice2==3:
                    while x==True:
                        print("\nPACKGED FOOD ITMES AVAILABLE: ")
                        print("1.Flour")
                        print("2.Refined Flour")
                        print("3.Sugar")
                        print("4.Kellogs")
                        print("5.Chips")
                        print("6.Biscuits")
                        print("7.Custard Powder")
                        print("8.Fruit Cake")
                        choice3=int(input("What do you want to buy?"))
                        try:
                            p=choice3>8
                            if p==True:
                                raise ValueError(" More Value")
                        except ValueError:
                            sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                            continue
                        choice4=int(input("How much quantity you want to buy(in kg or no. of packets)?"))
                        a=packfooditem1[choice3]
                        l.append(a*choice4)
                        m=list(packfooditem.values())
                        n=list(packfooditem1.values())                
                        k1=m[choice3 -1]
                        k2=n[choice3 -1]
                        p=(k2,choice4,a*choice4)
                        products[k1]=p                        
                        c=input("Do you want to buy anything else from here(y/n)?")
                        back_menu(c)
                     
            
                if choice2==4:
                    while x==True:
                        print("\nSPICES AVAILABLE")
                        print("1.Asafoetida")
                        print("2.Bay leaves")
                        print("3.Cardamom")
                        print("4.Salt")
                        print("5.Red chilli powder")
                        print("6.Turmeric")
                        print("7.Black Pepper")
                        print("8.Black Salt")
                        print("9.Cloves")
                        print("10.Corriander Seeds")
                        print("11.Fenugreek Seeds")
                        
                        choice3=int(input("What do you want to buy?"))
                        try:
                            p=choice3>11
                            if p==True:
                                raise ValueError(" More Value")
                        except ValueError:
                            sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                            continue
                        choice4=int(input("How much quantity you want to buy(in packets)?"))
                        a=spices1[choice3]  
                        l.append(a*choice4)
                        m=list(spices.values())
                        n=list(spices1.values())                
                        k1=m[choice3 -1]
                        k2=n[choice3 -1]
                        p=(k2,choice4,a*choice4)
                        products[k1]=p
                        c=input("Do you want to buy anything else from here(y/n)?")
                        back_menu(c)

                    
                if choice2==5:
                    while x==True:
                        print("\nPULSES AVAILABLE")
                        print("1.Green Gram")
                        print("2.Lentil")
                        print("3.Red Gram")
                        print("4.Black Lentils")
                        print("5.Chickpeas")
                        print("6.Cowpeas")
                        print("7.Kidney Beans")
                        print("8.Turkish Gram")
                        print("9.Sago")
                        choice3=int(input("What do you want to buy?"))
                        try:
                            p=choice3>5
                            if p==True:
                                raise ValueError(" More Value")
                        except ValueError:
                            sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                            continue
                        choice4=int(input("How much quantity you want to buy(in packets)?"))
                        a=pulses1[choice3]  
                        l.append(a*choice4)
                        m=list(pulses.values())
                        n=list(pulses1.values())                
                        k1=m[choice3 -1]
                        k2=n[choice3 -1]
                        p=(k2,choice4,a*choice4)
                        products[k1]=p
                        c=input("Do you want to buy anything else from here(y/n)?")
                        back_menu(c)

                  
                c=input("Do you want to buy anything else from this section(y/n)?")
                back_menu(c)
        if choice1==4:
            root=Tk()
            root.title("Welcome To Electronics Section")
            root.geometry("4000x4000")
            root.configure(bg="black")
            background_image=PhotoImage(file="electronics.png")
            background_label=Label(root,image=background_image)
            background_label.place(x=2,y=2,relwidth=1,relheight=1)
            root.after(3000,root.destroy)
            root.mainloop()

            while x==True:
                print("\n","*"*32, "WELCOME TO ELECTRONICS SECTION", "*"*35)
                print("\nItems Available:- ")
                print("1.Television")
                print("2.Refrigerator")
                print("3.Air Conditioner")
                print("4.Summer Cooler")
                print("5.Fan")
                print("6.Water Purifier")            
                print("7.Headphones")              
                print("8.Earpods")
                print("9.Smart Watches")
                print("10.Smartphones")
                print("11.Laptops")
                print("12.Computers")
                print("13.Tabs")
                print("14.Tubelight")
                print("15.LED Bulbs")
                choice3=int(input("What do you want to buy?"))
                try:
                    p=choice3>15
                    if p==True:
                        raise ValueError(" More Value")
                except ValueError:
                    sys.stderr.write("\n\n\t\tInvalid Choice, Try again!!!")
                    continue
                choice4=int(input("Enter the no. of pieces you want to buy:"))
                a=electronics1[choice3]
                l.append(a*choice4)
                m=list(electronics.values())
                n=list(electronics1.values())                
                k1=m[choice3 -1]
                k2=n[choice3 -1]
                p=(k2,choice4,a*choice4)
                products[k1]=p
                c=input("Do you want to buy anything else from this section(y/n)?")
                back_menu(c)
         
        c=input("Do you want to buy anything else from any other section?")
        back_menu(c)
        if x==True:
            main()
        else:
            break
    
                    
main()

#for i in products:
 #   z=list(i)
#writer.writerow(z) '''

sqlconnect.call()
def payment():
    
    import time
    def abc():
        for i in range(1,51):
            time.sleep(0.1)
            print("$",end=" ")
        print()    
    abc()
    r=products.keys()
    print("\t\t\tVenice Shopping Mall")
    print(" \t\t\t\t BILL")
    print("Name-",name)
    t_date=datetime.date.today()
    t_time=datetime.datetime.now()
    print( "Date",t_date)
    print()
    print("-"*90)
    for i in r :
        print("\nProduct:",i,":")
        z=list(products[i])
        print("Price","\t","Quantity","\t","Net Amount")
        for j in z:
            print(j,end="\t\t")

    print()
    print("-"*90)
print("")
print("#"*40,"MODES OF PAYMENTS","#"*40)
print("1.Cash")
print("2.Cheque")
print("3.Digital Payment")
print("4.Installment")
ch=int(input("Enter the mode of payment"))
name=input("Enter your name:")
try:
    p=ch>4
    if p==True:
        raise ValueError(" More Value")
except ValueError:
    sys.stderr.write(w)
    print()
d=sum(l)
discount=0
def shopping():
    print("Net Amount to be paid after discount: ",d)
    print("Today you saved rupees: ",discount)        
    print("")
    
def disc():
    global discount
    global d
    print("5% Discount on total amount ")
    discount=d*0.1
    d=d-discount
    shopping()
if(ch==1):
    payment()
    print("\nAmount to be paid (in rupees): ",d)

elif(ch==2):
     payment()
     print("\nAmount to be paid through cheque :",d)

elif(ch==3):
    print("1.Google Pay")
    print("2.Future Pay")
    print("3.Pay Pal One Touch")
    print("4.Paytm")
    ch=int(input("Enter the mode through which you prefer paying the bill: "))
    if(ch==1):
        payment()
        print("\nDiscount upto 10%")
        print("Amount to be paid: ",d)
        if(d<50000):
            disc()
        else:
            print("$$$$$ 6% discount on total amount $$$$$")
            discount=d*0.06
            d=d-discount
            shopping()
    elif(ch==2):
        payment()
        print("\nDiscount upto 10%")
        print("Amount to be paid: ",d)
        if(d<50000):
            disc()
        else:
            print("$$$$$ 7% discount on total amount $$$$$")
            discount=d*0.15
            d=d-discount

            shopping()
    elif(ch==3):
        payment()
        print("\nDiscount upto 8%")
        print("Amount to be paid: ",d)
        if(d<50000):
            disc()
        else:
            print("$$$$$ 8% discount on total amount $$$$$")
            discount=d*0.08
            d=d-discount
            shopping()
    elif(ch==4):
        payment()
        print("\nDiscount upto 20%")
        print("Amount to be paid: ",d)
        if(d<50000):
            disc()
        else:
            print("$$$$$ 10% discount on total amount $$$$$")
            discount=d*0.1
            d=d-discount
            shopping()

elif(ch==4):
    print("\n30% of the total amount needs to be paid at the time of purchase and rest of the amount through installments.")
    amt=d*0.3
    print("Amount to be paid : ",amt)
    amt1=d-amt
    print("Remaining Amount to be paid:",amt1)
    print("Number of Installments:  ")
    print("1.6 Installment")
    print("2.8 Installments")
    print("3.12 Installments ")
    ch=int(input("Enter the installment plan to pay remaining amount: "))
    try:
        p=ch>3
        if p==True:
            raise ValueError(" More Value")
    except ValueError:
        sys.stderr.write(w)
        print()
    if(ch==1):
        payment()
        print("\nRate of Interest : 1.5%")
        amt2=amt1*(15/100)
        print("Net Amount to be Paid= ",amt2)
    elif(ch==2):
        payment()
        print("\nRate of Interest : 2%")
        amt2=amt1*(0.02)
        print("Net Amount to be Paid= ",amt2)
    elif(ch==3):
        payment()
        print("\nRate of Interest : 2.5%")
        amt2=amt1*(0.025)
        print("Net Amount to be Paid= ",amt2)
print("")
print("Price Incl. of all the taxes")
print("In case of any exchange or query contact within 3 days.")
print("No exchange or return without bill.")

print("HAPPY SHOPPING:)....VISIT AGAIN")
print("\n")

import time
def abc():
   for i in range(1,51):
       time.sleep(0.1)
       print("$",end=" ")
    
abc()        
print()
see=input("\nDo you want to see your last time bought products ?")
if see=="y" or "Y":
    f=g.read()
    for i in f:
        print(i,sep=",",end=" ")
        
#else:
 #   print()
root=Tk()
root.title("Thanks For Visiting")
root.geometry("4000x4000")
root.configure(bg="black")
background_image=PhotoImage(file="ty.png")
background_label=Label(root,image=background_image)
background_label.place(x=2,y=2,relwidth=1,relheight=1)
root.after(3000,root.destroy)
root.mainloop()
mm=[]
for i in products:
    mm.append(i)

with open("bill.txt","a") as bill:
    bill.write(name)
    bill.write(":")
    for i in mm:
        bill.write(i)
        bill.write(",")
    bill.write("\n")

g.close()


        
