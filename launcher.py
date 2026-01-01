import tkinter as tk
from tkinter import messagebox
import webbrowser
import pygame

# ---------------- MUSIC ----------------
pygame.mixer.init()
pygame.mixer.music.load("bg.mp3")
pygame.mixer.music.play(-1)

# ---------------- FILES ----------------
USER_FILE = "users.txt"
ADMIN_FILE = "admins.txt"

# ---------------- CHECK LOGIN ----------------
def check_login():
    u = username.get()
    p = password.get()

    if check_admin(u, p):
        login.destroy()
        open_admin_panel()
        return

    if check_user(u, p):
        login.destroy()
        open_launcher()
        return

    messagebox.showerror("Error", "Invalid login")

def check_user(u, p):
    try:
        with open(USER_FILE) as f:
            for line in f:
                user, pwd = line.strip().split(":")
                if u == user and p == pwd:
                    return True
    except:
        pass
    return False

def check_admin(u, p):
    try:
        with open(ADMIN_FILE) as f:
            for line in f:
                user, pwd = line.strip().split(":")
                if u == user and p == pwd:
                    return True
    except:
        pass
    return False

# ---------------- ADMIN PANEL ----------------
def open_admin_panel():
    admin = tk.Tk()
    admin.title("ADMIN PANEL")
    admin.geometry("500x400")
    admin.configure(bg="#0a0a0a")

    tk.Label(admin, text="ADMIN PANEL", fg="red",
             bg="#0a0a0a", font=("Arial Black", 22)).pack(pady=15)

    # add user
    new_user = tk.Entry(admin)
    new_user.pack(pady=5)
    new_user.insert(0, "username")

    new_pass = tk.Entry(admin)
    new_pass.pack(pady=5)
    new_pass.insert(0, "password")

    def add_user():
        with open(USER_FILE, "a") as f:
            f.write(f"\n{new_user.get()}:{new_pass.get()}")
        messagebox.showinfo("Done", "User Added")

    tk.Button(admin, text="➕ Add User",
              command=add_user,
              bg="red", fg="black", width=20).pack(pady=8)

    # view users
    def view_users():
        data = open(USER_FILE).read()
        messagebox.showinfo("Users", data)

    tk.Button(admin, text="📄 View Users",
              command=view_users,
              bg="#222", fg="white", width=20).pack(pady=6)

    # open launcher
    tk.Button(admin, text="🚀 Open Launcher",
              command=lambda: [admin.destroy(), open_launcher()],
              bg="#111", fg="red", width=20).pack(pady=20)

    admin.mainloop()

# ---------------- MAIN LAUNCHER ----------------
def open_launcher():
    app = tk.Tk()
    app.title("BAKU ARENA")
    app.geometry("600x420")
    app.configure(bg="#050505")

    title = tk.Label(app, text="⚡ BAKU ARENA ⚡",
                     fg="red", bg="#050505",
                     font=("Arial Black", 26))
    title.pack(pady=20)

    def neon():
        colors = ["red", "#ff3c3c", "#ff0000"]
        i = 0
        def loop():
            nonlocal i
            title.config(fg=colors[i])
            i = (i + 1) % len(colors)
            app.after(300, loop)
        loop()

    neon()

    btn = {
        "font": ("Arial", 12, "bold"),
        "width": 25,
        "height": 2,
        "bg": "#111",
        "fg": "red"
    }

    tk.Button(app, text="🎮 Open Game Store",
              command=lambda: webbrowser.open("https://store.steampowered.com"),
              **btn).pack(pady=6)

    tk.Button(app, text="▶ YouTube",
              command=lambda: webbrowser.open("https://youtube.com/@bakuarena"),
              **btn).pack(pady=6)

    tk.Button(app, text="📸 Instagram",
              command=lambda: webbrowser.open("https://instagram.com/_raghav__247"),
              **btn).pack(pady=6)

    tk.Button(app, text="🔊 Music ON",
              command=lambda: pygame.mixer.music.play(-1),
              **btn).pack(pady=6)

    tk.Button(app, text="🔇 Music OFF",
              command=pygame.mixer.music.stop,
              **btn).pack(pady=6)

    app.mainloop()

# ---------------- LOGIN WINDOW ----------------
login = tk.Tk()
login.title("Login")
login.geometry("350x260")
login.configure(bg="#0a0a0a")

tk.Label(login, text="LOGIN",
         fg="red", bg="#0a0a0a",
         font=("Arial Black", 22)).pack(pady=10)

username = tk.Entry(login, font=("Arial", 12))
username.pack(pady=8)
username.insert(0, "username")

password = tk.Entry(login, font=("Arial", 12), show="*")
password.pack(pady=8)
password.insert(0, "password")

tk.Button(login, text="LOGIN",
          bg="red", fg="black",
          font=("Arial", 12, "bold"),
          command=check_login).pack(pady=15)

login.mainloop()
