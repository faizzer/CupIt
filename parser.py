import pandas as pd   
from statistics import mean
import funcs

#Load data from jsonl
jsonObj = pd.read_json(path_or_buf="data/ranking_train.jsonl", lines=True)

#initialization
four_score = []
three_score = []
two_score = []
one_score = []
zero_score = []
df = {"text":[], "comments":[], "lem_comments":[], "score":[]}
text_ar = []
comment_ar = []
score_ar = []
lem_com_ar = []

#Writing text, comments, scores into arrays and making them in lowercase
#len(jsonObj)
for i in range(0, 100):
    for j in range(0,5):
        #funcs.lemmatizer(jsonObj['text'][i].lower())
        
        text_ar.append(jsonObj['text'][i].lower())
        comment_ar.append(jsonObj["comments"][i][j]['text'].lower())
        lem_com_ar.append(funcs.lemmatizer(jsonObj["comments"][i][j]['text'].lower()))
        score_ar.append(jsonObj['comments'][i][j]['score'])

#Creating dictionary of values for pandas df
data_dict = {"text":text_ar, "comment":comment_ar, "lem_comments":lem_com_ar, "score":score_ar}

#Creating pandas df
df = pd.DataFrame(data_dict)
f = open("pd.txt", 'a')
f.writelines(['\n', str(df['comment'].to_string()), ' ', str(df['lem_comments'].to_string()), ' '])
f.close()
print(df[::5])