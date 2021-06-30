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

