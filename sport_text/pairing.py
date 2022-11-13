import os
import re



def write(path, str):
    with open(path, "a+", encoding="utf8") as f:
        f.write(str)

root_dir = r"C:\Users\10423\Desktop\learn_pytorch\sport_text\sports_data"
live_row = "live_row.txt"
news_row = "news_row.txt"
pairing_path = "pair.txt"
text_path = os.listdir(root_dir)

for file_path in text_path:
    live_row_path= os.path.join(root_dir, file_path, live_row)
    live_row_file = open(live_row_path, "r", encoding="utf8")

    news_row_path = os.path.join(root_dir, file_path, news_row)
    news_row_file = open(news_row_path, "r", encoding="utf8")

    pair_path = os.path.join(root_dir, file_path, pairing_path)

    live_clean_lines = live_row_file.read().splitlines()
    news_result_lines = news_row_file.read().splitlines()

    for news_result_line in news_result_lines:
        news_resul_flag = news_result_line.split("'", 1)
        news_time = int(news_resul_flag[0])
        for live_clean_line in live_clean_lines:
            live_line_flag = live_clean_line.split("'", 1)
            live_time = int(live_line_flag[0])
            if live_time >= news_time and live_time <= news_time + 3:
                pairing = live_clean_line + "                   " + news_result_line + "\n"
                print(file_path + "        " + pairing)
                write(pair_path, pairing)



