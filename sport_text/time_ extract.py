import re
import json
import os
import pandas as pd

from bert_score import score

# file = open(r"C:\Users\10423\Desktop\learn_pytorch\sport_text\sport_data\train\bundesliga_0000\news_result.txt",encoding="utf8")
# line = file.readline()
# file1 = open(r"C:\Users\10423\Desktop\learn_pytorch\sport_text\sport_data\train\bundesliga_0000\live.txt",encoding="utf8")
# line1 = file1.readline()
# while line and line1 :
#     print(line,end = '')
#     P, R, F1 = score(line,line1, lang="zh", verbose=True)
#     print(f"{F1.mean():.3f}")
#     line = file.readline()
#     line1 = file1.readline()

with open(r"C:\Users\10423\Desktop\learn_pytorch\sport_text\sport_data\train\bundesliga_0000\news_result.txt", encoding="utf8") as f:
    cands = [line.strip() for line in f]

with open(r"C:\Users\10423\Desktop\learn_pytorch\sport_text\sport_data\train\bundesliga_0000\live.txt",encoding="utf8") as f:
    refs = [line.strip() for line in f]

new_cands = []
for i in range(8):
    new_cands.append(cands[i])
print(new_cands)
new_refs = []
for j in range(8):
    new_refs.append(refs[j])
P, R, F1 = score(new_cands, new_refs, lang="zh", verbose=True)
print(f"System level F1 score: {F1.mean():.3f}")

# data
# cands = ['我们都曾经年轻过']
# refs = ['虽然我们都年少，但还是懂事的']
#
# P, R, F1 = score(cands, refs, lang="zh", verbose=True)
#
# print(f"System level F1 score: {F1.mean():.3f}")

