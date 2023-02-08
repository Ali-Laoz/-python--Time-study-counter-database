#what this program is doing?
# count the time and data and what you learn and tells u how much you sduied 
#uses ms acsses for database and txt file
#uses python as programming language and tkinter for gui
#i know there is chaos with the naming of vars and grammar 


# Import the required libraries
from asyncore import loop
from cProfile import label
import datetime    #import for times and data minupaltions
from distutils import command
from tkinter import * #import for gui and data minupaltions
from tkinter import ttk #import for gui and data minupaltions
from tkinter import messagebox #for notification in order
import winsound #for sound in order 
import time 
from pyparsing import sys
from winotify import Notification,audio #for notification and sound parallel
import os
import sys


#my files -importing my functions
import File_handler 
import Ms_DataBase
import functions
import tikner_types

win = Tk() 
win.title("Time counter")
# Set the size of the window
win.geometry("1300x700")



temp=0
running = False
count = 0


FirstTimeHour=0
FirstTimeMin=0
FirstTimeSec=0
datetimeStart=None
study=""
time_sec=0
##is the timers up?
timer_is_up=False
##is the timer is Started?
timer_started=False
##is the timer is Paused?
timer_paused=False
##is the timer is Stopped?
timer_stop=False


# Define a function to print the text in a loop
def print_text():
   global running
   global temp
  # winsound.Beep(freq, duration)
   
   if running:
      global count 
     # print("temp:"+str(temp))
      if (temp)>-1:
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to
        # two decimal places
       # print("hours:"+str(hours))
       # print("mins:"+str(mins))
       # print("secs:"+str(secs))

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the
        # temp value every time
        win.update()
  
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            countDownIsOver()


        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1

      else:
          pass 

   win.after(1000, print_text)



#####prints item chooset only from the-> all list#########
def printItemFromList():
    get = listbox.curselection()
    for i in get:
        print(listbox.get(i))

def deleteItemFromList():
    count=0
    list1=[]
    deleted = listbox.curselection()
    for i in deleted:
        count=i
        print('One item Deleted')
        #list1.append(listbox.get(i))
        Ms_DataBase.deleteFromSubs(listbox.get(i))
        listbox.delete(i)
   	

    
   # File_handler.fileDeleteLine(count)    

def addItemToTheList():
    if not str(add_item_to_list.get()):
        print("there is not text")
        return

    global listbox    

    list1=[]
    list1.append(add_item_to_list.get())
    Ms_DataBase.addNewSubToAList(list1)
    
    listbox.delete(0,END)

    list_study=Ms_DataBase.selectALLFromSubjects()
    list_study=functions.remove_symbols_from_list(list_study)
    counter=0
    for i in list_study:
    #adding widget to Tab
        counter+=1
        listbox.insert(counter, i)

    add_To_List.delete(0, END) 
    pass

########################

def countDownIsOver():
    global running
    running=False
    test=None
    global study
    global timer_is_up

    global FirstTimeHour
    global FirstTimeMin
    global FirstTimeSec
    global datetimeStart
    global time_sec
    global timer_paused
    global timer_is_up
    global timer_started
    global timer_stop
    print(FirstTimeHour)
    print(FirstTimeMin)
    print(FirstTimeSec)

    timer_is_up=False
    timer_started=False
    timer_stop=False
    timer_paused=False

    toast=Notification(app_id="Times from me",title="Time Countdown",msg="Time's up",duration="long",icon="")
    toast.set_audio(audio.LoopingAlarm9,loop=True)
    toast.show()
    
    p=Ms_DataBase.get_ID_subject(study)
    print(p)
    if len(p)>0:
       Ms_DataBase.DataBase_insert(p[0],datetimeStart,study,time_sec)

    last_study_label_var.set(study)

    hour.set(FirstTimeHour)
    minute.set(FirstTimeMin)
    second.set(FirstTimeSec)

    ##last study
    first_name_list=Ms_DataBase.selectFirstRow()
    learned=functions.func(first_name_list)
    last_study_label_var.set(learned)

    ###today
    times_sec=Ms_DataBase.selectTimeBYSecAndDate()
    st=str(datetime.timedelta(seconds=times_sec))
    lerned_today_label_var.set(st)

    ###week
    studied_this_week_by_sec=Ms_DataBase.selectTimeBYSecAndDateWeek()
    studied_this_week_by_sec_str=str(datetime.timedelta(seconds=studied_this_week_by_sec))
    last_week_label_var.set(studied_this_week_by_sec_str)

    ###month
    studied_this_month_by_sec=Ms_DataBase.selectTimeBYSecAndDateMonth()
    studied_this_month_by_sec_str=str(datetime.timedelta(seconds=studied_this_month_by_sec))
    last_month_label_var.set(studied_this_month_by_sec_str)

    ###year
    studied_this_year_by_sec=Ms_DataBase.selectTimeBYSecAndDateYear()
    studied_this_year_by_sec_str=str(datetime.timedelta(seconds=studied_this_year_by_sec))
    last_year_label_var.set(studied_this_year_by_sec_str)

    ###all the time
    studied_all_time=Ms_DataBase.selectTimeBYSecAndDateAll_Time()
    studied_all_time=str(datetime.timedelta(seconds=studied_all_time))
    studied_all_time_label_var.set(studied_all_time)

    ##### inseting form ms database recet 3 subjects in listbox
    recent_list=Ms_DataBase.DataBase_Select_First_three_Subjects()
    recent_list=functions.remove_symbols_from_list(recent_list)

    recentListBox.delete(0,END)
    counter=0
    for i in recent_list:
        #adding widget to Tab
        counter+=1
        recentListBox.insert(counter, i)
    ############ done#########
    

