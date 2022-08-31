import random

dzien = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
obiad_listy = ["Carbonara", "Pierogi", "Ryż z mięsem", "Somon", "Menemen", "Kebab", "Mantı"]

kombinacja = {}

def yemek2():
	dzien_input = input("Napisz ile dzień chcesz gotować obiad? Proszę napisać cyfry! lub q ")

	if dzien_input.isdigit():
		for dzien_input in range(len(dzien)):
			kombinacja[dzien[dzien_input]] = obiad_listy[dzien_input]
	return

yemek2()
print(kombinacja)
