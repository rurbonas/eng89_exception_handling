# Working with Files
## Exception handling
### File permissions

##### Example of errors/exception
-  `value error`
- `syntax error`
- `out of bounce `
- `key error`
- `attribute error`
- `ZeroDivisionError: division by zero`

##### File permissions

- `r` This is the default mode. It opens file for reading
- `w` This mode opens file for writing. If file doesn't exist, it creates a new file for us
- `x` Creates a new file, if already exists, the operation fails
- `a` Opens file in Append Mode, if file doesn't exist, it creates a new one
- `t` This the default mode to open in text mode
- `b` This for binary mode
- `+` This will open a file for reading and writing (updating) 

**we have `try` `except` and `finally`**
- `try` works as `if condition`
- `except` works as `elif`
- `finally` works as `else`, `finally` will execute regardless of `try` and `except` conditions

#### Exception code within a class for package use
Reading the file:
```python
# file = open("order.text") # open() takes a string arg with file name
# print(file)
# FileNotFoundError: [Errno 2] No such file or directory: 'order.text'
# Let's create an exception:

class FileOpenHandling:
    def FileRead(self, xfile):
        try:
            file = open(xfile)  # open() takes a string arg with file name
            return ("File was found")
        except FileNotFoundError as err: # if FileNotFoundError error is found print:
            return (f"File not found {err}")
        finally:
            print ("Thank you for visiting, here's what we found:")

    def FileOpen(self, xfile):
        with open(xfile, "r") as file:
            #file = open(xfile, "r")  # open() takes a string arg with file name
            return file.read()
```
Writing/Adding to the file:
```python
class FileWriteHandling:
    def FileWrite(self, xfile, new_text):
        try:
            with open(xfile, "a") as file:
                file.write("\n" + new_text)
                file.close()
                return "Your text has been added"

        except FileNotFoundError as err:
            return "File not found: {}.".format(err)
```
The user is prompt to input a file name and it will be compared to `order.text`
```python
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

```