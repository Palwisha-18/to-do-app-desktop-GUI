
import PySimpleGUI as psg

label = psg.Text("Enter a to-do")
input_box = psg.InputText(tooltip="Enter todo", key='todo')
add_button = psg.Button("Add")

window = psg.Window("To-Do App",
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 20))
event, values = window.read()
window.close()
