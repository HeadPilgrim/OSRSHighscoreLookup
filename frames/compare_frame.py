import customtkinter as ctk

class CompareFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Add compare content here
        compare_label = ctk.CTkLabel(self, text="Compare Content")
        compare_label.pack(pady=20)