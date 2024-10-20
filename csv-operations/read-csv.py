import csv

with open("csv-operations/csv-files/products.csv") as file:
    # print(file.read())
    # Okunan veriyi bir object yapabilmek ve object e ait özellikleri kullanabilmek için 
    # csv kütüphanesi kullanılır
    csv_reader = csv.reader(file)
    # print(csv_reader)

    # başlıklar görünmesin istersek next i kullanabiliriz
    next(csv_reader)
    for p in csv_reader:
        # print(p)
        # print(p[0], p[1])
        review = float(p[4])
        if review >= 4.5:
            print(p[0])