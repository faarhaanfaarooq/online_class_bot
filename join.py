import timings
import routine
import time

def join_cse111():
    driver.get(cse_111)
    time.sleep(60)
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(4800)
    driver.quit()

def join_mat120():
    driver.get(mat_120)
    time.sleep(60)
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(4800)
    driver.quit()

def join_cse230():
    driver.get(cse_230)
    time.sleep(60)
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(4800)
    driver.quit()

def join_bio101():
    driver.get(bio_101)
    time.sleep(60)
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(4800)
    driver.quit()

def join_lab():
    driver.get(lab)
    time.sleep(60)
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(10800)
    driver.quit()

