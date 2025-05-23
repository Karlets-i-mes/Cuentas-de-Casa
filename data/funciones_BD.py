import sqlite3
from prettytable import PrettyTable
import os
from datetime import datetime

empresa = "Mi Empresa"
BasedeDatos = f"bd_{empresa}.db"
ruta_BD = f"./data/{BasedeDatos}"

# --------------------------- CREAR BASE DE DATOS ---------------------------

def crear_base_datos():
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()
    conn.commit()
    conn.close()

def ver_tablas_base_datos():
    """Consulta y muestra todas las tablas existentes en la base de datos."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Consulta para obtener los nombres de todas las tablas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tablas = cursor.fetchall()

    print("Tablas en la base de datos:")
    if tablas:
        for tabla in tablas:
            print(f"- {tabla[0]}")
    else:
        print("No hay tablas en la base de datos.")

    conn.close()

#crear_base_datos()
#ver_tablas_base_datos()


# ------------------------  TABLA_NIVEL1
def crear_tabla_nivel1():
    """Crea la tabla nivel1 si no existe."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Crear tabla para el nivel 1
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nivel1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("Tabla nivel1 creada (si no existía).")

def insertar_datos_nivel1(descripcion):
    """Inserta un nuevo registro en la tabla nivel1."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Insertar un nuevo registro en la tabla nivel1
    cursor.execute("INSERT INTO nivel1 (descripcion) VALUES (?)", (descripcion,))
    
    conn.commit()
    conn.close()
    print(f"Se ha insertado el registro en nivel1: {descripcion}")

def ver_tabla_nivel1():
    """Consulta y muestra todos los registros de la tabla nivel1."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Consulta para obtener todos los registros de la tabla nivel1
    cursor.execute("SELECT * FROM nivel1")
    resultados = cursor.fetchall()

    print("Contenido de la tabla nivel1:")
    if resultados:
        for fila in resultados:
            print(f"ID: {fila[0]}, {fila[1]}")
    else:
        print("La tabla nivel1 está vacía.")

    conn.close()

def eliminar_datos_nivel1():
    """Elimina todos los registros de la tabla nivel1."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Eliminar todos los registros de la tabla nivel1
    cursor.execute("DELETE FROM nivel1")
    
    conn.commit()
    conn.close()
    print("Todos los registros de la tabla nivel1 han sido eliminados.")

#crear_tabla_nivel1()
#insertar_datos_nivel1("Cuentas Financieras")
#insertar_datos_nivel1("Deudas")
#insertar_datos_nivel1("Gastos")
#insertar_datos_nivel1("Ingresos")
#ver_tabla_nivel1()
#eliminar_datos_nivel1()

# -------------------------  TABLA_NIVEL2  
def crear_tabla_nivel2():
    """Crea la tabla nivel2 si no existe."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Crear tabla para el nivel 2
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nivel2 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion TEXT NOT NULL,
        nivel1_id INTEGER NOT NULL,
        FOREIGN KEY (nivel1_id) REFERENCES nivel1 (id)
    )
    """)

    conn.commit()
    conn.close()

def insertar_datos_nivel2(descripcion, nivel1_id):
    """Inserta un nuevo registro en la tabla nivel2."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Insertar un nuevo registro en la tabla nivel2
    cursor.execute("INSERT INTO nivel2 (descripcion, nivel1_id) VALUES (?, ?)", (descripcion, nivel1_id))
    
    conn.commit()
    conn.close()
    print(f"Se ha insertado el registro en nivel2: {descripcion}, nivel1_id: {nivel1_id}")

def ver_tabla_nivel2():
    """Consulta y muestra todos los registros de la tabla nivel2."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Consulta para obtener todos los registros de la tabla nivel2
    cursor.execute("SELECT * FROM nivel2")
    resultados = cursor.fetchall()

    print("Contenido de la tabla nivel2:")
    if resultados:
        for fila in resultados:
            print(f"ID: {fila[0]}, Descripción: {fila[1]}, Nivel1_ID: {fila[2]}")
    else:
        print("La tabla nivel2 está vacía.")

    conn.close()

def actualizar_datos_nivel2(id, nueva_descripcion, nuevo_nivel1_id):
    """Actualiza un registro en la tabla nivel2."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE nivel2
    SET descripcion = ?, nivel1_id = ?
    WHERE id = ?
    """, (nueva_descripcion, nuevo_nivel1_id, id))
    
    conn.commit()
    conn.close()
    print(f"Se ha actualizado el registro con ID: {id}")

def eliminar_datos_nivel2(id):
    """Elimina un registro específico de la tabla nivel2."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Eliminar el registro con el ID especificado
    cursor.execute("DELETE FROM nivel2 WHERE id = ?", (id,))
    
    conn.commit()
    conn.close()
    print(f"Se ha eliminado el registro con ID: {id}")

