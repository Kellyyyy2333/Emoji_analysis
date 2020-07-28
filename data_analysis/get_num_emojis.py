# From all comments with emoji usage, find how the number of emoji
# usage in one PR associate with the length of this PR (#messages
# in this PR conversation).
#
# INPUT: PR_withEmoji.txt,cleaned_pull_request_comments.txt
#
# OUTPUT: PRid_label_numEmoji_Length.txt
#

from utilities import find_full_comment
from utilities import get_time_list
from utilities import get_num_emojis


file = open('PR_withEmoji.txt','r')
full_file = open('./data_preprocessing/cleaned_pull_request_comments.txt', 'r')


result_file = open('PRid_label_numEmoji_Length.txt','w')

comments_with_emoji_list = file.readlines()
full_list = full_file.readlines()

readed_PRid = []

for i in range(0,3594): # Modify the range of data to perform parallel processing
    current_list = comments_with_emoji_list[i].split('\t|\t')
    PRid = current_list[0]

    if PRid not in readed_PRid:
        readed_PRid.append(PRid)
        
        full_comment_list = find_full_comment(current_list,full_list)
        #label = current_list[-1][:-1]

        length = len(full_comment_list)
        num_emoji = get_num_emojis(full_comment_list)
        
        print(f'{i} iteration')
        result_str = f'{PRid}\t|\t{length}\t|\t{num_emoji}\n'
        print()
        print(result_str)
        result_file.write(result_str)
        #print('finish')
    else:
        pass



file.close()
full_file.close()
result_file.close()
    
    
    










    
