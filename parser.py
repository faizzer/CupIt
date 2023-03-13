import pandas as pd    

jsonObj = pd.read_json(path_or_buf="data/ranking_test.jsonl", lines=True)

for i in range(0,5):
    print(jsonObj['comments'][0][i]['text'], jsonObj['comments'][0][i]['score'])
    print('\n')