from unicode import UNICODE

# list of subjects
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

# column titles
file = open('clean_data.csv', encoding="utf8", mode="w")
file.write("name" + ",")
file.write("dob" + ",")
for key, value in SUBJECTS.items():
    file.write(value + ",")
file.write("\n")

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

file = open('raw_data.txt', 'r')

data = file.readline()
data = data.split("\\n")


def write_info(data):
    for i in range(len(data)):
        data[i] = data[i].replace("\\r", "")
        data[i] = data[i].replace("\\t", "")
        data[i] = remove_tags(data[i])
        data[i] = data[i].strip()

    not_blank_lines = []
    for i in range(len(data)):
        if data[i] != "":
            not_blank_lines.append(data[i])

    if len(not_blank_lines) > 8:
        name = not_blank_lines[7]
        dob = not_blank_lines[8]
        scores = not_blank_lines[9]

    for key, value in UNICODE.items():
        name = name.replace(key, value)
        scores = scores.replace(key, value)

    unicode_deximal_codes_name = []
    unicode_deximal_codes_scores = []

    for i in range(len(name)):
        if name[i] == "&":
            unicode_deximal_codes_name.append(name[i:i+6])


    for code in unicode_deximal_codes_name:
        name = name.replace(code, chr(int(code[2:5])))

    for i in range(len(scores)):
        if scores[i] == "&":
            unicode_deximal_codes_scores.append(scores[i:i+6])


    for code in unicode_deximal_codes_scores:
        scores = scores.replace(code, chr(int(code[2:5])))

    scores = scores.lower()
    scores = scores.replace(":", "")
    scores = scores.replace("khtn ", "khtn   ")
    scores = scores.replace("khxh ", "khxh   ")

    scores_list = scores.split("   ")
    subjects_individual = [scores_list[i] for i in range(len(scores_list)) if i%2==0]
    scores_individual = [scores_list[i] for i in range(len(scores_list)) if i%2==1]

    individual = {}
    for i in range(len(subjects_individual)):
        individual[subjects_individual[i]] = scores_individual[i]

    not_blank_lines = [name, dob, scores]

    name = name.lower()

    file = open('test.txt', encoding="utf8", mode="w")
    for line in not_blank_lines:
        file.write(line + ",")


    file = open('clean_data.csv', encoding="utf8", mode="a")
    file.write(name + ",")
    file.write(dob + ",")
    for key, value in SUBJECTS.items():
        if key in individual.keys():
            file.write(individual[key] + ",")
        else:
            file.write("-1" + ",")
    file.write("\n")

write_info(data)






