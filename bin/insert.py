import whosThatPokemon
import sqlite3
import os
import click

@click.command()
@click.option('--generation', help='Generation to download')
def main(generation):
	regions = {
				1: "Kanto", 
				2: "Johto", 
				3: "Hoenn", 
				4: "Sinnoh", 
				5: "Unova", 
				6: "Kalos",
				7: "Alola",
				8: "Galar",
	}
	region = regions[int(generation)]
	name = os.path.join(
		os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
		'whosThatPokemon','var', 'pokemon.sqlite3')
	print(name)
	conn = sqlite3.connect(name)
	cursor = conn.cursor()

	project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

	color = os.path.join(project_dir, 'whosThatPokemon','static', 'img', 'color_pokemon', region)

	for filename in os.listdir(color):
		pokemon_name = filename[:filename.find('.png')]
		print(pokemon_name)
		cursor.execute("INSERT INTO pokemon VALUES(?,?)", (pokemon_name, region))
	conn.commit()
	print(cursor.execute("SELECT * FROM pokemon").fetchall())
	conn.close()

if __name__ == "__main__":
	main()