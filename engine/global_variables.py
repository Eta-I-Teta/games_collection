from engine.utilities import read_json_file
import pygame

CONFIG_SCREEN = read_json_file("data/configs/screen.json")
COLOR = read_json_file("data/configs/colors.json")

FONT = pygame.font.Font(CONFIG_SCREEN["font"]["family"], CONFIG_SCREEN["font"]["size"])