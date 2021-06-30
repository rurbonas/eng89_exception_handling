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
```python
# file = open("order.text") # open() takes a string arg with file name
# print(file)
# FileNotFoundError: [Errno 2] No such file or directory: 'order.text'
# Let's create an exception:

class FileHandling:
    def FileOpen(self, xfile):
        try:
            file = open(xfile)  # open() takes a string arg with file name
            print("File found")
        except FileNotFoundError as err: # if FileNotFoundError error is found print:
            print(f"File not found {err}")
        finally:
            print("Thank you for visiting, have a great day.")
```
The user is prompt to input a file name and it will be compared to `order.text`
```python
from app.files_and_exception_handling import FileHandling

x = FileHandling()

xfile = input("What file would you like to open? (with extension) >> ")
print(x.FileOpen(xfile))
```