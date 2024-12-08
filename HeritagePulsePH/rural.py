import tkinter as tk
from PIL import Image, ImageTk

def create_header(parent_frame, app):
    """Create the header with the website name (text) and logo next to each other, with the text first."""
    complementary_color_1 = "#003366"
    accent_color_1 = "#FF8C00"

    header_frame = tk.Frame(parent_frame, bg=complementary_color_1)
    header_frame.pack(fill="x", pady=10)

    # Create a frame for logo and text together
    logo_text_frame = tk.Frame(header_frame, bg=complementary_color_1)
    logo_text_frame.pack(side="right")

    # Add the website name first (text)
    website_name = tk.Label(
        logo_text_frame, text="HeritagePulsePH",
        font=("Helvetica", 18, "bold"), fg=accent_color_1, bg=complementary_color_1
    )
    website_name.pack(side="left", padx=10)  # Position the website name on the left side

    # Add the logo next to the text
    if hasattr(app, "logo_image") and app.logo_image:  # Ensure app has a logo_image attribute
        logo_label = tk.Label(logo_text_frame, image=app.logo_image, bg=complementary_color_1)
        logo_label.pack(side="left", padx=10)  # Position the logo after the text

def show_images_for_dance(parent_frame, dance_name, image_paths, app):
    """Display the images for the selected dance."""
    # Clear previous content
    for widget in parent_frame.winfo_children():
        widget.destroy()

    main_color = "#F5F5DC"
    accent_color_2 = "#FF8C00"

    # Add the header
    create_header(parent_frame, app)

    # Create a canvas and scrollbar for scrolling
    canvas = tk.Canvas(parent_frame, bg=main_color)
    scrollbar = tk.Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=main_color)

    # Configure the canvas
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

            # Resize the image to fit the frame width, maintaining aspect ratio
            frame_width = parent_frame.winfo_width()
            img_width = frame_width - 40  # Leave some padding
            aspect_ratio = img.width / img.height
            img_height = int(img_width / aspect_ratio)
            img_resized = img.resize((img_width, img_height), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img_resized)

            img_label = tk.Label(scrollable_frame, image=img_tk, bg=main_color)
            img_label.image = img_tk  # Keep a reference to prevent garbage collection
            img_label.pack(pady=20, anchor="center")  # Center the image
        except Exception as e:
            print(f"Error loading image {path}: {e}")

    # Add Back to Dashboard button
    back_button = tk.Button(
        scrollable_frame, text="Back to Dashboard", bg=accent_color_2, fg="white",
        command=lambda: app.create_dashboard()  # Call the app's create_dashboard method
    )
    back_button.pack(pady=20)

def show_rural_section(root, parent_frame, app):
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
        "Salakban": [
            "assets/Salakban.jpg", "assets/Salakban_2.jpg", "assets/Salakban_3.jpg",
            "assets/Salakban_4.jpg", "assets/Salakban_5.jpg", "assets/Salakban_6.jpg",
            "assets/Salakban_7.jpg", "assets/Salakban_8.jpg", "assets/Salakban_9.jpg"
        ],
        "Polka Sa Nayon": [
            "assets/Polka_Sa_Nayon.jpg", "assets/PolkaSaNayon_2.jpg"
        ],
        "Jota Vizcayana": [
            "assets/Jota_Vizcayana.jpg", "assets/Jota_Vizcayana_2.jpg", "assets/Jota_Vizcayana_3.jpg",
            "assets/Jota_Vizcayana_4.jpg", "assets/Jota_Vizcayana_5.jpg", "assets/Jota_Vizcayana_6.jpg"
        ],
        "Infantes": [
            "assets/Infantes.jpg", "assets/Infantes_2.jpg", "assets/Infantes_3.jpg",
            "assets/Infantes_4.jpg", "assets/Infantes_5.jpg", "assets/Infantes_6.jpg",
            "assets/Infantes_7.jpg", "assets/Infantes_8.jpg"
        ],
        "Pabayle Iloco": [
            "assets/Pabayle_Iloco.jpg", "assets/Pabayle_Iloco_2.jpg", "assets/Pabayle_Iloco_3.jpg",
            "assets/Pabayle_Iloco_4.jpg", "assets/Pabayle_Iloco_5.jpg", "assets/Pabayle_Iloco_6.jpg",
            "assets/Pabayle_Iloco_7.jpg"
        ],
        "Los Bailes De San Antonio": [
            "assets/Los_Bailes_De_San_Antonio.jpg", "assets/Los_Bailes_De_San_Antonio_2.jpg", "assets/Los_Bailes_De_San_Antonio_3.jpg",
            "assets/Los_Bailes_De_San_Antonio_4.jpg", "assets/Los_Bailes_De_San_Antonio_5.jpg"
        ]
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
        command=lambda: app.create_dashboard()  # Call the app's create_dashboard method
    )
    back_button.pack(pady=20)
