
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import Checkbutton, BooleanVar, Label
from tkinter import filedialog, messagebox
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/chanbak/py_workplace/GalleryGenius/GalleryGenius/figma_gui/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def choose_image_path():
    image_folder_path = filedialog.askdirectory()
    if image_folder_path:
        image_directory_label.config(text=image_folder_path)
        # load_images(image_folder_path)

            
window = Tk()

window.geometry("1300x800")
window.configure(bg = "#E9E2E2")


canvas = Canvas(
    window,
    bg = "#E9E2E2",
    height = 800,
    width = 1300,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    200.0,
    800.0,
    fill="#F1F1F1",
    outline="")

canvas.create_text(
    60.0,
    134.0,
    anchor="nw",
    text=":",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    126.0,
    165.0,
    anchor="nw",
    text="/",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    60.0,
    165.0,
    anchor="nw",
    text=":",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    15.0,
    17.0,
    anchor="nw",
    text="Easy Chu",
    fill="#000000",
    font=("Inter", 32 * -1)
)

canvas.create_text(
    18.0,
    134.0,
    anchor="nw",
    text="파일명",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    71.0,
    134.0,
    anchor="nw",
    text="file name",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    18.0,
    165.0,
    anchor="nw",
    text="Index",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    68.0,
    165.0,
    anchor="nw",
    text="8888",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    133.0,
    165.0,
    anchor="nw",
    text="8888",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    18.0,
    77.0,
    anchor="nw",
    text="이미지 경로",
    fill="#000000",
    font=("Inter", 13 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    100.0,
    134.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    100.0,
    274.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=choose_image_path,
    relief="flat"
)
button_1.place(
    x=166.0,
    y=78.0,
    width=16.0,
    height=15.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=166.0,
    y=224.0,
    width=16.0,
    height=15.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=166.0,
    y=243.0,
    width=16.0,
    height=15.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=166.0,
    y=262.0,
    width=16.0,
    height=15.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=166.0,
    y=281.0,
    width=16.0,
    height=15.0
)

canvas.create_text(
    60.0,
    223.0,
    anchor="nw",
    text=":",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    45.0,
    223.0,
    anchor="nw",
    text="Q",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    68.0,
    223.0,
    anchor="nw",
    text="Folder name",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    60.0,
    242.0,
    anchor="nw",
    text=":",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    44.0,
    242.0,
    anchor="nw",
    text="W",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    68.0,
    242.0,
    anchor="nw",
    text="Folder name",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    60.0,
    261.0,
    anchor="nw",
    text=":",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    46.0,
    261.0,
    anchor="nw",
    text="E",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    68.0,
    261.0,
    anchor="nw",
    text="Folder name",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    60.0,
    280.0,
    anchor="nw",
    text=":",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    46.0,
    280.0,
    anchor="nw",
    text="R",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    18.0,
    306.0,
    anchor="nw",
    text="F : ",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    39.0,
    306.0,
    anchor="nw",
    text="-90°",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    78.0,
    306.0,
    anchor="nw",
    text="G : ",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    99.0,
    306.0,
    anchor="nw",
    text="+90°",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    138.0,
    306.0,
    anchor="nw",
    text="V : ",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    159.0,
    306.0,
    anchor="nw",
    text="0°",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    68.0,
    280.0,
    anchor="nw",
    text="Folder name",
    fill="#000000",
    font=("Inter", 13 * -1)
)

# canvas.create_text(
#     18.0,
#     99.0,
#     anchor="nw",
#     text="Choose Directory",
#     fill="#000000",
#     font=("Inter", 10 * -1)
# )

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    746.0,
    421.0,
    image=image_image_3
)

########################################################################
# self made

image_directory_label = Label(
    text="Choose Directory",
    font=("Inter", 10 * -1),
    background="#F1F1F1",
    foreground="#000000",
    anchor="nw"
)
image_directory_label.place(
    x=18.0,
    y=99.0
)


checkbtn_q_var = BooleanVar()
checkbtn_w_var = BooleanVar()
checkbtn_e_var = BooleanVar()
checkbtn_r_var = BooleanVar()
checkbtn_state_dict = {
    'q': checkbtn_q_var,
    'w': checkbtn_w_var,
    'e': checkbtn_e_var,
    'r': checkbtn_r_var,
}
for var in checkbtn_state_dict.values():
    var.set(True)

checkbtn_q = Checkbutton(
    borderwidth=1,
    highlightthickness=1,
    command=lambda: print("checkbtn_q clicked"),
    relief="flat",
    variable=checkbtn_q_var,
    background="#F1F1F1",
)
checkbtn_q.place(
    x=18.5,
    y=221.0,
)

checkbtn_w = Checkbutton(
    borderwidth=1,
    highlightthickness=1,
    command=lambda: print("checkbtn_w clicked"),
    relief="flat",
    variable=checkbtn_w_var,
    background="#F1F1F1",
)
checkbtn_w.place(
    x=18.5,
    y=240.0,
)

checkbtn_e = Checkbutton(
    borderwidth=1,
    highlightthickness=1,
    command=lambda: print("checkbtn_e clicked"),
    relief="flat",
    variable=checkbtn_e_var,
    background="#F1F1F1",
)
checkbtn_e.place(
    x=18.5,
    y=259.0,
)

checkbtn_r = Checkbutton(
    borderwidth=1,
    highlightthickness=1,
    command=lambda: print("checkbtn_r clicked"),
    relief="flat",
    variable=checkbtn_r_var,
    background="#F1F1F1",
)
checkbtn_r.place(
    x=18.5,
    y=278.0,
)

################################################################
window.resizable(False, False)
window.mainloop()
