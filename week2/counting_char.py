input_string = input()
string_set = []

def counting_char(input_string):
    for i in input_string:
        if i in string_set:
            continue
        else:
            string_set.append(i)            
    my_dict = {string_set[i]:input_string.count(string_set[i]) for i in range(len(string_set))}
    return my_dict   
  
print(counting_char(input_string))