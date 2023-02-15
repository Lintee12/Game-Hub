
import tkinter as tk
import os

root = tk.Tk()
dir = "dir"
game_dir = os.path.dirname(__file__)
formated = os.listdir(dir)

root.geometry("1280x720")
root.title("Game Hub")

scrollbar = tk.Scrollbar(root)
scrollbar.pack( side = tk.RIGHT, fill = tk.Y )

game = []

def open(i):
    """ rel_path = "dir" + x + ".lnk" """
    rel_path = os.path.join("dir", str(i) + ".lnk")
    print("!opening file" + " - " + rel_path)
    os.system(rel_path)


for i in formated:
    game.append(i.replace(".lnk", ""))

your_games_label = tk.Label(
    root, 
    text="Your Games", 
    font=("sans serif", 28), 
    fg="#1e81b0", 
    justify="left")


your_games_label.pack(pady=5)

your_games = tk.Listbox(root, yscrollcommand = scrollbar.set )
for i in game:
    photo = tk.PhotoImage(file="fire.png")
    tk.Button(
        root, 
        font=("sans serif", 18), 
        text=i.replace(".exe", ""), 
        image=photo,
        compound = tk.TOP,
        command=lambda x=i: open(x)).pack(padx=10, pady=10, side = tk.TOP)

your_games.pack( side = tk.LEFT, fill = tk.BOTH )
scrollbar.config( command = your_games.yview )

print(game)

root.mainloop()


def start():
    print("Welcome to Game Hub!\n \n-Your Games-")
    for i in formated:
        print(i.replace(".exe", ""))


start()
