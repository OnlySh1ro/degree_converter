def fahrenheit(f):
    celcius = (f - 32) / 1.8
    return celcius

def celcius(c):
    farenheit = (1.8 * c + 32)
    return farenheit


convertidor = input("que quieres convertir? (F-C?: ").lower()
grados_convertir = float(input("que grado desea convertir?: "))


if convertidor == "f":
     print(f"el resultado de la conversion fue de: {fahrenheit(grados_convertir)}")

elif convertidor == "c":
    print(f"el resultado de la conversion fue de: {celcius(grados_convertir)}")

else:
    print("expression incorrecta / numero incorrecto")