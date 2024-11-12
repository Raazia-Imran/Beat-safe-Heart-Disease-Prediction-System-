import mysql.connector
from tkinter import messagebox

#B,C,D,E,F,G,H,I,J,K,L,M,N,P,Q,R
def Save_Data_MySql(B,C,D,E,F,G,H,I,J,K,L,M,N,P,Q,R):
    try:
        mydb = mysql.connector.connect(host='localhost',user='root',password='22billo123')
        mycursor = mydb.cursor()  # Define cursor after connection
        print("Connection established")

    except:
        messagebox.showerror("Connection","Database connection not established!!!")

    try:
       command="create database Heart_Data"
       mycursor.execute(command)

       command="use Heart_Data"
       mycursor.execute(command)

       command="create table data(user in AUTO_INCREMENT key not null, Name varchar(50), DOB varchar(100), age varchar(100), sex varchar(100), Cp varchar(100), trestbps varchar(100), chol varchar(100), fbs varchar(100), restecg varchar(100). thalach varchar(100), exang varchar(100), oldpeak varchar(100), slope varchar(100), ca varchar(100), thal varchar(100), result varchar(100))"
       mycursor.execute(command)

       command="insert into data(Name,Date,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
       mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,P,Q,R))
       mydb.commit()
       mydb.close()
       messagebox.showinfo("Register","New user added successfully!!!")

    except:
        mycursor.execute("use Heart_Data")
        mydb=mysql.connector.connect(hosts="localhost",user='root',password='22billo123',database='Heart_Data')
        mycursor=mydb.cursor()

        command = "insert into data(Name,Date,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(command, (B, C, D, E, F, G, H, I, J, K, L, M, N, P, Q, R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Register", "New user added successfully!!!")


#Save_Data_MySql('mr unknown','08/08/2024','1973','44','1','1','233','233','1','1','233','1','233.0','0','2','1','0')