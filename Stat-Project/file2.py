import tkinter
from tkinter import IntVar
from tkinter import*
import matplotlib.pyplot as plt
from pandas import read_csv, DataFrame
#window
window = Tk()
window.title('Application Statistcs')
#readdata
data = read_csv(r'C:\Users\pc\PycharmProjects\students.csv')
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
x = 0
y = 0
def getxyvalue():
    if var1.get() == 1and var2.get() == 1:
      x = data['District Number']
      y = data['Test-takers: 2012']
      plt.bar(x, y, color='blue', label=' yasmina')
      plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
      plt.show()
    elif var1.get() == 1and var3.get() == 1 :
      x=data['District Number']
      y=data['Test-takers: 2013']
      plt.bar(x, y, color='blue', label=' yasmina')
      plt.legend(facecolor='gray',shadow='True',loc=5, title='the title')
      plt.show()
    elif var1.get()==1and var4.get()==1:
        x=data['District Number']
        y=data['Test-takers: Change%']
        plt.bar(x, y, color='blue', label=' yasmina')
        plt.legend(facecolor='gray',shadow='True',loc=5, title='the title')
        plt.show()
    elif var1.get()==1and var5.get()==1 :
      x=data['District Number']
      y=data['Participation Rate (estimate): 2012']
      plt.bar(x, y, color='blue', label=' yasmina')
      plt.legend(facecolor='gray',shadow='True',loc=5, title='the title')
      plt.show()
    elif var1.get()==1and var6.get()==1 :
      x=data['District Number']
      y=data['Participation Rate (estimate): 2013']
      plt.bar(x, y, color='blue', label=' yasmina')
      plt.legend(facecolor='gray',shadow='True',loc=5, title='the title')
      plt.show()
    elif var1.get()==1and var7.get()==1 :
      x=data['District Number']
      y=data['Participation Rate (estimate): Change%']
      plt.bar(x, y, color='blue', label=' yasmina')
      plt.legend(facecolor='gray',shadow='True',loc=5, title='the title')
      plt.show()
    elif var1.get()==1and var8.get()==1 :
       x=data['District Number']
       y=data['Percent Meeting Benchmark: 2012']
       plt.bar(x, y, color='blue', label=' yasmina')
       plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
       plt.show()
    elif var1.get()==1and var9.get() ==1:
        x=data['District Number']
        y=data['Percent Meeting Benchmark: Change%']
        plt.bar(x, y, color='blue', label=' yasmina')
        plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
        plt.show()
    elif var2.get()==1and var3.get()==1:
         x=data['Test-takers: 2012']
         y=data['Test-takers: 2013']
         plt.bar(x, y, color='blue', label=' yasmina')
         plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
         plt.show()
    elif var2.get()==1and var4.get()==1:
          x=data['Test-takers: 2012']
          y=data['Test-takers: Change%']
          plt.bar(x, y, color='blue', label=' yasmina')
          plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
          plt.show()
    elif var2.get()==1and var5.get()==1:
        x=data['Test-takers: 2012']
        y=data['Participation Rate (estimate): 2012']
        plt.bar(x, y, color='blue', label=' yasmina')
        plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
        plt.show()
    elif var2.get()==1and var6.get()==1 :
         x=data['Test-takers: 2012']
         y=data['Participation Rate (estimate): 2013']
         plt.bar(x, y, color='blue', label=' yasmina')
         plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
         plt.show()
    elif var2.get()==1and var7.get()== 1:
         x=data['Test-takers: 2012']
         y=data['Participation Rate (estimate): Change%']
         plt.bar(x, y, color='blue', label=' yasmina')
         plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
         plt.show()
    elif var2.get()==1and var8.get() == 1 :
          x=data['Test-takers: 2012']
          y=data['Percent Meeting Benchmark: 2012']
          plt.bar(x, y, color='blue', label=' yasmina')
          plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
          plt.show()
    elif var2.get()==1and var9.get()==1 :
        x=data['Test-takers: 2012']
        y=data['Percent Meeting Benchmark: Change%']
        plt.bar(x, y, color='blue', label=' yasmina')
        plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
        plt.show()
    elif var3.get()==1and var4.get()==1 :
        x=data['Test-takers: 2012']
        y=data['Test-takers: Change%']
        plt.bar(x, y, color='blue', label=' yasmina')
        plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
        plt.show()
    elif var3.get()==1and var5.get()==1:
            x=data['Test-takers: 2013']
            y=data['Participation Rate (estimate): 2012']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var3.get()==1and var6.get()==1 :
        x=data['Test-takers: 2013']
        y=data['Participation Rate (estimate): 2013']
        plt.bar(x, y, color='blue', label=' yasmina')
        plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
        plt.show()
    elif var3.get()==1and var7.get()==1 :
        x=data['Test-takers: 2013']
        y=data['Participation Rate (estimate): Change%']
        plt.bar(x, y, color='blue', label=' yasmina')
        plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
        plt.show()
    elif var3.get()==1and var8.get()==1:
            x=data['Test-takers: 2013']
            y=data['Percent Meeting Benchmark: 2012']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var3.get()==1and var9.get()==1 :
        x=data['Test-takers: 2013']
        y=data['Percent Meeting Benchmark: Change%']
        plt.bar(x, y, color='blue', label=' yasmina')
        plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
        plt.show()
    elif var4.get()==1and var5.get()==1:
            x=data['Test-takers: 2012']
            y=data['Participation Rate (estimate): 2012']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var4.get()==1and var6.get()==1:
            x=data['Test-takers: Change%']
            y=data['Participation Rate (estimate): 2013']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var4.get()==1and var7.get()==1:
            x=data['Test-takers: Change%']
            y=data['Participation Rate (estimate): Change%']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var4.get()==1and var8.get()==1:
            x=data['Test-takers: Change%']
            y=data['Percent Meeting Benchmark: 2012']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var4.get()==1 and var9.get()==1:
            x=data['Test-takers: Change%']
            y=data['Percent Meeting Benchmark: Change%']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var5.get()==1 and var6.get()==1:
            x=data['Participation Rate (estimate): 2012']
            y=data['Participation Rate (estimate): 2013']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var5.get()==1and var7.get()==1:
            x=data['Participation Rate (estimate): 2012']
            y=data['Participation Rate (estimate): Change%']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var5.get()==1and var8.get()==1:
            x=data['Participation Rate (estimate): 2012']
            y=data['Percent Meeting Benchmark: 2012']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var5.get()==1and var9.get()==1:
            x=data['Participation Rate (estimate): 2012']
            y=data['Percent Meeting Benchmark: Change%']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var6.get()==1and var7.get()==1:
            x=data['Participation Rate (estimate): 2013']
            y=data['Participation Rate (estimate): Change%']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var6.get()==1and var8.get()==1:
            x=data['Participation Rate (estimate): 2013']
            y=data['Percent Meeting Benchmark: 2012']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var6.get()==1and var9.get()==1:
            x=data['Participation Rate (estimate): 2013']
            y=data['Percent Meeting Benchmark: Change%']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var7.get()==1and var8.get()==1:
            x=data['Participation Rate (estimate): Change%']
            y=data['Percent Meeting Benchmark: 2012']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
    elif var8.get()==1and var9.get()==1:
            x=data['Percent Meeting Benchmark: 2012']
            y=data['Percent Meeting Benchmark: Change%']
            plt.bar(x, y, color='blue', label=' yasmina')
            plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
            plt.show()
