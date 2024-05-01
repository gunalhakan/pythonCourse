from methods import *
import os 
os.system("clear")

selectUrunler()
print("-"*20)

insertUrun("makas",24.5)
insertUrun("Sıvı Sabun",64.5)

selectUrunler()
print("-"*20)

updateUrun(1006,"Makas",35.7)
selectUrunler()
print("-"*20)

deleteUrun(1004)
selectUrunler()
print("-"*20)