import join
import routine
import timings
import schedule
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    executable_path='C:\\Drivers\\Chrome\\chromedriver.exe'
)

time = datetime.datetime.now()
day = (time.strftime("%d"))

def sunday():
    schedule.every.sunday.at(1st_class).do(join_mat120)
    schedule.every.sunday.at(2nd_class).do(join_cse111)

def monday():
    schedule.every.sunday.at(1st_class).do(join_mat120)
    schedule.every.sunday.at(2nd_class).do(join_bio101)
    schedule.every.sunday.at(3rd_class).do(join_cse230)

def tuesday():
    schedule.every.sunday.at(2nd_class).do(join_cse230)

def wednesday():
    schedule.every.sunday.at(1st_class).do(join_mat120)
    schedule.every.sunday.at(2nd_class).do(join_bio101)
    schedule.every.sunday.at(3rd_class).do(join_cse230)

def thursday():
    schedule.every.sunday.at(lab).do(join_lab)


if day == "Sun":
    sunday()
elif day == "Mon":
    monday()
elif day == "Tue":
    tuesday()
elif day == "Wed":
    wednesday()
elif day == "Thu":
    thursday()
else:
    print("It's off day yaaaaasssssss!!!!!")
