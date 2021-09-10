from datetime import date
from tkinter import *
from numpy import median, mean
import statistics
import pandas as pd
from tkinter.ttk import Combobox
from pandas import DataFrame
from pandas.io.parsers import TextFileReader
import tkinter
from tkinter import *
#show
window = Tk()
window.title('Application Statistcs')
# photo = PhotoImage(file = r"C:\Users\HP\OneDrive\Desktop\GIF.gif")
# photo = photo.zoom(2)
background_image=PhotoImage(file = r"C:\Users\HP\OneDrive\Desktop\200w.gif")
background_label = Label(window, image=background_image)
background_label.place(x=100, y=20, relwidth=20, relheight=31)
window.geometry("500x550")
# window['bg']='C:\\Users\\HP\OneDrive\Desktop\GIF.gif'
# label = Label(window, image=photo)
background_label.pack()

#readfromfile
data = pd.read_csv(r'D:\2nd year projects\Stat-Project\students.csv')
#checkboxList
var1 = tkinter.IntVar()
tkinter.Checkbutton(window, text="District Number", variable=var1).pack()
var2 = tkinter.IntVar()
tkinter.Checkbutton(window, text="Test-takers: 2012", variable=var2).pack()
var3 = tkinter.IntVar()
tkinter.Checkbutton(window, text="Test-takers: 2013", variable=var3).pack()
var4 = tkinter.IntVar()
tkinter.Checkbutton(window, text="Test-takers: Change%", variable=var4).pack()
var5 = tkinter.IntVar()
tkinter.Checkbutton(window, text="Participation Rate (estimate): 2012", variable=var5).pack()
var6 = tkinter.IntVar()
tkinter.Checkbutton(window, text="Participation Rate (estimate): 2013", variable=var6).pack()
var7 = tkinter.IntVar()
tkinter.Checkbutton(window, text="Participation Rate (estimate): Change%", variable=var7).pack()
var8 = tkinter.IntVar()
tkinter.Checkbutton(window, text="Percent Meeting Benchmark: 2012", variable=var8).pack()
var9 = tkinter.IntVar()
tkinter.Checkbutton(window,text="Percent Meeting Benchmark: Change%", variable=var9).pack()
#choice
def checkWhitchcol():
    global df
    if var1.get() == 1:
        df = data['District Number']
    elif var2.get() == 1:
        df = data['Test-takers: 2012']
    elif var3.get() == 1:
        df = data['Test-takers: 2013']
    elif var4.get() == 1:
        df = data['Test-takers: Change%']
    elif var5.get() == 1:
        df = data['Participation Rate (estimate): 2012']
    elif var6.get() == 1:
        df = data['Participation Rate (estimate): 2013']
    elif var7.get() == 1:
        df = data['Participation Rate (estimate): Change%']
    elif var8.get() == 1:
        df = data['Percent Meeting Benchmark: 2012']
    elif var9.get() == 1:
        df = data['Percent Meeting Benchmark: Change%']
    return df
#mean
def showMean():
      returnvalue = checkWhitchcol()
      MeanOperation = mean(returnvalue)
      labelshowMean = Label(window,text=MeanOperation).pack()
buttonShowMean = Button(window,text="Show Me Mean",command=showMean).pack()
#Mode
def ShowMode():
            returnvalue = checkWhitchcol()
            ModeOperation = data.mode(axis=0, numeric_only=True, dropna=True)
            labelshowMode = Label(window, text=ModeOperation).pack()
buttonShowMode = Button(window, text = "Show Me Mode", command=ShowMode).pack()
#Madium
def ShowMadiun():
            returnvalue = checkWhitchcol()
            MedianOperation = median(returnvalue)
            labelshowMadium = Label(window, text=MedianOperation).pack()
buttonShowMadiun = Button(window, text = "Show Me Median", command=ShowMadiun).pack()
#window
window.geometry('700x700')
window.config(bg='#afd7d7')
window.mainloop()
