# Image_tile
command line tool to tile a smaller image onto a bigger one

## Installation
pip install -r requirements.txt
## Running 
Layer the background first and then the pixel artifacts. Use -nt or --num_tiles to state how many times you want the artifacts to be randomly stacked.
python tile.py bg.png --allow_overlap tiles/wood_1.png tiles/wood_2.png tiles/wood_3.png -nt 2 2 1
...(sorry)
