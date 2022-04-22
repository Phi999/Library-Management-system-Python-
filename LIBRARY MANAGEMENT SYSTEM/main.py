import csv
import os
import sys
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

from datetime import timedelta, date

t = 0
from datetime import date

today = date.today()





while True:
    today = date.today()
    print("Hello!")
    print("Please choose what you want to do (type the number):")
    print(" 1 - See all books that are still in the library")
    print("2 - Borrow a book")
    print("3 -Bring back a book")
    print("4 - See all books")
    print("5 - See borrowed books at the moment")
    a = input("\n")
    if a == '4':
        t = 0

        with open("books_in_rn.csv", 'r') as f:

            csv_reader = csv.reader(f)
            for line in csv_reader:
                if line[7] != "":
                    print("book " + line[0]  + " genre " + line[2] + " id " + line[6] + "  status :  " + line[7] )
                else:
                    print("book " + line[0] + " genre " + line[2] + " id " + line[6] + "  status :  " + " not taken")

                t+=1
        input("Press enter to continue")
    if a == '5':
        t = 0

        with open("books_borrowed.csv", 'r') as f:

            csv_reader = csv.reader(f)
            for line in csv_reader:
                if t != 0 and line[0] != '':
                    print("book " + line[0] + " from " + line[2] + " to " + line[3] + " with id "+ line[1])
                t+=1
        input("Press enter to continue")


    if a == '1':
        with open('books_in_rn.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if(line[7] != 'taken'):
                    print(line)
        input("Press enter to continue")
        csv_file.close()
        os.system('cls')
    if a == '2':
        with open('books_borrowed.csv', 'a',newline='') as f:

            twriter = csv.writer(f)
            title = input('What is the title of your book ?\n')
            input("Press enter to continue\n")
            id = input("What is the id of your book?\n")
            input("Press enter to continue\n")
            days2 = input("How many days do you need to read this book ?\n")
            today = date.today()
            EndDate = date.today() + timedelta(days=int(days2))

            print(today)
            print("to")
            print(EndDate)
            input("Press enter to continue")

            print("You got  " + title + " with  id  " + id + " time from " + str(today) + " to " + str(EndDate) + "\n")
            input("Press enter to continue")
            twriter.writerow([title, id, today, EndDate])
            supremID = id
            f.close()
        df = pd.read_csv("books_in_rn.csv")

        # updating the column value/data
        if title == str(df.loc[int(supremID), 'Title']):
            df.loc[int(supremID), 'Status'] = 'taken'

            # writing into the file8

            df.to_csv("books_in_rn.csv", index=False)



            print("Successful! Enjoy your book")
        else :
            print("Something went wrong. Please try again")


        input("Press enter to continue")
        os.system('cls')

    if a == '3':
        title = input("What book are you bringing?\n")
        input("Press enter to continue\n")

        id = input("What is the id of that book?\n")
        input("Press enter to continue\n")

        df = pd.read_csv("books_borrowed.csv")
        ok = 0
        for i in range (0,df.shape[0]):
            if float(id) == float(df.loc[i, 'Id']):
                df.loc[i, 'Title'] = ""
                df.loc[i, 'Id'] = ""
                start_date = df.loc[i,'From']
                end_date = df.loc[i, 'To']
                df.loc[i, 'From'] = ""
                df.loc[i,'To'] = ""
                if str(today) <= end_date:
                    print("You are on time!")
                ok = 1
                break

        df.to_csv("books_borrowed.csv", index=False)


        boooks_in = pd.read_csv("books_in_rn.csv")
       # print(df.loc[id, 'Status'])
        boooks_in.loc[int(id), 'Status'] = ""

        boooks_in.to_csv("books_in_rn.csv", index=False)

        if ok == 1:
            print("Successful!")
        input("Press enter to continue!")















