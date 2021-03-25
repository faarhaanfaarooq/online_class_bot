
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