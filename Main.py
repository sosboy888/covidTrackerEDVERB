import requestData
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

window=Tk()
window.minsize(300,300)
window.title("Coronavirus Tracker")
logo=PhotoImage(file="icon.png")
window.iconphoto(False, logo)
imageLabel=Label(window, image=logo)
imageLabel.grid()
textLabel=Label(window, text="Enter the name of the country you want to know the number of cases for")
textLabel.grid()
countryName=StringVar()
countryEntry=Entry(window, width=30, textvariable=countryName)
countryEntry.grid()

def getCases():
    response=requestData.request(countryName.get())
    messagebox.showinfo(response[0]["country"]+" Cases","Confirmed Cases:"+str(response[0]["confirmed"])+"\nRecovered Cases:"+str(response[0]["recovered"]))
def getIndiaCases():
    response=requestData.request("india")
    messagebox.showinfo(response[0]["country"]+" Cases","Confirmed Cases:"+str(response[0]["confirmed"])+"\nRecovered Cases:"+str(response[0]["recovered"]))
goButton=Button(window, text="GO", command=getCases)
goButton.grid()
indiaButton=Button(window, text="Display number of cases in India",command=getIndiaCases)
indiaButton.grid()
