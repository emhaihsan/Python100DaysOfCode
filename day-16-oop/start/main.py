# from turtle import Turtle, Screen

# # Membuat objek Turtle
# timmy = Turtle()

# # Menyetel bentuk dan warna kura-kura
# timmy.shape("turtle")
# timmy.color("coral")

# # Menggerakkan kura-kura ke kanan
# timmy.forward(100)  # Menggerakkan kura-kura maju sejauh 100 unit

# # Membuat objek Screen
# my_screen = Screen()
# print(my_screen.canvheight)

# # Menutup jendela ketika diklik
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# table.add_row(["Darwin", 112, 120900, 1714.7])
# table.add_row(["Hobart", 1357, 205556, 619.5])
# table.add_row(["Sydney", 2058, 4336374, 1214.8])
# table.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.add_row(["Perth", 5386, 1554769, 869.4])

table.field_names = ["Pokemon Name", "Type"]
table.add_row(['Pikachu', 'Electric'])
table.add_row(['Squirtle', 'Water'])
table.add_row(['Chamander', 'Fire'])
table.align = 'l'
print(table)