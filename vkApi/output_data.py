import os
import csv
import json


def output_data(data: list, id_user: int, extension: str, path: str):
    if os.path.exists(path):
        if extension == '.json':
            with open(f"{path}\{id_user}{extension}", 'w', encoding="utf-8") as f:
                                f.write(json.dumps(data, ensure_ascii=False))
        elif extension == '.csv':
            columns = list(data[0])

            with open(f"{path}\{id_user}{extension}", 'w', encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=columns)
                writer.writeheader() 
                for row in data:
                    writer.writerow(row)
        elif extension == '.tsv':
            columns = list(data[0])
            
            with open(f"{path}\{id_user}{extension}", 'w', encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=columns, delimiter=" ")
                writer.writeheader() 
                for row in data:
                    writer.writerow(row)
        else:
            print('Incorrect file extension')
            return 1
    else:
        print('Incorrect file path')
        return 1