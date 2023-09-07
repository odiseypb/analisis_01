
"""crear entorno virutal
python -m venv venv
python3 -m venv venv

Activar entorno virutal
windows: /venv/Scripts/activate
linux: source ./venv/bin/activate
snake_kase para variables, funciones, archivos y proyectos
instalar pandas pip install pandas
importar pandas para el analisis de datos
"""
import pandas as pd
import matplotlib.pyplot as plt

def recopilar_datos():
   datos= pd.read_csv('./data/Map-Crime_Incidents-Previous_Three_Months.csv')

   return datos


def preparar_datos(marco_datos):
    #Aplicar el proceso de ETL
    del marco_datos['IncidntNum']
    del marco_datos['Resolution']
    del marco_datos['Address']
    #del marco_datos['X']
    #del marco_datos['Y']
    del marco_datos['Location']
    return marco_datos

def modelo_analisis(marco_datos):
    #Técnica de análisis: Reducción de la dimensionalidad
    #Con la limpieza de los datos y la filtración de categoría, día y distrito
    #aplicamos análisis descriptivo para conocer la media, mediana, desviación estándar, máximos y mínimo
    asaltos = marco_datos.query('Category == "ASSAULT" and DayOfWeek == "Saturday" and (PdDistrict=="RICHMOND" or PdDistrict=="SOUTHERN") ')

    return asaltos

def presentar_datos(asaltos):
    #pip install matplotlib
    plt.plot(asaltos['X'], asaltos['Y'], 'ro')

    plt.show()

def generar_grafica_bar(asaltos):
    conteo=asaltos['PdDistrict'].value_counts()

    #plt.style.use("bmh")
    #https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
    # Envia datos de la variable conteo para el eje x y el eje y
    plt.bar(conteo.index, conteo)
    plt.show()
    plt.close('all')

if __name__ == '__main__':
    print("Iniciando python")
    datos=recopilar_datos()
    marco_datos=preparar_datos(datos)
    asaltos=modelo_analisis(marco_datos)
    presentar_datos(asaltos)
    generar_grafica_bar(asaltos)









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
