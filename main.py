import os
import sys
from tkinter import *
import math


def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def provjera_red(polje, x, y):
	red = polje[x]
	pozicija = polje[x][y]

	promjena = False

	brojevi_u_redu = []
	moguci_brojevi_red = []
	for i in range(len(red)):
		try:
			len(red[i])
			if i != y:
				moguci_brojevi_red.extend(red[i])
		except TypeError:
			brojevi_u_redu.append(red[i])

	izbrisano = 0
	for i in range(len(pozicija)):
		if pozicija[i - izbrisano] in brojevi_u_redu:
			del pozicija[i - izbrisano]
			izbrisano += 1
			promjena = True

	for i in pozicija:
		if i not in moguci_brojevi_red:
			pozicija = [i]
			promjena = True
			break

	del polje[x][y]
	if len(pozicija) == 1:
		polje[x].insert(y, pozicija[0])
	else:
		polje[x].insert(y, pozicija)

	return polje, promjena

def provjera_stupac(polje, x, y):
	stupac = []
	for i in range(9):
		stupac.append(polje[i][y])
	pozicija = polje[x][y]

	promjena = False

	brojevi_u_stupcu = []
	moguci_brojevi_stupac = []
	for i in range(len(stupac)):
		try:
			len(stupac[i])
			if i != y:
				moguci_brojevi_stupac.extend(stupac[i])
		except TypeError:
			brojevi_u_stupcu.append(stupac[i])

	izbrisano = 0
	for i in range(len(pozicija)):
		if pozicija[i - izbrisano] in brojevi_u_stupcu:
			del pozicija[i - izbrisano]
			izbrisano += 1
			promjena = True

	for i in pozicija:
		if i not in moguci_brojevi_stupac:
			pozicija = [i]
			promjena = True
			break

	del polje[x][y]
	if len(pozicija) == 1:
		polje[x].insert(y, pozicija[0])
	else:
		polje[x].insert(y, pozicija)

	return polje, promjena

def provjera_kvadrat(polje, x, y):
	kvadrat = []
	for i in range((math.ceil((x + 1) / 3) - 1) * 3, math.ceil((x + 1) / 3) * 3):
		for j in range((math.ceil((y + 1) / 3) - 1) * 3, math.ceil((y + 1) / 3) * 3):
			kvadrat.append(polje[i][j])
	pozicija = polje[x][y]

	promjena = False

	brojevi_u_kvadratu = []
	moguci_brojevi_kvadrat = []
	for i in range(len(kvadrat)):
		try:
			len(kvadrat[i])
			if i != y:
				moguci_brojevi_kvadrat.extend(kvadrat[i])
		except TypeError:
			brojevi_u_kvadratu.append(kvadrat[i])

	izbrisano = 0
	for i in range(len(pozicija)):
		if pozicija[i - izbrisano] in brojevi_u_kvadratu:
			del pozicija[i - izbrisano]
			izbrisano += 1
			promjena = True

	for i in pozicija:
		if i not in moguci_brojevi_kvadrat:
			pozicija = [i]
			promjena = True
			break

	del polje[x][y]
	if len(pozicija) == 1:
		polje[x].insert(y, pozicija[0])
	else:
		polje[x].insert(y, pozicija)

	return polje, promjena

def provjera_parovi_redovi(polje):
	promjena = False
	for z in range(9):
		red = polje[z]
		red_dict = {}
		for i in range(len(red)):
			if type(red[i]) == list:
				for j in red[i]:
					if j in red_dict.keys():
						red_dict[j][0] += 1
						red_dict[j][1].append(i)
					else:
						red_dict[j] = [1, [i]]
		possible_pair_digits = []
		for i in red_dict.keys():
			if red_dict[i][0] == 2:
				possible_pair_digits.append(i)
		do_break = False
		for i in possible_pair_digits:
			for j in possible_pair_digits:
				if i != j:
					broj_istih_pozicija = 0
					iste_pozicije = []
					for x in red_dict[i][1]:
						if x in red_dict[j][1]:
							broj_istih_pozicija += 1
							iste_pozicije.append(x)
					if broj_istih_pozicija == 2:
						pair = [i, j]
						do_break = True
						break
			if do_break:
				break
		if do_break:
			if polje[z][iste_pozicije[0]] != pair:
				promjena = True
				polje[z][iste_pozicije[0]] = pair
			if polje[z][iste_pozicije[1]] != pair:
				promjena = True
				polje[z][iste_pozicije[1]] = pair

	return polje, promjena

