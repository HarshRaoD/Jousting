import tkinter as tk
import webbrowser

from onePlayer import *
from twoPlayer import twoPlayerGame

# Creating a window
window = tk.Tk()


def twoPlayer(event):
    """On pressing the "2 Player" Button"""
    print("Calling twoPlayerGame")
    twoPlayerGame()
    print("twoPlayerGame is quit")


def onePlayer(event):
    """On pressing the "1 Player" Button"""
    # Initialising Variables
    global colour
    colour = tk.BooleanVar(False)  # False for red and True for green
    global diff
    diff = tk.BooleanVar(False)  # False for Easy and True for Hard
    # Creating a new window to show controls
    global window_1play
    window_1play = tk.Toplevel(window)
    # Set the window_1play's title and icon
    window_1play.title("Single Player")
    window_1play.iconphoto(False, tk.PhotoImage(file='knight.png'))
    # Set window_1play's size
    window_1play.geometry("250x250")
    # Change background colour of window_ctrls
    window_1play['background'] = '#000096'
    # Display Colour
    lbl_colour = tk.Label(window_1play, text="Colour", bg='#000096', fg='#fdcb03')
    lbl_colour.config(font=("Cambria", 20))
    lbl_colour.grid(row=0, column=0)
    # Choice of colour
    rbtn_red = tk.Radiobutton(window_1play, variable=colour, value=False, text="Red", bg='#000096', fg='#ff0000')
    rbtn_red.config(font=("Cambria", 15))
    rbtn_red.grid(row=1, column=0)
    rbtn_green = tk.Radiobutton(window_1play, variable=colour, value=True, text="Green", bg='#000096', fg='#00ff00')
    rbtn_green.config(font=("Cambria", 15))
    rbtn_green.grid(row=1, column=1)
    # Display Difficulty
    lbl_colour = tk.Label(window_1play, text="Difficulty", bg='#000096', fg='#fdcb03')
    lbl_colour.config(font=("Cambria", 20))
    tk.Label(window_1play, text=" ", bg='#000096', fg='#fdcb03').grid(row=2, column=0)
    lbl_colour.grid(row=3, column=0)
    # Choice of Difficulty
    rbtn_easy = tk.Radiobutton(window_1play, variable=diff, value=False, text="Easy", bg='#000096', fg='#fdcb03')
    rbtn_easy.config(font=("Cambria", 15))
    rbtn_easy.grid(row=4, column=0)
    rbtn_difficult = tk.Radiobutton(window_1play, variable=diff, value=True, text="Medium", bg='#000096', fg='#fdcb03')
    rbtn_difficult.config(font=("Cambria", 15))
    rbtn_difficult.grid(row=4, column=1)

    # Play button
    tk.Label(window, text=" ", bg='#000096').pack()
    btn_play = tk.Button(window_1play, text="Play", width=7, height=1, bg='#fdcb03', fg='#000096')
    btn_play.config(font=("Cambria", 15))
    btn_play.bind("<Button-1>", playOnePlayer)
    tk.Label(window_1play, text=" ", bg='#000096', fg='#fdcb03').grid(row=5, column=0)
    btn_play.grid(row=6, column=1)

    window_1play.mainloop()


def playOnePlayer(event):
    """On pressing the 'Play' Button in 1 player"""
    window_1play.destroy()
    if colour.get():
        if diff.get():
            oneGreenPlayerGameMed()
        else:
            oneGreenPlayerGame()
    else:
        if diff.get():
            oneRedPlayerGameMed()
        else:
            oneRedPlayerGame()
    return


def goToGithub(event):
    webbrowser.open_new("https://github.com/HarshRaoD")


