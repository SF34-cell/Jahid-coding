import pandas as pd
print("Which file do you want to work with?\n1. Pokemons' Information\n2.Students' Information")
try:
    choice=int(input("Enter you choice:"))
except ValueError:
    print("Error!!(Invalid input from user)\nEnter only number as your choice:")
    exit()
if choice==1:
    print("What do you want?\n1.Information about particular Pokemon\n2.Information about certain range")
    try:
        choice2=int(input("Enter your choice:"))
    except ValueError:
        print("Error!!(Invalid input from user)\nEnter only number as your choice:")
        exit()
    if  choice2==1:
        print("By how you want to find information?\n1.BY 'Name'\n2.By 'No'")
        try:
            choice3=int(input("Enter your choice:"))
        except ValueError:
            print("Error!!(Invalid input from user)\nEnter only number as your choice:")
            exit()
        if choice3==1:
            names=input("Enter the 'Name' of the Pokemon:")
            dt=pd.read_csv(r"C:\Users\Fahim\OneDrive\Desktop\python notes\Pokémon.csv",index_col="Name")
            try:
                print(dt.loc["names"])
            except KeyError:
                print(f"{names} not found")
                exit()
        else:
            no=int(input("Enter the 'No' of the Pokemon:"))
            dt=pd.read_csv(r"C:\Users\Fahim\OneDrive\Desktop\python notes\Pokémon.csv",index_col="No")
            try:
                print(dt.loc[no])
            except KeyError:
                print(f"{no} out of range")
                exit()
    else:
        print("By how you want to find information?\n1.BY 'Name'\n2.By 'No'")
        try:
            choice3=int(input("Enter your choice:"))
        except ValueError:
            print("Error!!(Invalid input from user)\nEnter only number as your choice:")
            exit()
        if choice3==1:
            names=input("Enter the starting 'Name' of the Pokemon:")
            names2=input("Enter the ending 'Name' of the Pokemon:")
            dt=pd.read_csv(r"C:\Users\Fahim\OneDrive\Desktop\python notes\Pokémon.csv",index_col="Name")
            try:
                print(dt.loc[names:names2])
            except KeyError:
                print(f"{names} and {names2} not found")
                exit()
        else:
            no=int(input("Enter the starting 'No' of the Pokemon:"))
            no2=int(input("Enter the ending 'No' of the Pokemon:"))
            dt=pd.read_csv(r"C:\Users\Fahim\OneDrive\Desktop\python notes\Pokémon.csv",index_col="No")
            try:
                print(dt.loc[no: no2])
            except KeyError:
                print(f"{no} to {no2} is out of range")
                exit()
else:
    print("What do you want?\n1.Information about particular student\n2.Information about certain range")
    try:
        choice2=int(input("Enter your choice:"))
    except ValueError:
        print("Error!!(Invalid input from user)\nEnter only number as your choice:")
        exit()
    if  choice2==1:
        print("By how you want to find information?\n1.BY 'Name'\n2.By 'Roll'")
        try:
            choice3=int(input("Enter your choice:"))
        except ValueError:
            print("Error!!(Invalid input from user)\nEnter only number as your choice:")
            exit()
        if choice3==1:
            names=input("Enter the 'Name' of the student:")
            dt=pd.read_csv(r"C:\Users\Fahim\Downloads\150_students_separate_roll_name.csv",index_col="Name")
            try:
                print(dt.loc["names"])
            except KeyError:
                print(f"{names} not found")
                exit()
        else:
            roll=int(input("Enter the 'Roll' of the Pokemon:"))
            dt=pd.read_csv(r"C:\Users\Fahim\Downloads\150_students_separate_roll_name.csv",index_col="Roll")
            try:
                print(dt.loc[roll])
            except KeyError:
                print(f"{roll} out of range")
                exit()
    else:
        print("By how you want to find information?\n1.BY 'Name'\n2.By 'Roll'")
        try:
            choice3=int(input("Enter your choice:"))
        except ValueError:
            print("Error!!(Invalid input from user)\nEnter only number as your choice:")
            exit()
        if choice3==1:
            names=input("Enter the starting 'Name' of the student:")
            names2=input("Enter the ending 'Name' of the student:")
            dt=pd.read_csv(r"C:\Users\Fahim\Downloads\150_students_separate_roll_name.csv",index_col="Name")
            try:
                print(dt.loc[names:names2])
            except KeyError:
                print(f"{names} and {names2} not found")
                exit()
        else:
            roll=int(input("Enter the starting 'Roll' of the Pokemon:"))
            roll2=itn(input("Enter the ending 'Roll' of the Pokemon:"))
            dt=pd.read_csv(r"C:\Users\Fahim\Downloads\150_students_separate_roll_name.csv",index_col="Roll")
            try:
                print(dt.loc[roll: roll2])
            except KeyError:
                print(f"{roll} to {roll2} is out of range")
                exit()
    
        
        