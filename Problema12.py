# La mayoría de los archivos tienen extensiones de archivo, el cual es un sufijo que comienza con un
#punto (.) al final de su nombre. Por ejemplo, los nombres de archivo para GIF terminan en .gif y los
#nombres de archivo para JPEG terminan en .jpg o .jpeg. Mientras que en los sistemas operativos
#como Windows, el tipo de archivo le sirve al computador abrir el archivo en el formato apropiado, en
#la web esto es distinto. Los navegadores web, por el contrario, se basan en tipos de medios,
#anteriormente conocidos como tipos MIME, para determinar cómo mostrar los archivos que viven en
#la web.
#Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de
#archivo MIME correspondiente.


def obtener_tipo_mime(nombre_archivo):
    # Obtener la extensión del archivo (sufijo) en minúsculas
    extension = nombre_archivo.lower().split('.')[-1]

    # Mapear extensiones a tipos MIME
    tipos_mime = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }

    # Obtener el tipo MIME correspondiente o 'application/octet-stream' si no coincide
    return tipos_mime.get(extension, 'application/octet-stream')

# Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener y mostrar el tipo MIME correspondiente
tipo_mime = obtener_tipo_mime(nombre_archivo)
print("El tipo MIME del archivo {} es: {}".format(nombre_archivo, tipo_mime))