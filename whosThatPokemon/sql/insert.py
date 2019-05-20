import whosThatPokemon
import sqlite3
import os

name = os.path.join(
	os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
	'var', 'pokemon.sqlite3')
print(name)
conn = sqlite3.connect(name)
cursor = conn.cursor()

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

color = os.path.join(project_dir, 'static', 'img', 'color_pokemon')

for filename in os.listdir(color):
	pokemon_name = filename[:filename.find('.png')]
	print(pokemon_name)
	cursor.execute("INSERT INTO pokemon VALUES(?,?)", (pokemon_name, "Kanto"))
conn.commit()
print(cursor.execute("SELECT * FROM pokemon").fetchall())
conn.close()