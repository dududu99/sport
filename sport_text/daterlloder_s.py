import re
import json
import os
import pandas as pd


# root_dir = "sport_data/train"
# live_dir = "live.json"
# text_path = os.listdir(root_dir)
# for file_path in text_path:
#     print(file_path)
#     path = os.path.join(root_dir, file_path, live_dir)
#     json_file = open(path, "r")
#     item_list1 = json.load(json_file)
#     item_list = item_list1["result"]["data"]
#     sentence_frame = pd.DataFrame(item_list)
#     for index, row in sentence_frame.iterrows():
#         print( row['t'],row['m'])

# numb_dict = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
# e_news_path = os.path.join("sport_data/train/bundesliga_0000/e_news.txt")
# file_e_news = open(e_news_path, "a+", encoding="utf8")
# path = r"C:\Users\10423\Desktop\learn_pytorch\sport_text\sport_data\train\bundesliga_0000\news.txt"
# file = open(path, encoding="utf8")
# mystr = file.read()
# pattern = re.compile('一开场|开场后|开场[\d]+分钟|开始[\d]+分钟|开场[仅][\d]+秒|第[\d]+分钟|[\d]+分钟')
# extract = re.findall(pattern, mystr)
# print(extract)
# file_e_news.write(str(extract) + "\n")

