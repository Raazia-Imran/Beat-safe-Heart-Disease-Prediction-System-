
import mysql.connector
import _mysql_connector


from tkinter import messagebox

#B,C,D,E,F,G,H,I,J,K,L,M,N,P,Q,R
def Save_Data_MySql(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R):

    try:
        mydb = mysql.connector.connect(host='localhost',user='root',password='22billo123')
        mycursor = mydb.cursor()  # Define cursor after connection
        print("Connection established")


        mycursor.execute("USE Heart_Data")

        command="""CREATE TABLE IF NOT EXISTS data(user_id INT AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(50),DOB VARCHAR(100),age VARCHAR(100),sex VARCHAR(100),Cp VARCHAR(100),trestbps VARCHAR(100),chol VARCHAR(100),fbs VARCHAR(100),restecg VARCHAR(100),thalach VARCHAR(100),exang VARCHAR(100),oldpeak VARCHAR(100),slope VARCHAR(100),ca VARCHAR(100),thal VARCHAR(100),result VARCHAR(100))"""
        mycursor.execute(command)

        command="""INSERT INTO data(Name,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))

       # Commit the changes
        mydb.commit()

       # Close the connection
        mydb.close()
        messagebox.showinfo("Register", "New user added successfully!!!")

    except mysql.connector.Error as err:
        mydb.rollback()  # Rollback if there's an error during execution
        messagebox.showerror("MySQL Error", f"Error: {err}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")






#Save_Data_MySql('John Doe', '1990-05-20', '34', 'Male', '1', '120', '200', '1', 'Normal', '150', 'No', '1', 'Up', '0', 'Normal', 'Healthy','Positive')