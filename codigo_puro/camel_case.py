from re import findall


def split_method(string_word):

    list_out = findall('[a-zA-Z][^A-Z]*', string_word)
    
    for x in range(0, len(list_out)):
        list_out[x] = list_out[x].lower()
    
    str_out = ' '.join(list_out)
    return str_out

def combine_method(string_word, type_operation):
    list_out = string_word.split()
    
    if(type_operation == 'M'):
        for x in range(1, len(list_out)):
            list_out[x] = list_out[x][0].upper() + list_out[x][1:]
        list_out.append("()")

    elif(type_operation == 'C'):
        for x in range(0, len(list_out)):
            list_out[x] = list_out[x][0].upper() + list_out[x][1:]

    else:
        for x in range(1, len(list_out)):
            list_out[x] = list_out[x][0].upper() + list_out[x][1:]
    
    string_out = ''.join(list_out)
    
    return string_out

 
string_word = input()

if ')' in string_word:
   string_word = string_word.strip("()")

list_string = string_word.split(';')
if(list_string[0] == 'S'):
    print(split_method(list_string[2]))
if(list_string[0] == 'C'):
    print(combine_method(list_string[2], list_string[1]))

print(string_word)