#crear_tabla_nivel2()
#insertar_datos_nivel2("CaixaEnginyers", 1)
#actualizar_datos_nivel2(3, "Self Bank", 1)
#eliminar_datos_nivel2(3)
#ver_tabla_nivel2()

# -------------------------  TABLA PRODUCTOS FINANCIEROS

def crear_tabla_productosfinancieros():
    """Crea la tabla productosfinancieros si no existe."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Crear tabla para productos financieros
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productosfinancieros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("Tabla productosfinancieros creada (si no existía).")

def insertar_datos_productosfinancieros(descripcion):
    """Inserta un nuevo registro en la tabla productosfinancieros."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Insertar un nuevo registro en la tabla productosfinancieros
    cursor.execute("""
    INSERT INTO productosfinancieros (descripcion)
    VALUES (?)
    """, (descripcion,))
    
    conn.commit()
    conn.close()
    print(f"Se ha insertado el registro en productosfinancieros: {descripcion}")

def ver_tabla_productosfinancieros():
    """Consulta y muestra todos los registros de la tabla productosfinancieros."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Consulta para obtener todos los registros de la tabla productosfinancieros
    cursor.execute("SELECT * FROM productosfinancieros")
    resultados = cursor.fetchall()

    print("Contenido de la tabla productosfinancieros:")
    if resultados:
        for fila in resultados:
            print(f"ID: {fila[0]}, Descripción: {fila[1]}")
    else:
        print("La tabla productosfinancieros está vacía.")

    conn.close()

def actualizar_datos_productosfinancieros(id, nueva_descripcion):
    """Actualiza un registro en la tabla productosfinancieros."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Actualizar el registro con el ID especificado
    cursor.execute("""
    UPDATE productosfinancieros
    SET descripcion = ?
    WHERE id = ?
    """, (nueva_descripcion, id))
    
    conn.commit()
    conn.close()
    print(f"Se ha actualizado el registro con ID: {id}")

