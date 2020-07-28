# Give PR comments with emoji usage, for each comment, find the order
# of this message within its whole PR conversation; based on the total
# number of messages in this PR, return the stage percentage calculated
# by order/#total * 100
#
# INPUT: PR_withEmoji_Labeled.txt, cleaned_pull_request_comments.txt
#
# OUTPUT: PR_withEmoji_StageInfo.txt
#

from utilities import find_full_comment
from utilities import get_time_list



file = open('PR_withEmoji_Labeled.txt','r')
full_file = open('./data_preprocessing/cleaned_pull_request_comments.txt', 'r')


result_file = open('PR_withEmoji_StageInfo.txt','w')

comments_with_emoji_list = file.readlines()
full_list = full_file.readlines()

for i in range(0,3594): # Modify the range of data to perform parallel processing
    print(f'{i} iteration')
    current_list = comments_with_emoji_list[i].split('\t|\t')
    full_comment_list = find_full_comment(current_list,full_list)
    #print(full_comment_list)
    
    current_time = current_list[-2]
    full_time_list = get_time_list(full_comment_list)
    
    sorted_list = sorted(full_time_list)
    order = sorted_list.index(current_time) + 1
    full_num = len(sorted_list)
    percentage = round(order/full_num,3) * 100

    result_str = f'{comments_with_emoji_list[i][:-1]}\t|\t{order}|{full_num}|{percentage}\n'
    print()
    print(result_str)
    result_file.write(result_str)
    print('finish')



file.close()
full_file.close()
result_file.close()
    
    
    










    
