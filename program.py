from app.files_and_exception_handling import FileHandling

x = FileHandling()

xfile = input("What file would you like to open? (with extension) >> ")
print(x.FileOpen(xfile))