def emptyFunc():
    pass
# Define a function to start the loop
def on_start():
   global running
   global temp
   global datetimeStart
   global study
   global time_sec
   global last_study_time_hour
   global last_study_time_min
   global last_study_time_sec
   global timer_started
   global timer_paused
   global FirstTimeHour
   global FirstTimeMin
   global FirstTimeSec
   global start_time_label_var



   try:
        # the input provided by the user is
        # stored in here##   
        ## if its the first time
        if timer_paused==False:

          FirstTimeHour=int(hour.get())
          FirstTimeMin=int(minute.get())
          FirstTimeSec=int(second.get())

          hour.set("{0:2d}".format(FirstTimeHour))
          minute.set("{0:2d}".format(FirstTimeMin))
          second.set("{0:2d}".format(FirstTimeSec))
      
          start.config(state="enabled") #after setting the times
          time_sec=FirstTimeHour*60*60
          time_sec+=FirstTimeMin*60
          time_sec+=FirstTimeSec
          
          #start_time_label_var.set((datetime.datetime.time()))
          timestart=datetime.datetime.now().strftime("%H:%M:%S")
          timestart=str(timestart)
          start_time_label_var.set(timestart)

          timeend=datetime.datetime.now()+datetime.timedelta(seconds=time_sec)
          timeend=str(timeend)
          timeend=timeend[11:]
          timeend=timeend[:8]
          end_time_label_var.set(timeend)
          #print("test:")
          #print(timeend)



   except:
        input_invalid=False
        messagebox.showinfo("Invalid Input", "Please input the right value")
        return

   datetimeStart=datetime.datetime.now().strftime("%H:%M:%S")
   
   if timer_paused==False:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        time_sec=temp

   if timer_paused==True:
      timeend=datetime.datetime.now()+datetime.timedelta(seconds=time_sec)
      timeend=str(timeend)
      timeend=timeend[11:]
      timeend=timeend[:8]
      end_time_label_var.set(timeend)
      

   flag=False
   get = recentListBox.curselection()
   for i in get:
    flag=True
    #print(recentListBox.get(i))
    if recentListBox.get(i)!="":
        study=recentListBox.get(i)
    
   get = listbox.curselection()
   for i in get:
    flag=True
    if listbox.get(i)!="":
        study=listbox.get(i)

   #what we are studing
   print("To study:"+study)
   Studing_label_var.set(study) 

   if flag==False:
    messagebox.showinfo("Warning", "You didnt choose what to study")
    return

   timer_paused=False
   timer_started=True 
   hourEntry.config(state="readonly")
   minuteEntry.config(state="readonly")
   secondEntry.config(state="readonly") 
   start.config(state="disabled")
  # SetTimeCountdown.config(state="disabled")
   pause1.config(state="enable")
   stop.config(state="enable")
   running = True
   #Ms_DataBase.DataBase_print_all()
    #Ms_DataBase


