#Ejercicio 2: Métodos estáticos (@staticmethod) como librería de utilidades
#Concepto: @STATICMETHOD
class ValidadorFinanciero:
    @staticmethod
    def es_cuit_valido(cuit: str) -> bool:
        return cuit.isdigit and len(cuit) == 11
    @staticmethod
    def convertir_moneda(monto:float,tasa_cambio:float,comision:float=0.02) ->float:
        monto = (monto * tasa_cambio) * (1-comision)
        return monto


print(ValidadorFinanciero.es_cuit_valido("20384920194"))
print(ValidadorFinanciero.es_cuit_valido("20-38492019-4"))
print(ValidadorFinanciero.convertir_moneda(100.0, 1000.0, comision=0.05))
print()