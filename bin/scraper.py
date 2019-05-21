import os
import csv
import requests
from bs4 import BeautifulSoup
import click
import shutil

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
	project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	new_dir = "whosThatPokemon/static/img/color_pokemon/{}".format(region)
	folder = os.path.join(project_dir,new_dir)
	if os.path.isdir(folder):
		shutil.rmtree(folder)
	os.mkdir(folder)
	with open("bin/pokemon.csv", errors='ignore') as f_in:
		pokemon_list = list(csv.DictReader(f_in))
		i = 0
		while True:
			if i  == len(pokemon_list):
				break
			row = pokemon_list[i]
			if int(row['generation']) < int(generation):
				i +=1
				continue
			if int(row['generation']) > int(generation):
				break
			
			pokemon_name = row['name']
			try:
				img = get_img_url(row["pokedex_number"], pokemon_name)
				saveFile = get_save_url(region,pokemon_name)
				with open(saveFile, "wb") as f:
					f.write(img.content)
			except:
				print("Skipped " + pokemon_name)
			i += 1


def get_img_url(i, pokemon_name):
	filename = None
	if len(str(i)) == 1:
		filename = "File:00{}{}.png".format(i, pokemon_name)
	if len(str(i)) == 2:
		filename = "File:0{}{}.png".format(i, pokemon_name)
	if len(str(i)) == 3:
		filename = "File:{}{}.png".format(i, pokemon_name)

	url = "https://m.bulbapedia.bulbagarden.net/wiki/{}".format(filename)
	response = requests.get(url)
	page_content = BeautifulSoup(response.content, "html.parser")
	img_tag = page_content.find("img", alt=filename)
	print(filename)
	return requests.get("https:{}".format(img_tag['src']))

def get_save_url(region,pokemon_name):
	project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	newfilename = "whosThatPokemon/static/img/color_pokemon/{}/{}.png".format(region,pokemon_name)
	return os.path.join(project_dir,newfilename)


if __name__ == "__main__":
	main()
