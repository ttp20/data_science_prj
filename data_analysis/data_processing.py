from unicode import UNICODE
from one_row_processing import write_info

SUBJECTS = {
    'toán': 'math',
    'vật lí': 'physics',
    'hóa học': 'chemistry',
    'tiếng anh': 'english',
    'sinh học': 'biology',
    'ngữ văn': 'literature',
    'lịch sử': 'history',
    'địa lí': 'geography',
    'gdcd': 'civic education',
    'khtn': 'natural science',
    'khxh': 'social science',
}

def remove_tags(html_str):
    tags = []

    for i in range(len(html_str)):
        if html_str[i] == "<":
            begin = i
        if html_str[i] == ">":
            end = i
            tags.append(html_str[begin:end+1])

    for tag in tags:
        html_str = html_str.replace(tag, "")

    return html_str

# print(all_data[0])
# print(type(all_data))

file = open('clean_data.csv', encoding="utf8", mode="w")
file.write("name" + ",")
file.write("dob" + ",")
for key, value in SUBJECTS.items():
    file.write(value + ",")
file.write("\n")


file = open('raw_data.txt', 'r')
all_data = file.read().split("\n")
id = 0

for i in range(len(all_data)):
    try:
        write_info(all_data[i].split("\\n"))
    except:
        print(i)
        continue


