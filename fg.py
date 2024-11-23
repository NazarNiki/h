import json
directory_path  = "./directory/"
# Загрузка данных из JSON файла
def remove_duples(file_name,directory_path):

    #file_name='German.json'
    print(file_name)
    print(directory_path+file_name)
    with open(directory_path+file_name, 'r', encoding='utf-8') as file:
        data = json.loads(file)

    # Remove duplicates using a set of tuples
        unique_data = list({frozenset(item.items()): item for item in data}.values())

        # Convert back to JSON
        unique_json = json.dumps(unique_data, indent=4)
    # Writing to sample.json
        with open(directory_path+file_name, "w") as outfile:
            outfile.write(unique_json)

'''   try:
  hj = frozenset(dhg)
    except TypeError:
        print("no")
        hj = frozenset()  

        ol = len(hj)
        print(file_name)
    #with open(directory_path+file_name, 'w', encoding='utf-8') as unique_file:
     #   json.dump(list(hj), unique_file, ensure_ascii=False,)
    
    print('Столько стало')
    print(ol)
#remove_duples(file_name='German.json')
'''