"""
Descripción del problema: En un supermercado cada tres productos que se compren se debe 
de generar un reporte en el servidor central. Para este reporte se necesita tener el total del 
precio de venta, el total de los impuestos a pagar por los productos vendidos además de 
contener un mensaje donde se digan los nombres de los tres productos.
Cada que una caja en el supermercado vende tres productos envía un diccionario al servidor 
central para que elabore el informe. Escriba una función qué reciba cómo parámetro un 
diccionario con la siguiente estructura:

productos_vendidos = {
 'producto1' : {
 'nombre' : 'nombreproducto1',
 'precio' : precio (numero decimal),
 'iva' : porcentaje_iva(numero decimal),
 },
 'producto2' : {
 'nombre' : 'nombreproducto2',
 'precio' : precio (numero decimal),
 'iva' : porcentaje_iva(numero decimal),
 },
 'producto3' : {
 'nombre' : 'nombreproducto3',
 'precio' : precio (numero decimal),
 'iva' : porcentaje_iva(numero decimal),
 }
}

La función programada debe de generar un diccionario con la siguiente estructura:
reporte = {
 "total_precio" : {total_precio},
 "total_impuestos" : {total_impuestos},
 "mensaje" : {mensaje}
 }
"""


def reporte_supermercado(productos_vendidos):
    reporte = dict()
    total_precio = 0
    total_impuesto = 0
    mensaje = "Los productos a contar son: "
    for i in range(3):
        total_precio = total_precio + productos_vendidos['producto'+str(i+1)]['precio']
        total_impuesto = total_impuesto + (productos_vendidos['producto'+str(i+1)]['precio']*productos_vendidos['producto'+str(i+1)]['iva'])
        if i == 2:
            mensaje = mensaje + productos_vendidos['producto'+str(i+1)]['nombre']
        else:
            mensaje = mensaje + productos_vendidos['producto'+str(i+1)]['nombre']+", "
    reporte['total_precio'] = total_precio
    reporte['total_impuesto'] = total_impuesto
    reporte['mensaje'] = mensaje

    return reporte

def productos_vendidos():
    lista ={
        'producto1' : {'nombre' : 'Huevos','precio' : 1800,'iva' : 0.19,},
        'producto2' : {'nombre' : 'Agua','precio' : 2500,'iva' : 0.05,},
        'producto3' : {'nombre' : 'Leche','precio' : 2900,'iva' : 0,}
        }


    return lista

print(reporte_supermercado(productos_vendidos()))