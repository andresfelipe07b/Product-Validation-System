# 🧮 Sistema de validación de productos

Este es un pequeño script en Python que simula el costo total de una compra en una tienda, incluyendo el cálculo del subtotal, descuento aplicado y total a pagar. Está pensado como una herramienta de práctica o como base para desarrollar un sistema de punto de venta (POS) sencillo.

---

## 📌 Características

- Solicita el nombre del producto.
- Valida correctamente el ingreso de:
  - Precio unitario (positivo).
  - Cantidad (mayor a cero).
  - Descuento (entre 0% y 100%).
- Calcula:
  - Subtotal.
  - Monto del descuento.
  - Total a pagar.
- Muestra los valores formateados como moneda colombiana (`COP`).

---

## 🛠️ Tecnologías utilizadas

- **Lenguaje**: Python 3
- **Módulo estándar**:
  - `locale`: Para formatear los valores en moneda local.

---

## ▶️ Cómo ejecutar el programa

1. Asegúrate de tener Python 3 instalado en tu sistema.
2. Clona este repositorio o descarga el archivo `.py`.

```bash
git clone https://github.com/andresfelipe07b/Riwi-Modulo-1.git
cd tu_repositorio
```

3. Ejecuta el script en consola:

```bash
python calculadora_descuento.py
```

4. Sigue las instrucciones que aparecen en pantalla.

---

## 💡 Posibles mejoras a futuro

- [ ] Agregar soporte para múltiples productos en una sola ejecución.
- [ ] Incluir cálculo de IVA (impuesto).
- [ ] Exportar la información a un archivo `.txt` o `.csv`.
- [ ] Crear una interfaz gráfica simple.
- [ ] Hacer una versión web con Flask o Django.
- [ ] Agregar historial de ventas por sesión.
- [ ] Pruebas unitarias para las funciones de cálculo.

---

## 📷 Ejemplo de uso

```
Ingresa el nombre del producto: Zapatos
Ingresa el precio del producto: 120000
Ingresa la cantidad: 2
Ingresa el descuento a aplicar: 10

======================
Producto:         Zapatos
Precio unitario:  $120.000,00
Cantidad:         2.00
Subtotal:         $240.000,00
Descuento:        10.0%
Monto descuento:  $24.000,00
-------------------------------
TOTAL A PAGAR:    $216.000,00
==============================
```


