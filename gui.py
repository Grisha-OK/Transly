from pystray import MenuItem as item
import pystray
from PIL import Image
import customtkinter
import sys
import os

class TranslyGUI:
    def __init__(self, file_icon_path, switch_off, shron, push_config_file):

        self.file_icon_path = file_icon_path
        self.switch_off = switch_off
        self.shron = shron
        self.push_config_file = push_config_file

        # Create an instance of the tkinter frame or window
        self.win = customtkinter.CTk()
        self.win.title("Transly")
        self.win.iconbitmap(file_icon_path)
        self.win.geometry("300x85")
        customtkinter.set_widget_scaling(0.85)

        self._create_widgets()
        self._setup_tray()

    def _create_widgets(self):
        # Add a separating border
        self.frame = customtkinter.CTkFrame(self.win)
        self.frame.pack(fill='both', side='left', expand=True)

        # Add indentation
        customtkinter.CTkLabel(self.frame, text="Changing the layout:", font=(0, 17)
                               ).pack(side='top', pady=10)
        customtkinter.CTkLabel(self.win, text="   ", fg_color="transparent"
                               ).pack(side='top', pady=0)
        
        # Add a button to exit the program
        customtkinter.CTkButton(self.win, text="Quit", font=(0, 17), command=lambda: sys.exit(),
                                fg_color="gray10", corner_radius=16).pack(
                                    side='top',
                                    padx=(10,10),
                                    pady=(0,20),
                                    ipadx=5,
                                    ipady=5)
        
        # Specifically the toggle itself:
        self.is_on = customtkinter.BooleanVar(value=False)
        self.toggle_button = customtkinter.CTkSwitch(
            self.frame,
            text="", width=10,
            variable=self.is_on, onvalue="on",
            offvalue="off", command=lambda: self._toggle_switch())
        self.toggle_button.pack(side='top')
        
        if self.switch_off:
            self.toggle_button.select()
   
    #Check window closing and tray icon initialization
    def _setup_tray(self):
        self.win.protocol('WM_DELETE_WINDOW', self._hide_window)
    
    # Function true/false switch
    def _toggle_switch(self):
        self.switch_off = not(self.switch_off)
        self.shron["switch_off"] = self.switch_off
        self.push_config_file(self.shron)
    
    # Hide the window and show it on the system taskbar
    def _hide_window(self):
       self.win.withdraw()
       image = Image.open(self.file_icon_path)
       menu = (item('Quit', lambda : self._quit_window(self.icon)),
               item('Show', lambda : self._show_window(self.icon)))
       self.icon = pystray.Icon("name", image, "Trans Translation", menu)
       self.icon.run()
    
    # Define a function to exit the window / and by compatibility for exiting the entire program
    def _quit_window(self):
           self.icon.stop()
           os.abort()
    
    # A function for re-displaying the window
    def _show_window(self):
        self.icon.stop()
        self.win.deiconify() #I'll probably leave it here <win.after(0,win.deiconify())>

    def run(self):
        self.win.mainloop() 