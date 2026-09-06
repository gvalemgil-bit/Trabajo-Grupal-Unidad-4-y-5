#Ejercicio 1: Funciones puras con parámetros opcionales y keyword arguments
#Concepto: Parámetros opcionales
def calcular_factura_final(monto_base:float,impuesto:float=21.0,descuento:float=0.0,envio_prioritario:float|None=None) ->float:
    subtotal = monto_base*(1-descuento/100)
    total_impuesto = subtotal * (1+impuesto/100)
    if envio_prioritario is not None:
        total_impuesto += envio_prioritario
    return round(total_impuesto)
print(calcular_factura_final(1000))
print(calcular_factura_final(1000,descuento=10))
print(calcular_factura_final(1000,impuesto=10,descuento=5,envio_prioritario=150))
print()
