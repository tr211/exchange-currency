import tkinter as tk
from tkinter import ttk
import requests, json
from bs4 import BeautifulSoup as bs
from tkinter import *

class CurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']
        
m = tk.Tk()
m.title('Currency Converter')
m.geometry("300x150")
m.eval('tk::PlaceWindow . center')

Label(m, text='Source Currency  :').grid(row=0)
Label(m, text='Target Currency  :').grid(row=1)
Label(m, text='Amount  :').grid(row=2)
Label(m, text='Result  :').grid(row=8)
label=Label(m, text =" ").grid(row=8, column=1)

source_currency_entry = Entry(m)
target_currency_entry = Entry(m)
amount_entry = Entry(m)

source_currency_entry.grid(row=0, column=1)
target_currency_entry.grid(row=1, column=1)
amount_entry.grid(row=2, column=1)


def clear(): 
  source_currency_entry.delete(0, END)
  target_currency_entry.delete(0, END)
  amount_entry.delete(0, END)


def convert():
    source_currency = source_currency_entry.get()
    target_currency = target_currency_entry.get()
    amount = float(amount_entry.get())
    
    response = requests.get(f"https://www.x-rates.com/calculator/?from={source_currency}&to={target_currency}&amount=1")
    soup = bs(response.text, "html.parser")
    
    text1 = soup.find(class_="ccOutputTrail").previous_sibling
    text2 = soup.find(class_="ccOutputTrail").get_text(strip=True)
    rate = "{}{}".format(text1,text2)
    result=amount*float(rate)
    #return result

    res = Label(m, text =result,font='Helvetica 10 bold')   
    res.grid(row=8, column=1)
    
           
button = tk.Button(m, text='Convert', command=convert)
button.grid(row=3, column=1)

button2 = tk.Button(m, text='Clear', command=clear)
button2.grid(row=4, column=1)

m.mainloop()