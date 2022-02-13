from tkinter import *
import Program_do_faktur2
class Settings:
    def settings(self):
        self.Settings_frame = Frame(self.root, height=self.screen_height, width=self.screen_width,
                                    bg=self.background_color)
        self.Settings_frame.grid()
        self.Settings_frame.grid_propagate(0)

        dark_mode = Button(master=self.Settings_frame, text="Dark mode", font=Program_do_faktur2.self.basic_font, fg=self.foreground_color,
                           bg=self.background_color,
                           command=lambda: [(self.Settings_frame.grid_forget(), self.darkmode(), self.settings())])
        dark_mode.grid(column=3, row=0, sticky=NS, pady=5)

        light_mode = Button(master=self.Settings_frame, text="Light mode", font=Program_do_faktur2.self.basic_font, fg=self.foreground_color,
                            bg=self.background_color,
                            command=lambda: [(self.Settings_frame.grid_forget(), self.lightmode(), self.settings())])
        light_mode.grid(column=3, row=1, sticky=NS, pady=5)

        Back_But = Button(self.Settings_frame, text="Back to menu", font=Program_do_faktur2.self.basic_font, fg=self.foreground_color,
                          bg=self.background_color,
                          command=lambda: [self.Settings_frame.grid_forget(), self.menu()])
        Back_But.grid(column=3, row=2)