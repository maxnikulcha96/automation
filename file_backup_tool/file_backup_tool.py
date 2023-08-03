import PySimpleGUI as sg
import os
import shutil

from layout import layout
from datetime import date
from consts import GOOGLE_DRIVE_BASE_PATH, BOX_DRIVE_BASE_PATH


window = sg.Window('Backup Tool', layout)

while True:
    event, values = window.read()

    src_file_path = values['src_file_input']
    src_file_base_path = os.path.dirname(src_file_path)
    src_file_extension = os.path.splitext(os.path.basename(src_file_path))[1]

    if event == sg.WINDOW_CLOSED:
        break

    elif event == 'Append date':

        
        today = date.today()
        new_file_name = str.format(
            '{}_{}{}', values['rename_file_input'], today, src_file_extension)
        window['rename_file_input'].update(new_file_name)

    elif event == 'Rename':
        new_file_path = os.path.join(src_file_base_path, new_file_name)
        os.rename(src_file_path, new_file_path)

    elif event == 'Backup':
        dest_folder = values['dest_file_input']

        if dest_folder is not None:
            shutil.copy(new_file_path, os.path.join(
                dest_folder, new_file_name))

            box_dest_folder = str.replace(
                dest_folder, GOOGLE_DRIVE_BASE_PATH, BOX_DRIVE_BASE_PATH)
            shutil.move(new_file_path, os.path.join(
                box_dest_folder, new_file_name))

window.close()
