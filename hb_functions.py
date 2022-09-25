def new_data(id, surname, name, phone_number):
    new_str = [id, surname, name, phone_number]    
    return '**'.join(new_str)

def new_id(handbook):
    id_temp = [handbook[i][1] for i in range(len(handbook))]
    id_list = tuple(map(int, id_temp))
    return str(max(id_list) + 1)

def read_base(handbook):
    handbook = [handbook[i][:-1] for i in range(len(handbook))]
    handbook = [handbook[i].split('**') for i in range(len(handbook))]
    # handbook = [handbook[i].remove('') for i in range(len(handbook))]
    return handbook

def find(surname, handbook):
    surname_list = [handbook[i] for i in range(len(handbook)) if handbook[i][2] == surname]
    return surname_list