def solve_click(event=None):
	global fields

	lista = []
	for i in fields:
		red = []
		for j in i:
			try:
				red.append(int(j["text"]))
			except ValueError:
				red.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
		lista.append(red)
	del red

	# lista_easy = [[8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 6, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], 6], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8]]
	# lista_medium
	# lista_hard = [[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]

	promjena = True
	while promjena:
		print(lista)
		promjena = False

		# scanning
		promjena_scanning = True
		while promjena_scanning:
			promjena_scanning = False
			for i in range(len(lista)):
				for j in range(len(lista[i])):
					try:
						len(lista[i][j])

						red = provjera_red(lista, i, j)
						if red[1]:
							lista = red[0]
							promjena = True
							promjena_scanning = True

						stupac = provjera_stupac(lista, i, j)
						if stupac[1]:
							lista = stupac[0]
							promjena = True
							promjena_scanning = True

						kvadrat = provjera_kvadrat(lista, i, j)
						if kvadrat[1]:
							lista = kvadrat[0]
							promjena = True
							promjena_scanning = True

					except TypeError:
						pass

		print(lista)
		# pairs
		parovi_redovi = provjera_parovi_redovi(lista)
		if parovi_redovi[1]:
			lista = parovi_redovi[0]
			promjena = True

		# x wing

	clear_click()
	for i in range(9):
		for j in range(9):
			if type(lista[i][j]) == int:
				fields[i][j].config(text=str(lista[i][j]))

def clear_click(event=None):
	global fields, select_position, select_active
	for i in fields:
		for j in i:
			j.config(text="")
	fields[select_position[0]][select_position[1]].config(highlightthickness=2)
	select_active = False
	select_position = [0, 0]

def field_click(event, i, j):
	global fields, select_position, select_active
	if select_active:
		if [i, j] == select_position:
			select_active = False
			fields[i][j].config(highlightthickness=2)
		else:
			fields[select_position[0]][select_position[1]].config(highlightthickness=2)
			fields[i][j].config(highlightthickness=4)
			select_position = [i, j]
	else:
		select_active = True
		fields[i][j].config(highlightthickness=4)
		select_position = [i, j]

def arrow_press(event, arrow):
	global fields, select_position, select_active
	match arrow:
		case "left":
			if select_position[1] != 0:
				fields[select_position[0]][select_position[1]].config(highlightthickness=2)
				select_position[1] -= 1
		case "right":
			if select_position[1] != 8:
				fields[select_position[0]][select_position[1]].config(highlightthickness=2)
				select_position[1] += 1
		case "up":
			if select_position[0] != 0:
				fields[select_position[0]][select_position[1]].config(highlightthickness=2)
				select_position[0] -= 1
		case "down":
			if select_position[0] != 8:
				fields[select_position[0]][select_position[1]].config(highlightthickness=2)
				select_position[0] += 1
	select_active = True
	fields[select_position[0]][select_position[1]].config(highlightthickness=4)

def num_press(event, num):
	global fields, select_position, select_active
	if select_active:
		if num != 0:
			fields[select_position[0]][select_position[1]].config(text=str(num))
		else:
			fields[select_position[0]][select_position[1]].config(text="")


