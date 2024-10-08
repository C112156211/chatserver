import json
import csv

# 讀取 JSON 檔案
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# 確定 JSON 資料是列表
if isinstance(data, list):
    # 取得 CSV 欄位名稱
    keys = data[0].keys()

    # 寫入 CSV 檔案
    with open('data.csv', 'w', newline='', encoding='utf-8') as csv_file:
        dict_writer = csv.DictWriter(csv_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
else:
    print("JSON 資料格式不正確，應該是列表格式。")# chatserver
