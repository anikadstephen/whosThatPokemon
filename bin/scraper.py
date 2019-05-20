import os
import csv
import requests
from bs4 import BeautifulSoup

def main():
	with open("pokemon.csv", errors='ignore') as f_in:
		pokemon_list = list(csv.DictReader(f_in))
		i = 258
		while True:
			row = pokemon_list[i-1]
			if int(row['Generation']) != 3:
				break
			pokemon_name = row['Name']
			try:
				img = get_img_url(row["#"], pokemon_name)
				saveFile = get_save_url(pokemon_name)
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

def get_save_url(pokemon_name):
	project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	newfilename = "whosThatPokemon/static/img/color_pokemon/Hoenn/{}.png".format(pokemon_name)
	return os.path.join(project_dir,newfilename)


if __name__ == "__main__":
	main()
