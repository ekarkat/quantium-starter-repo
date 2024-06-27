import csv

with open('data/daily_sales_data_0.csv', 'r') as csvfile:
    data = csv.DictReader(csvfile)

    with open('newdata.csv', 'w') as newdata:
        fieldnames = ['sales', 'date', 'region']
        csv_write = csv.DictWriter(newdata, fieldnames=fieldnames)
        csv_write.writeheader()

        for line in data:
            if line['product'] == 'pink morsel':
                sales = round((float(line['price'][1:]) * int(line['quantity'])), 2)
                date = line['date']
                region = line['region']
                new_line = {'sales': sales, 'date': date, 'region': region}
                # print(new_line)
                csv_write.writerow(new_line)