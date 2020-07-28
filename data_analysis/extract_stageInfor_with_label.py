# Extract two columns(stageInfor,label) for graph plotting.
#
# INPUT: PR_withEmoji_StageInfo.txt
#
# OUTPUT: stageInfor_withLabel.txt
#
#

file = open('PR_withEmoji_StageInfo.txt','r')
file_list = file.readlines()

result_file = open('stageInfor_withLabel.txt','w')

for i in range(len(file_list)):
    data_list = file_list[i].split('\t|\t')
    label = data_list[-2]
    stage_infor = data_list[-1][:-1]
    line = f'{label}\t|\t{stage_infor}\n'
    #print(line)
    result_file.write(line)


file.close()
result_file.close()
