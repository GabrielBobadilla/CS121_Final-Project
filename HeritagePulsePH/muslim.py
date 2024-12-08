import tkinter as tk
from PIL import Image, ImageTk
import os

class HeritagePulseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HeritagePulsePH")
        self.root.geometry("800x600")
        self.logo_image = self.load_logo_image()

        # Create the main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        # Create dashboard content
        self.create_dashboard()

    def load_logo_image(self):
        """Load the logo image for the app."""
        try:
            logo_path = "assets/logo.png"  # Adjust path to your logo
            img = Image.open(logo_path)
            img_resized = img.resize((50, 50), Image.LANCZOS)
            return ImageTk.PhotoImage(img_resized)
        except Exception as e:
            print(f"Error loading logo: {e}")
            return None

    def create_dashboard(self):
        """Create the main dashboard with buttons to navigate to sections."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        dashboard_frame = tk.Frame(self.main_frame)
        dashboard_frame.pack(fill="both", expand=True)

        # Add the header
        create_header(dashboard_frame, self)

        # Add buttons for sections
        muslim_button = tk.Button(
            dashboard_frame, text="Muslim", command=lambda: show_muslim_section(self.root, dashboard_frame, self)
        )
        muslim_button.pack(pady=20)

        # Other section buttons can be added here (e.g., Rural, Cordillera, etc.)

    def run(self):
        self.root.mainloop()

def create_header(parent_frame, app):
    """Create the header with the website name (text) and logo next to each other."""
    complementary_color_1 = "#003366"
    accent_color_1 = "#FF8C00"

    header_frame = tk.Frame(parent_frame, bg=complementary_color_1)
    header_frame.pack(fill="x", pady=10)

    logo_text_frame = tk.Frame(header_frame, bg=complementary_color_1)
    logo_text_frame.pack(side="right")

    # Website name
    website_name = tk.Label(
        logo_text_frame, text="HeritagePulsePH",
        font=("Helvetica", 18, "bold"), fg=accent_color_1, bg=complementary_color_1
    )
    website_name.pack(side="left", padx=10)

    # Logo
    if hasattr(app, "logo_image") and app.logo_image:
        logo_label = tk.Label(logo_text_frame, image=app.logo_image, bg=complementary_color_1)
        logo_label.pack(side="left", padx=10)

def show_images_for_dance(parent_frame, dance_name, image_paths, app):
    """Display the images for the selected dance."""
    # Clear previous content
    for widget in parent_frame.winfo_children():
        widget.destroy()

    main_color = "#F5F5DC"
    accent_color_2 = "#FF8C00"

    # Add the header
    create_header(parent_frame, app)

    # Create canvas and scrollbar for scrolling
    canvas = tk.Canvas(parent_frame, bg=main_color)
    scrollbar = tk.Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=main_color)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Display the dance title
    tk.Label(
        scrollable_frame, text=f"{dance_name} Dance", font=("Helvetica", 18, "bold"),
        bg=main_color
    ).pack(pady=10)

    # Display images
    for path in image_paths:
        try:
            img = Image.open(path)

            # Resize image to fit the frame width
            frame_width = parent_frame.winfo_width()
            img_width = frame_width - 40
            aspect_ratio = img.width / img.height
            img_height = int(img_width / aspect_ratio)
            img_resized = img.resize((img_width, img_height), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img_resized)

            img_label = tk.Label(scrollable_frame, image=img_tk, bg=main_color)
            img_label.image = img_tk  # Keep reference
            img_label.pack(pady=20, anchor="center")
        except Exception as e:
            print(f"Error loading image {path}: {e}")

    # Add Back to Dashboard button
    back_button = tk.Button(
        scrollable_frame, text="Back to Dashboard", bg=accent_color_2, fg="white",
        command=lambda: app.create_dashboard()
    )
    back_button.pack(pady=20)

def show_muslim_section(root, parent_frame, app):
    """Allow the user to choose a dance and view its images."""
    # Clear previous content
    for widget in parent_frame.winfo_children():
        widget.destroy()

    main_color = "#F5F5DC"
    accent_color_2 = "#FF8C00"

    # Add the header
    create_header(parent_frame, app)

    # Create the menu for dances
    dances = {
        "Maral Dad Libun": [
            "assets/Maral Dad Libun_1.jpg", "assets/Maral Dad Libun_2.jpg", "assets/Maral Dad Libun_3.jpg",
            "assets/Maral Dad Libun_4.jpg", "assets/Maral Dad Libun_5.jpg", "assets/Maral Dad Libun_6.jpg",
            "assets/Maral Dad Libun_7.jpg", "assets/Maral Dad Libun_8.jpg", "assets/Maral Dad Libun_9.jpg",
            "assets/Maral Dad Libun_10.jpg", "assets/Maral Dad Libun_11.jpg", "assets/Maral Dad Libun_12.jpg",
            "assets/Maral Dad Libun_13.jpg"
        ],
    }

    # Display the dance options
    options_frame = tk.Frame(parent_frame, bg=main_color)
    options_frame.pack(pady=20)
    tk.Label(
        options_frame, text="Select a Dance to View:", font=("Helvetica", 16, "bold"),
        bg=main_color
    ).pack(pady=10)

    for dance_name, image_paths in dances.items():
        dance_button = tk.Button(
            options_frame, text=dance_name, bg=accent_color_2, fg="white",
            command=lambda name=dance_name, paths=image_paths: show_images_for_dance(parent_frame, name, paths, app)
        )
        dance_button.pack(pady=10, fill="x", padx=20)

    # Add Back to Dashboard button
    back_button = tk.Button(
        parent_frame, text="Back to Dashboard", bg=accent_color_2, fg="white",
        command=lambda: app.create_dashboard()
    )
    back_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = HeritagePulseApp(root)
    app.run()