if __name__ == '__main__':
	root = Tk()
	root.title("S-Sudoku")
	root.resizable(False, False)
	root.geometry(f"420x515+{root.winfo_screenwidth() // 2 - 210}+{root.winfo_screenheight() // 2 - 257}")
	root.iconbitmap(resource_path("sudoku-icon.ico"))
	root.config(background="#9AE6FC")

	title_lbl = Label(root, text="S-Sudoku", font=("Helvetica", 30, "bold", "italic"), foreground="white", activeforeground="white", activebackground="#9AE6FC", background="#9AE6FC", highlightthickness=0, borderwidth=0)
	title_lbl.place(width=420, height=95, x=0, y=0)

	clr_bt = Label(root, text="Clear", font=("Helvetica", 15, "bold"), justify="center", anchor="center", background="#5c8a97", activebackground="#5c8a97", foreground="white", activeforeground="white", borderwidth=0, highlightthickness=2, highlightcolor="#0f1719", highlightbackground="#0f1719")
	clr_bt.place(width=100, height=35, x=40, y=460)
	clr_bt.bind("<ButtonRelease-1>", clear_click)
	clr_bt.bind("<Enter>", lambda event: clr_bt.config(highlightthickness=4))
	clr_bt.bind("<Leave>", lambda event: clr_bt.config(highlightthickness=2))

	slv_bt = Label(root, text="Solve", font=("Helvetica", 15, "bold"), justify="center", anchor="center", background="#5c8a97", activebackground="#5c8a97", foreground="white", activeforeground="white", borderwidth=0, highlightthickness=2, highlightcolor="#0f1719", highlightbackground="#0f1719")
	slv_bt.place(width=100, height=35, x=280, y=460)
	slv_bt.bind("<ButtonRelease-1>", solve_click)
	slv_bt.bind("<Enter>", lambda event: slv_bt.config(highlightthickness=4))
	slv_bt.bind("<Leave>", lambda event: slv_bt.config(highlightthickness=2))

	fields = []
	for i in range(9):
		red = []
		for j in range(9):
			red.append(Label(root, cursor="tcross", text="", font=("Helvetica", 18), justify="center", anchor="center", background="#7bb8c9", activebackground="#7bb8c9", foreground="white", activeforeground="white", borderwidth=0, highlightthickness=2, highlightcolor="#2e454b", highlightbackground="#2e454b"))
			red[-1].place(height=30, width=30, x=(40 + (j * 35) + ((j // 3) * 15)), y=(100 + (i * 35) + ((i // 3) * 15)))
			red[-1].bind("<ButtonRelease-1>", lambda event, i=i, j=j: field_click(event, i, j))
		fields.append(red)
	select_position = [0, 0]
	select_active = False

	root.bind("<KeyPress-Left>", lambda event: arrow_press(event, "left"))
	root.bind("<KeyPress-Right>", lambda event: arrow_press(event, "right"))
	root.bind("<KeyPress-Up>", lambda event: arrow_press(event, "up"))
	root.bind("<KeyPress-Down>", lambda event: arrow_press(event, "down"))

	root.bind("<KeyPress-1>", lambda event: num_press(event, 1))
	root.bind("<KeyPress-2>", lambda event: num_press(event, 2))
	root.bind("<KeyPress-3>", lambda event: num_press(event, 3))
	root.bind("<KeyPress-4>", lambda event: num_press(event, 4))
	root.bind("<KeyPress-5>", lambda event: num_press(event, 5))
	root.bind("<KeyPress-6>", lambda event: num_press(event, 6))
	root.bind("<KeyPress-7>", lambda event: num_press(event, 7))
	root.bind("<KeyPress-8>", lambda event: num_press(event, 8))
	root.bind("<KeyPress-9>", lambda event: num_press(event, 9))
	root.bind("<KeyPress-Delete>", lambda event: num_press(event, 0))
	root.bind("<KeyPress-BackSpace>", lambda event: num_press(event, 0))

	root.mainloop()
	sys.exit()
