<br />Extract two columns(stageInfor,label) for graph plotting.
<br />  extract_stageInfor_with_label.py
<br />  |
<br />  |INPUT
<br />  -- PR_withEmoji_StageInfo.txt 
<br />  | 
<br />  |OUTPUT
<br />  -- stageInfor_withLabel.txt
<br />
<br />From all PR comment with emoji usage associated with their stage information, extract the comment with the first emoji usage within all PRs.
<br />  find_first_stage.py
<br />  |
<br />  |INPUT
<br />  -- PR_withEmoji_StageInfo.txt 
<br />  | 
<br />  |OUTPUT
<br />  -- PR_firstUsage_StageInfo.txt
<br />
<br />Give PR comments with emoji usage, for each comment, find the order of this message within its whole PR conversation; based on the total number of messages in this PR, return the stage percentage calculated by order/#total * 100.
<br />  find_order.py
<br />  |
<br />  |INPUT
<br />  -- PR_withEmoji_Labeled.txt, cleaned_pull_request_comments.txt
<br />  | 
<br />  |OUTPUT
<br />  -- PR_withEmoji_StageInfo.txt
<br />
<br />Give PR comments with emoji usage, for each comment, find how much time it takes for this comment to get a response.
<br />  find_reponseTime.py
<br />  |
<br />  |INPUT
<br />  -- PR_withEmoji_Labeled.txt, cleaned_pull_request_comments.txt
<br />  | 
<br />  |OUTPUT
<br />  -- PR_response_time.txt
<br />
<br />From all comments with emoji usage, find how the number of emoji usage in one PR associate with the length of this PR (#messages in this PR conversation).
<br />  |
<br />  |INPUT
<br />  -- PR_withEmoji_Labeled.txt, cleaned_pull_request_comments.txt
<br />  | 
<br />  |OUTPUT
<br />  -- PRid_label_numEmoji_Length.txt