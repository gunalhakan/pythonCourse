from csv import DictReader

with open("csv-operations/csv-files/products.csv") as file:
    # Verileri sözlük şeklinde almak için Dictreader kullanılır.
    csv_reader = DictReader(file)
    print(csv_reader)
    for p in csv_reader:
        # print(p)
        print(p["ProductName"],p["Price"])
    