def Set_Time_Countdown():
    global FirstTimeHour
    global FirstTimeMin
    global FirstTimeSec
    global time_sec
    try:
        # the input provided by the user is
        # stored in here 
         FirstTimeHour=int(hour.get())
         FirstTimeMin=int(minute.get())
         FirstTimeSec=int(second.get())

         hour.set("{0:2d}".format(FirstTimeHour))
         minute.set("{0:2d}".format(FirstTimeMin))
         second.set("{0:2d}".format(FirstTimeSec))
      
         start.config(state="enabled") #after setting the times
         time_sec=FirstTimeHour*60*60
         time_sec+=FirstTimeMin*60
         time_sec+=FirstTimeSec
         print("time_sec:"+str(time_sec)) 
    except:
        input_invalid=False
        messagebox.showinfo("Invalid Input", "Please input the right value")
        return
    pass

# Define a function to stop the loop
def on_stop():
   global running
   running = False

   global FirstTimeHour
   global FirstTimeMin
   global FirstTimeSec
   global timer_is_up
   global timer_started
   global timer_paused
   global end_time_label_var
   global start_time_label_var
   

   start_time_label_var.set("")
   end_time_label_var.set("")

   
   hourEntry.config(state="normal")
   minuteEntry.config(state="normal")
   secondEntry.config(state="normal") 
   print("timer_is_up:"+str(timer_is_up))
   print("timer_started:"+str(timer_started))

   if timer_is_up==False and timer_started==True:
       answer_msg_box=messagebox.askquestion("Confirm","To update the database?")
       if answer_msg_box=='yes':
        remin_to_study_sec = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        was_time_sec=int(FirstTimeHour)*3600 + int(FirstTimeMin)*60 + int(FirstTimeSec)
        print("Choosed yes")
        study_time_sec=was_time_sec-remin_to_study_sec
        print("stduying:"+study)
        p=Ms_DataBase.get_ID_subject(study)
        print(p)
        if len(p)>0:
            Ms_DataBase.DataBase_insert(p[0],datetimeStart,study,study_time_sec)

        ##last study
        first_name_list=Ms_DataBase.selectFirstRow()
        learned=functions.func(first_name_list)
        last_study_label_var.set(learned)

        ###today
        times_sec=Ms_DataBase.selectTimeBYSecAndDate()
        st=str(datetime.timedelta(seconds=times_sec))
        lerned_today_label_var.set(st)

        ###week
        studied_this_week_by_sec=Ms_DataBase.selectTimeBYSecAndDateWeek()
        studied_this_week_by_sec_str=str(datetime.timedelta(seconds=studied_this_week_by_sec))
        last_week_label_var.set(studied_this_week_by_sec_str)

        ###month
        studied_this_month_by_sec=Ms_DataBase.selectTimeBYSecAndDateMonth()
        studied_this_month_by_sec_str=str(datetime.timedelta(seconds=studied_this_month_by_sec))
        last_month_label_var.set(studied_this_month_by_sec_str)

        ###year
        studied_this_year_by_sec=Ms_DataBase.selectTimeBYSecAndDateYear()
        studied_this_year_by_sec_str=str(datetime.timedelta(seconds=studied_this_year_by_sec))
        last_year_label_var.set(studied_this_year_by_sec_str)

        ###all the time
        studied_all_time=Ms_DataBase.selectTimeBYSecAndDateAll_Time()
        studied_all_time=str(datetime.timedelta(seconds=studied_all_time))
        studied_all_time_label_var.set(studied_all_time)

            ##### inseting form ms database recet 3 subjects in listbox
        recent_list=Ms_DataBase.DataBase_Select_First_three_Subjects()
        recent_list=functions.remove_symbols_from_list(recent_list)

        recentListBox.delete(0,END)
        counter=0
        for i in recent_list:
            #adding widget to Tab
            counter+=1
            recentListBox.insert(counter, i)
        ############ done#########

   timer_paused=False
   hour.set("{00:2d}".format(FirstTimeHour))
   minute.set("{00:2d}".format(FirstTimeMin))
   second.set("{00:2d}".format(FirstTimeSec))
   start.config(state="enabled") #after setting the times 
   #SetTimeCountdown.config(state="enabled")
   stop.config(state="disable")
   pause1.config(state="disable")
   emptyFunc()


def on_pause():
    global running
    running = False
    global timer_paused

    timer_paused=True

    hourEntry.config(state="readonly")
    minuteEntry.config(state="readonly")
    secondEntry.config(state="readonly") 
    start.config(state="enabled")

    end_time_label_var.set("")
   # SetTimeCountdown.config(state="enabled")

