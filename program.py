from app.read_file import FileOpenHandling
from app.write_file import FileWriteHandling

readf = FileOpenHandling()
writef = FileWriteHandling()

while True:
    xfile = input("Name of the file you would like to open? >> ")
    found = readf.FileRead(xfile)
    print(found)
    if found == "File was found":
        view = input("Would you like to see your file? y/n  ").lower()
        if view == "y":
            print(readf.FileOpen(xfile))
            write = input("Would you like to add to your file? y/n  ").lower()
            if write == "y":
                new_text = input("What text would you like to add? Press enter to complete.  \n")
                print(writef.FileWrite(xfile, new_text))
                view_update = input("Would you like to view your file again? y/n  ").lower()
                if view_update == "y":
                    print(readf.FileOpen(xfile))
                    break
                elif view_update == "n":
                    print("Thank you for visiting, see you again!")
                    break
            elif write == "n":
                print("Thank you for visiting, see you again!")
                break
        elif view == "n":
            write = input("Would you like to add to your file? y/n  ").lower()
            if write == "y":
                new_text = input("What text would you like to add? Press enter to complete.  \n")
                print(writef.FileWrite(xfile, new_text))
                break
            elif write == "n":
                print("Thank you for visiting, see you again!")
                break
            else:
                print("Thank you for visiting, see you again!")
                break
        else:
            print("Invalid input, please try again.")
