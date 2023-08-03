import PySimpleGUI as sg

layout = [
    [
        sg.Text('Select file'),
        sg.Input(key='src_file_input'),
        sg.FileBrowse(file_types=(("ALL Files", "*.*"),))
    ],
    [
        sg.Text('Rename file', size=(15, 1)), sg.InputText(
            key='rename_file_input'),
        sg.Button("Append date"),
        sg.Button("Rename"),
    ],
    [
        # lst
        sg.Text('Select destination'),
        sg.Input(key='dest_file_input'),
        sg.FolderBrowse(size=(10, 1))
    ],
    [
        sg.Button("Backup"),
    ]
]
