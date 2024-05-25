import csv


input_filename = 'divan_prices.csv'
output_filename = 'processed_divan_prices.csv'

with open(input_filename, newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    headers = next(reader)
    data = []
    for row in reader:

        price = int(row[0].replace('руб.', '').replace(',', '').strip())
        data.append([price])

with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)
    writer.writerows(data)

print(f'Данные успешно обработаны и записаны в {output_filename}.')