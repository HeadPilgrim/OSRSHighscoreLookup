import customtkinter as ctk

class ActivityFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Create a canvas and a vertical scrollbar
        self.canvas = ctk.CTkCanvas(self, highlightthickness=0)
        self.scrollbar = ctk.CTkScrollbar(self, orientation="vertical", command=self.canvas.yview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas)

        # Configure grid layout (3 columns x 28 rows)
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        for i in range(28):
            self.grid_rowconfigure(i, weight=1)

        # Configure the canvas
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        # Add the scrollable frame to the canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack the canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Initialize an empty activities list
        self.activities = []

        # Initialize an empty list to hold activity labels
        self.activity_labels = []

        # Configure grid for activities (3 columns)
        for i in range(3):
            self.scrollable_frame.grid_columnconfigure(i, weight=1)

    def update_activity_labels(self, player_data):
        """Update the activity labels with player data and generate the activities list."""
        # Extract the activities data from player_data
        activity_data = player_data['activities']

        # Generate the activities list dynamically
        self.activities = [activity['name'] for activity in activity_data]

        # Clear existing activity labels (if any)
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.activity_labels = []

        # Create activity frames and labels dynamically
        for i, activity in enumerate(self.activities):
            row = i // 3  # Calculate row (3 activities per row)
            col = i % 3   # Calculate column

            # Create a frame for each activity
            activity_frame = ctk.CTkFrame(self.scrollable_frame)
            activity_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

            # Activity name label
            activity_label = ctk.CTkLabel(activity_frame, text=activity)
            activity_label.pack(pady=5)

            # Activity score label (initially empty)
            score_label = ctk.CTkLabel(activity_frame, text="")
            score_label.pack(pady=2)
            self.activity_labels.append(score_label)

        # Update the score labels with the player data
        for i, activity_label in enumerate(self.activity_labels):
            score = activity_data[i]['score']
            activity_label.configure(text=f"Score: {0 if score == -1 else score}")