
import datetime 


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
        last_name=list[1]
        last_Date=list[2]
        last_time1=list[3]
        last_time2=list[4]
        last_passed_sec=list[5]

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
