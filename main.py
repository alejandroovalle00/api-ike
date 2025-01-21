# main.py
 
import pyodbc
from fastapi import FastAPI
 
app = FastAPI()
 
# Cadena de conexión a la base de datos SQL Server
cadena_conexion = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=128.11.1.6;"
    "DATABASE=DWH_MX;"
    "UID=DF_APPBI;"
    "PWD=H8TWzzN;"
)
 
@app.get("/end1")
def get_end1():
    try:
        conn = pyodbc.connect(cadena_conexion)
        cursor = conn.cursor()
        query = "SELECT * FROM PRUEBA_API"
        cursor.execute(query)
 
        columns = [desc[0] for desc in cursor.description]
        resultados = []
        for row in cursor.fetchall():
            resultados.append(dict(zip(columns, row)))
 
        cursor.close()
        conn.close()
        return resultados
 
    except Exception as e:
        return {"error": str(e)}
 
 
@app.get("/end2")
def get_end2():
    try:
        conn = pyodbc.connect(cadena_conexion)
        cursor = conn.cursor()
        query = "SELECT * FROM bi_sta_planit_encuestas_v1 WHERE [INICIO DE LA ENCUESTA] LIKE '%12/2024%'"
        cursor.execute(query)
 
        columns = [desc[0] for desc in cursor.description]
        resultados = []
        for row in cursor.fetchall():
            resultados.append(dict(zip(columns, row)))
 
        cursor.close()
        conn.close()
        return resultados
 
    except Exception as e:
        return {"error": str(e)}