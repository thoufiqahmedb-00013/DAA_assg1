import csv

def find_ai_in_names(filename):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  
            name_col_index = header.index("Name")  

            matches = []
            for row_num, row in enumerate(reader, start=2):  
                name = row[name_col_index]
                if "ai" in name:
                    cell = f"({row_num}, {name_col_index + 1})"  
                    matches.append(cell)

            if matches:
                print("'ai' in Name column:")
                for cell in matches:
                    print(cell) 
            else:
                print("No names containing 'ai' found.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

find_ai_in_names("student_data.csv")