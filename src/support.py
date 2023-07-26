import pygame
from csv import reader
from os import walk


def import_csv_layout(path):
    """Import a CSV layout file and return the corresponding Layout object.
    # Read in data from csv file. Each row represents one key, with columns for x/
    y coordinates of each point on that key's shape (in units). The first column is assumed to
    be empty since it contains no text label or other metadata about this specific key."""

    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(row)
        return terrain_map


def import_folder(path):
    surface_list = []
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path+'/'+image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list
