# def displayUserArgs(*args):
#     print(type(args))
#     print(args)

# displayUserArgs("Mehmet","Yılmaz","Zeynep","Çelik")

def displayUserKwargs(**kwargs):
    #** işareti ile key value çifti yani dict türünde veri alınır, kwargs değişken ismi
    # print(type(kwargs))
    # print(kwargs)
    for key,value in kwargs.items():
        print(f"{key} : {value}")

    print()

def mixedFunc(a,b,c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

displayUserKwargs(username="Hakan", mail="hakan@epsis.app",city="Bordeaux")

mixedFunc(10,20,30,100,200,300,key1="value1",key2="value2",key3="value3")