def showControls(event):
    """On pressing the "Controls" button"""
    # Creating a new window to show controls
    window_ctrls = tk.Toplevel(window)
    # Set the window_ctrls' title and icon
    window_ctrls.title("Controls")
    window_ctrls.iconphoto(False, tk.PhotoImage(file='knight.png'))
    # Set window_ctrls' size
    window_ctrls.geometry("300x450")
    # Change background colour of window_ctrls
    window_ctrls['background'] = '#000096'
    # Display 'Controls'
    lbl_controls = tk.Label(window_ctrls, text="Controls", bg='#000096', fg='#fdcb03')
    lbl_controls.config(font=("Cambria", 35))
    lbl_controls.pack()
    # Controls
    tk.Label(window_ctrls, text="1) Use Arrow keys to move Red Knight.", bg='#000096', fg='#fdcb03').pack()
    tk.Label(window_ctrls, text="2) Use W A S D to move Green Knight.", bg='#000096', fg='#fdcb03').pack()
    # Display 'Rules'
    tk.Label(window_ctrls, text=" ", bg='#000096', fg='#fdcb03').pack()
    lbl_rules = tk.Label(window_ctrls, text="Rules", bg='#000096', fg='#fdcb03')
    lbl_rules.config(font=("Cambria", 35))
    lbl_rules.pack()
    # Rules
    tk.Label(window_ctrls, text="1) Objective of the game is to poke the opponent", bg='#000096', fg='#fdcb03').pack()
    tk.Label(window_ctrls, text="with your spear tip", bg='#000096', fg='#fdcb03').pack()
    tk.Label(window_ctrls, text="2) 'Poke' means that your spear tip is inside the", bg='#000096', fg='#fdcb03').pack()
    tk.Label(window_ctrls, text="opponent's box", bg='#000096', fg='#fdcb03').pack()
    tk.Label(window_ctrls, text="3) The first player to poke the other wins !!", bg='#000096', fg='#fdcb03').pack()
    # Display 'Credits'
    tk.Label(window_ctrls, text=" ", bg='#000096', fg='#fdcb03').pack()
    lbl_rules = tk.Label(window_ctrls, text="Credits", bg='#000096', fg='#fdcb03')
    lbl_rules.config(font=("Cambria", 35))
    lbl_rules.pack()
    # Credits
    tk.Label(window_ctrls, text="Made By: Harsh Rao Dhanyamraju", bg='#000096', fg='#fdcb03').pack()
    btn_github = tk.Button(window_ctrls, text="Github: HarshRaoD", width=20, height=1, fg='#fdcb03', bg='#000096',
                           borderwidth=0)
    btn_github.bind("<Button-1>", goToGithub)
    btn_github.pack()
    tk.Label(window_ctrls, text="Icon by freepik.com, retrived from flaticon.com", bg='#000096', fg='#fdcb03').pack()

    window_ctrls.mainloop()


# Set the window's title and icon
window.title("Jousting")
window.iconphoto(False, tk.PhotoImage(file='knight.png'))
''' Icons made by "https://www.freepik.com"  
    from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>'''

# Change background colour of window
window['background'] = '#000096'

# Set window size
window.geometry("300x475")

# Set Display Image
my_image = tk.PhotoImage(file="knight2.png")
tk.Label(window, text=" ", bg='#000096').pack()
tk.Label(window, image=my_image, borderwidth=0).pack()

# Display 'Jousting'
lbl_main = tk.Label(window, text="Jousting", bg='#000096', fg='#fdcb03')
lbl_main.config(font=("Cambria", 44))
lbl_main.pack()

# 1 Player button
tk.Label(window, text=" ", bg='#000096').pack()
btn_play1 = tk.Button(window, text="1 Player", width=7, height=1, bg='#fdcb03', fg='#000096')
btn_play1.config(font=("Cambria", 20))
btn_play1.bind("<Button-1>", onePlayer)
btn_play1.pack()

# 2 Player button
tk.Label(window, text=" ", bg='#000096').pack()
btn_play2 = tk.Button(window, text="2 Player", width=7, height=1, bg='#fdcb03', fg='#000096')
btn_play2.config(font=("Cambria", 20))
btn_play2.bind("<Button-1>", twoPlayer)
btn_play2.pack()

# Controls button
tk.Label(window, text=" ", bg='#000096').pack()
btn_ctrls = tk.Button(window, text="Controls", width=7, height=1, bg='#fdcb03', fg='#000096')
btn_ctrls.config(font=("Cambria", 12))
btn_ctrls.bind("<Button-1>", showControls)
btn_ctrls.pack()

window.mainloop()
