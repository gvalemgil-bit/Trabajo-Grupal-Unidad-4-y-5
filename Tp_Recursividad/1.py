
class Archivo:
    def __init__(self, nombre: str, tamano_bytes: int):
        self.nombre = nombre
        self.tamano_bytes = tamano_bytes

class Directorio:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.archivos = []       
        self.subdirectorios = []  


def calcular_tamano_total(directorio: Directorio) -> int:
    total = sum(archivo.tamano_bytes for archivo in directorio.archivos)
    for subdirectorio in directorio.subdirectorios:
        total += calcular_tamano_total(subdirectorio)
    return total

def buscar_por_extension(directorio: Directorio, extension: str, ruta_actual: str = "") -> list[str]:
    if not ruta_actual:
        ruta_actual = directorio.nombre
    else:
        ruta_actual = f"{ruta_actual}/{directorio.nombre}"
    resultados = []
    for archivo in directorio.archivos:
        if archivo.nombre.endswith(extension):
            resultados.append(f"{ruta_actual}/{archivo.nombre}")
    for subdirectorio in directorio.subdirectorios:
        resultados.extend(buscar_por_extension(subdirectorio, extension, ruta_actual))
    return resultados

def limpiar_archivos_vacios(directorio: Directorio) -> int:
    archivos_iniciales = len(directorio.archivos)
    directorio.archivos = [arch for arch in directorio.archivos if arch.tamano_bytes > 0]
    eliminados_locales = archivos_iniciales - len(directorio.archivos)
    total_eliminados = eliminados_locales
    for subdirectorio in directorio.subdirectorios:
        total_eliminados += limpiar_archivos_vacios(subdirectorio)
    return total_eliminados

if __name__ == "__main__":
    root = Directorio("root")
    root.archivos.append(Archivo("documento.pdf", 1500))
    root.archivos.append(Archivo("config.txt", 0))
    imagenes = Directorio("imagenes")
    imagenes.archivos.append(Archivo("foto1.png", 2000))
    imagenes.archivos.append(Archivo("foto2.png", 3500))
    root.subdirectorios.append(imagenes)
    proyectos = Directorio("proyectos")
    proyectos.archivos.append(Archivo("avance.pdf", 800))
    temp = Directorio("temp")
    temp.archivos.append(Archivo("log.txt", 0))
    proyectos.subdirectorios.append(temp)
    root.subdirectorios.append(proyectos)
    print("--- VALIDACIÓN DE RESULTADOS ---")
    tamano_total = calcular_tamano_total(root)
    print(f"1. Tamaño Total: {tamano_total} bytes (Esperado: 7800 bytes)")
    archivos_pdf = buscar_por_extension(root, ".pdf")
    print(f"2. Archivos PDF: {archivos_pdf}")
    print('   (Esperado: ["root/documento.pdf", "root/proyectos/avance.pdf"])')
    eliminados = limpiar_archivos_vacios(root)
    print(f"3. Archivos vacíos eliminados: {eliminados} (Esperado: 2)")
    tamano_pos_limpieza = calcular_tamano_total(root)
    print(f"   Tamaño tras la limpieza: {tamano_pos_limpieza} bytes")
    