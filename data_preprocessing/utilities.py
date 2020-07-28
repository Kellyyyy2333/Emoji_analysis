from emoji import UNICODE_EMOJI
from datetime import datetime

def format_list(line:str) -> list:
    result = line.strip()
    result = result[2:-3]
    result = result.split("\', \'")
    return result
    
def count_emojis(message: str):
    count = 0
    for c in message: 
        if c in UNICODE_EMOJI:
            count += 1
    return count



def find_full_comment(current_comment, full_comment):
    ID = current_comment[0]
    same_id_comment = []
    for i in range(len(full_comment)):
        current_list = full_comment[i].split('\t|\t')
        current_id = current_list[0]
        if current_id == ID:
            same_id_comment.append(current_list)
    return same_id_comment
        
def get_time_list(comment_list):
    time_list = []
    for i in comment_list:
        time_list.append(i[-1][:-1])
    return time_list


def format_list2(line:str) -> list:
    result = line.strip()

    result = result.split(",")
    return result

def get_num_emojis(comment_list):
    count = 0
    for i in comment_list:
        count += count_emojis(i[4])

    return count


def get_time_diff(time1, time2):
    t1 = datetime.strptime(time1,"%Y-%m-%d %H:%M:%S")
    t2 = datetime.strptime(time2,"%Y-%m-%d %H:%M:%S")
    return str(t2-t1)
    





    
