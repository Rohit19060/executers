import os
import sys
from datetime import date


def work(workSpace="Default"):
    close = False
    path = "D:\\Projects\\"
    files = os.listdir(path)
    files = [i for i in files if i.endswith(".code-workspace")]
    try:
        if (workSpace != "Default"):
            y = [i for i in files if i.lower(
            ).startswith(workSpace.lower())][0]
        else:
            x = 1
            for i in files:
                print(f'{x}: {i}')
                x = x+1
            y = input(
                "WorkSpace Not Found! Which Work Space you want to work in or Press y for Exit: ")
            if (y.lower() == "y"):
                close = True
                return
            if (y.isdigit()):
                y = files[int(y) - 1]
            else:
                y = [i for i in files if i.lower().startswith(y.lower())][0]
        os.startfile(path+y)
    except:
        work()
    if (close):
        exit("Exit")


if (sys.argv[1] == "Work"):
    if len(sys.argv) == 3:
        work(sys.argv[2])
    else:
        work()


elif (sys.argv[1] == "Blog"):
    os.chdir("D:\\King Technologies\\Blogs")
    b_name = str(input("Blog name: "))
    if (b_name != ""):
        os.system(f'echo # {b_name} > "{str(date.today())+"-"+b_name}".md')
    os.system("code .")
    os.system("exit")

elif (sys.argv[1] == "Space"):
    x = input("Enter String for Replacing Space with `%20`: ")
    print(x.replace(" ", "%20"))
    input("Press Enter to Exit..")

elif (sys.argv[1] == "Notes"):
    os.chdir("D:\\Projects\\developer-utilities")
    os.system("code .")
