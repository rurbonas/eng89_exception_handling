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