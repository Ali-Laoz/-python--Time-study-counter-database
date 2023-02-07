
import datetime 

def Convert(string):
    li = list(string.split(" "))
    return li

def remove_symbols_from_list(list1):
    # take list
# initializing special characters
    special_char = '@_!#$%^&*()<>?/\|}{~:;.[]'
 
# using join() + generator to remove special characters
    out_list = [''.join(x for x in string if not x in special_char) for string in list1]
 
# print list without special characters
    return out_list


#remove_symbols_from_list1 with spicific change
def remove_symbols_from_list1(list1):
    # take list
# initializing special characters
    special_char = '@_!#$%^&*()<>?/\|}{~;.[]'
 
# using join() + generator to remove special characters
    out_list = [''.join(x for x in string if not x in special_char) for string in list1]
 
# print list without special characters
    return out_list



#### from data base row of list name date time1,time2,seconds### make
def func(list):

    last_passed_sec=""
    last_name=""
    last_Date=""
    last_time1=""
    last_time2=""
    learned=""
    count=0
    if len(list)>0:
        last_name=list[2]
        last_Date=list[3]
        last_time1=list[4]
        last_time2=list[5]
        last_passed_sec=list[6]

    last_time1=str(last_time1)
    last_time1=last_time1[10:]

    last_time2=str(last_time2)
    last_time2=last_time2[10:]

    last_Date=str(last_Date)
    last_Date=last_Date[:10]

    last_passed_sec=str(datetime.timedelta(seconds=last_passed_sec))

    last_name = last_name.strip()

    learned=learned+str(last_name)
    learned=learned+" "
    learned=learned+str(last_Date)
    learned=learned+" "
    learned=learned+str(last_time1)
    learned=learned+" "
    learned=learned+str(last_time2)
    learned=learned+" "   
    learned=learned+str(last_passed_sec)
    return learned





def same_week(dateString):
    '''returns true if a dateString in %Y%m%d format is part of the current week'''
    d1 = datetime.datetime.strptime(dateString,'%Y%m%d')
    d2 = datetime.datetime.today()
    return d1.isocalendar()[1] == d2.isocalendar()[1] \
              and d1.year == d2.year



def selectThreeSubsFromSameWeek(list1_secs,list2_names):
    recent_names=[]
    recnet_secs=[]
    sec_list=[]
    count=0
    element_count=0
    
    for name in list2_names:
       # print(name)
        if count==0:
           recent_names.append(name)
           recnet_secs.append(0)
           count+=1
           continue 


        element_count=len(recent_names)
        if name not in recent_names and element_count<3:
            recent_names.append(name)
            recnet_secs.append(0)


        count+=1

    recnet_secs,sum_sec_by_name(recent_names,recnet_secs,list2_names,list1_secs)
    return recent_names,recnet_secs    
    pass





def sum_sec_by_name(recnt_name,recent_sec,list_names,list_secs):
    count_list_names_small=0
    for name in recnt_name:
        count_list_names_big=0
        for i in list_names:
            
            if name==list_names[count_list_names_big]:
                recent_sec[count_list_names_small]+=list_secs[count_list_names_big]

            count_list_names_big+=1
        count_list_names_small+=1        
           
    pass


    return recent_sec
    pass


   # recnt_list1=[]
  
   # count=0
   # element_count=0
   # for row,id in cursor.fetchall():
   #     if count==0:
   #        recnt_list1.append(row)
           
   #        count+=1
   #        continue

   #    element_count=len(recnt_list1)        
   #     if row not in recnt_list1 and element_count<3:
   #         recnt_list1.append(row)
            
   #     count+=1       
   
   # return recnt_list1