from tkinter import Button
from constants import ORIGIN, TOKENIZED, MOVE_NEXT,  MOVE_PREV
import line_ui

def file_move(event, txt_labeling, key, direction):
        file = txt_labeling.files[key]
        if file:
            if direction == MOVE_NEXT:
                file.next()
            elif direction == MOVE_PREV:
                file.prev()
        line_ui.update_label(txt_labeling, key)

def files_next(event, txt_labeling):
    file_move(event, txt_labeling, ORIGIN, MOVE_NEXT)
    file_move(event, txt_labeling, TOKENIZED, MOVE_NEXT)

def files_prev(event, txt_labeling):
    file_move(event, txt_labeling, ORIGIN, MOVE_PREV)
    file_move(event, txt_labeling, TOKENIZED, MOVE_PREV)

def button_init(txt_labeling):
    app = txt_labeling.app

    # Origin Previous
    prev_button = Button(app, text='Previous')
    prev_button.grid(row=3, column=0)
    prev_button.bind('<Button-1>', lambda event: file_move(event, txt_labeling, ORIGIN, MOVE_PREV))
    # Origin Next
    next_button = Button(app, text='Next')
    next_button.grid(row=3, column=1)
    next_button.bind('<Button-1>', lambda event: file_move(event, txt_labeling, ORIGIN, MOVE_NEXT))
    # Tokenized Previous
    prev_button = Button(app, text='Tokenized Previous')
    prev_button.grid(row=3, column=2)
    prev_button.bind('<Button-1>', lambda event: file_move(event, txt_labeling, TOKENIZED, MOVE_PREV))
    # Tokenized Next
    next_button = Button(app, text='Tokenized Next')
    next_button.grid(row=3, column=3)
    next_button.bind('<Button-1>', lambda event: file_move(event, txt_labeling, TOKENIZED, MOVE_NEXT))
    app.bind('<Left>', lambda event: files_prev(event, txt_labeling))
    app.bind('<Right>', lambda event: files_next(event, txt_labeling))
