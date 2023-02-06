import pyodbc
import datetime
import os



def DataBase_print_all():
    try:
     conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
     cursor = conn.cursor()
     cursor.execute('SELECT * FROM Table1')
   
     for row in cursor.fetchall():
         print (row)
    except:
        print("no found")
        return 1      



def DataBase_insert(datetimeStart,study,time_sec):
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    
    datetimeNow=datetime.datetime.now().strftime("%H:%M:%S") # for now time h/m/s only
    

    datetimeDate=datetime.datetime.now().date()
    data_to_insert=(
        (study,datetimeDate,datetimeStart,datetimeNow,time_sec),
    )
   
    cursor.executemany('INSERT INTO Table1 (Task_Name,Task_Date,Task_Start_Time, Task_End_Time,Task_Passed_Time_sec_int) VALUES( ?, ?, ?, ?, ?)',data_to_insert)
    conn.commit()
    print("Data Inserted")



def DataBase_Select_First_three_Subjects():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    cursor.execute('SELECT Task_Name FROM Table1 ORDER BY Task_Id DESC')
   
    recnt_list1=[]
    count=0
    element_count=0
    for row in cursor.fetchall():
        if count==0:
           recnt_list1.append(row)
           count+=1
           continue

        element_count=len(recnt_list1)        
        if row not in recnt_list1 and element_count<3:
            recnt_list1.append(row)
        count+=1       
   
    return recnt_list1


def selectTimePassedRow():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    cursor.execute('SELECT Task_Passed_Time_sec_int FROM Table1')
    row_to_list=[]
    
    for row in cursor.fetchall():
        row_to_list.append(row)

    
    return row_to_list   



def selectFirstRow():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    cursor.execute('SELECT TOP 1 * FROM Table1 ORDER BY Task_Id DESC')
    row_to_list=[]
    for row in cursor.fetchall():
        row_to_list = [elem for elem in row]

    return row_to_list



def selectTimeBYSec():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    cursor.execute('SELECT Task_Passed_Time_sec_int FROM Table1')
    row_to_list=[]
    for row in cursor.fetchall():
        row_to_list.append(row)

    return row_to_list

####returns last study today by sec int()#####
def selectTimeBYSecToday():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    seclist=0

    cursor.execute('SELECT  TOP 1 Task_Passed_Time_sec_int,Task_Date FROM Table1 ORDER BY Task_Id DESC')
    for sec,row in cursor.fetchall():
        seclist=sec

    
    return seclist



##### returns how much time learned this day by seconds int() #####
def selectTimeBYSecAndDate():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    seclist=[]

    cursor.execute('SELECT Task_Passed_Time_sec_int,Task_Date FROM Table1')
    for row,sec in cursor.fetchall():
       ttt=str(sec) 
       if ttt[:10]==str((datetime.datetime.now().date())):
           seclist.append(row)

    sum_sec=sum(seclist)
    return sum_sec


##### returns how much time learned this week by seconds int() #####
def selectTimeBYSecAndDateWeek():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    seclist=[]
    
    cursor.execute('SELECT Task_Passed_Time_sec_int,Task_Date FROM Table1')
    for sec,date in cursor.fetchall():
        date=str(date)
        x = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        if x.year==datetime.datetime.now().year:
            if x.month==datetime.datetime.now().month:
                if x.isocalendar().week==datetime.datetime.now().isocalendar().week:
                    seclist.append(sec)

    sum_sec=sum(seclist)
    return sum_sec

  



##### returns how much time learned this month by seconds int() #####
def selectTimeBYSecAndDateMonth():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    seclist=[]
    
    cursor.execute('SELECT Task_Passed_Time_sec_int,Task_Date FROM Table1')
    for sec,date in cursor.fetchall():
        date=str(date)
        x = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        if x.year==datetime.datetime.now().year:
            if x.month==datetime.datetime.now().month:
                seclist.append(sec)

    sum_sec=sum(seclist)
    return sum_sec
   


##### returns how much time learned this year by seconds int() #####
def selectTimeBYSecAndDateYear():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    seclist=[]
    
    cursor.execute('SELECT Task_Passed_Time_sec_int,Task_Date FROM Table1')
    for sec,date in cursor.fetchall():
        date=str(date)
        x = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        if x.year==datetime.datetime.now().year:
            seclist.append(sec)

    sum_sec=sum(seclist)
    return sum_sec




##### returns  learned ALL the times by seconds int()  #####
def selectTimeBYSecAndDateAll_Time():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    seclist=[]
    
    cursor.execute('SELECT Task_Passed_Time_sec_int,Task_Date FROM Table1')
    for sec,date in cursor.fetchall():
      seclist.append(sec)

    
    sum_sec=sum(seclist)
    return sum_sec         
    



