import csv


def read_inventory(filename):
    clean_data = []

    with open(filename, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        
        for row in reader:

            clean_row = {}

            for key, value in row.items():

                if key is None or value is None:
                    continue

                clean_key = key.replace("\ufeff","").strip()

                clean_value = value.strip()

                clean_row[clean_key] = clean_value

            if clean_row:
                clean_data.append(clean_row)

    return clean_data


data = read_inventory("inventory_raw_3.csv")

print(data)