def eliminar_datos_productosfinancieros(id):
    """Elimina un registro específico de la tabla productosfinancieros."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Eliminar el registro con el ID especificado
    cursor.execute("DELETE FROM productosfinancieros WHERE id = ?", (id,))
    
    conn.commit()
    conn.close()
    print(f"Se ha eliminado el registro con ID: {id}")

#crear_tabla_productosfinancieros()
#insertar_datos_productosfinancieros("Cta.Remunerada")
#actualizar_datos_productosfinancieros(2, "Cta.Remunerada")
#eliminar_datos_productosfinancieros(3)
#ver_tabla_productosfinancieros()


# --------------------------   TABLA_NIVEL3

def crear_tabla_nivel3():
    """Crea la tabla nivel3 si no existe."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Crear tabla para el nivel 3
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nivel3 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nivel3_id INTEGER NOT NULL,  -- Nuevo campo que reinicia desde 1 para cada combinación de nivel1_id y nivel2_id
        nivel1_id INTEGER NOT NULL,  
        nivel2_id INTEGER NOT NULL,
        descripcion TEXT NOT NULL,
        importe REAL DEFAULT 0,  
        fecha_inicio TEXT NOT NULL DEFAULT (DATE('now')),  -- Fecha obligatoria, por defecto el día actual
        FOREIGN KEY (nivel1_id) REFERENCES nivel1 (id),  -- Relación con nivel1
        FOREIGN KEY (nivel2_id) REFERENCES nivel2 (id)   -- Relación con nivel2
    )
    """)

    conn.commit()
    conn.close()
    print("Tabla nivel3 creada (si no existía).")

def insertar_datos_nivel3(nivel1_id, nivel2_id, descripcion, importe=0, fecha_inicio=None):
    """Inserta un nuevo registro en la tabla nivel3 con un sistema en árbol.
    Reinicia el contador de nivel3_id para cada combinación de nivel1_id y nivel2_id."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Obtener el último nivel3_id para la combinación de nivel1_id y nivel2_id
    cursor.execute("""
    SELECT MAX(nivel3_id) FROM nivel3 
    WHERE nivel1_id = ? AND nivel2_id = ?
    """, (nivel1_id, nivel2_id))
    ultimo_nivel3_id = cursor.fetchone()[0]

    # Calcular el nuevo nivel3_id
    nuevo_nivel3_id = (ultimo_nivel3_id + 1) if ultimo_nivel3_id else 1

    # Insertar el nuevo registro
    cursor.execute("""
    INSERT INTO nivel3 (nivel3_id, nivel1_id, nivel2_id, descripcion, importe, fecha_inicio)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nuevo_nivel3_id, nivel1_id, nivel2_id, descripcion, importe, fecha_inicio))
    
    conn.commit()
    conn.close()
    print(f"Se ha insertado el registro en nivel3: {descripcion}, nivel3_id: {nuevo_nivel3_id}")

def ver_tabla_nivel3():
    """Consulta y muestra todos los registros de la tabla nivel3 en el formato solicitado."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Consulta para obtener todos los registros de la tabla nivel3 con los datos relacionados
    cursor.execute("""
    SELECT 
        nivel1.id || '.' || nivel2.id || '.' || nivel3.nivel3_id AS codigo,
        nivel1.descripcion AS descripcion_nivel1,
        nivel2.descripcion AS descripcion_nivel2,
        nivel3.descripcion AS descripcion_nivel3,
        nivel3.importe,
        nivel3.fecha_inicio
    FROM nivel3
    INNER JOIN nivel2 ON nivel3.nivel2_id = nivel2.id
    INNER JOIN nivel1 ON nivel3.nivel1_id = nivel1.id
    ORDER BY nivel1.id, nivel2.id, nivel3.nivel3_id
    """)
    resultados = cursor.fetchall()

    print("Contenido de la tabla nivel3:")
    if resultados:
        for fila in resultados:
            # Convertir la fecha al formato dd.mm.aa
            fecha_formateada = datetime.strptime(fila[5], "%Y-%m-%d").strftime("%d.%m.%y")
            print(f"{fila[0]}, {fila[1]}, {fila[2]}, {fila[3]}, Importe: {fila[4]}, Fecha Inicio: {fecha_formateada}")
    else:
        print("La tabla nivel3 está vacía.")

    conn.close()

def actualizar_datos_nivel3(id, nueva_descripcion, nuevo_nivel1_id, nuevo_nivel2_id, nuevo_importe, nueva_fecha_inicio):
    """Actualiza un registro en la tabla nivel3."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Actualizar el registro con el ID especificado
    cursor.execute("""
    UPDATE nivel3
    SET descripcion = ?, nivel1_id = ?, nivel2_id = ?, importe = ?, fecha_inicio = ?
    WHERE id = ?
    """, (nueva_descripcion, nuevo_nivel1_id, nuevo_nivel2_id, nuevo_importe, nueva_fecha_inicio, id))
    
    conn.commit()
    conn.close()
    print(f"Se ha actualizado el registro con ID: {id}")

def eliminar_datos_nivel3(id):
    """Elimina un registro específico de la tabla nivel3."""
    conn = sqlite3.connect(ruta_BD)
    cursor = conn.cursor()

    # Eliminar el registro con el ID especificado
    cursor.execute("DELETE FROM nivel3 WHERE id = ?", (id,))
    
    conn.commit()
    conn.close()
    print(f"Se ha eliminado el registro con ID: {id}")

#crear_tabla_nivel3()
#insertar_datos_nivel3( 1, 1,"Carlos", 100, "2025-01-01")  # Suponiendo que nivel2_id = 1 existe
#insertar_datos_nivel3("Montse", 1, 1, 200, "2025-01-02")  # Suponiendo que nivel2_id = 1 existe
#insertar_datos_nivel3("Cta.Cte.", 1, 3, 3000, "2025-01-03")  # Suponiendo que nivel2_id = 1 existe
#actualizar_datos_nivel3(4, "Depósito", 1, 1, 20000, "2025-03-10")
#eliminar_datos_nivel3(3)
#ver_tabla_nivel3()



# ------------------------------ CREAR TABLA INICIAL ------------------------------
# ---------------------------------------------------------------------------------

def insertar_datos_iniciales():
    #crear_base_datos()
    # Crear tablas productos financieros
    #crear_tabla_productosfinancieros()
    insertar_datos_productosfinancieros("Cta. Cte.")
    insertar_datos_productosfinancieros("Cta. Remunerada")
    insertar_datos_productosfinancieros("Depósito")
    insertar_datos_productosfinancieros("Fondo Inversión")
    insertar_datos_productosfinancieros("Renta Fija")
    insertar_datos_productosfinancieros("Renta Variable")
    insertar_datos_productosfinancieros("Fondo Pensiones")
    insertar_datos_productosfinancieros("Crowdfunding")
    insertar_datos_productosfinancieros("Inversiones en empresas")
    insertar_datos_productosfinancieros("Derivados fiancieros")
    #Datos Tabla_nivel1
    #crear_tabla_nivel1()
    insertar_datos_nivel1("Cuentas Financieras")
    insertar_datos_nivel1("Deudas")
    insertar_datos_nivel1("Gastos")
    insertar_datos_nivel1("Ingresos")
    #Datos Tabla_nivel2
    #crear_tabla_nivel2()
    insertar_datos_nivel2("Efectivo", 1)  
    insertar_datos_nivel2("Caixa Enginyers", 1)
    insertar_datos_nivel2("Self Bank", 1)
    insertar_datos_nivel2("DeGiro", 1)
    insertar_datos_nivel2("Trade Republic", 1)
    insertar_datos_nivel2("Santander", 1)
    insertar_datos_nivel2("BBVA", 1)
    insertar_datos_nivel2("B.Sabadell", 1)
    insertar_datos_nivel2("Civislend", 1)
    insertar_datos_nivel2("StockCrowd", 1)
    insertar_datos_nivel2("Mintos", 1)
    insertar_datos_nivel2("Bestinver", 1)
    insertar_datos_nivel2("Ahorro Hijos", 2)
    insertar_datos_nivel2("Deudas Casa", 2)
    insertar_datos_nivel2("Deudas inversiones", 2)   
    insertar_datos_nivel2("Gastos fijos", 3)
    insertar_datos_nivel2("Gastos Variables", 3)
    insertar_datos_nivel2("Otros Gastos", 3)       
    insertar_datos_nivel2("Salarios", 4)
    insertar_datos_nivel2("No Salariales", 4)
    insertar_datos_nivel2("Otros Ingresos", 4)
    #Datos Tabla_nivel3
    #crear_tabla_nivel3()
    insertar_datos_nivel3(1,1,"Carlos", 50, "2025-01-01") 
    insertar_datos_nivel3(1,1,"Montse", 50, "2025-01-01")
    insertar_datos_nivel3(1,2,"Cta. Cte.", 5060, "2025-01-01")
    insertar_datos_nivel3(1,2,"Cta. Remunerada", 10000, "2025-01-01")
    insertar_datos_nivel3(1,3,"Cta. Cte.", 1000, "2025-01-01")
    insertar_datos_nivel3(1,3,"Cta. Remunerada", 6000, "2025-01-01")
    insertar_datos_nivel3(2,1,"Roger", 6000, "2025-01-01")
    insertar_datos_nivel3(2,1,"Enric", 6000, "2025-01-01")
    insertar_datos_nivel3(2,2,"Enaire 0%", 6000, "2025-01-01")
    insertar_datos_nivel3(2,2,"Avis", 6000, "2025-01-01")
    insertar_datos_nivel3(2,3,"JMG inversiones", 90000, "2025-01-01")
    insertar_datos_nivel3(3,1,"Agua", 10, "2025-01-01")
    insertar_datos_nivel3(3,1,"Luz", 20, "2025-01-01")
    insertar_datos_nivel3(3,1,"Gas", 30, "2025-01-01")
    insertar_datos_nivel3(3,2,"Salud", 40, "2025-01-01")
    insertar_datos_nivel3(3,3,"Otros Gastos", 50, "2025-01-01")
    insertar_datos_nivel3(4,1,"Montse", 100, "2025-01-01")
    insertar_datos_nivel3(4,1,"Carlos", 200, "2025-01-01")
    insertar_datos_nivel3(4,1,"Pensió", 150, "2025-01-01")
    insertar_datos_nivel3(4,2,"Int. Bancarios", 10, "2025-01-01")
    insertar_datos_nivel3(4,2,"Int. Crowd.", 20, "2025-01-01")
    insertar_datos_nivel3(4,3,"Otros Ingresos", 30, "2025-01-01")

def crear_tablas_codigo_inicio():
    """Crea las tablas iniciales en la base de datos."""
    # Crear base de datos
    crear_base_datos()

    # Crear tablas
    crear_tabla_nivel1()
    crear_tabla_nivel2()
    crear_tabla_productosfinancieros()
    crear_tabla_nivel3()

    # Insertar datos iniciales
    insertar_datos_iniciales()
    print("Tablas iniciales creadas y datos insertados correctamente.")

#crear_tablas_codigo_inicio()
#ver_tablas_base_datos()
#insertar_datos_iniciales()
#ver_tabla_nivel3()


# ----------------------------- VISTAS TABLAS -----------------------------
# -------------------------------------------------------------------


# ------------------------------ Insertar Codgio en tabla -----------------------------
# -------------------------------------------------------------------------------------





