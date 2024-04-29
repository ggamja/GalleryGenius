import os, shutil
from pathlib import Path

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import Checkbutton, BooleanVar, Label
from tkinter import filedialog, messagebox

from settings.config import Config

GUI_WIDTH = 1300
GUI_HEIGHT = 800
CANVAS_WIDTH = 850
CANVAS_HEIGHT = 700


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/chanbak/py_workplace/GalleryGenius/GalleryGenius/figma_gui/build/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ImageMoverApp:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry(f"{GUI_WIDTH}x{GUI_HEIGHT}")
        self.root.configure(bg=Config.window_color)
        
        
        self.image_folder_path = ""
        self.image_files = []
        self.current_img_idx = 1
        self.angle = 0
        self.target_folders = {'q': '', 'w': '', 'e': '', 'r': ''}
        self.target_folder_widgets_positions = {
            'q': {
                'checkbutton' : {'x': 18.5, 'y': 221},
                'path_label' : {'x': 68, 'y': 221},
                'button' : {'x': 165, 'y': 221+5},
            },
            'w': {
                'checkbutton' : {'x': 18.5, 'y': 240},
                'path_label' : {'x': 68, 'y': 240},
                'button' : {'x': 165, 'y': 240+5},
            },
            'e': {
                'checkbutton' : {'x': 18.5, 'y': 259},
                'path_label' : {'x': 68, 'y': 259},
                'button' : {'x': 165, 'y': 259+5},
            },
            'r': {
                'checkbutton' : {'x': 18.5, 'y': 278},
                'path_label' : {'x': 68, 'y': 278},
                'button' : {'x': 165, 'y': 278+5},
            },
            
        }
        self.selected_image_extensions = ('.jpg', '.jpeg', '.png', )
        self.selected_image_extensions = self.selected_image_extensions + tuple(ext.upper() for ext in self.selected_image_extensions)
        
        self.setup_ui()
        # self.bind_keyboard()
        
        # self.image_folder_path = "/Users/chanbak/Downloads/test_folder"
        # self.load_images()
        
    def setup_ui(self):
        main_canvas = Canvas(self.root, width=GUI_WIDTH, height=GUI_HEIGHT,
                        bg=Config.window_color, bd=0, highlightthickness=0, relief='ridge')
        main_canvas.place(x=0, y=0)
        main_canvas.create_rectangle(
            0, 0, Config.sidebar_width, Config.sidebar_height,
            fill=Config.sidebar_color, outline=""
        )
        
        self.image_groupbox_border = PhotoImage(
            file=relative_to_assets("image_1.png"))
        main_canvas.create_image(
            100.0, 134.0,
            image=self.image_groupbox_border
        )

        self.shortcut_groupbox_border = PhotoImage(
            file=relative_to_assets("image_2.png"))
        main_canvas.create_image(
            100.0, 274.0,
            image=self.shortcut_groupbox_border
        )
        
        self.photo_groupbox_border = PhotoImage(file=relative_to_assets("image_3.png"))
        main_canvas.create_image(
            Config.photo_canvas_background_x,
            Config.photo_canvas_background_y,
            image=self.photo_groupbox_border
        )
        
        self.simple_button_image = PhotoImage(
            file=relative_to_assets("button_1.png")
        )
        
        self.main_canvas = main_canvas
        self.photo_canvas = Canvas(
            main_canvas, 
            width=Config.canvas_width, height=Config.canvas_height,
            bg="#eeeeee",
            bd=0, highlightthickness=0, relief='ridge'
        )
        self.photo_canvas.place(
            x=Config.photo_canvas_background_x-Config.canvas_width // 2,
            y=Config.photo_canvas_background_y-Config.canvas_height // 2,
        )
        
        self.setup_sidebar_img_text_setting()
        self.setup_sidebar_img_widget_setting()
        self.setup_sidebar_shortcut_text_setting()
        self.setup_sidebar_shortcut_widget_setting()
        
        
    def setup_sidebar_img_text_setting(self):
        self.main_canvas.create_text(
            15.0, 17.0,
            anchor='nw', text="Easy Chuu",
            fill=Config.text_color, font=("Inter", 32 * -1)
        )
        
        self.main_canvas.create_text(
            18.0, 77.0,
            anchor='nw', text="이미지 경로",
            fill=Config.text_color, font=("Inter", 13 * -1)
        )
        
        self.main_canvas.create_text(
            18, 134,
            anchor='nw', text="파일명",
            fill=Config.text_color, font=("Inter", 13 * -1)
        )
        self.main_canvas.create_text(
            60.0, 134.0,
            anchor='nw', text=":",
            fill=Config.text_color, font=("Inter", 13 * -1)
        )
        # Label 변경 예정
        # self.main_canvas.create_text(
        #     71.0, 134.0,
        #     anchor='nw', text="file name",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
        
        self.main_canvas.create_text(
            18.0, 165.0,
            anchor="nw", text="Index",
            fill=Config.text_color, font=("Inter", 13 * -1)
        )
        self.main_canvas.create_text(
            60.9, 165.0,
            anchor="nw", text=":",
            fill=Config.text_color, font=("Inter", 13 * -1)
        )
        self.main_canvas.create_text(
            130.0, 165.0,
            anchor="nw", text="/",
            fill=Config.text_color, font=("Inter", 13 * -1)
        )
        # Label 변경 예정
        # self.main_canvas.create_text(
        #     68, 165,
        #     anchor="nw", text="8888",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
        # # Label 변경 예정
        # self.main_canvas.create_text(
        #     133.0, 165.0,
        #     anchor="nw", text="8888",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
    
    def setup_sidebar_img_widget_setting(self):
        self.image_dirctory_label = Label(
            text="Select Image Directory",
            anchor="nw", font=("Inter", 13 * -1),
            background=Config.sidebar_color,
            foreground=Config.text_color
        )
        self.image_dirctory_label.place(
            x=18.0,
            y=99.0
        )
        self.image_directory_button = Button(
            image=self.simple_button_image,
            command=self.choose_image_directory,
            background=Config.sidebar_color,
            foreground=Config.text_color,
            highlightbackground=Config.sidebar_color,
            highlightcolor=Config.sidebar_color,
            highlightthickness=0,
            activebackground=Config.sidebar_color,
            activeforeground=Config.text_color,
            relief="flat"
        )
        self.image_directory_button.place(
            x=165.0,
            y=99.0
        )
        
        self.image_filename_label = Label(
            text="file name", anchor="nw", font=("Inter", 13 * -1),
            background=Config.sidebar_color,
            foreground=Config.text_color
        )
        self.image_filename_label.place(
            x=71.0,
            y=130.0
        )
        
        self.image_index_spinbox = tk.Spinbox(
            from_=1, to=99999, increment=1,
            command=self.update_image_index_from_spinbox,
            width=4, 
            background=Config.sidebar_color,
            foreground=Config.text_color,
            highlightbackground=Config.sidebar_color,
            highlightcolor=Config.sidebar_color,
            highlightthickness=0,
        )
        self.image_index_spinbox.place(
            x=68.0,
            y=165.0
        )
        self.image_index_spinbox.bind("<Return>", self.handle_spinbox_return)
        
        self.image_total_count_label = Label(
            text="99999", anchor="nw", font=("Inter", 13 * -1),
            background=Config.sidebar_color,
            foreground=Config.text_color
        )
        self.image_total_count_label.place(
            x=135.0,
            y=162.0
        )
    
    def choose_image_directory(self):
        image_folder_path = filedialog.askdirectory()
        if image_folder_path:
            self.image_folder_path = image_folder_path
            shorten_path = self.shorten_directory_path(self.image_folder_path, 25)
            self.image_dirctory_label.config(text=shorten_path)
            self.load_images()
    
    @staticmethod
    def shorten_directory_path(path, max_length=25):
        if max_length <= 5:
            raise ValueError("max_length must be greater than 5")
        
        if len(path) <= max_length:
            return path
        parts = path.split("/")
        if len(parts) == 1:
            return path[:max_length-5] + "..."
        elif len(parts) == 2:
            if len(parts[1]) <= max_length:
                return path
            else:
                return path[:max_length-5] + "..."

        first_part = parts[0]
        last_part = parts[-1]
        mid_part = "/..."
        for part in parts[1:-1]:
            if len(first_part) + len(mid_part) + len(last_part) + len(part) < max_length:
                first_part += "/" + part
            else:
                break
        return f"{first_part}{mid_part}/{last_part}" 
        
    def update_image_index_from_spinbox(self):
        pass
    
    def handle_spinbox_return(self, event):
        pass
        
     
    def setup_sidebar_shortcut_text_setting(self):
        # self.main_canvas.create_text(
        #     45, 223,
        #     anchor="nw", text="Q",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
        # self.main_canvas.create_text(
        #     60, 223,
        #     anchor="nw", text=":",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
        # self.main_canvas.create_text(
        #     68, 223,
        #     anchor="nw", text="Folder name",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
        
        # self.main_canvas.create_text(
        #     45, 242,
        #     anchor="nw", text="W",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
        # self.main_canvas.create_text(
        #     60, 242,
        #     anchor="nw", text=":",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
        # self.main_canvas.create_text(
        #     68, 242,
        #     anchor="nw", text="Folder name",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
        
        # self.main_canvas.create_text(
        #     45, 261,
        #     anchor="nw", text="E",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
        # self.main_canvas.create_text(
        #     60, 261,
        #     anchor="nw", text=":",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
        # self.main_canvas.create_text(
        #     68, 261,
        #     anchor="nw", text="Folder name",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
        
        # self.main_canvas.create_text(
        #     45, 280,
        #     anchor="nw", text="R",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
        # self.main_canvas.create_text(
        #     60, 280,
        #     anchor="nw", text=":",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
        # self.main_canvas.create_text(
        #     68, 280,
        #     anchor="nw", text="Folder name",
        #     fill=Config.text_color, font=("Inter", 13 * -1)
        # )
        
        self.main_canvas.create_text(
            18, 306, anchor="nw", text="F: ",
            fill=Config.text_color, font=("Inter", 13 * -1)
        )
        self.main_canvas.create_text(
            39, 306, anchor="nw", text="-90°",
            fill=Config.text_color, font=("Inter", 13 * -1)
        )
        self.main_canvas.create_text(
            78, 306, anchor="nw", text="G: ",
            fill=Config.text_color, font=("Inter", 13 * -1)
        )
        self.main_canvas.create_text(
            99, 306, anchor="nw", text="+90°",
            fill=Config.text_color, font=("Inter", 13 * -1)
        )
        self.main_canvas.create_text(
            138, 306, anchor="nw", text="V: ",
            fill=Config.text_color, font=("Inter", 13 * -1)
        )
        self.main_canvas.create_text(
            159, 306, anchor="nw", text="0°",
            fill=Config.text_color, font=("Inter", 13 * -1)
        )
    
    def setup_sidebar_shortcut_widget_setting(self):
        self.directory_checkbox_dict = {}
        self.directory_path_label_dict = {}
        self.directory_button_dict = {}
        self.directory_checkbox_states_dict = {}
        for i, key in enumerate(self.target_folders.keys()):
            checkbox_state = tk.BooleanVar()
            checkbox_state.set(True)
            self.directory_checkbox_states_dict[key] = checkbox_state
            
            checkbox = tk.Checkbutton(
                borderwidth=1, highlightthickness=1,
                text=f"{key.upper()} : ", 
                variable=checkbox_state,
                command=lambda: print("Check button clicked"),
                relief='flat',
                background=Config.sidebar_color,
                foreground=Config.text_color,
                font=("Courier")
            )
            checkbox.place(
                **self.target_folder_widgets_positions[key]['checkbutton'],
            )
            self.directory_checkbox_dict[key] = checkbox
            
            directory_path_label = tk.Label(
                text="Auto Mode".format(key=key),
                background=Config.sidebar_color,
                foreground=Config.text_color,
            )
            directory_path_label.place(
                **self.target_folder_widgets_positions[key]['path_label'],
            )
            self.directory_path_label_dict[key] = directory_path_label
            
            directory_button = tk.Button(
                image=self.simple_button_image,
                borderwidth=0, highlightthickness=0, 
                command=lambda k=key: self.choose_move_folder(k),
                relief="flat",
            )
            directory_button.place(
                **self.target_folder_widgets_positions[key]['button'],
            )
            self.directory_button_dict[key] = directory_button
            
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.choose_image_path)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        
    def undo(self):
        pass
    
    def redo(self):
        pass
    
    def bind_keyboard(self):
        self.root.bind("<Control-z>", lambda event: self.undo())
        self.root.bind("<Control-y>", lambda event: self.redo())
        self.root.bind("<Left>", lambda event: self.show_previous_image())
        self.root.bind("<Right>", lambda event: self.show_next_image())
        self.root.bind("<d>", lambda event: self.rotate_image(90))
        self.root.bind("<f>", lambda event: self.rotate_image(-90))
        self.root.bind("<v>", lambda event: self.show_org_image())
        
    
    def show_previous_image(self):
        if self.current_img_idx > 1:
            self.current_img_idx -= 1
            self.show_current_image()
            self.change_spinbox_value(self.current_img_idx)
    
    def show_next_image(self):
        if self.current_img_idx < len(self.image_files):
            self.current_img_idx += 1
            self.show_current_image()
            self.change_spinbox_value(self.current_img_idx)

    def change_spinbox_value(self, value):
        self.current_idx_spinbox.delete(0, tk.END)
        self.current_idx_spinbox.insert(0, str(value))

    def rotate_image(self, angle):
        self.angle = self.angle + angle
        self.show_current_image()
    
    def show_org_image(self):
        self.angle = 0
        self.show_current_image()
        
    def setup_user_frame_ui(self):
        self.image_info_frame = tk.LabelFrame(self.user_frame, text="Image Info", padx=5, pady=5)
        self.image_info_frame.grid(row=0, column=0, sticky='nsew')
        
        self.move_info_frame = tk.LabelFrame(self.user_frame, text="Move Info", padx=5, pady=5)
        self.move_info_frame.grid(row=0, column=1, sticky='nsew', padx=10)
        
    def setup_media_frame_ui(self):
        self.canvas_frame = tk.LabelFrame(self.media_frame, text="Canvas")
        self.canvas_frame.pack(pady=5, fill='both', expand=True)
        
    def setup_widgets(self):
        self.setup_image_info_directory()
        self.setup_image_informations()
        self.setup_move_dirctory_informations()
    
    def setup_canvas(self):
        self.canvas = tk.Canvas(self.canvas_frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack(padx=10, pady=10, fill='both', expand=True)

    def setup_image_info_directory(self):
        self.image_folder_path_label = tk.Label(self.image_info_frame, text="이미지 경로 :")
        self.image_folder_path_label.grid(row=0, column=0, sticky='w')
        
        self.image_path_selection_button = tk.Button(self.image_info_frame, text="Select", command=self.choose_image_path)
        self.image_path_selection_button.grid(row=0, column=1, sticky='e')
        
    def setup_move_dirctory_informations(self):
        self.init_directories()
        
    def init_directories(self):
        self.directory_checkbox_dict = {}
        self.directory_path_label_dict = {}
        self.directory_button_dict = {}
        self.directory_checkbox_states_dict = {}
        for i, key in enumerate(self.target_folders.keys()):
            checkbox_state = tk.BooleanVar()
            checkbox_state.set(True)
            self.directory_checkbox_states_dict[key] = checkbox_state
            
            checkbox = tk.Checkbutton(self.move_info_frame, text=f"{key.upper()} : ", variable=checkbox_state)
            checkbox.grid(row=i, column=0, sticky='w')
            self.directory_checkbox_dict[key] = checkbox
            
            directory_path_label = tk.Label(self.move_info_frame, text="현재 경로는 자동 생성 폴더입니다.".format(key=key))
            directory_path_label.grid(row=i, column=1, sticky='w')
            self.directory_path_label_dict[key] = directory_path_label
            
            directory_button = tk.Button(self.move_info_frame, text="Select", command=lambda k=key: self.choose_move_folder(k))
            directory_button.grid(row=i, column=2, sticky='e')
            self.directory_button_dict[key] = directory_button
        
    def choose_move_folder(self, key):
        directory = filedialog.askdirectory()
        self.target_folders[key] = directory
        self.display_selected_move_directory(key)
        
    def display_selected_move_directory(self, key):
        directory = self.target_folders[key]
        if directory is not None:
            self.directory_path_label_dict[key]['text'] = directory
        else:
            self.directory_path_label_dict[key]['text'] = "현재 경로는 자동 생성 폴더입니다."
        
    def setup_image_informations(self):
        self.current_image_label = tk.Label(self.image_info_frame, text="현재 파일명 : ")
        self.current_image_label.grid(row=1, column=0, sticky='w')
        
        self.current_idx_label = tk.Label(self.image_info_frame, text="Image Index : ")
        self.current_idx_label.grid(row=2, column=0, sticky='w')
        self.current_idx_spinbox = tk.Spinbox(self.image_info_frame, width=8, 
                                              from_=1, to=1, increment=1,
                                              command=self.update_image_idx_from_spinbox)
        self.current_idx_spinbox.bind('<Return>', self.handle_spinbox_return)
        self.current_idx_spinbox.grid(row=2, column=1, sticky='w')

        self.total_images_label = tk.Label(self.image_info_frame, text="   / total count")
        self.total_images_label.grid(row=2, column=2, sticky='w')
        
    # Functions for widget function
    def choose_image_path(self):
        image_folder_path = filedialog.askdirectory()
        if image_folder_path:
            self.image_folder_path = image_folder_path 
        if self.image_folder_path:
            self.image_folder_path_label.config(text="이미지 경로 : " + self.image_folder_path)
            print("Image Path is selected : " + self.image_folder_path)
            self.load_images()
        
    def load_images(self):
        self.image_files = [f for f in os.listdir(self.image_folder_path) if f.endswith(self.selected_image_extensions)]
        self.total_images_label['text'] = f"   /  {len(self.image_files)}"
        self.init_spinbox()
        if self.image_files:
            self.show_current_image()
        else:
            self.show_init()
            
    def show_init(self):
        self.current_image_label.config(text="현재 파일명 : ")
        self.current_idx_label.config(text="Image Index : ")
        self.current_idx_spinbox.config(from_=1, to=1, increment=1)
        self.current_img_idx = 1
    
    def show_current_image(self):
        if self.image_files:
            self.canvas.delete("all")
            
            current_image_file = self.image_files[self.current_img_idx-1]
            current_image_path = os.path.join(self.image_folder_path, current_image_file)
            
            image = Image.open(current_image_path)
            image = image.rotate(self.angle, expand=True)
            # image = image.resize((CANVAS_WIDTH, CANVAS_HEIGHT), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=photo)
            self.canvas.image = photo
            
            self.current_image_label.config(text="현재 파일명 : " + current_image_file)
            # self.current_idx_label.config(text="Image Index : " + str(self.current_img_idx))
            
    def handle_spinbox_return(self, event):
        self.update_image_idx_from_spinbox()
        
    def update_image_idx_from_spinbox(self):
        new_idx = self.current_idx_spinbox.get()
        if new_idx:
            new_idx = int(new_idx)
            
            if new_idx < 1:
                new_idx = 1
            elif new_idx > len(self.image_files):
                new_idx = len(self.image_files)
                
            self.current_img_idx = new_idx
            self.change_spinbox_value(new_idx)
            self.show_current_image()
    
    def init_spinbox(self):
        self.current_idx_spinbox.config(from_=1, to=len(self.image_files) if self.image_files else 0, increment=1)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageMoverApp(root)
    root.mainloop()