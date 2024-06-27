import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

# MySQL database connection configuration
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gurinder@27",
    database="futurense"
)

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = "grey"
        self.default_fg_color = self["fg"]

        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)

        self.put_placeholder()

    def _on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.default_fg_color)

    def _on_focus_out(self, event):
        if not self.get():
            self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self.config(fg=self.placeholder_color)

class LoginApp:
    def __init__(self, root, bg_image_path, form_image_path, db_connection):
        self.root = root
        self.root.title("FutureNse Login")
        self.root.geometry("1366x768")  # Full screen size

        self.db_connection = db_connection  # Store the database connection

        # Create main frames for layout
        self.left_frame = tk.Frame(root, width=683, height=768)  # Half width for left frame
        self.left_frame.pack(side='left', fill='both', expand=True)
        self.right_frame = tk.Frame(root, width=683, height=768, bg='white')  # Half width for right frame
        self.right_frame.pack(side='right', fill='both', expand=True)

        # Load and display background image
        self.bg_image = self.load_image(bg_image_path, (683, 768))

        self.canvas = tk.Canvas(self.left_frame, width=683, height=768)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor='nw')

        # Load and display form image
        self.form_image = self.load_image(form_image_path, (409, 146))

        # Create login form in the right frame
        self.create_login_form()

        # Initialize course IDs list
        self.course_ids = self.fetch_course_ids()  # Fetch course IDs from database

        self.notification_popup = tk.Toplevel(self.root)
        self.notification_popup.title("Notifications")
        self.notification_popup.geometry("500x350")
        self.notification_popup.configure(bg='white')
        self.notification_popup.withdraw()  # Hide initially

        notification_label = tk.Label(self.notification_popup, text="You have new notifications!", bg='white')
        notification_label.pack(pady=20)

        
    def load_image(self, path, size):
        try:
            image = Image.open(path)
            image = image.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(image)
        except IOError as e:
            print(f"Error loading image: {e}")
            return None

    def create_login_form(self):
        form_frame = tk.Frame(self.right_frame, bg='white', padx=20, pady=20)
        form_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Add form image
        image_label = tk.Label(form_frame, image=self.form_image, bg='white')
        image_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Username field
        username_label = tk.Label(form_frame, text="Username", font=("Helvetica", 12), bg='white')
        username_label.grid(row=1, column=0, sticky='w', pady=(20, 5))

        username_frame = tk.Frame(form_frame, bg='white')
        username_frame.grid(row=2, column=0, sticky='w')

        # Username entry
        self.username_entry = EntryWithPlaceholder(username_frame, placeholder="Username", width=30, font=("Helvetica", 12), bd=1)
        self.username_entry.grid(row=0, column=0, sticky="ew")

        # Password field
        password_label = tk.Label(form_frame, text="Password", font=("Helvetica", 12), bg='white')
        password_label.grid(row=3, column=0, sticky='w', pady=(20, 5))

        password_frame = tk.Frame(form_frame, bg='white')
        password_frame.grid(row=4, column=0, sticky='w')

        # Password entry
        self.password_entry = EntryWithPlaceholder(password_frame, placeholder="Password", width=30, font=("Helvetica", 12), show="*", bd=1)
        self.password_entry.grid(row=0, column=0, sticky="ew")

        # Remember username checkbox
        remember_var = tk.IntVar()
        remember_check = tk.Checkbutton(form_frame, text="Remember username", variable=remember_var, bg='white')
        remember_check.grid(row=5, column=0, columnspan=2, pady=5, sticky='w')

        # Login button
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="black", foreground="black")
        login_button = ttk.Button(form_frame, text="Log in", style="TButton", command=self.check_credentials)
        login_button.grid(row=6, column=0, columnspan=2, pady=10, ipadx=100)  # Increase button width

        # Forgotten username or password
        forgotten_label = tk.Label(form_frame, text="Forgotten your username or password?", font=("Helvetica", 10), fg="blue", bg='white')
        forgotten_label.grid(row=7, column=0, columnspan=2, pady=5, sticky='w')

    def fetch_course_ids(self):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT C_id FROM Courses"
            cursor.execute(query)
            course_ids = [row[0] for row in cursor.fetchall()]  # Fetch all course IDs into a list
            cursor.close()
            return course_ids
        except mysql.connector.Error as err:
            print(f"Error fetching course IDs: {err}")
            return []  # Return an empty list if there's an error

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Use the database connection stored in self.db_connection
        cursor = self.db_connection.cursor(dictionary=True)
        query = f"SELECT S_id FROM Login WHERE L_id = '{username}' AND Password = '{password}'"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()

        if result:
            messagebox.showinfo("Success", "Login Successful!")
            self.show_dashboard(result['S_id'])
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def show_dashboard(self, s_id):
        # Fetch student name (S_name) based on S_id
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = f"SELECT S_name FROM Student WHERE S_id = {s_id}"
            cursor.execute(query)
            student_info = cursor.fetchone()
            cursor.close()

            if student_info:
                student_name = student_info['S_name']
            else:
                student_name = "Unknown"

        except mysql.connector.Error as err:
            print(f"Error fetching student info: {err}")
            student_name = "Unknown"

        # Destroy the main window
        self.root.withdraw()

        # Create a new window for the dashboard
        dashboard_window = tk.Toplevel(self.root)
        dashboard_window.title("Dashboard")
        dashboard_window.geometry("1366x768")
        dashboard_window.configure(bg='white')

        # Create top frame for user info and navigation
        top_frame = tk.Frame(dashboard_window, bg='#F5F5F5', height=100)
        top_frame.pack(fill='x')

        # Random text on left side of navigation bar
        random_text_label = tk.Label(top_frame, text="Welcome to FutureNse!", font=("Helvetica", 16), bg='#F5F5F5')
        random_text_label.pack(side='left', padx=20)

        # User profile image placeholder
        user_image_path = r"C:\Users\ASUS\Desktop\OIP.jpeg"  # Replace with actual path
        user_image = self.load_image(user_image_path, (50, 50))
        user_image_label = tk.Label(top_frame, image=user_image, bg='#F5F5F5')
        user_image_label.image = user_image  # Keep a reference
        user_image_label.pack(side='right', padx=20)

        bell_icon = tk.Label(top_frame, text="🔔", font=("Arial", 24), cursor="hand2", bg='#F5F5F5')
        bell_icon.pack(side='right', padx=20)
        bell_icon.bind("<Button-1>", lambda e: self.toggle_notifications())

        # User name label
        user_name_label = tk.Label(top_frame, text=student_name, font=("Helvetica", 16), bg='#F5F5F5')
        user_name_label.pack(side='right')

        # Dashboard content frame
        content_frame = tk.Frame(dashboard_window, bg='white')
        content_frame.pack(fill='both', expand=True)

        # Left portion for courses section
        left_courses_frame = tk.Frame(content_frame, bg='white', width=683, padx=20, pady=20)
        left_courses_frame.pack(side='left', fill='both', expand=True)

        # Paths for course images
        course_images = [
            r"C:\Users\ASUS\Desktop\Data Structures   Algorithms.png",  # Replace with actual paths
            r"C:\Users\ASUS\Desktop\Database Design  and Modelling  (SQL).png  ",
            r"C:\Users\ASUS\Desktop\MicrosoftTeams-image (1).jpg  ",
            r"C:\Users\ASUS\Desktop\Data  Communication  and Computer  Networks.png"
        ]

        # Create grid for courses
        for i in range(2):
            for j in range(2):
                if i*2 + j < len(self.course_ids):
                    cid = self.course_ids[i*2 + j]

                    course_frame = tk.Frame(left_courses_frame, bg='white', bd=1, relief='solid', width=500, height=500)
                    course_frame.grid(row=i, column=j, padx=75, pady=50, sticky="nsew")

                    # Load and display course cover image
                    course_image_path = course_images[i*2 + j]
                    course_cover_image = self.load_image(course_image_path, (300, 150))
                    if course_cover_image:
                        course_cover_label = tk.Label(course_frame, image=course_cover_image, bg='white')
                        course_cover_label.image = course_cover_image  # Keep a reference
                        course_cover_label.pack(pady=(0, 5))

                    # Fetch and display course name based on C_id
                    course_name = self.fetch_course_name(cid)
                    course_title_label = tk.Label(course_frame, text=course_name, font=("Helvetica", 12, "bold"), bg='white')
                    course_title_label.pack()

                    # Course button
                    course_button = ttk.Button(course_frame, text="Get Started", command=lambda cid=cid: self.course_button_action(cid))
                    course_button.pack(pady=(5, 0))

        # Right portion for profile section
        right_profile_frame = tk.Frame(content_frame, bg='#F5F5F5', width=683, padx=20, pady=20)
        right_profile_frame.pack(side='right', fill='both', expand=True)

        # Fetch and display profile information
        profile_info = self.fetch_profile_info(s_id)

        # Profile section labels
        profile_labels = ["Name", "Degree", "Batch", "Ongoing Semester", "Roll No.", "Phone", "Email", "Address"]
        for index, label_text in enumerate(profile_labels):
            label = tk.Label(right_profile_frame, text=f"{label_text}: {profile_info[label_text]}", font=("Helvetica", 12), bg='#F5F5F5')
            label.grid(row=index, column=0, sticky='w', pady=5)

        # Logout button at the bottom
        logout_button = ttk.Button(right_profile_frame, text="Logout", command=self.logout)
        logout_button.grid(row=len(profile_labels) + 1, column=0, pady=20, sticky='w')

        # Back to Login button at the bottom
        back_button = ttk.Button(right_profile_frame, text="Back to Login", command=lambda: self.back_to_login(dashboard_window))
        back_button.grid(row=len(profile_labels) + 2, column=0, pady=10, sticky='w')

        # Run the dashboard window
        dashboard_window.mainloop()

    def fetch_profile_info(self, s_id):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = f"SELECT * FROM Student WHERE S_id = {s_id}"
            cursor.execute(query)
            profile_info = cursor.fetchone()
            cursor.close()

            if profile_info:
                return {
                    "Name": profile_info.get('S_name', ''),
                    "Degree": profile_info.get('Degree', ''),
                    "Batch": profile_info.get('Batch', ''),
                    "Ongoing Semester": profile_info.get('Ongoingsem', ''),
                    "Roll No.": profile_info.get('Rollno', ''),
                    "Phone": profile_info.get('Phone1', ''),
                    "Email": profile_info.get('Email', ''),
                    "Address": profile_info.get('Address', '')
                }
            else:
                return {
                    "Name": "Unknown",
                    "Degree": "Unknown",
                    "Batch": "Unknown",
                    "Ongoing Semester": "Unknown",
                    "Roll No.": "Unknown",
                    "Phone": "Unknown",
                    "Email": "Unknown",
                    "Address": "Unknown"
                }

        except mysql.connector.Error as err:
            print(f"Error fetching profile info: {err}")
            return {
                "Name": "Unknown",
                "Degree": "Unknown",
                "Batch": "Unknown",
                "Ongoing Semester": "Unknown",
                "Roll No.": "Unknown",
                "Phone": "Unknown",
                "Email": "Unknown",
                "Address": "Unknown"
            }

    def back_to_login(self, dashboard_window):
        dashboard_window.destroy()
        self.root.deiconify()
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.username_entry.put_placeholder()
        self.password_entry.put_placeholder()

    def logout(self):
        self.root.destroy()  # Close the entire application

    def course_button_action(self, cid):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = f"SELECT * FROM Courses WHERE C_id = {cid}"
            cursor.execute(query)
            course_info = cursor.fetchone()
            cursor.close()

            if course_info:
                messagebox.showinfo("Course Info", f"Course Name: {course_info['C_name']}, Teacher ID: {course_info['T_id']}")
            else:
                messagebox.showerror("Error", "Course details not found.")
        except mysql.connector.Error as err:
            print(f"Error fetching course info: {err}")
            messagebox.showerror("Error", "Failed to fetch course details.")

    def fetch_course_name(self, cid):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = f"SELECT C_name FROM Courses WHERE C_id = {cid}"
            cursor.execute(query)
            course_info = cursor.fetchone()
            cursor.close()

            if course_info:
                return course_info['C_name']
            else:
                return "Unknown"

        except mysql.connector.Error as err:
            print(f"Error fetching course name: {err}")
            return "Unknown"
    def toggle_notifications(self):
        if self.notification_popup.state() == "withdrawn":
            self.notification_popup.deiconify()
        else:
            self.notification_popup.withdraw()

# Initialize the application
if __name__ == "__main__":
    root = tk.Tk()
    bg_image_path = r"C:\Users\ASUS\Downloads\Screenshot (19).png"  # Replace with actual path
    form_image_path = r"C:\Users\ASUS\Desktop\LPU_X_Futurense_Logo.png"  # Replace with actual path
    app = LoginApp(root, bg_image_path, form_image_path, mydb)
    root.mainloop()
