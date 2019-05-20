import os
from PIL import Image

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
directory = "whosThatPokemon/static/img/color_pokemon/"

color = os.path.join(project_dir,directory)

for filename in os.listdir(color):
	print(filename)
	# picture = Image.open(os.path.join(color,filename))
	# pix = picture.load()
	# new_pic = Image.new("RGB", picture.size)
	# new_pix = new_pic.load()

	# width, height = picture.size

	# for x in range(0,width):
	# 	for y in range(0,height):
	# 		r,g,b,a = pix[x,y]  # for png images
	# 		print(pix[x,y])
	# 		if r == 0 and g == 0 and b == 0 and a == 0:
	# 			new_pix[x,y] = (255,255,255,0)
	# 		else:
	# 			new_pix[x,y] = (0,0,0,a)
    
	# project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	# directory = "whosThatPokemon/static/img/silhouette_pokemon/{}".format(filename)
	# new_pic.save(os.path.join(project_dir,directory))

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
	directory = "whosThatPokemon/static/img/silhouette_pokemon/{}".format(filename)
	name = os.path.join(project_dir,directory)
	img.save(name, 'PNG')