#gets by minutes
def set_min_by_button(btn_min):

    if btn_min<60:
        hour.set("{0:2d}".format(0))
        minute.set("{0:2d}".format(btn_min))
        second.set("{0:2d}".format(0))
    else:
        hour.set("{0:2d}".format(1))
        minute.set("{0:2d}".format(0))
        second.set("{0:2d}".format(0))    

    pass


canvas = Canvas(win, bg="skyblue3", width=600, height=60)
canvas.create_text(150, 10, text="Click the Start/Stop to execute the Code", font=('', 13))
canvas.pack()


hour=StringVar()
minute=StringVar()
second=StringVar()

  
# setting the default value as 0



hour.set("00")
minute.set("00")
second.set("00")


# Use of Entry class to take input from the user
hourEntry= Entry(win, width=3, font=("Arial",18,""),
                 textvariable=hour)
hourEntry.place(x=80,y=100)

minuteEntry= Entry(win, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=130,y=100)
  
secondEntry= Entry(win, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=180,y=100)

###labels to show started time and end time
start_time_static_label=Label(win,text="Start time:",relief=FLAT)
start_time_static_label.place(x=70,y=150)

start_time_label_var = StringVar()
start_time_label = Label( win,textvariable=start_time_label_var,bd=1,relief=FLAT,font=("Arial",14,""))
start_time_label.place(x=130,y=150)

end_time_static_label=Label(win,text="End time:",relief=FLAT)
end_time_static_label.place(x=70,y=180)

end_time_label_var = StringVar()
end_time_label = Label( win,textvariable=end_time_label_var,bd=1,relief=FLAT,font=("Arial",14,""))
end_time_label.place(x=130,y=180)



###### Add a Button to start/stop the loop#########
start = ttk.Button(win, text="Start", command=on_start)
start.place(x=250,y=70)


#SetTimeCountdown = ttk.Button(win, text="Set Time Countdown", command=Set_Time_Countdown)
#SetTimeCountdown.place(x=250,y=90)

stop = ttk.Button(win, text="Stop", command=on_stop)
stop.place(x=250,y=110)

pause1 = ttk.Button(win, text="pause", command=on_pause)
pause1.place(x=250,y=150)


#add labels
Goal_Today=Label(win,text="Goal Today",relief=FLAT)
Goal_Today.place(x=120,y=60)

label_hour = Label( win,text="H",relief=FLAT)
label_hour.place(x=90,y=80)

label_min = Label( win,text="M",relief=FLAT)
label_min.place(x=140,y=80)

label_sec = Label( win,text="S",relief=FLAT)
label_sec.place(x=190,y=80)

btn_5min = ttk.Button(win, text="Set 5min", command=lambda: set_min_by_button(5))
btn_5min.place(x=100,y=220)

btn_10min = ttk.Button(win, text="Set 10min", command=lambda: set_min_by_button(10))
btn_10min.place(x=100,y=250)

btn_15min = ttk.Button(win, text="Set 15min", command=lambda: set_min_by_button(15))
btn_15min.place(x=100,y=280)

btn_20min = ttk.Button(win, text="Set 20min", command=lambda: set_min_by_button(20))
btn_20min.place(x=100,y=310)

btn_25min = ttk.Button(win, text="Set 25min", command=lambda: set_min_by_button(25))
btn_25min.place(x=100,y=340)

btn_30min = ttk.Button(win, text="Set 30min", command=lambda: set_min_by_button(30))
btn_30min.place(x=100,y=370)

btn_45min = ttk.Button(win, text="Set 45min", command=lambda: set_min_by_button(45))
btn_45min.place(x=100,y=400)

btn_1hour = ttk.Button(win, text="Set 1hour", command=lambda: set_min_by_button(60))
btn_1hour.place(x=100,y=430)

####################Done###########




# ListBox for all the subjects
subjects_Label = Label( win,text="All the subjects",relief=FLAT)
subjects_Label.place(x=350,y=180)

listbox = Listbox(win, width=35, height=8)
listbox.place(x=350,y=200)

list_all_study=Ms_DataBase.selectALLFromSubjects()
#list_all_study=functions.remove_symbols_from_list(list_all_study)

#File_handler.fileRead()
counter=0
for i in list_all_study:
    #adding widget to Tab
    counter+=1
    listbox.insert(counter, i)


# ListBox for 3 recent subjects
recent_subjects = Label( win,text="Recent subjects",relief=FLAT)
recent_subjects.place(x=250,y=180)

