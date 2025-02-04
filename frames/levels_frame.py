import customtkinter as ctk

class LevelsFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Initialize an empty skills list
        self.skills = []

        # Initialize an empty list to hold skill labels
        self.skill_labels = []

        # Configure grid layout (3 columns x 8 rows)
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        for i in range(8):
            self.grid_rowconfigure(i, weight=1)

    def update_skill_labels(self, player_data):
        """Update the skill labels with player data and generate the skills list."""
        # Extract the skills data from player_data
        skills_data = player_data['skills']

        # Generate the skills list dynamically
        self.skills = [skill['name'] for skill in skills_data]

        # Clear existing skill labels (if any)
        for widget in self.winfo_children():
            widget.destroy()
        self.skill_labels = []

        # Create skill frames and labels dynamically
        for i, skill in enumerate(self.skills):
            row = i // 3  # Calculate row (3 skills per row)
            col = i % 3   # Calculate column

            # Create a frame for each skill
            skill_frame = ctk.CTkFrame(self)
            skill_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

            # Skill name label
            skill_label = ctk.CTkLabel(skill_frame, text=skill)
            skill_label.pack(pady=5)

            # Skill level label (initially empty)
            level_label = ctk.CTkLabel(skill_frame, text="")
            level_label.pack(pady=2)
            self.skill_labels.append(level_label)

        # Update the level labels with the player data
        for i, skill_label in enumerate(self.skill_labels):
            skill_label.configure(text=f"Level: {skills_data[i]['level']}")