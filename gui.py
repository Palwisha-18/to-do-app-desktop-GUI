import time

import PySimpleGUI as psg

from helper_functions import get_todos, write_todos

psg.theme('DarkGreen4')

clock = psg.Text("", key='clock')
label = psg.Text("Enter a to-do")
input_box = psg.InputText(tooltip="Enter todo", key='todo')
add_button = psg.Button("Add")

list_box = psg.Listbox(values=get_todos(),
                       key='todos',
                       enable_events=True,
                       size=[45, 10])
edit_button = psg.Button("Edit")
complete_button = psg.Button("Completed")
exit_button = psg.Button("Exit")

window = psg.Window("To-Do App",
                    layout=[[clock], [label], [input_box, add_button],
                            [list_box, edit_button, complete_button], [exit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d, %Y - %H:%M:%S'))

    if event == 'Add':

        new_to_do = f"{values['todo']}\n"
        to_dos = get_todos()
        to_dos.append(new_to_do)
        write_todos(to_dos)
        window['todos'].update(values=to_dos)

    elif event == 'Edit':
        try:
            to_do_to_edit = values['todos'][0]
            new_to_do = f"{values['todo']}\n"

            to_dos = get_todos()
            index = to_dos.index(to_do_to_edit)
            to_dos[index] = new_to_do

            write_todos(to_dos)
            window['todos'].update(values=to_dos)
        except IndexError:
            psg.popup("Please select an item first.", font=('Helvetica', 20))

    elif event == 'todos':

        window['todo'].update(value=values['todos'][0])

    elif event == 'Completed':
        try:
            to_do_completed = values['todos'][0]
            to_dos = get_todos()
            to_dos.remove(to_do_completed)
            write_todos(to_dos)
            window['todos'].update(values=to_dos)
            window['todo'].update(value='')
        except IndexError:
            psg.popup("Please select an item first.", font=('Helvetica', 20))

    elif event == 'Exit':
        break
    elif psg.WIN_CLOSED:
        break

window.close()
