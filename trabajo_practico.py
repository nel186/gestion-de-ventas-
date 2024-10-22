import flet as ft

# Declarar la lista de tareas a nivel global
tasks = []

def main(page: ft.Page):
    # Establecer el tamaño de la ventana
    page.window_width = 600 
    page.window_height = 400
    page.title = "Lista de compras"

    # Crear un campo de texto para la lista de compras
    new_task = ft.TextField(hint_text="¿Qué necesitas comprar?", width=300)

    # Función para agregar una tarea
    def add_clicked(e):
        task = ft.Checkbox(label=new_task.value, value=False)
        tasks.append(task)
        page.add(task)
        new_task.value = ""
        new_task.focus()
        new_task.update()

    # Función para modificar la tarea seleccionada
    def modify_clicked(e):
        for task in tasks:
            if task.value:  # Si el checkbox está marcado
                task.label = new_task.value
                task.update()
        new_task.value = ""
        new_task.update()

    # Función para eliminar las tareas seleccionadas
    def delete_clicked(e):
        global tasks  # Declarar tasks como global
        # Eliminar las tareas seleccionadas tanto de la lista como de la página
        tasks_to_remove = [task for task in tasks if task.value]  # Tareas seleccionadas
        for task in tasks_to_remove:
            page.controls.remove(task)  # Eliminar de la página
            tasks.remove(task)  # Eliminar de la lista de tareas

        page.update()  # Actualizar la página para reflejar los cambios

    # Logo y texto del encabezado
    logo = ft.Image(src=r"c:\Users\canet\Downloads\logo.ttp.jpg", width=150, height=150)
    header_text = ft.Text("Bienvenidos a la App de Lista de Compras", size=20, weight=ft.FontWeight.BOLD)

    # Organizar el encabezado en una columna
    header = ft.Column([
        logo,
        header_text
    ], alignment="center")

    # Botones para agregar, modificar y eliminar elementos
    buttons_row = ft.Row([
        ft.ElevatedButton("Agregar", on_click=add_clicked),
        ft.ElevatedButton("Modificar", on_click=modify_clicked),
        ft.ElevatedButton("Eliminar", on_click=delete_clicked)
    ], alignment="center")

    # Agregar elementos a la aplicación
    page.add(
        header,
        ft.Divider(height=20),  # Agregar un divisor
        ft.Row([new_task]),  # Campo de entrada
        buttons_row  # Fila de botones
    )

# Ejecutar la aplicación 
ft.app(main)
