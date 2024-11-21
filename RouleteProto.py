import tkinter as tk
from tkinter import messagebox
import random
import math
import time

def add_name():
    """Tambahkan nama ke list."""
    new_name = entry.get().strip()
    if new_name:
        names.append(new_name)
        listbox.insert(tk.END, new_name)
        entry.delete(0, tk.END)
        draw_wheel()
        draw_arrow()

def reset_names():
    """Reset daftar nama."""
    names.clear()
    listbox.delete(0, tk.END)
    result_label.config(text="")
    draw_wheel()
    draw_arrow()

def spin_wheel():
    """Putar roda dengan animasi."""
    global current_angle

    spins = random.randint(30, 50)
    speed = 0.0001
    for _ in range(spins):
        current_angle = (current_angle + 15) % 360
        draw_wheel()
        draw_arrow()
        root.update()
        time.sleep(speed)
        speed += 0.005

    # Menghitung pemenang berdasarkan posisi panah
    sector_size = 360 / len(names)
    
    # Menyesuaikan sudut karena panah di sebelah kanan (0 derajat)
    # Dan roda berputar berlawanan arah jarum jam
    adjusted_angle = (360 - current_angle) % 360
    
    # Menghitung indeks yang sesuai dengan posisi panah
    index = int(adjusted_angle / sector_size)
    if index >= len(names):
        index = 0
        
    final_choice = names[index]
    
    messagebox.showinfo("You got a choice!", f"Pilihan untukmu adalah:\n\n{final_choice}")
    result_label.config(text=f"Pemenang: {final_choice}", fg="green")

def draw_wheel():
    """Gambar roda dan bagiannya di Canvas."""
    canvas.delete("all")
    num_names = len(names)
    if num_names == 0:
        return

    center_x = 200  # Posisi x dari tengah roda
    center_y = 200  # Posisi y dari tengah roda
    radius = 150    # Radius roda

    #Jika Hanya Menginputkan 1 elemen saja, Warna lingkaran akan berubah menjadi blossom pink
    if num_names == 1:
        canvas.create_oval(50, 50, 350, 350, fill="#F9B7FF", outline="white", width=2)
        canvas.create_text(center_x, center_y, 
                           text=names[0], 
                           fill="black", 
                           font=("Arial", 16, "bold"))
        return
    angle_per_sector = 360 / num_names
    start_angle = current_angle

    # Tambahkan lingkaran luar sebagai border
    canvas.create_oval(50, 50, 350, 350, outline="white", width=2)

    for i, name in enumerate(names):
        end_angle = start_angle + angle_per_sector

        # Gambar sektor
        canvas.create_arc(50, 50, 350, 350, 
                            start=start_angle, 
                            extent=angle_per_sector,
                            fill=colors[i % len(colors)], 
                            outline="white", 
                            tags="wheel")

        # Sesuaikan posisi dan rotasi teks
        text_angle = math.radians((start_angle + end_angle) / 2)
        x = center_x + (radius * 0.7) * math.cos(text_angle)
        y = center_y - (radius * 0.7) * math.sin(text_angle)

        # Rotasi teks agar lebih mudah dibaca
        rotation = (start_angle + angle_per_sector / 2) + 90
        if 90 <= rotation <= 270:
            rotation += 180

        canvas.create_text(x, y, 
                            text=name, 
                            fill="black", 
                            font=("Arial", 12, "bold"), 
                            angle=rotation,
                            tags="wheel")

        start_angle = end_angle

    """Gambar roda dan bagiannya di Canvas."""
    canvas.delete("all")
    num_names = len(names)
    if num_names == 0:
        return

    # Gambar roda
    angle_per_sector = 360 / num_names
    start_angle = current_angle
    center_x = 200
    center_y = 200
    radius = 150  # Radius roda

    # Tambahkan lingkaran luar sebagai border
    canvas.create_oval(50, 50, 350, 350, outline="white", width=2)

    for i, name in enumerate(names):
        end_angle = start_angle + angle_per_sector

        # Gambar sektor
        canvas.create_arc(50, 50, 350, 350, 
                         start=start_angle, 
                         extent=angle_per_sector,
                         fill=colors[i % len(colors)], 
                         outline="white", 
                         tags="wheel")

        # Sesuaikan posisi dan rotasi teks
        text_angle = math.radians((start_angle + end_angle) / 2)
        x = center_x + (radius * 0.7) * math.cos(text_angle)
        y = center_y - (radius * 0.7) * math.sin(text_angle)
        
        # Rotasi teks agar lebih mudah dibaca
        rotation = (start_angle + angle_per_sector / 2) + 90
        if 90 <= rotation <= 270:
            rotation += 180

        canvas.create_text(x, y, 
                         text=name, 
                         fill="black", 
                         font=("Arial", 12, "bold"), 
                         angle=rotation,
                         tags="wheel")

        start_angle = end_angle

