try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
# Sadece except ile tüm hata türleri yakalanır.

# except:
#     print("Hata oluştu")
#     # Yakalanan hataları türlerine göre ayırt etmek için except yanına hata türleri eklenir.

# Birden fazla except kullanılabilir, 
#   şart olarak en altta except Exception ya da sadece except kullanılmalıdır.
#   Tüm hatalardan sonra except e girmelidir.

# except ZeroDivisionError:
#     print("Sıfıra bölme hatası")
# except ValueError:
#     print("Girilen değerlerde hata var")
# except Exception:
#     print("Bilinmeyen bir hata oluştu")

# as e ile hata başlığı e değişkenine atanabilir.
# birden fazla hata (ZeroDivisionError,ValueError) ile birleştirilebilir.

#
except ZeroDivisionError as e:
    print(e)
    print("Sıfıra bölme hatası")
except ValueError:
    print("Girilen değerlerde hata var")
except Exception:
    print("Bilinmeyen bir hata oluştu")
# Hata yoksa else bloğu çalıştırabilir
else:
    pass
# Her durumda kullanılmak için finally bloğu kullanılabilir.
finally :
    pass