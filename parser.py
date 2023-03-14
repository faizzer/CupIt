import pandas as pd   
from statistics import mean

#Load data from jsonl
jsonObj = pd.read_json(path_or_buf="data/ranking_train.jsonl", lines=True)

#initialization
four_score = []
three_score = []
two_score = []
one_score = []
zero_score = []
df = {"text":[], "comments":[], "score":[]}
text_ar = []
comment_ar = []
score_ar = []

#Writing text, comments, scores into arrays
for i in range(0, len(jsonObj)):
    for j in range(0,5):
        text_ar.append(jsonObj['text'][i])
        comment_ar.append(jsonObj["comments"][i][j]['text'])
        score_ar.append(jsonObj['comments'][i][j]['score'])

#Creating dictionary of values for pandas df
data_dict = {"text":text_ar, "comment":comment_ar, "score":score_ar}

#Creating pandas df
df = pd.DataFrame(data_dict)

print(df)