def draw_arrow():
    # Gambar panah di sisi kanan yang mengarah ke dalam
    arrow_size = 20
    arrow_base = 15
    arrow_x = 350  # Posisi x di sisi kanan roda
    arrow_y = 200  # Tengah vertikal

    # Titik-titik untuk membentuk panah yang mengarah ke dalam
    points = [
        arrow_x, arrow_y,  # Ujung panah (paling kiri)
        arrow_x + arrow_base, arrow_y - arrow_size,  # Ujung atas
        arrow_x + arrow_base, arrow_y + arrow_size,  # Ujung bawah
    ]
    
    # Buat panah yang mengarah ke dalam dan tidak berputar
    canvas.create_polygon(
        points,
        fill="#9F000F",  #Mengubah Warna Panah
        outline="black",
        width=2,
        tags="indicator"
    )

    # Gambar panah di sisi kanan yang mengarah ke dalam
    arrow_size = 20
    arrow_base = 15
    arrow_x = 350  # Posisi x di sisi kanan roda
    arrow_y = 200  # Tengah vertikal

    # Titik-titik untuk membentuk panah yang mengarah ke dalam
    points = [
        arrow_x, arrow_y,  # Ujung panah (paling kiri)
        arrow_x + arrow_base, arrow_y - arrow_size,  # Ujung atas
        arrow_x + arrow_base, arrow_y + arrow_size,  # Ujung bawah
    ]  
    
# Inisialisasi GUI
root = tk.Tk()
root.title("Twist & Turn")
root.geometry("500x700")
root.config(bg="black") #mengubah warna latar GUI

# Data
names = []
current_angle = 0
colors = ["#F9B7FF", "#EDE6D6", "#E0B0FF", "#9E7BFF", "#822EFF", "#736AFF", "#D291BC", 
          "#D462FF", "#FF77FF", "#FF69B4", "#FFB2D0", "#F8B88B", "#F75D59", "#FF8674", 
          "#FFA07A", "#8A865D", "#E9AB17", "#BCB88A", "#FBB117", "#FFDAB9", 
          "#64E986", "#A0D6B4", "#A0D6B4"] #Mengubah Warna Sektor tiap Elemen

# Canvas untuk roda
canvas = tk.Canvas(root, width=400, height=400, highlightthickness=0
                   , bg="black" #Jika Mengubah Warna Latar GUi, maka bg harus diubah juga
                   )
canvas.pack(pady=10)


# Frame untuk input dan tombol
frame = tk.Frame(root, bg="black") #Jika Mengubah Warna Latar GUi, maka bg harus diubah juga
frame.pack(pady=10)

# Konfigurasi kolom agar ukuran seragam
frame.columnconfigure(0, weight=1, uniform="group1")
frame.columnconfigure(1, weight=1, uniform="group1")
frame.columnconfigure(2, weight=1, uniform="group1")
frame.columnconfigure(3, weight=1, uniform="group1")

# Entry untuk input
entry = tk.Entry(frame, bg="white", justify="center", font=("Arial", 12))
entry.grid(row=0, column=0, sticky="nsew", padx=5, pady=5, ipady=5)

# Tombol Tambahkan
add_button = tk.Button(frame, text="Tambahkan", command=add_name, 
                      bg="green", fg="black", font=("Arial", 12), width=12, height=1)   #Mengubah Warna Tombol Hijau
add_button.grid(row=0, column=1, padx=5, pady=5)

# Tombol Reset
reset_button = tk.Button(frame, text="Reset", command=reset_names, 
                        bg="red", fg="black", font=("Arial", 12), width=12, height=1)   #Mengubah Warna Tombol Merah
reset_button.grid(row=0, column=2, padx=5, pady=5)

# Tombol SPIN
spin_button = tk.Button(frame, text="SPIN!", command=spin_wheel, 
                       bg="#f39c12", fg="black", font=("Arial", 12, "bold"),    #Mengubah Warna Tombol Spin
                       width=12, height=1)
spin_button.grid(row=0, column=3, padx=5, pady=5)

# Listbox label
listbox_label = tk.Label(root, text="Daftar Nama:", bg="black", #Jika Mengubah Warna Latar GUi, maka bg harus diubah juga
                         fg="white", font=("Arial", 12))
listbox_label.pack()

# Listbox
listbox = tk.Listbox(root, width=30, height=10, bg="#DADBDD" #Mengubah Warna Background List 
                     , fg="black", #Mengubah Warna Tulisan didalam List
                     relief=tk.SOLID, bd=1)  
listbox.pack(pady=10)

# Label hasil
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), 
                       bg="black"  #Jika Mengubah Warna Latar GUi, maka bg harus diubah juga
                       , fg="white")    
result_label.pack(pady=10)

# Gambar roda awal
draw_wheel()

root.mainloop()