recentListBox = Listbox(win, width=12, height=8)
recentListBox.place(x=250,y=200)


##### inseting form ms database recet 3 subjects in listbox
recent_list=Ms_DataBase.DataBase_Select_First_three_Subjects()
#recent_list=functions.remove_symbols_from_list(recent_list)

for i in recent_list:
    #adding widget to Tab
    counter+=1
    recentListBox.insert(counter, i)
############ done#########

btn0 = Button(win, text="Print", command=printItemFromList)
btn0.place(x=350,y=350)


btn1 = Button(win, text="Add New Item", command=addItemToTheList)
btn1.place(x=400,y=350)

#StringVar
add_item_to_list=StringVar()
add_item_to_list.set("")
add_To_List= Entry(win, width=10, font=("Arial",18,""),
                 textvariable=add_item_to_list)
add_To_List.place(x=375,y=400)

btn2 = Button(win, text="Delete", command=deleteItemFromList)
btn2.place(x=500,y=350)


#what do you study now
study_now_label = Label( win,text="Studing:",bd=2,relief=FLAT,font=("Arial",14,""))
study_now_label.place(x=700,y=90)

Studing_label_var = StringVar()
Studing_label = Label( win,textvariable=Studing_label_var,bd=2,relief=FLAT,font=("Arial",14,""))
Studing_label.place(x=770,y=90)

#last study
last_study_static_label = Label( win,text="Last Studied:",bd=2,relief=FLAT,font=("Arial",14,""))
last_study_static_label.place(x=700,y=120)

last_study_label_var = StringVar()
last_study_label = Label( win,textvariable=last_study_label_var,bd=2,relief=FLAT,font=("Arial",14,""))
last_study_label.place(x=820,y=120)


######## from data base to the program making from data a last studieed
first_name_list=Ms_DataBase.selectFirstRow()
learned=functions.func(first_name_list)
last_study_label_var.set(learned)

##########Done#######################


#####sum of today lerned###
last_study_static_label = Label( win,text="Learned today:",bd=2,relief=FLAT,font=("Arial",14,""))
last_study_static_label.place(x=700,y=150)

lerned_today_label_var = StringVar()
lerned_today_label = Label( win,textvariable=lerned_today_label_var,bd=2,relief=FLAT,font=("Arial",14,""))
lerned_today_label.place(x=890,y=150)

##########Done#######################


####sum of week i studied####
last_week_static_label = Label( win,text="Learned this week:",bd=2,relief=FLAT,font=("Arial",14,""))
last_week_static_label.place(x=700,y=180)

last_week_label_var = StringVar()
last_week_label = Label( win,textvariable=last_week_label_var,bd=2,relief=FLAT,font=("Arial",14,""))
last_week_label.place(x=890,y=180)


##########Done#######################

####sum of month i studied####
last_month_static_label = Label( win,text="Learned this month:",bd=2,relief=FLAT,font=("Arial",14,""))
last_month_static_label.place(x=700,y=210)

last_month_label_var = StringVar()
last_month_label = Label( win,textvariable=last_month_label_var,bd=2,relief=FLAT,font=("Arial",14,""))
last_month_label.place(x=890,y=210)


####sum of year i studied####
last_year_static_label = Label( win,text="Learned this year:",bd=2,relief=FLAT,font=("Arial",14,""))
last_year_static_label.place(x=700,y=240)

last_year_label_var = StringVar()
last_year_label = Label( win,textvariable=last_year_label_var,bd=2,relief=FLAT,font=("Arial",14,""))
last_year_label.place(x=890,y=240)

#all time study

all_time_static_label = Label( win,text="Learned all time:",bd=2,relief=FLAT,font=("Arial",14,""))
all_time_static_label.place(x=700,y=270)

studied_all_time_label_var = StringVar()
all_time_label = Label( win,textvariable=studied_all_time_label_var,bd=2,relief=FLAT,font=("Arial",14,""))
all_time_label.place(x=890,y=270)

##get time make it str

##today learned subjects by sec and name and date labels

week_last_sub_name_static1=Label( win,text="Week subject1:",bd=2,relief=FLAT,font=("Arial",14,"")) 
week_last_sub_name_static1.place(x=700,y=400)

week_sub_name_var1 = StringVar()
week_sub_name_label1 = Label( win,textvariable=week_sub_name_var1,bd=2,relief=FLAT,font=("Arial",14,""))
week_sub_name_label1.place(x=840,y=400)


