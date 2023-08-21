# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: Eli Ritter downloaded the assignment seven starter file before then adding onto it.
# Eli Ritter, <8/19/2023>, Created Script
# ------------------------------------------------- #
import pickle, shelve  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    # Code taken from the assignment five answer key.
    if "y" == str(input("Save this data to file? (y/n) - ")).strip().lower():
        strFile = open(strFileName, "w")
        for dicRow in lstCustomer:
            strFile.write(dicRow["ID"] + "," + dicRow["Name"] + "\n")
        strFile.close()
        input("Data saved to file! Press the [Enter] key to return to menu.")
    else:
        input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")

def read_data_from_file(file_name):
    # Code taken from the assignment five answer key.
    strFile = open(strFileName, "r")
    for line in strFile:
        strData = line.split(",")
        dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
        lstCustomer.append(dicRow)
    strFile.close()

# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
# TODO: store the list object into a binary file
# TODO: Read the data from the file into a new list object and display the contents

strID = str(input("Please enter your ID: ")).strip()
strName = str(input("Please enter your name: ")).strip()
dicRow = {"ID": strID, "Name": strName}
lstCustomer.append(dicRow)

# Page 201 and 202 of the textbook
s = open("AppData.dat", "wb")
pickle.dump(lstCustomer, s)

s = open("AppData.dat", "rb")
lstCustomer = pickle.load(s)
print(lstCustomer)

