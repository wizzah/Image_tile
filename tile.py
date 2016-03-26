from PIL import Image
from random import randint

import argparse
parser = argparse.ArgumentParser(description='Tiles a smaller image onto a larger one')
parser.add_argument('big_image', type=str, help='Bigger image that gets tiled ontop of')
parser.add_argument('tile_attempts', type=int, nargs='?', default=50, help='Default 50. Number of times to attempt to tile smaller image into bigger image before giving up')
parser.add_argument('--allow_overlap', dest='allow_overlap', action='store_true', help='Default False. Allows the smaller image to be placed ontop of previously placed images')
parser.add_argument('small_image', type=str, nargs='+', help='Smaller images that get tiled ontop of the bigger image')
parser.add_argument('-nt', '--num_tiles', type=int, nargs='+', help='How many times to stack each tile listed')
parser.set_defaults(allow_overlap=False)

args = parser.parse_args()

try:
	big_im = Image.open(args.big_image)
except IOError:
	print "Could not open big image"

def rectangle_overlap(r1, r2):
	'''
	returns whether the two rectangles are overlapping
	'''
	return ( (r1[0] <= r2[2]) and (r2[0] <= r1[2]) and (r1[1] <= r2[3]) and (r2[1] <= r1[3]) )

for index, small_im in enumerate(args.small_image):
	try:
		stacker_tile = Image.open(small_im)
	except Exception as e:
		print "It was ", small_im, " in the study with the ", e
		print "tl;dr failed trying to open ", small_im
	small_width, small_height = stacker_tile.size
	big_width, big_height = big_im.size

	# Regions the smaller image is allowed to be paste into and still fit
	diff_x = big_width - small_width
	diff_y = big_height - small_height

	previous_placings = []
	for i in xrange(args.num_tiles[index]):
		print args.num_tiles[index]
		for n in xrange(args.tile_attempts):

			# Random point within safe region
			x_point = randint(0, diff_x)
			y_point = randint(0, diff_y)

			paste_rect = (x_point, y_point, x_point + small_width, y_point + small_height)
			if not args.allow_overlap or not any([rectangle_overlap(r, paste_rect) for r in previous_placings]):
				big_im.paste(stacker_tile, paste_rect, stacker_tile)
				previous_placings.append(paste_rect)
				break

big_im.show()
big_im.save("test.png", "PNG")