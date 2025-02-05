import customtkinter as ctk
from PIL import Image
from frames.levels_frame import LevelsFrame
from frames.activity_frame import ActivityFrame
from frames.compare_frame import CompareFrame


def fetch_player_data(username):
    """Fetch player data from the API."""
    from api.api_client import fetch_player_data  # Import here to avoid circular imports
    return fetch_player_data(username)

class RuneScapeStats(ctk.CTk):
    """Main application class."""
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("RuneScape Stats Lookup")
        self.geometry("500x800")

        # Main container frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Top frame for logo and search
        self.top_frame = ctk.CTkFrame(self.main_frame)
        self.top_frame.pack(fill="x", pady=(0, 10))

        # Logo placeholder
        self.label_image = ctk.CTkImage(Image.open("assets/logo.jpg"), size=(60, 60))
        self.logo_label = ctk.CTkLabel(self.top_frame, image=self.label_image, text="")
        self.logo_label.pack(side="left", padx=10, pady=10)

        # Search entry
        self.search_entry = ctk.CTkEntry(self.top_frame, placeholder_text="Enter username...")
        self.search_entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)

        # Submit button
        self.submit_button = ctk.CTkButton(self.top_frame, text="Search", command=self.on_submit)
        self.submit_button.pack(side="left", padx=10, pady=10)

        # Navigation buttons frame
        self.nav_frame = ctk.CTkFrame(self.main_frame)
        self.nav_frame.pack(fill="x", pady=(0, 10))

        # Navigation buttons
        self.levels_button = ctk.CTkButton(self.nav_frame, text="Skills", command=self.on_levels_button_clicked)
        self.levels_button.pack(side="left", padx=5, pady=5)

        self.activity_button = ctk.CTkButton(self.nav_frame, text="Activity Highscores", command=self.on_activity_button_clicked)
        self.activity_button.pack(side="left", padx=5, pady=5)

        self.compare_button = ctk.CTkButton(self.nav_frame, text="Compare", command=lambda: self.show_frame("compare"))
        self.compare_button.pack(side="left", padx=5, pady=5)

        # Initialize frames
        self.frames = {"levels": LevelsFrame(self.main_frame, self),
                       "activity": ActivityFrame(self.main_frame, self),
                       "compare": CompareFrame(self.main_frame, self)}

        # Show the default frame
        self.show_frame("levels")

        #Switches to Levels Frame and resizes geometry to default
    def on_levels_button_clicked(self):
        """Show the levels frame and change window size geometry"""
        self.show_frame("levels")
        self.geometry("500x800")

    def on_activity_button_clicked(self):
        """Show the activity frame and change window size geometry"""
        self.show_frame("activity")
        self.geometry("650x800")
        
    def show_frame(self, frame_name):
        """Show the selected frame and hide the others."""
        if hasattr(self, "current_frame"):
            self.current_frame.pack_forget()
        self.current_frame = self.frames[frame_name]
        self.current_frame.pack(fill="both", expand=True)

    def on_submit(self):
        """Handle the search submission."""
        username = self.search_entry.get()
        player_data = fetch_player_data(username)
        if player_data:
            self.frames["levels"].update_skill_labels(player_data)
            self.frames["activity"].update_activity_labels(player_data)

