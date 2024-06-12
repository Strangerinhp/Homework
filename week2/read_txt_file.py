def word_count(word_list, word_set):
  my_dict = {word_set[i]:word_list.count(word_set[i]) for i in range(len(word_set))}
  return my_dict

!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
with open("/content/P1_data.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
raw_list = raw_text.split("\n")
word_list= []
word_set = []
for i in raw_list:
  processed = i.lower()
  line_list = processed.split(" ")
  for j in line_list:
    if j not in word_set:
      word_list.append(j)
      word_set.append(j)
    else:
      word_list.append(j)
word_count(word_list, word_set)