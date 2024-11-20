import tkinter as tk
from tkinter import ttk
import random
import math
import time

class WheelOfNames(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wheel of Names")
        self.geometry("800x600")
        self.configure(bg="#2b2b2b")

        self.listbox = tk.Listbox(self, width=30, height=10, bg="#3b3b3b", fg="white", 
        selectbackground="green", relief=tk.SOLID, bd=1)
        self.listbox.place(x=50, y=100)

        # Create the canvas for the wheel
        self.canvas = tk.Canvas(self, width=400, height=400, bg="#2b2b2b", highlightthickness=0)
        self.canvas.place(x=200, y=100)

        # Create the input field and buttons
        self.entry = ttk.Entry(self, font=("Arial", 16))
        self.entry.place(x=200, y=500, width=200, height=40)

        self.add_button = ttk.Button(self, text="Tambahkan", command=self.add_name)
        self.add_button.place(x=420, y=500, width=100, height=40)

        self.reset_button = ttk.Button(self, text="Reset", command=self.reset_names)
        self.reset_button.place(x=530, y=500, width=100, height=40)

        self.spin_button = ttk.Button(self, text="SPIN!", command=self.spin_wheel)
        self.spin_button.place(x=640, y=500, width=100, height=40)

        self.result_label = ttk.Label(self, text="", font=("Arial", 16), foreground="white", background="#2b2b2b")
        self.result_label.place(x=200, y=550)

        self.names = []
        self.current_angle = 0
        self.colors = ["#FF5733", "#33FF57", "#3357FF", "#F1C40F", "#8E44AD", "#E67E22", "#1ABC9C"]

        self.draw_wheel()

    def add_name(self):
        new_name = self.entry.get().strip()
        if new_name:
            self.names.append(new_name)
            self.listbox.insert(tk.END, new_name)
            self.entry.delete(0, tk.END)
            self.draw_wheel()

    def reset_names(self):
        self.names.clear()
        self.listbox.delete(0, tk.END)
        self.result_label.configure(text="")
        self.draw_wheel()

    def spin_wheel(self):
        if not self.names:
            self.result_label.configure(text="Tambahkan elemen terlebih dahulu!", foreground="red")
            return

        self.result_label.configure(text="Spinning...", foreground="white")
        self.update()

        spins = random.randint(30, 50)
        speed = 0.01
        for _ in range(spins):
            self.current_angle = (self.current_angle + 15) % 360
            self.draw_wheel()
            self.update()
            time.sleep(speed)
            speed += 0.005

        sector_size = 360 / len(self.names)
        adjusted_angle = (360 - self.current_angle) % 360
        index = int(adjusted_angle / sector_size)
        if index >= len(self.names):
            index = 0

        final_choice = self.names[index]
        self.result_label.configure(text=f"Pemenang: {final_choice}", foreground="green")

    def draw_wheel(self):
        self.canvas.delete("all")
        num_names = len(self.names)
        if num_names == 0:
            self.canvas.create_oval(50, 50, 350, 350, outline="#808080", width=2, fill="#424242")
            return

        angle_per_sector = 360 / num_names
        start_angle = self.current_angle
        center_x = 200
        center_y = 200
        radius = 150

        self.canvas.create_oval(50, 50, 350, 350, outline="white", width=2)

        for i, name in enumerate(self.names):
            end_angle = start_angle + angle_per_sector

            if num_names == 1:
                self.canvas.create_arc(50, 50, 350, 350, start=0, extent=360, fill="red", outline="white", tags="wheel")
            else:
                self.canvas.create_arc(50, 50, 350, 350, start=start_angle, extent=angle_per_sector, fill=self.colors[i % len(self.colors)], outline="white", tags="wheel")

            text_angle = math.radians((start_angle + end_angle) / 2)
            x = center_x + (radius * 0.7) * math.cos(text_angle)
            y = center_y - (radius * 0.7) * math.sin(text_angle)
            rotation = (start_angle + angle_per_sector / 2) + 90
            if 90 <= rotation <= 270:
                rotation += 180

            self.canvas.create_text(x, y, text=name, fill="white", font=("Arial", 12, "bold"), angle=rotation, tags="wheel")
            start_angle = end_angle

        self.canvas.create_polygon(
            350, 200, 350 + 15, 200 - 15, 350 + 15, 200 + 15,
            fill="red", outline="white", width=2, tags="indicator"
        )

if __name__ == "__main__":
    app = WheelOfNames()
    app.mainloop()