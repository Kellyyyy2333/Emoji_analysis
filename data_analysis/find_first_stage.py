
# From all PR comment with emoji usage associated with their stage information, 
# extract the comment with the first emoji usage within all PRs.
#
# INPUT: PR_withEmoji_StageInfo.txt
#
# OUTPUT: PR_firstUsage_StageInfo.txt
#


def find_first_stage(PR_commentList):
    stage = 101.0
    result = ''
    for i in PR_commentList:
        current_stage = float(i.split('\t|\t')[-1].split('|')[-1][:-1])
        if current_stage < stage:
            stage = current_stage
            result = i
    return result
        



file = open('PR_withEmoji_StageInfo.txt','r')
full_list = file.readlines()

full_dict = {}

result_file = open('PR_firstUsage_StageInfo.txt','w')

# Construct full dict
for i in full_list:
    data = i.split('\t|\t')
    PRid = data[0]
    if PRid not in full_dict.keys():
        full_dict[PRid] = [i]
    else:
        full_dict[PRid].append(i)

print('finish construct')
print(len(full_dict))

# find first usage

for PRid in full_dict.keys():
    first_stage = find_first_stage(full_dict[PRid])
    data = first_stage.split('\t|\t')
    string = f'{data[0]}\t|\t{data[1]}\t|\t{data[2]}\t|\t{data[3]}\t|\t{data[4]}\t|\t{data[5]}\t|\t{data[6]}\t|\t{data[-1]}'
    result_file.write(string)

file.close()
result_file.close()
