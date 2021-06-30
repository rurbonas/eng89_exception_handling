class FileWriteHandling:
    def FileWrite(self, xfile, new_text):
        try:
            with open(xfile, "a") as file:
                file.write("\n" + new_text)
                file.close()
                return "Your text has been added"

        except FileNotFoundError as err:
            return "File not found: {}.".format(err)