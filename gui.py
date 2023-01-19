from helper_functions import get_todos, write_todos
import PySimpleGUI as psg

label = psg.Text("Enter a to-do")
input_box = psg.InputText(tooltip="Enter todo", key='todo')
add_button = psg.Button("Add")

window = psg.Window("To-Do App",
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()

    if event == 'Add':

        new_to_do = f"{values['todo']}\n"
        to_dos = get_todos()
        to_dos.append(new_to_do)
        write_todos(to_dos)

    elif psg.WIN_CLOSE:
        break

window.close()
