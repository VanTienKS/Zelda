import pygame
from scripts.settings import *

class UI:
    def __init__(self):
        # general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SiZE)
        
        # bar setup
        self.health_bar_rect = pygame.Rect(
            10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(
            10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)
        
        # convert weapon dictionary
        self.weapon_graphics = []
        for weapon in weapon_data.values():
            path = weapon['graphic']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)

    def show_bar(self, current, max_amount, bg_rect, color):
        # draw bg
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # converting star to pixel
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # drawing the bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    def show_exp(self, exp):
        text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)
        text_pos =  self.display_surface.get_size() - pygame.math.Vector2(20,20)
        text_rect = text_surf.get_rect(bottomright = text_pos)
        
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20,10))
        self.display_surface.blit(text_surf,text_rect) 
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20,10), 3)

    def selection_box(self, x, y, has_switched):
        bg_rect = pygame.Rect(x, y, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        
        if has_switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
        else:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

        
        return bg_rect

    def weapon_overplay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(10,SCREEN_HEIGHT - ITEM_BOX_SIZE - 20, has_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center = bg_rect.center)
        
        self.display_surface.blit(weapon_surf, weapon_rect)

    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect,ENERGY_COLOR)

        self.show_exp(player.exp)
        
        self.selection_box(80,SCREEN_HEIGHT - ITEM_BOX_SIZE - 10, player.can_switch_weapon)
        self.weapon_overplay(player.weapon_index, player.can_switch_weapon)
        