week_last_sub_name_static2=Label( win,text="Week subject2:",bd=2,relief=FLAT,font=("Arial",14,"")) 
week_last_sub_name_static2.place(x=700,y=430)

week_sub_name_var2 = StringVar()
week_sub_name_label2 = Label( win,textvariable=week_sub_name_var2,bd=2,relief=FLAT,font=("Arial",14,""))
week_sub_name_label2.place(x=840,y=430)


week_last_sub_name_static3=Label( win,text="Week subject3:",bd=2,relief=FLAT,font=("Arial",14,"")) 
week_last_sub_name_static3.place(x=700,y=460)

week_sub_name_var3 = StringVar()
week_sub_name_label3 = Label( win,textvariable=week_sub_name_var3,bd=2,relief=FLAT,font=("Arial",14,""))
week_sub_name_label3.place(x=840,y=460)


#########done############   
sumPassedTime=Ms_DataBase.selectTimePassedRow()

#for i in sumPassedTime:
 #   sum+=i

new_list = []

for item in sumPassedTime:
    new_item = str(item)
    new_list.append(new_item)
  
new_list=functions.remove_symbols_from_list(new_list)

####gets seconds from ms data makes to h/m/s
lise1=Ms_DataBase.selectTimeBYSec()
sum1=0
for i in lise1:
    try:
        sum1+=(i[0])
    except:
        print("no")    

print(sum1)
sum=3600
print(str(datetime.timedelta(seconds=sum)))




#timenow=datetime.datetime.now().strftime("%H:%M:%S")
#print("new Time:"+str(timenow))


stop.config(state="disable")
pause1.config(state="disable")


###today
times_sec=Ms_DataBase.selectTimeBYSecAndDate()
st=str(datetime.timedelta(seconds=times_sec))
lerned_today_label_var.set(st)

###week
studied_this_week_by_sec=Ms_DataBase.selectTimeBYSecAndDateWeek()
studied_this_week_by_sec_str=str(datetime.timedelta(seconds=studied_this_week_by_sec))
last_week_label_var.set(studied_this_week_by_sec_str)

###month
studied_this_month_by_sec=Ms_DataBase.selectTimeBYSecAndDateMonth()
studied_this_month_by_sec_str=str(datetime.timedelta(seconds=studied_this_month_by_sec))
last_month_label_var.set(studied_this_month_by_sec_str)

###year
studied_this_year_by_sec=Ms_DataBase.selectTimeBYSecAndDateYear()
studied_this_year_by_sec_str=str(datetime.timedelta(seconds=studied_this_year_by_sec))
last_year_label_var.set(studied_this_year_by_sec_str)

###all the time
studied_all_time=Ms_DataBase.selectTimeBYSecAndDateAll_Time()
studied_all_time=str(datetime.timedelta(seconds=studied_all_time))
studied_all_time_label_var.set(studied_all_time)


####studied today seconds remember for countdown
last_study_time_sec=Ms_DataBase.selectTimeBYSecToday()
last_study_time_min, last_study_time_sec = divmod(last_study_time_sec, 60)
last_study_time_hour, last_study_time_min = divmod(last_study_time_min, 60)

hour.set(last_study_time_hour)
minute.set(last_study_time_min)
second.set(last_study_time_sec)

FirstTimeHour=last_study_time_hour
FirstTimeMin=last_study_time_min
FirstTimeSec=last_study_time_sec

##geting from ms_database all today learned subjects by sec and name and date  
recent_3_subs_names,recent_3_subs_secs=Ms_DataBase.DataBase_Select_First_three_Subjects_all_info()

recnt_names,recntsecs=functions.selectThreeSubsFromSameWeek(recent_3_subs_secs,recent_3_subs_names)

count=0
recent_3_subs=""

for i in recnt_names:
    if count==0:
        recent_3_subs=str(datetime.timedelta(seconds=recntsecs[count]))
        week_sub_name_var1.set(i+"  "+recent_3_subs)
    if count==1:
        recent_3_subs=str(datetime.timedelta(seconds=recntsecs[count]))
        week_sub_name_var2.set(i+"  "+recent_3_subs)  
    if count==2:
        recent_3_subs=str(datetime.timedelta(seconds=recntsecs[count]))
        week_sub_name_var3.set(i+"  "+recent_3_subs)    
    count+=1





#print(recent_3_subs_names)
#print(recent_3_subs_secs)



# Run a function to print text in window
win.after(1000, print_text)

win.mainloop()