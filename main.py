import customtkinter
from tkinter import colorchooser

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Color Picker Tool")


def pick_color():
    color_code = colorchooser.askcolor(title="Choose a color")[1]
    if color_code:
        color_display.configure(fg_color=color_code)
        color_label.configure(text=f"Selected Color: {color_code}")

        rgb_color = colorchooser.askcolor(title="Choose a color")[0]
        if rgb_color:
            rgb_label.configure(text=f"RGB: {int(rgb_color[0])}, {int(rgb_color[1])}, {int(rgb_color[2])}")
            rgba_label.configure(text=f"RGBA: {int(rgb_color[0])}, {int(rgb_color[1])}, {int(rgb_color[2])}, 255")


color_button = customtkinter.CTkButton(app, text="Pick a Color", command=pick_color)
color_button.pack(pady=20)

color_label = customtkinter.CTkLabel(app, text="No color selected", font=("Arial", 16))
color_label.pack(pady=10)

color_display = customtkinter.CTkFrame(app, width=200, height=100)
color_display.pack(pady=10)

rgb_label = customtkinter.CTkLabel(app, text="RGB: ", font=("Arial", 14))
rgb_label.pack(pady=5)

rgba_label = customtkinter.CTkLabel(app, text="RGBA: ", font=("Arial", 14))
rgba_label.pack(pady=5)

app.mainloop()