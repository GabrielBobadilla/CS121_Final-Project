import mysql.connector
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from cordillera import show_cordillera_section
from western_influence import show_western_influence_section
from rural import show_rural_section
from muslim import show_muslim_section

class HeritagePulsePHApp:
    def __init__(self, root):
        self.root = root
        self.root.title("")  # Remove title
        self.root.geometry("900x600")  # Set the window size
        self.logo_path = "assets/HPPH.png"  # Logo path

        # Define color scheme
        self.main_color = "#F5F5DC"  # Warm beige
        self.complementary_color_1 = "#003366"  # Deep blue/navy blue
        self.complementary_color_2 = "#6B8E23"  # Vibrant green
        self.accent_color_1 = "#FFD700"  # Rich gold
        self.accent_color_2 = "#FF8C00"  # Burnt orange

        # Preload the logo once and reuse
        self.logo_image = self.load_logo()

        # Initialize MySQL connection
        self.db_connection = self.connect_to_db()

        self.dance_mapping = {
            "Futageh": (show_cordillera_section, "Cordillera"),
            "Jota Rizal": (show_western_influence_section, "Western Influence"),
            "Komintang": (show_western_influence_section, "Western Influence"),
            "Polka Sa Nayon": (show_rural_section, "Rural"),
            "Salakban": (show_rural_section, "Rural"),
            "Jota Vizcayana": (show_rural_section, "Rural"),
            "Infantes": (show_rural_section, "Rural"),
            "Pabayle Iloco": (show_rural_section, "Rural"),
            "Los Bailes De San Antonio": (show_rural_section, "Rural"),
            "Maral Dad Libun": (show_muslim_section, "Muslim"),
            # Add more dances as needed
        }

        # Create login screen when app starts
        self.create_login_screen()

    def connect_to_db(self):
        """Establish a connection to the MySQL database."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Default XAMPP username
                password="",  # Default XAMPP password is empty
                database="heritagepulseph"  # The database you created
            )
            return connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def load_logo(self):
        """Load the logo once and return the PhotoImage object."""
        try:
            img = Image.open(self.logo_path)
            img = img.resize((100, 100), Image.Resampling.LANCZOS)  # Resize logo
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading logo: {e}")
            return None

    def check_login(self):
        """Handle the login logic with database check."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        cursor = self.db_connection.cursor()
        query = "SELECT password FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if result and result[0] == password:
            self.create_dashboard()
        else:
            messagebox.showerror("Login Error", "Invalid username or password!")
        cursor.close()

    def register_user(self):
        """Register a new user in the database."""
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()
        role = self.role_var.get()

        if not username or not password:
            messagebox.showerror("Registration Error", "All fields are required!")
            return

        cursor = self.db_connection.cursor()
        query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query, (username, password, role))
            self.db_connection.commit()
            messagebox.showinfo("Registration Successful", "Account created successfully!")
            self.create_login_screen()
        except mysql.connector.IntegrityError:
            messagebox.showerror("Registration Error", "Username already exists!")
        finally:
            cursor.close()

    def delete_account(self):
        """Handle account deletion."""
        username = self.username_entry.get()

        if not username:
            messagebox.showerror("Delete Account Error", "Please enter a username.")
            return

        confirmation = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the account '{username}'?")
        if confirmation:
            cursor = self.db_connection.cursor()
            query = "DELETE FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            self.db_connection.commit()
            cursor.close()

            messagebox.showinfo("Account Deleted", "Your account has been deleted successfully.")
            self.create_login_screen()

    def create_dashboard(self):
        """Clear the current view and create the dashboard."""
        for widget in self.root.winfo_children():
            widget.destroy()

        self.dashboard_frame = tk.Frame(self.root, bg=self.main_color)
        self.dashboard_frame.pack(fill="both", expand=True)

        self.create_header()  # Search bar is part of the header
        self.create_sidebar()
        self.add_mission_vision_goals()

    def add_mission_vision_goals(self):
        """Add mission, vision, and goals to the dashboard."""
        info_frame = tk.Frame(self.dashboard_frame, bg=self.main_color)
        info_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Adjusted padding

        mission_text = (
        "To promote and preserve the diverse cultural heritage of the Philippines through "
        "a comprehensive exploration of traditional dances, literature, and local practices, "
        "fostering understanding and appreciation among younger generations."
        )
        vision_text = (
        "HeritagePulsePH envisions a future where the rich cultural legacy of the Philippines is "
        "celebrated, shared, and passed on to future generations, ensuring the continuity of these traditions "
        "through education, research, and engagement."
        )
        goals_text = (
        "1. To educate the public on the significance of Filipino folk dances and literature.\n"
        "2. To serve as a digital platform for preserving cultural knowledge.\n"
        "3. To facilitate the appreciation of Filipino heritage across local and global audiences."
        )

        # Configure labels with word wrapping
        tk.Label(info_frame, text="Mission", font=("Helvetica", 14, "bold"), fg="black", bg=self.main_color).pack(pady=5)
        tk.Label(info_frame, text=mission_text, font=("Helvetica", 12), fg="black", bg=self.main_color, wraplength=600).pack(pady=5)

        tk.Label(info_frame, text="Vision", font=("Helvetica", 14, "bold"), fg="black", bg=self.main_color).pack(pady=5)
        tk.Label(info_frame, text=vision_text, font=("Helvetica", 12), fg="black", bg=self.main_color, wraplength=600).pack(pady=5)

        tk.Label(info_frame, text="Goals", font=("Helvetica", 14, "bold"), fg="black", bg=self.main_color).pack(pady=5)
        tk.Label(info_frame, text=goals_text, font=("Helvetica", 12), fg="black", bg=self.main_color, wraplength=600, justify="left").pack(pady=5)


    def create_header(self):
        """Create the header with the logo, title, and search bar."""
        header_frame = tk.Frame(self.dashboard_frame, bg=self.complementary_color_1)
        header_frame.pack(fill="x", pady=10)

        # Left side: Search bar
        search_frame = tk.Frame(header_frame, bg=self.complementary_color_1)
        search_frame.pack(side="left", padx=10)

        search_label = tk.Label(search_frame, text="Search:", bg=self.complementary_color_1, fg="white", font=("Helvetica", 12, "bold"))
        search_label.pack(side="left", padx=5)

        self.search_entry = tk.Entry(search_frame, width=40, font=("Helvetica", 12))
        self.search_entry.pack(side="left", padx=5)

        search_button = tk.Button(
        search_frame, text="Search", command=self.perform_search, bg=self.accent_color_2, fg="white", font=("Helvetica", 12, "bold")
        )
        search_button.pack(side="left", padx=5)

        # Right side: Logo and title
        right_frame = tk.Frame(header_frame, bg=self.complementary_color_1)
        right_frame.pack(side="right", padx=10)

        if self.logo_image:
            logo_label = tk.Label(right_frame, image=self.logo_image, bg=self.complementary_color_1)
            logo_label.pack(side="left", padx=5)

        # Add the "HeritagePulsePH" text next to the logo
        title_label = tk.Label(
        right_frame,
        text="HeritagePulsePH",
        font=("Helvetica", 16, "bold"),
        fg="white",
        bg=self.complementary_color_1
        )
        title_label.pack(side="left", padx=5)

    def create_sidebar(self):
        """Create the sidebar with sections."""
        # Create the sidebar frame with a consistent background color
        sidebar_frame = tk.Frame(self.dashboard_frame, bg=self.complementary_color_1, padx=10, pady=10)
        sidebar_frame.pack(side="left", fill="y")  # Pack the sidebar to the left and fill vertically

        # Define sections to be added to the sidebar
        sections = ["Cordillera", "Western Influence", "Rural", "Muslim"]

        # Create buttons for each section
        for section in sections:
            section_button = tk.Button(
                sidebar_frame,
                text=section,
                command=lambda sec=section: self.show_section(sec),  # Pass the section name to the handler
                bg=self.accent_color_2,  # Use accent color for the button background
                fg="white",  # White text for contrast
                font=("Helvetica", 12, "bold"),  # Styling for the button text
                relief="flat",  # Flat design for buttons
                padx=10,
                pady=5
            )
            section_button.pack(fill="x", pady=10)  # Pack buttons horizontally and add vertical spacing
        
        # Add Log Out button at the bottom of the sidebar
        logout_button = tk.Button(
            sidebar_frame,
            text="Log Out",
            command=self.logout,
            bg="red",  # Red color for emphasis
            fg="white",
            font=("Helvetica", 12, "bold"),
            relief="flat",
            padx=10,
            pady=5
        )
        logout_button.pack(side="bottom", pady=10)  # Pack it at the bottom

    def logout(self):
        """Handle log out with confirmation."""
        confirmation = messagebox.askyesno(
            "Log Out Confirmation", "Are you sure you want to log out your account?"
        )
        if confirmation:
            self.create_login_screen()  # Redirect back to the login screen

    def perform_search(self):
        """Perform the search and navigate to the appropriate section."""
        search_query = self.search_entry.get().strip()

        # Check if the search query matches any dance in the mapping
        if search_query in self.dance_mapping:
            # Get the function to call and the section name
            section_function, section_name = self.dance_mapping[search_query]

            # Show a message indicating which section will be displayed
            messagebox.showinfo("Search Result", f"Displaying {section_name} section for {search_query}")

            # Call the relevant section function to display the content
            section_function(self.root, self.dashboard_frame, self)  # Make sure these functions are set up to display content
        else:
            # If the dance is not found, show an error message
            messagebox.showerror("Search Error", f"Dance '{search_query}' not found in the database.")

    def show_section(self, section_name):
        """Show the content of the selected section."""
        if section_name == "Cordillera":
            show_cordillera_section(self.root, self.dashboard_frame, self)  # Pass required arguments
        elif section_name == "Western Influence":
            show_western_influence_section(self.root, self.dashboard_frame, self)
        elif section_name == "Rural":
            show_rural_section(self.root, self.dashboard_frame, self)
        elif section_name == "Muslim":
            show_muslim_section(self.root, self.dashboard_frame, self)

    def create_login_screen(self):
        """Create the login screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

        login_frame = tk.Frame(self.root, bg=self.main_color)
        login_frame.pack(fill="both", expand=True)

        if self.logo_image:
            logo_label = tk.Label(login_frame, image=self.logo_image, bg=self.main_color)
            logo_label.pack(pady=20)

        username_label = tk.Label(login_frame, text="Username", font=("Helvetica", 12), bg=self.main_color)
        username_label.pack(pady=5)
        self.username_entry = tk.Entry(login_frame, font=("Helvetica", 12))
        self.username_entry.pack(pady=5)

        password_label = tk.Label(login_frame, text="Password", font=("Helvetica", 12), bg=self.main_color)
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(login_frame, show="*", font=("Helvetica", 12))
        self.password_entry.pack(pady=5)

        login_button = tk.Button(
        login_frame,
        text="Login",
        command=self.check_login,
        bg=self.accent_color_1,
        fg="white",
        font=("Helvetica", 12, "bold"),
        relief="flat"
        )
        login_button.pack(pady=10)

        signup_button = tk.Button(
        login_frame,
        text="Sign Up",
        command=self.create_signup_screen,
        bg=self.accent_color_2,
        fg="white",
        font=("Helvetica", 12, "bold"),
        relief="flat"
        )
        signup_button.pack(pady=5)

        delete_button = tk.Button(
        login_frame,
        text="Delete Account",
        command=self.delete_account,
        bg="red",
        fg="white",
        font=("Helvetica", 12, "bold"),
        relief="flat"
        )
        delete_button.pack(pady=10)


    def create_signup_screen(self):
        """Create a signup screen with role selection."""
        for widget in self.root.winfo_children():
            widget.destroy()

        signup_frame = tk.Frame(self.root, bg=self.main_color)
        signup_frame.pack(fill="both", expand=True)

        if self.logo_image:
            logo_label = tk.Label(signup_frame, image=self.logo_image, bg=self.main_color)
            logo_label.pack(pady=20)

        username_label = tk.Label(signup_frame, text="Username", font=("Helvetica", 12), bg=self.main_color)
        username_label.pack(pady=5)
        self.signup_username_entry = tk.Entry(signup_frame, font=("Helvetica", 12))
        self.signup_username_entry.pack(pady=5)

        password_label = tk.Label(signup_frame, text="Password", font=("Helvetica", 12), bg=self.main_color)
        password_label.pack(pady=5)
        self.signup_password_entry = tk.Entry(signup_frame, show="*", font=("Helvetica", 12))
        self.signup_password_entry.pack(pady=5)

        role_label = tk.Label(signup_frame, text="Role", font=("Helvetica", 12), bg=self.main_color)
        role_label.pack(pady=5)

        self.role_var = tk.StringVar(value="Student")  # Default role
        role_dropdown = tk.OptionMenu(signup_frame, self.role_var, "Student", "Dancer", "Dance Researcher", "Choreographer")
        role_dropdown.config(font=("Helvetica", 12), bg=self.main_color)
        role_dropdown.pack(pady=5)

        signup_button = tk.Button(
            signup_frame,
            text="Sign Up",
            command=self.register_user,
            bg=self.accent_color_1,
            fg="white",
            font=("Helvetica", 12, "bold"),
            relief="flat"
        )
        signup_button.pack(pady=10)

        back_button = tk.Button(
            signup_frame,
            text="Back to Login",
            command=self.create_login_screen,
            bg=self.accent_color_2,
            fg="white",
            font=("Helvetica", 12, "bold"),
            relief="flat"
        )
        back_button.pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = HeritagePulsePHApp(root)
    root.mainloop()