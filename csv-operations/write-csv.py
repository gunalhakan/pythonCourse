from csv import writer,reader

# with open("csv-operations/csv-files/cars.csv","w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Marka","Model"])
#     csv_writer.writerow(["Toyota","Auris"])
#     csv_writer.writerow(["Toyota","Corolla"])
#     csv_writer.writerow(["Toyota","Yaris"])

# with open("csv-operations/csv-files/cars.csv","w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerows([
#         ["Marka","Model"],
#         ["Seat","Ibıza"],
#         ["Seat","Leon"]
#     ])
# with open("csv-operations/csv-files/cars.csv","a") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Seat","Cordoba"])

# with open("csv-operations/csv-files/cars.csv") as readFile:
#     csv_reader = reader(readFile)
#     with open("csv-operations/csv-files/new-cars.csv","w") as writeFile:
#         csv_writer = writer(writeFile)
#         for car_row in csv_reader:
#             csv_writer.writerow([c.upper() for c in car_row])

with open("csv-operations/csv-files/products.csv","r+") as file:
    csv_reader = reader(file)
    csv_writer = writer(file)
    next(csv_reader)
    products = [[p[0],float(p[1])*1.2,p[2],p[3],p[4]] for p in csv_reader]
    file.seek(0)
    csv_writer.writerow(["ProductName","Price","IsPublished","Category","Reviews"])
    csv_writer.writerows(products)

