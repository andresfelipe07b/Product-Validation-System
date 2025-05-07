#importa un modulo para darle formato a numeros, monedas, cadenas y fechas segun la region
import locale
locale.setlocale(locale.LC_ALL, 'es_CO') 

#se controla que la entrada del nombre no sea vacia 
#asigna el nombre del producto a la variable "producto"
while True:
    producto = str(input("Ingresa el nombre del producto: ")).strip()
    if producto:
        break
    else:
        print("El nombre del producto no puede estar vacio.")

# Valida el precio unitario,si es un valor positivo o valido
#asigna el precio del producto a la variable "PrecioUnitario"
while True:
    try:
        precioUnitario = float(input("Ingresa el precio del producto: "))
        if precioUnitario > 0 : 
            break
        else:
            print("el precio debe ser mayor a cero")
    except ValueError : 
        print("Ingrese un precio valido")

#valida que la cantidad ingresada no sea negativa o mayor a cero
#asigna la cantidad del producto a la variable "cantidad"
while True:
    try:
        cantidad = float(input("Ingresa la cantidad: "))
        if cantidad > 0:
            break
        else:
            print("La cantidad debe ser mayor a cero")
    except ValueError:
        print("Ingresa un valor valido")

# Valida que el descuento se encuentre dentro del rango 0-100
#asigna el porcentaje de descuento a la variable "descuento" 
while True:
    try:
        descuento = float(input("Ingresa el descuento a aplicar: "))
        if descuento >= 0 and descuento <= 100:
            break
        else: 
            print("El descuento debe estar entre el rango 0 y 100")
    except ValueError:
        print("ingresa un valor valido")
        

#al obtener las variables necesarias se procede con los calculos
subtotal = precioUnitario * cantidad
montoDescuento = subtotal * (descuento / 100)
total = subtotal - montoDescuento

print("\n======================")
print(f"Producto:         {producto}")
print(f"Precio unitario:  {locale.currency(precioUnitario, grouping=True, symbol=True)}")
print(f"Cantidad:         {cantidad}")
print(f"Subtotal:         {locale.currency(subtotal, grouping=True, symbol=True)}")
print(f"Descuento:        {descuento}%")
print(f"Monto descuento:  {locale.currency(montoDescuento, grouping=True, symbol=True)}")
print("-------------------------------")
print(f"TOTAL A PAGAR:    {locale.currency(total, grouping=True, symbol=True)}")
print("===============================\n")



       
       
        
        
        
    
