import os
import click
import shutil
from PIL import Image


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
	new_dir = "whosThatPokemon/static/img/silhouette_pokemon/{}".format(region)
	folder = os.path.join(project_dir,new_dir)
	if os.path.isdir(folder):
		shutil.rmtree(folder)
	os.mkdir(folder)

	project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	directory = "whosThatPokemon/static/img/color_pokemon/{}".format(region)

	color = os.path.join(project_dir,directory)

	for filename in os.listdir(color):
		print(filename)

		img = Image.open(os.path.join(color,filename))
		img = img.convert('RGBA')
		datas = img.getdata()
		newData = []
		for item in datas:
			if item[0] == 0 and item[1] == 0 and item[2] == 0 and item[3] == 0:
				newData.append(item)
			else:
				newData.append((0,0,0,item[3]))
		img.putdata(newData)
		project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		directory = folder + "/" + filename
		name = os.path.join(project_dir,directory)
		img.save(name, 'PNG')

if __name__ == "__main__":
	main()
