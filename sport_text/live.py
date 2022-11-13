import json
import os
import re
import pandas as pd

root_dir = r"C:\Users\10423\Desktop\learn_pytorch\sport_text\sports_data"                #根目录
live_dir = "live.json"
text_path = os.listdir(root_dir)              #生成列表：根目录下所有文件名称
for file_path in text_path:                   #遍历根目录下所有文件中live，json
    txt_path = os.path.join(root_dir, file_path, "live.txt")
    file = open(txt_path, "a+", encoding="utf8")
    path = os.path.join(root_dir, file_path, live_dir)
    json_file = open(path, "r")
    item_list1 = json.load(json_file)
    item_list = item_list1["result"]["data"]
    for list1 in item_list:                   #删除属性，只保留时间和评论句子
        list1.pop("id")
        list1.pop("s1")
        list1.pop("s2")
        list1.pop("s")
    item_list.reverse()                       #逆序排列（因为原数据是逆序排列的）
    sentence_frame = pd.DataFrame(item_list)
    sentence_list = list(sentence_frame.iterrows())
    for index, row in sentence_frame.iterrows():
        str = row['t'] + row['m'] + "\n"
        print(file_path + "   " + str)
        file.write(str)
print("OK")


