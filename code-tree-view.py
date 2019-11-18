# Get the number of spaces at the beginning of each line in the code 
def space_number(symbolString):
    index = 0
    while index < len(symbolString):
        if symbolString[index] != ' ':
            return(len(symbolString[0:index]))
            break
        index += 1


# Read the code in
def read_file(file_path):
    f = open(file_path, 'r')  
    code = f.read().split('\n')
    code_in_str_list = []
    for elem in code:
        if elem != '':
            code_in_str_list.append(elem)
    return code_in_str_list


# Get the name and the level of each function or class in the code
def get_level_name(code_in_str_list):
    function_name = []
    function_level = []
    for elem in code_in_str_list:
        index = 0
        while index < len(elem):
            symbol = elem[index]
            if symbol == ' ':
                space = index
            elif symbol == '(':
                if elem[0] != ' ':
                    function_name.append(elem[space + 1:index])
                    function_level.append(0)
                else:
                    function_name.append(elem[space + 1:index])
                    function_level.append(int(space_number(elem) / 4))
            index += 1
    return function_level, function_name