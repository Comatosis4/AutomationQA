import csv

def unic_csv(input_file, output_file):
    seen = set()
    unic_rows = []

    with open(input_file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            row_tuple = tuple(row)

            if row_tuple not in seen:
                seen.add(row_tuple)
                unic_rows.append(row)

    with open(input_file, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(unic_rows)


unic_csv('random.csv', 'result_Cherniai.csv')