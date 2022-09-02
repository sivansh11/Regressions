from tkinter.messagebox import NO
import pygame
import pygame_gui
import pandas as pd


pygame.init()

window_surface = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))


file_chooser = pygame_gui.windows.UIFileDialog(rect=pygame.Rect((0, 0), (800, 600)), manager=manager)

data_set_path = None
data_set = None


is_running = True
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
            data_set_path = file_chooser.file_path_text_line.get_text()
            data_set = pd.read_csv(data_set_path)
        
        manager.process_events(event)
    manager.update(time_delta)
    
    if data_set is not None:
        data_viewer = pygame_gui.

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()