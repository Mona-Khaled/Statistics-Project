import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\pc\PycharmProjects\students.csv')
#background
root = Tk()
root.title('Application Statistcs')
#DrawPieChart
def showPie():
    labels=df['School']
    sizes=df['Test-takers: 2012']
    colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E", "#d62728", "#8c564b"]
    explode=(0,0,0, 0,0, 0,0, 0,0,0,0,0 )
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()
showbutton = Button(root, text="PieChart", command=showPie).pack()
#showstd
def show_std():
    valueOfStd = df.std()
    showStdLabel=Label(root,text= valueOfStd).pack()
showbuttonstd = Button(root,text="Show me std",command=show_std).pack()
#showvar
def show_var():
    valueOfvar = df.var()
    showvarLabel=Label(root,text= valueOfvar).pack()
showbuttonvar = Button(root,text="Show me var",command=show_var).pack()
root.geometry('700x700')
root.config(bg="black")
root.mainloop()
