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


# Put functions and classes in the form of tree using dictionary
def layout_code(level_list, function_list):
    
    # Tree each function or class as a member
    members = []
    # Create a basic dictionary (without the value of 'children') for each member 
    for i in range(len(level_list)):
        members.append({
            'level': level_list[i],
            'index': i,
            'name': function_list[i],
            'children': []
        })

    # Group the members by their levels in the code
    lst_levels_indices = []
    for i in range(max(level_list) + 1):
        lst_levels_indices.append(
            [j for j in range(len(level_list)) if level_list[j] == i])

    # Assign 'children' to each member from the bottom up
    for i in reversed(range(len(lst_levels_indices))):
        if i != 0:
            level_indices = lst_levels_indices[i]

            for index in level_indices:
                
                for k in reversed(range(index)):
                    if k in lst_levels_indices[i - 1]:
                        members[k]['children'].append(members[index])
                        break
    # Return the top-most member as the structure of whole family
    return members[0]

file_path = 'code.txt'
code_in_str_list = read_file(file_path)
level_list, function_list = get_level_name(code_in_str_list)
family = layout_code(level_list, function_list)
print(family)
