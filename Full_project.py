import mysql.connector
from textblob import  TextBlob
import random
import string
import smtplib as s

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "**********", database="admin_panel")
cursor=mydb.cursor()


def project_admin_panel():
  #admistration panel from line 10 to 265
  def login():
    def change_pswd():
      id=input("\nEnter your key = ")
      username=input("Enter username = ")
      sql=f"select * from admins WHERE id=('{id}') AND username=('{username}')"
      cursor.execute(sql)
      result=cursor.fetchone()
      if result:
        for username in result:
          def password3():
            password1=input("It must contains 8 characters, at least one lowercase letter, at least one uppercase letter, at least one symbol and at least one numeric character.\nEnter New Password = ")
            if len(password1) < 8 or password1.lower() == password1 or password1.upper() == password1 or password1.isalnum() or not any(i.isdigit() for i in password1):
              print('your password is weak')
              password3()
            else:
              print('your password is strong')
              sql=f"update admins set password=('{password1}') where id=('{id}')"
              cursor.execute(sql)
              cursor.fetchone()
              mydb.commit()
              try:
                ob = s.SMTP("smtp.gmail.com", 587)
                ob.starttls()
                ob.login("Email id", "Password")      #Email ID & Password
                subject1=('Admistrations Confidential Information')
                subject = subject1
                body = f"Your New Password = ('{password1}')"
                message = "Subject:{}\n\n{}".format(subject, body)
                sql=f"select * from admins where id=('{id}')"
                cursor.execute(sql)
                result=cursor.fetchall()
                if result:
                  for email in result:
                    email=email[1]
                    Address =f'{email}'
                    ob.sendmail("suyoggawande999@gmail.com", Address, message)
                    ob.quit()
                    print("Mail sends successfully.")
                    break
              except Exception:
                  print("\nYour Email id is not found.")
              finally:
                  choice=int(input("\nyour Password is Updated.\nEnter 0 for login again = "))
                  if choice == 0:
                    login()
          password3()
      else:
        choice=int(input("\nInvalid id or username.\nEnter 0 for try again = "))
        if choice==0:
          change_pswd()
        
    def menu():
      def set_admin():
        def delete_admin():
          username=input("Enter the Username = ")
          sql=f"delete from admins where username = ('{username}')"
          print(f"\nYou really wants to delete admin", username)
          choice=int(input("Enter 1 for YES or 2 for NO = "))
          if choice==1:
            cursor.execute(sql)
            mydb.commit()
            print("\nAdmin deleted Successfully.")
            choice= int(input("Enter 0 for Admin Settings = "))
            if choice == 0:
              set_admin()
          if choice==2:
            set_admin()

        def new_admin():
          print("\nEnter New Admin Details")
          name=input("Name = ")
          surname=input("Surname = ")
          email=input("Email id = ")
          mob_no=input("Mobile no. = ")
          username=input("Username = ")
          def password1(): 
            password=input("It must contains 8 characters, at least one lowercase letter, at least one uppercase letter, at least one symbol and at least one numeric character.\nPassword = ")
            if len(password) < 8 or password.lower() == password or password.upper() == password or password.isalnum() or not any(i.isdigit() for i in password):
              print('your password is weak ')
              password1()
            else:
              print('your password is strong')
              designation=input("Designation: ")
              length=int(4)
              num = string.digits
              temp = random.sample(num,length)
              id = "".join(temp)
              print("Your Unique id", id)
              sql = f"INSERT INTO admins(id, email, username, password, name, surname, designation, mob_no) values( '{id}','{email}','{username}','{password}','{name}','{surname}','{designation}','{mob_no}')"
              cursor.execute(sql)
              mydb.commit()
              try:
                ob = s.SMTP("smtp.gmail.com", 587)
                ob.starttls()
                ob.login("Email id", "Password")      #Email ID & Password
                subject1=('Admistrations Confidential Information')
                subject = subject1
                body = f"This is your Unique ID for Future Use = '{id}'\nEmail ID = '{email}'\nUsername = '{username}'\nPassword = '{password}'\nMobile Number = '{mob_no}'\nYou are now an Admin.\nThis is system generated message. Please do not reply. )"
                message = "Subject:{}\n\n{}".format(subject, body)
                Address =f'{email}'
                ob.sendmail("suyoggawande999@gmail.com", Address, message)
                ob.quit()
                print("\nNew Admin Information sends to their mail id.")
              except Exception:
                print("\nEmail id not found.")
              finally:
                print("\nNew Admin added Successfully")
                choice= int(input("Press 0 for Admin Settings = "))
                if choice == 0:
                  set_admin()
          password1()
          
        designation='head'
        sql=f"select * from admins WHERE username=('{username}') AND designation=('{designation}')"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
          for i in result:
            print("1. Create New Admin")
            print("2. Delete Admin")
            print("Press 0 for Home Page")
            choice = int(input("\nEnter the choice = "))
            if choice == 1:
              new_admin()
            if choice == 2:
              delete_admin()
            if choice == 0:
              menu()
              break
        else:
          print("\nYou are not allow to change here")
          choice = int(input("\nPress 0 for Home Page = "))
          if choice == 0:
            menu()

      def manage_db():
        def deactivate():
          count=int(5)
          sql=f"select * from abuse_count where Count>{count}"
          cursor.execute(sql)
          result = cursor.fetchall()
          if result:
            for username in result:
              username=username[1]
              Deactivate=str("deactivate")
              sql=f"update p3_email_registration set take_action = '{Deactivate}' where Email_ID='{username}'"
              cursor.execute(sql)
              mydb.commit()
              print("\nAccount De-Activated Successfully.")
              choice = int(input("\nEnter 0 for back = "))
              if choice == 0:
                manage_db()
                break
          else:
            print("\nNothing Found")
            choice = int(input("\nEnter 0 for back = "))
            if choice == 0:
              manage_db()

        def activate():
          request=str("requested")
          sql=f"select * from p3_email_registration where request=('{request}')"
          cursor.execute(sql)
          result = cursor.fetchall()
          if result:
            for i in result:
              activate=str("activate")
              deactivate=str("deactivate")
              sql=f"update p3_email_registration set take_action=('{activate}') where take_action=('{deactivate}')"
              cursor.execute(sql)
              mydb.commit()
              zero=int(0)
              count=int(5)
              sql=f"update abuse_count set Count=('{zero}') where Count>{count}"
              cursor.execute(sql)
              mydb.commit()
              print("\nAll acounts are activated successfully.")
              sql=f"alter table p3_email_registration drop column request"
              cursor.execute(sql)
              sql=f"alter table p3_email_registration add column request varchar(10)"
              cursor.execute(sql)
              choice = int(input("\nEnter 0 for back = "))
              if choice == 0:
                manage_db()
                break
          else:
            print("\nNo requests are found.")
            choice = int(input("\nEnter 0 for back = "))
            if choice == 0:
              manage_db()

        def delete_info():
          print("\nChoose Database that you wants to clean")
          print("1. p1_sentiment_analysis")
          print("2. p2_abusing_words")
          print("3. p3_email_registration")
          print("4. abuse_count")
          print("5. Press 0 for Home Page")
          choice = int(input("\nEnter the choice = "))
          if choice == 0:
            manage_db()
          elif choice == 1:
            abc=str("p1_sentiment_analysis")
          elif choice == 2:
            abc=("abuse_word")
          elif choice == 3:
            abc=("p3_email_registration")
          elif choice == 4:
            abc=("abuse_count")
          else:
            print("\nChoose the correct option.")
            view_db()

          sql=f"truncate table {abc}"
          cursor.execute(sql)
          print(abc,"table is clean now.")
          choice= int(input("\n1. Enter 0 for View another Dataset\n2. Enter 1 for manage database menu\n choose option = "))
          if choice == 0:
            delete_info()
          if choice == 1:
            manage_db()

        print("1. Deactivate Users")
        print("2. Activate Users")
        print("3. Clean Datasets")
        print("4. Enter 0 for Main Menu")
        choice = int(input("\nEnter the choice = "))
        if choice == 1:
          deactivate()
        if choice == 2:
          activate()
        if choice == 3:
          delete_info()
        if choice == 0:
          menu()
        else:
          print("\nInvalid selection")
          manage_db()

      def view_db():
        print("\nChoose Database that you wants to view")
        print("0. Press 0 for Home Page")
        print("1. Admins Database")
        print("2. Sentiment Analysis Database")
        print("3. Abusing Count Database")
        print("4. Authentication Database")
        print("5. Active Users Database")
        print("6. De-active Users Database")
        print("7. Requested Users Database")
        print("8. Abusing Words Database")
        choice = int(input("\nEnter the choice = "))
        if choice == 0:
          menu()
        elif choice == 1:
          print("\n**Admins Database**\n")
          abc='select name, surname, id, designation, Username, email, mob_no from admins'
        elif choice == 2:
          print("\n**Sentiment Analysis Database**\n")
          abc='select Sr_Number,login_id,output from p1_sentiment_analysis'
        elif choice == 3:
          print("\n**Abusing Count Database**\n")
          abc='select Serial_No, username, Count from abuse_count'
        elif choice == 4:
          print("\n**Authentication Database**\n")
          abc='select Serial_Number, Email_ID, Phone_number, take_action, request from p3_email_registration'
        elif choice==5:
          print("\n**Active Users Database**\n")
          activate=str('activate')
          abc=f"select Serial_Number, Email_ID, Phone_number from p3_email_registration where take_action='{activate}'"
          print(abc)
        elif choice==6:
          print("\n**De-active Users Database**\n")
          deactivate=str('deactivate')
          abc=f"select Serial_Number, Email_ID, Phone_number from p3_email_registration where take_action='{deactivate}'"
        elif choice==7:
          print("\n**Requested Users Database**\n")
          requested=str('requested')
          abc=f"select Serial_Number, Email_ID, Phone_number from p3_email_registration where request='{requested}'"
        elif choice==8:
          print("\n**Abusing Words Database**\n")
          abc='select List_of_abusing_words from abuse_count'
        else:
          print("\nChoose the correct option.")
          view_db()

        sql=f"({abc})"
        cursor.execute(sql)
        result=cursor.fetchall()
        for i in result:
          print(i)
        choice= int(input("\nPress 0 for View another Dataset = "))
        if choice == 0:
          view_db()
        
      def logout():
        print("\nLOGOUT SUCCESSFULLY")
        project_admin_panel()
            
      print(f"\n-----Welcome {username}-----\n")
      print("-----HOME PAGE-----\n")
      print("1. View Databases")
      print("2. Manage Databases")
      print("3. Change Password")
      print("4. Add or Delete Admin")
      print("5. Log out")
      choice = int(input("\nEnter the choice = "))
      if choice == 1:
        view_db()
      if choice == 2:
        manage_db()
      if choice == 3:
        change_pswd()
        choice = int(input("Enter 0 for menu = "))
        if choice == 0:
          menu()
      if choice == 4:
        set_admin()
      if choice == 5:
        logout()
      else:
        print("Choose the correct option.")
        menu()

    print("\n**********ADMINISTRATIONS LOGIN**********\n")
    username=input("username = ")
    password=input("password = ")
    sql=f"select * from admins WHERE username=('{username}') AND password=('{password}')"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
      for i in result:
        menu()
        break
    else:
      print("\nInvalid username or password.")
      print("1. Login again")
      print("2. Forgot Password")
      choice = int(input("\nEnter the choice = "))
      if choice == 1:
        login()
      if choice == 2:
        change_pswd()

  def login_user():
    def abusing():
      project="ABUSIVE WORDS DETECTION"
      print(project.center(len(project)+30,"*"))
      ID=input("Enter the Login ID:")
      bad_words=["abc","abd","avd","rty","dfg","kjg","wer","mnb","zxs","wes"]
      print("")
      userinput=input("Enter the data such as comments/sentence/words:")
      state=userinput.split()
      count=0
      new=[]
      for word1 in state:
          for word in bad_words:
              if word1==word:
                  length=word[1:-1]
                  userinput=userinput.replace(word1,word1[0]+(len(length) * "*") + word1[-1])
                  count += 1
                  new.append(word1)
      project = "Find The Abusing Words"
      print(project.center(len(project) + 30, "*"))
      print("Output:")
      print("\nThe Output Of Your Comments/Sentence/Words:\n",userinput)
      print("\nThe Count Of Abusing Words Use In Given Comments/Sentence/Words :",count)
      sql=f'insert into abuse_count(List_of_abusing_words,username,Abusing_word,Count)values("{bad_words}","{ID}","{new}",{count})'
      cursor.execute(sql)
      mydb.commit()
      choice=int(input("\n1. Enter 0 for Menu\n2. Enter 1 for analysis\n3. Enter 2 for send report on mail\nChoose option = "))
      if choice == 0:
        menu()
      if choice == 1:
        abusing()
      if choice== 2:
        try:
          ob = s.SMTP("smtp.gmail.com", 587)
          ob.starttls()
          ob.login("Email id", "Password")      #Email ID & Password
          subject1=('Report of Abusing word analysis')
          subject = subject1
          body = f"Your Abusing word count is ('{count}')"
          message = "Subject:{}\n\n{}".format(subject, body)
          Address =f'{username}'
          ob.sendmail("suyoggawande999@gmail.com", Address, message)
          ob.quit()
          print("Mail sends successfully.")
        except Exception:
          print("\nYour Email id is not found.")
        finally:
          choice=int(input("Enter 0 for Menu = "))
          if choice == 0:
            menu()

    def sentiment_analysis():
      while True:
        print("\n*****Sentiment Analyzer*****\n")
        username2= username
        text=str(input("ENTER YOUR TEXT =\n"))
        edu=TextBlob(text)
        text2=edu.sentiment.polarity
        print("\nTHE POLARITY OF THE TEXT IS", text2)
        if (text2<0):
          print("negative")
          abc=str('negative')
        elif (text2==0):
          print("neutral")
          abc=str('neutral')
        elif (text2>0):
          print("Positive")
          abc=str('positive')
        sql = f"insert into p1_sentiment_analysis(login_id, Output) values(('{username2}'), ('{abc}'))"
        cursor.execute(sql)
        mydb.commit()
        print("\nAnalysis executed.\n1. Enter 0 for Menu\n2. Enter 1 for Analysis\n3. Enter 2 for get report on Email")
        choice=int(input("\nEnter Your Choice = "))
        if choice == 0:
          menu()
          break
        if choice == 1:
          sentiment_analysis()
          break
        if choice== 2:
          try:
            ob = s.SMTP("smtp.gmail.com", 587)
            ob.starttls()
            ob.login("Email id", "Password")      #Email ID & Password
            subject1=('Report of Abusing word analysis')
            subject = subject1
            body = f"Sentiment Analysis of your paragraph is ('{abc}')"
            message = "Subject:{}\n\n{}".format(subject, body)
            Address =f'{username}'
            ob.sendmail("suyoggawande999@gmail.com", Address, message)
            ob.quit()
            print("Mail sends successfully.")
            choice=int(input("1. Enter 0 for Menu\n2. Enter 1 for Analysis = "))
            if choice == 0:
              menu()
            if choice == 1:
              sentiment_analysis()
          except Exception:
            print("\nYour Email id is not found.")
            choice=int(input("Enter 0 for Menu = "))
            if choice == 0:
              menu()
              break

    def logout():
      print("\nLogout Successfully.")
      project_admin_panel()

    def menu():
      print("\nWELCOME", username)
      print("\n-----Main Menu-----")
      print("\n1. Abusing Word Analysis")
      print("2. Sentiment Analysis")
      print("3. Logout")
      choice = int(input("\nChoose the option = "))
      if choice == 1:
        abusing()
      if choice == 2:
        sentiment_analysis()
      if choice == 3:
        logout()
      else:
        print("\nInvalid input.")
        menu()

    print("\n**********USER LOGIN**********\n")
    username=input("Email ID = ")
    password=input("password = ")
    def activate():
      sql=f"select * from p3_email_registration WHERE Email_ID=('{username}') AND password=('{password}')"
      cursor.execute(sql)
      result = cursor.fetchall()
      if result:
        for i in result:
          Activate=str("activate")
          sql=f"select * from p3_email_registration WHERE Email_ID=('{username}') AND take_action=('{Activate}')"
          cursor.execute(sql)
          result = cursor.fetchone()
          if result:
            for i in result:
              menu()
              break
          else:
            choice=int(input("Your account is Deactivated.\nIn case of Re-activating account, enter 0 or 1 for EXIT.: "))
            if choice == 0:
              request=str("requested")
              sql=f"update p3_email_registration set request=('{request}') where Email_ID=('{username}')"
              cursor.execute(sql)
              mydb.commit()
              print("Your request is submited successfully.\nKindly Login again in 24 hours.\nThank You.")
              project_admin_panel()
            else:
              print("Exit")
              project_admin_panel()
      else:
        print("\nInvalid username or password")
        print("\n1. Login again")
        print("2. Forgot Password")
        print("3. New User Registration")
        choice = int(input("\nEnter the choice = "))
        if choice == 1:
          login_user()
        elif choice == 2:
          change_pswd()
        elif choice == 3:
          registration()
    activate()

  def registration():
    print("Enter New User Details")
    username = input("Email ID: ")
    mob_no = input("Mobile no.: ")
    password=input("It must contains 8 characters, at least one lowercase letter, at least one uppercase letter, at least one symbol and at least one numeric character.\nPassword: ")
    def password1(): 
      if len(password) < 8 or password.lower() == password or password.upper() == password or password.isalnum() or not any(i.isdigit() for i in password):
        print('your password is weak ')
        password1()
      else:
        print('your password is strong')
    password1()
    try:
      ob = s.SMTP("smtp.gmail.com", 587)
      ob.starttls()
      ob.login("Email id", "Password")      #Email ID & Password
      subject1=('Confidential Information')
      subject = subject1
      body = f"('{username}')\n('{password}'\nThank You for registration.\nThis is system generated message. Please do not reply. )"
      message = "Subject:{}\n\n{}".format(subject, body)
      Address =f'{username}'
      ob.sendmail("suyoggawande999@gmail.com", Address, message)
      ob.quit()
      print("Registration Information sends to your mail id.")
    except Exception:
      print("Your Email id is Incorrect or Not Existed.")
    finally:
      action=str("activate")
      sql = f"INSERT INTO p3_email_registration( Email_ID, Password, Phone_number, take_action) values('{username}', '{password}', '{mob_no}', '{action}')"
      cursor.execute(sql)
      mydb.commit()
      print("New User added Successfully.")
      login_user()

  def change_pswd():
    Email_id=input("Enter your registered Email id: ")
    Number=(input("Enter your registered Phone Number: "))
    sql=f"select * from p3_email_registration WHERE Email_ID=('{Email_id}') and Phone_number=('{Number}')"
    cursor.execute(sql)
    result=cursor.fetchall()
    if result:
      for password1 in result:
        password1=str(input("It must contains 8 characters, at least one lowercase letter, at least one uppercase letter, at least one symbol and at least one numeric character.\nEnter New Password: "))
        password2=str(input("Enter New Password Again: "))
        if password1==password2:
          sql=f"update p3_email_registration set Password=('{password2}') where Email_ID=('{Email_id}')"
          cursor.execute(sql)
          cursor.fetchone()
          mydb.commit()
          try:
              ob = s.SMTP("smtp.gmail.com", 587)
              ob.starttls()
              ob.login("Email id", "Password")      #Email ID & Password
              subject1=('Admistrations Confidential Information')
              subject = subject1
              body = f"Your New Password = ('{password2}')"
              message = "Subject:{}\n\n{}".format(subject, body)
              sql=f"select * from admins where id=('{id}')"
              cursor.execute(sql)
              result=cursor.fetchall()
              if result:
                for email in result:
                  email=email[1]
                  Address =f'{email}'
                  ob.sendmail("suyoggawande999@gmail.com", Address, message)
                  ob.quit()
                  print("Mail sends successfully.")
                  break
          except Exception:
            print("Error 404!\nServer Is Not Responding!\nPlease Check Your Connection")
          finally:
            print("Your Password is Updated.\nKindly Login again.")
            login_user()
            break
        else:
          print("Not Matching Password")
          change_pswd()
    else:
      print("Invalid id or urername.")
      choice = int(input("Enter 0 for login again= "))
      if choice == 0:
        change_pswd()

  print("\n\n*****WELCOME TO SENTIMENT & ABUSING WORD ANALYSER*****\n\n")
  print("**********LOGIN PAGE**********\n")
  print("1. New User Registration")
  print("2. User Login")
  print("3. Admistration Login\n")
  choice = int(input("Enter Your Choice = "))
  if choice==1:
    registration()
  elif choice==2:
    login_user()
  elif choice==3:
    login()
  else:
    project_admin_panel()
project_admin_panel()