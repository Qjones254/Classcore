def main():
    
    choice =0
    while choice !=4:
        print(  "****CLASSCORE****" ) 

        print("1) Teacher")
        print("2) Student")
        print("3) Parent")
        print("4) Exit")
        choice = int(input())

        if choice ==1:
         name = input("Enter your name >>>")
         print(f"Welcome {name}")
         password = "Admin"
         password = input("Enter password :")
         if password != "Admin":
                print("Enter a valid password!")
         else:
                while choice !=3:
                 print("1) Mark Students' grades")
                 print("2) View Students' grades")
                 print("3) Exit")
                 choice = int(input())
                 
                 if choice == 1:
                     
                     while choice !=6:
                      print("What grade do you teach ?")
                      print("1) Grade 1")
                      print("2) Grade 2")
                      print("3) Grade 3")
                      print("4) Grade 4")
                      print("5) Grade 5")
                      print("6) Exit.")
                      choice= int(input())
                      if choice == 1:
                             password = "grade1"
                             password = input("Enter grade1 password :")
                             if password != "grade1":
                                 print(f"Enter a valid password {name} !!")
                             else:
                                 while choice !=2:
                                  print("Welcome")
                                  print("Choose an option")
                                  print("1)View students grades")
                                  print("2)Exit")
                                  choice = int(input())
         


if __name__ == "__main__":
    main()