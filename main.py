import os
import tkinter as tk
import subprocess

root = tk.Tk()
dir = "dir"
game_dir = os.path.dirname(__file__)
formated = os.listdir(dir)

root.geometry("1280x720")
root.title("Game Hub")

game = []


def open(x):
    print("opening file" + "-" + '/dir/' + x + '.lnk')
    # rel_path = 'dir/' + x + '.lnk' i dont know why this wont work
    rel_path = x + '.lnk'
    print(rel_path)
    os.system(str(rel_path))


for i in formated:
    game.append(i.replace(".lnk", ""))

for i in game:
    tk.Button(root, text=i.replace(".exe", ""),
              command=lambda: open(i)).pack(padx=10, pady=10)


print(game)

root.mainloop()


def start():
    print("Welcome to Game Hub!\n \n-Your Games-")
    for i in formated:
        print(i.replace(".exe", ""))


start()
