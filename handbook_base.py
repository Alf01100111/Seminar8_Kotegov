from datetime import datetime as dt

def get_storage(data):
    with open('handbook.txt', 'a', encoding="utf-8") as file:
        file.write(f'**{data}**\n')

def get_base():
    with open('handbook.txt', 'r', encoding="utf-8") as file:     
        return file.readlines()

        
def del_data(id, handbook):    
    handbook = [handbook[i] for i in range(len(handbook)) if handbook[i][1] != id]
    '**'.join(handbook)
    with open('handbook.txt', 'w', encoding="utf-8") as file:
        file.write(f'**{handbook}**\n')