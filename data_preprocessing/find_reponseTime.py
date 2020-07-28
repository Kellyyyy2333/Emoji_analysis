# Give PR comments with emoji usage, for each comment, find how much time it
# takes for this comment to get a response.
#
# INPUT: PR_withEmoji_Labeled.txt,cleaned_pull_request_comments.txt
#
# OUTPUT: PR_response_time.txt
#

from utilities import find_full_comment
from utilities import get_time_list
from utilities import get_time_diff
from textblob import TextBlob


file = open('PR_withEmoji_Labeled.txt','r')
full_file = open('./data_preprocessing/cleaned_pull_request_comments.txt', 'r')


result_file = open('PR_response_time.txt','w')

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
    next_order = sorted_list.index(current_time) + 1
    
    if next_order <= len(sorted_list)-1:
        next_time = sorted_list[next_order]

        res_time = get_time_diff(current_time,next_time)
        senti_score = round(TextBlob(current_list[4]).sentiment.polarity, 3)
        


        result_str = f'{comments_with_emoji_list[i][:-1]}\t|\t{senti_score}\t|\t{res_time}\n'
        print()
        print(result_str)
        result_file.write(result_str)
        print('finish')



file.close()
full_file.close()
result_file.close()
    
    
    










    
