import tkinter as tk
from constants import LABEL_DOMAIN_ROW, ORIGIN, TOKENIZED, LABEL

def init_radio(txt_labeling):
    for i, label in enumerate(txt_labeling.files[LABEL].label_domain):
        radio_button = tk.Radiobutton(txt_labeling.app, text=label, value=label, variable=txt_labeling.picked_label)
        radio_button.grid(row=LABEL_DOMAIN_ROW,column=i)
        txt_labeling.label_domain.append(radio_button)
