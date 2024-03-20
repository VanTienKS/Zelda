import pygame
from os import walk
from csv import reader


def import_csv_layout(path):

    terrain_map = []

    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path):
    surface_list = []
    for __, __, image_files in walk(path):
        for image in image_files:
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
    return surface_list


# print(import_csv_layout('map/map_FloorBlocks.csv'))
# print(import_folder('graphics/Grass')) # chua chay ham pygame.init() nen se bao loi o file nay
