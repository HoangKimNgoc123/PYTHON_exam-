import tkinter as tk
from tkinter import messagebox

class Critter:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.boredom = 0

    def pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def eat(self):
        self.hunger = max(0, self.hunger - 2)
        self.pass_time()

    def play(self):
        self.boredom = max(0, self.boredom - 2)
        self.pass_time()

    def sleep(self):
        self.boredom = max(0, self.boredom - 3)
        self.hunger += 1 
        self.pass_time()

class CritterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Critter Caretaker")
        self.critter = None

        self.frame = tk.Frame(root, padx=70, pady=60)
        self.frame.pack()

        # Entry để nhập tên
        self.entry = tk.Entry(self.frame, width=20)
        self.entry.pack(pady=5)

        self.create_btn = tk.Button(self.frame, text="Tạo", command=self.create_critter)
        self.create_btn.pack(pady=5)

        # Label hiển thị trạng thái
        self.name_label = tk.Label(self.frame, text="", font=("Arial", 12, "bold"))
        self.hunger_label = tk.Label(self.frame, text="")
        self.boredom_label = tk.Label(self.frame, text="")

        self.name_label.pack()
        self.hunger_label.pack()
        self.boredom_label.pack()

        # Nút hành động
        self.feed_btn = tk.Button(self.frame, text="Cho ăn", width=15, command=self.feed_critter)
        self.play_btn = tk.Button(self.frame, text="Chơi", width=15, command=self.play_critter)
        self.sleep_btn = tk.Button(self.frame, text="Ngủ", width=15, command=self.sleep_critter)

        self.feed_btn.pack(pady=2)
        self.play_btn.pack(pady=2)
        self.sleep_btn.pack(pady=2)

    def display_status(self):
        self.name_label.config(text=self.critter.name)
        self.hunger_label.config(text=f"Hunger: {self.critter.hunger}")
        self.boredom_label.config(text=f"Boredom: {self.critter.boredom}")

    def check_critter(self):
        if self.critter is None:
            messagebox.showerror("Lỗi", "Bạn chưa tạo Critter!")
            return False
        return True

    def create_critter(self):
        name = self.entry.get().strip()
        if name:
            self.critter = Critter(name)
            self.display_status()
        else:
            messagebox.showwarning("Lỗi", "Vui lòng nhập tên Critter.")
    
    def feed_critter(self):
        if self.check_critter():
            self.critter.eat()
            self.display_status()

    def play_critter(self):
        if self.check_critter():
            self.critter.play()
            self.display_status()

    def sleep_critter(self):
        if self.check_critter():
            self.critter.sleep()
            self.display_status()

if __name__ == "__main__":
    root = tk.Tk()
    app = CritterApp(root)
    root.mainloop()
