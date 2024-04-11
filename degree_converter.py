def fahrenheit(f):
    celcius = (f - 32) / 1.8
    return celcius

def celcius(c):
    farenheit = (1.8 * c + 32)
    return farenheit


convertidor = input("que quieres convertir? (F-C?: ").lower()
grados_convertir = float(input("que grado desea convertir?: "))


if convertidor == "f":
     print(f"el resultado de la conversion a celcius: {fahrenheit(grados_convertir):.2f}")

elif convertidor == "c":
    print(f"el resultado de la conversion a fahrenheit es: {celcius(grados_convertir):.2f}")

else:
    print("expression incorrecta / numero incorrecto")
