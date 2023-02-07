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



def DataBase_insert(id,datetimeStart,study,time_sec):
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    
    datetimeNow=datetime.datetime.now().strftime("%H:%M:%S") # for now time h/m/s only
    

    datetimeDate=datetime.datetime.now().date()
    data_to_insert=(
        (id,study,datetimeDate,datetimeStart,datetimeNow,time_sec),
    )
   
    cursor.executemany('INSERT INTO Table1 (Task_id_static,Task_Name,Task_Date,Task_Start_Time, Task_End_Time,Task_Passed_Time_sec_int) VALUES(?, ?, ?, ?, ?, ?)',data_to_insert)
    conn.commit()
    print("Data Inserted")



def DataBase_Select_First_three_Subjects():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    cursor.execute('SELECT Task_Name,Task_id_static FROM Table1 ORDER BY Task_Id DESC')
   
    recnt_list1=[]
  
    count=0
    element_count=0
    for row,id in cursor.fetchall():
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
    
##select by static id three subjects and seconds that you larned
def selectRecentThreeSubsAndBySec():
    print("we are in ms_access func=selectRecentThreeSubsAndBySec")
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    cursor.execute('SELECT Task_Name,Task_id_static FROM Table1 WHERE Task_Date=date() and Task_id_static=1')
    
    
    for row in cursor.fetchall():
         print(row)
   
    
    pass


#### get all subjects##
def selectALLFromSubjects():
    print("we are in ms_access func=selectRecentThreeSubsAndBySec")
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    cursor.execute('SELECT Sub_Name,Task_id FROM Task_ID')
    
    all_subs=[]
    
    for row,id in cursor.fetchall():
         all_subs.append(row)
   
    return all_subs
    pass


def addNewSubToAList(subName):
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()

    data_to_insert=(
        (subName),
    )
   
    cursor.executemany('INSERT INTO Task_ID (Sub_Name) VALUES(?)',data_to_insert)
    conn.commit()
    print("Data Inserted")
    pass


def deleteFromSubs(subName):
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')

    
   
    sql = 'DELETE FROM Task_ID WHERE Sub_Name=?'
    cursor = conn.cursor()
    cursor.execute(sql, (subName,))
    conn.commit()
    print("Data deleted")
    pass



#### get_ID_subject##
def get_ID_subject(subName):
    print("we are in ms_access func=get_ID_subject")
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    sql='SELECT Task_id FROM Task_ID WHERE Sub_Name=?'
    cursor.execute(sql, (subName,))
    row_to_list=[]
    
    for row in cursor.fetchall():
        row_to_list = [elem for elem in row]
   
    return row_to_list
    pass



def get_subject_by_ID(id):
    print("we are in ms_access func=get_subject_by_ID:")
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    sql='SELECT Task_Name,Task_Date,Task_Start_Time,Task_End_Time,Task_Passed_Time_sec_int FROM Table1 WHERE Task_id_static=?'
    cursor.execute(sql, (id,))
    row_table1=[]
    
    for row in cursor.fetchall():
        row_table1.append(row)
   
    return row_table1
    pass



def DataBase_Select_First_three_Subjects_all_info():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\My_subjects\Data_Study.accdb;')
    cursor = conn.cursor()
    seclist=[]
    namelist=[]

    cursor.execute('SELECT Task_Passed_Time_sec_int,Task_Date,Task_Name FROM Table1 ORDER BY Task_Id DESC')
    for sec,date,name in cursor.fetchall():
        date=str(date)
        x = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        if x.year==datetime.datetime.now().year:
            if x.month==datetime.datetime.now().month:
                if x.isocalendar().week==datetime.datetime.now().isocalendar().week:
                    seclist.append(sec)
                    namelist.append(name)

    
    return namelist,seclist