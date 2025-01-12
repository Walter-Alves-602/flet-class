import flet as ft

def main(page:ft.Page):
    page.title = "lista de tarefas"

    entrada = ft.TextField(label="tarefa",hint_text="digite sua tarefa aqui")
    page.add(entrada)
    btn_adicionar= ft.IconButton(icon=ft.Icons.ADD_CIRCLE_OUTLINE_SHARP)
    page.add(btn_adicionar)

ft.app(main)