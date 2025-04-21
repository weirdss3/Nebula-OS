import tkinter as tk
from tkinter import simpledialog, messagebox, colorchooser
import random

# --- Constants ---
USERNAME = "nebula"
PASSWORD = "1234"

# --- App Class ---
class NebulaOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Nebula OS")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e1e")
        self.dark_mode = True

        self.login_screen()

    # --- Login Screen ---
    def login_screen(self):
        self.clear_screen()
        self.login_frame = tk.Frame(self.root, bg="#2e2e2e")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.login_frame, text="Nebula OS Login", fg="white", bg="#2e2e2e", font=("Segoe UI", 16)).pack(pady=10)
        self.user_entry = tk.Entry(self.login_frame)
        self.pass_entry = tk.Entry(self.login_frame, show="*")
        self.user_entry.pack(pady=5)
        self.pass_entry.pack(pady=5)

        tk.Button(self.login_frame, text="Login", command=self.check_login).pack(pady=10)

    def check_login(self):
        if self.user_entry.get() == USERNAME and self.pass_entry.get() == PASSWORD:
            self.desktop()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")

    # --- Desktop ---
    def desktop(self):
        self.clear_screen()

        self.taskbar = tk.Frame(self.root, bg="#111", height=40)
        self.taskbar.pack(side="bottom", fill="x")

        self.label_battery = tk.Label(self.taskbar, text=f"🔋 {random.randint(50, 100)}%", fg="white", bg="#111")
        self.label_battery.pack(side="right", padx=10)

        tk.Button(self.taskbar, text="🌐 Google", command=self.launch_google).pack(side="left", padx=5)
        tk.Button(self.taskbar, text="🎮 NebulaX", command=self.launch_nebula).pack(side="left", padx=5)
        tk.Button(self.taskbar, text="📝 Notes", command=self.launch_notes).pack(side="left", padx=5)
        tk.Button(self.taskbar, text="🖌️ Paint", command=self.launch_paint).pack(side="left", padx=5)
        tk.Button(self.taskbar, text="⚙️ Settings", command=self.launch_settings).pack(side="left", padx=5)
        tk.Button(self.taskbar, text="🛒 Store", command=self.launch_store).pack(side="left", padx=5)

        self.notify("Welcome, nebula 👽")

    # --- Apps ---
    def create_window(self, title):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry("400x300")
        win.configure(bg="#2a2a2a" if self.dark_mode else "#f0f0f0")
        return win

    def launch_google(self):
        win = self.create_window("Fake Google")
        tk.Label(win, text="Search the fake web:", bg=win["bg"], fg="white" if self.dark_mode else "black").pack(pady=10)
        tk.Entry(win, width=30).pack(pady=5)

    def launch_nebula(self):
        win = self.create_window("NebulaX")
        tk.Label(win, text="Welcome to NebulaX - your fake Roblox!", bg=win["bg"], fg="white" if self.dark_mode else "black").pack(pady=10)

    def launch_notes(self):
        win = self.create_window("Notes")
        txt = tk.Text(win, bg="black", fg="lime" if self.dark_mode else "black")
        txt.pack(expand=True, fill="both")

    def launch_store(self):
        win = self.create_window("Nebula App Store")
        apps = ["NebulaX", "Notes", "Paint", "Settings"]
        for app in apps:
            tk.Label(win, text=f"📦 {app}", bg=win["bg"], fg="white" if self.dark_mode else "black").pack(pady=2)

    def launch_settings(self):
        win = self.create_window("Settings")
        def toggle_mode():
            self.dark_mode = not self.dark_mode
            self.desktop()
            win.destroy()

        tk.Button(win, text="Toggle Dark Mode", command=toggle_mode).pack(pady=20)

    def launch_paint(self):
        win = self.create_window("Paint")

        canvas = tk.Canvas(win, bg="white")
        canvas.pack(fill="both", expand=True)

        def draw(event):
            x, y = event.x, event.y
            r = 3
            canvas.create_oval(x - r, y - r, x + r, y + r, fill="black")

        canvas.bind("<B1-Motion>", draw)

    # --- Notifications ---
    def notify(self, msg):
        popup = tk.Toplevel(self.root)
        popup.overrideredirect(1)
        popup.geometry("200x50+600+500")
        popup.configure(bg="#222")

        tk.Label(popup, text=msg, fg="white", bg="#222").pack(expand=True)

        popup.after(3000, popup.destroy)

    # --- Utility ---
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = NebulaOS(root)
    root.mainloop()

