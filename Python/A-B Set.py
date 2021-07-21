# -*- coding: utf-8 -*-
"""
Created on Jul 21 2021, 4:42 PM
@author: amanj
"""
import csv

def readCSVFile(filename):
    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        print(f"Total no. of rows in {filename}: %d" % (csvreader.line_num))

    # printing the field names
    # print('Field names are:' + ', '.join(field for field in fields))

    #  printing first 5 rows
    #print('\nFirst 5 rows are:\n')
    #for row in rows[:5]:
        # parsing each column of a row
    #    for col in row:
    #        print("%10s" % col),
    #    print('\n')
    return(rows)

def flatternList(listOfList):
    return [item for sublist in listOfList for item in sublist]

if __name__ == '__main__':
    # csv file name
    file1 = "C:\\Users\\amanj\Desktop\D2S.csv"
    file2 = "C:\\Users\\amanj\Desktop\Mercury.csv"
    D2S = flatternList(readCSVFile(file1))
    Mercury = flatternList(readCSVFile(file2))
    print(len(Mercury), len(set(Mercury)))
    MercurySpecificFailure = [] #set(Mercury).difference(set(D2S))
    for i in Mercury:
        if i not in D2S:
            MercurySpecificFailure.append(i)
        else:
            continue

    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(*MercurySpecificFailure, sep = ", ")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(len(MercurySpecificFailure))