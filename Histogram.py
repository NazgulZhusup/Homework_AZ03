import csv
import matplotlib.pyplot as plt

input_filename = 'divan_prices.csv'
output_filename = 'processed_divan_prices.csv'


prices = []
with open(input_filename, newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    headers = next(reader)
    for row in reader:

        price = int(row[0].replace('руб.', '').replace(',', '').strip())
        prices.append(price)

with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)
    for price in prices:
        writer.writerow([price])

plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, edgecolor='black')
plt.title('Распределение цен на диваны')
plt.xlabel('Price (руб.)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