#plt.bar(x, y, color='blue', label=' yasmina')
#plt.legend(facecolor='gray',shadow='True',loc=5, title='the title')
#plt.show()
def showGraphScotter():
      if var1.get() == 1and var2.get() == 1:
          x = data['District Number']
          y = data['Test-takers: 2012']
          plt.scatter(x,y)
          plt.show()
      elif var1.get() == 1and var3.get() == 1 :
          x=data['District Number']
          y=data['Test-takers: 2013']
          plt.scatter(x,y)
          plt.show()
      elif var1.get()==1and var4.get()==1:
            x=data['District Number']
            y=data['Test-takers: Change%']
            plt.scatter(x,y)
            plt.show()
      elif var1.get()==1and var5.get()==1 :
              x=data['District Number']
              y=data['Participation Rate (estimate): 2012']
              plt.scatter(x,y)
              plt.show()
      elif var1.get()==1and var6.get()==1 :
              x=data['District Number']
              y=data['Participation Rate (estimate): 2013']
              plt.scatter(x,y)
              plt.show()
      elif var1.get()==1and var7.get()==1 :
              x=data['District Number']
              y=data['Participation Rate (estimate): Change%']
              plt.scatter(x,y)
              plt.show()
      elif var1.get()==1and var8.get()==1 :
           x=data['District Number']
           y=data['Percent Meeting Benchmark: 2012']
           plt.scatter(x,y)
           plt.show()
      elif var1.get()==1and var9.get() ==1:
            x=data['District Number']
            y=data['Percent Meeting Benchmark: Change%']
            plt.scatter(x,y)
            plt.show()
      elif var2.get()==1and var3.get()==1:
             x=data['Test-takers: 2012']
             y=data['Test-takers: 2013']
             plt.scatter(x,y)
             plt.show()
      elif var2.get()==1and var4.get()==1:
              x=data['Test-takers: 2012']
              y=data['Test-takers: Change%']
              plt.scatter(x,y)
              plt.show()
      elif var2.get()==1and var5.get()==1:
            x=data['Test-takers: 2012']
            y=data['Participation Rate (estimate): 2012']
            plt.scatter(x,y)
            plt.show()
      elif var2.get()==1and var6.get()==1 :
             x=data['Test-takers: 2012']
             y=data['Participation Rate (estimate): 2013']
             plt.scatter(x,y)
             plt.show()
      elif var2.get()==1and var7.get()== 1:
             x=data['Test-takers: 2012']
             y=data['Participation Rate (estimate): Change%']
             plt.scatter(x,y)
             plt.show()
      elif var2.get()==1and var8.get() == 1 :
              x=data['Test-takers: 2012']
              y=data['Percent Meeting Benchmark: 2012']
              plt.scatter(x,y)
              plt.show()
      elif var2.get()==1and var9.get()==1 :
            x=data['Test-takers: 2012']
            y=data['Percent Meeting Benchmark: Change%']
            plt.scatter(x,y)
            plt.show()
      elif var3.get()==1and var4.get()==1 :
            x=data['Test-takers: 2012']
            y=data['Test-takers: Change%']
            plt.scatter(x,y)
            plt.show()
      elif var3.get()==1and var5.get()==1:
                x=data['Test-takers: 2013']
                y=data['Participation Rate (estimate): 2012']
                plt.scatter(x,y)
                plt.show()
      elif var3.get()==1and var6.get()==1 :
            x=data['Test-takers: 2013']
            y=data['Participation Rate (estimate): 2013']
            plt.scatter(x,y)
            plt.show()
      elif var3.get()==1and var7.get()==1 :
            x=data['Test-takers: 2013']
            y=data['Participation Rate (estimate): Change%']
            plt.scatter(x,y)
            plt.show()
      elif var3.get()==1and var8.get()==1:
                x=data['Test-takers: 2013']
                y=data['Percent Meeting Benchmark: 2012']
                plt.scatter(x,y)
                plt.show()
      elif var3.get()==1and var9.get()==1 :
            x=data['Test-takers: 2013']
            y=data['Percent Meeting Benchmark: Change%']
            plt.scatter(x,y)
            plt.show()
      elif var4.get()==1and var5.get()==1:
                x=data['Test-takers: 2012']
                y=data['Participation Rate (estimate): 2012']
                plt.scatter(x,y)
                plt.show()
      elif var4.get()==1and var6.get()==1:
                x=data['Test-takers: Change%']
                y=data['Participation Rate (estimate): 2013']
                plt.scatter(x,y)
                plt.show()
      elif var4.get()==1and var7.get()==1:
                x=data['Test-takers: Change%']
                y=data['Participation Rate (estimate): Change%']
                plt.scatter(x,y)
                plt.show()
      elif var4.get()==1and var8.get()==1:
                x=data['Test-takers: Change%']
                y=data['Percent Meeting Benchmark: 2012']
                plt.scatter(x,y)
                plt.show()
      elif var4.get()==1 and var9.get()==1:
                x=data['Test-takers: Change%']
                y=data['Percent Meeting Benchmark: Change%']
                plt.scatter(x,y)
                plt.show()
      elif var5.get()==1 and var6.get()==1:
                x=data['Participation Rate (estimate): 2012']
                y=data['Participation Rate (estimate): 2013']
                plt.scatter(x,y)
                plt.show()
      elif var5.get()==1and var7.get()==1:
                x=data['Participation Rate (estimate): 2012']
                y=data['Participation Rate (estimate): Change%']
                plt.scatter(x,y)
                plt.show()
      elif var5.get()==1and var8.get()==1:
                x=data['Participation Rate (estimate): 2012']
                y=data['Percent Meeting Benchmark: 2012']
                plt.scatter(x,y)
                plt.show()
      elif var5.get()==1and var9.get()==1:
                x=data['Participation Rate (estimate): 2012']
                y=data['Percent Meeting Benchmark: Change%']
                plt.scatter(x,y)
                plt.show()
      elif var6.get()==1and var7.get()==1:
                x=data['Participation Rate (estimate): 2013']
                y=data['Participation Rate (estimate): Change%']
                plt.scatter(x,y)
                plt.show()
      elif var6.get()==1and var8.get()==1:
                x=data['Participation Rate (estimate): 2013']
                y=data['Percent Meeting Benchmark: 2012']
                plt.scatter(x,y)
                plt.show()
      elif var6.get()==1and var9.get()==1:
                x=data['Participation Rate (estimate): 2013']
                y=data['Percent Meeting Benchmark: Change%']
                plt.scatter(x,y)
                plt.show()
      elif var7.get()==1and var8.get()==1:
                x=data['Participation Rate (estimate): Change%']
                y=data['Percent Meeting Benchmark: 2012']
                plt.bar(x, y, color='blue', label=' yasmina')
                plt.legend(facecolor='gray', shadow='True', loc=5, title='the title')
                plt.show()
      elif var8.get()==1and var9.get()==1:
                x=data['Percent Meeting Benchmark: 2012']
                y=data['Percent Meeting Benchmark: Change%']
                plt.scatter(x,y)
                plt.show()
buttonShowGraph = Button(window, text ="show me Histogram", command=getxyvalue).pack()
buttonShowDotplot = Button(window, text="Show Me Dot plot", command=showGraphScotter).pack()
window.geometry('700x700')
window.config(bg='black')
window.mainloop()
