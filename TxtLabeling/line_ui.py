from asyncio.windows_events import NULL
import tkinter as tk
from constants import ORIGIN, TOKENIZED, INDEX

def update_index(txt_labeling):
    if txt_labeling.labels[INDEX] == NULL:
        index_label = tk.Label(txt_labeling.app, textvariable=txt_labeling.current_progress)
        index_label.grid(row=11, column=0)
        txt_labeling.labels[INDEX] = index_label
    current = txt_labeling.files[TOKENIZED].current
    total = len(txt_labeling.files[TOKENIZED].tokens_list)
    txt_labeling.current_progress.set(f'{current}/{total}')

def label_click(event, txt_labeling):
    name = str(event.widget)
    index = int(name.split('-')[-1])
    current_token = event.widget['text'].split()[0]
    txt_labeling.files[TOKENIZED].set_label(index, txt_labeling.picked_label.get())
    event.widget['text'] = current_token + '\n' + txt_labeling.picked_label.get()
    event.widget['bg'] = 'green'

def update_label(txt_labeling, key):
    label_list = []
    mixed = []
    if txt_labeling.files[key] != NULL:
        mixed = txt_labeling.files[key].get_mixed_list(key)
    for label in txt_labeling.labels[key]:
        label.destroy()
    for i, token in enumerate(mixed):
        label = tk.Label(txt_labeling.app, name=key + '-'+ str(i), text=token)
        row=1
        if key == TOKENIZED:
            row = 2
            label.bind("<Button-1>", lambda event:label_click(event, txt_labeling))
        label.grid(row=row, column=i)
        label_list.append(label)
    txt_labeling.labels[key] = label_list
    if key == TOKENIZED:
        update_index(txt_labeling)
