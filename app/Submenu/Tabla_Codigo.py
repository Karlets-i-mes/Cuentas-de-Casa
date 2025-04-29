import flet as ft   
import datetime



def TablaCodigos2():
    return ft.Column(
    [
        ft.Text("FUNCION TABLACODIGOS", size=30, weight=ft.FontWeight.BOLD),
        ft.Text("CONTENIDO DE LA FUNCION", size=16),
        
        ft.Text("Fecha actual: " + str(datetime.datetime.now().date()), size=16)
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )











'''
def TablaCodigos():
    # Submenu CRUD de la tabla código
    submenu = ft.Container(
        content=ft.Row(
            controls=[
                ft.TextButton(
                    text="Ver Tabla Códigos",
                    icon=ft.icons.TABLE_CHART,  # Ícono para "Ver Tabla"
                    on_click=ver_TablaCodigos,  # Pasa directamente la función
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(size=18, letter_spacing=2)
                    ),
                ),
                ft.TextButton(
                    text="Crear Código",
                    icon=ft.icons.ADD,  # Ícono para "Crear"
                    on_click=crear_codigo,  # Pasa directamente la función
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(size=18, letter_spacing=2)
                    ),
                ),

                ft.TextButton(
                    text="Actualizar Código",
                    icon=ft.icons.EDIT,  # Ícono para "Actualizar"
                    on_click=actualizar_codigo,  # Pasa directamente la función
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(size=18, letter_spacing=2)
                    ),
                ),
                ft.TextButton(
                    text="Eliminar Código",
                    icon=ft.icons.DELETE,  # Ícono para "Eliminar"
                    on_click=eliminar_codigo,  # Pasa directamente la función
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(size=18, letter_spacing=2)
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.START,  # Centrar los botones horizontalmente
            spacing=20,  # Espaciado entre los botones
        ),
        bgcolor=ft.colors.LIGHT_BLUE_50,  # Fondo suave para el submenú
        padding=10,  # Espaciado interno del contenedor
        border_radius=ft.border_radius.all(10),  # Bordes redondeados
            )
    
    # Contenido de la tabla de códigos
    contenido_cuerpo = ft.Container(
        # poner la tabla Códigos aquí------------------------------------
        content=ft.Column(
            controls=[
                ft.Text("Contenido de Tabla Códigos", size=20),
            ],
            expand=True,
        ),
        #expand=3,  # Asegura que el contenido ocupe más espacio que el submenú
    )

    # Fila que contiene el submenú y el coColumnnido
    cuerpo = ft.Column(
        controls=[
            submenu,  # Submenú a la izquierda
            contenido_cuerpo,  # Contenido a la derecha
        ],
        expand=True,
    )
    return cuerpo

'''

