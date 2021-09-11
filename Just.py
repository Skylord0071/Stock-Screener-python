import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

while True:
    print("Hello World")
    mm = input("Enter the company name : ")
    print("Year,month,date format")
    ya = int(input("start year : "))
    ma = int(input("start month : "))
    da = int(input("start date :"))
    yb = int(input("end year: "))
    mb = int(input("end month: "))
    db = int(input("end date: "))

    style.use('ggplot')
    so = input("Do you want to view some values ex. open, close etc in table form (y/n)? ")
    if so.lower() == 'y':
        print("The no. of values you give will be accounted from the start day..")
        v = int(input("No. date you want values : "))
        print(df.head(v))
        
    start = dt.datetime((ya),(ma),(da))
    end = dt.datetime((yb),(mb),(db))
    df = web.DataReader((mm), 'yahoo', start, end)
    dg = df['Adj Close']
    dg.plot()
    plt.show()
    choice = input("Do you wann a see once again? (y/n)")
    if choice.lower() == 'n':
        print("Thank you sir")
        speak("Thank you sir")
        break

        #https://github.com/Skylord0071/Stock-Screener-python

