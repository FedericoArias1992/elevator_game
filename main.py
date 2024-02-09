import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_0, K_9
from Elevator_01_Problema import Elevator
from datetime import datetime, timedelta
import asyncio

class ElevatorSimulation:
    '''Creamos la instancia de la similacion de elevador'''
    def __init__(self, elevator):
        pygame.init()
        self.elevator = elevator
        #Texto en el juego:
        self.font = pygame.font.Font(None, 24)
        self.text_background_color = (0, 0, 0, 128)
        #Tamanho del window del juego
        self.window_width = 700
        self.window_height = 780
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('Elevator Simulation')
        self.clock = pygame.time.Clock()
        self.target_floor = self.elevator.floor
        #Imagen de fondo
        self.background = pygame.image.load("new_background_image_elevator_game.png")
        self.background = pygame.transform.scale(self.background, (self.window_width, self.window_height))
        #Tamanho del elevador
        self.elevator_width = 68*1.8
        self.elevator_height = 80
        self.elevator_speed = 0.18
        self.max_height = 10
        #imagen del ascensor
        self.static_elevator_image = pygame.image.load('opened_door_elevator.png')
        self.static_elevator_image = pygame.transform.scale(self.static_elevator_image, (self.elevator_width, self.elevator_height))
        self.moving_elevator_image = pygame.image.load('Elevator_Image.png')
        self.moving_elevator_image = pygame.transform.scale(self.moving_elevator_image, (self.elevator_width, self.elevator_height))
        #Capacidades_ascensor
        self.max_capacity = 9  #uno por piso
        self.ascensor_con_gente = 0
        #Imagen del Evotar
        self.avatar = pygame.image.load("Evotar_Image.png")
        self.avatar = pygame.transform.scale(self.avatar, (self.elevator_width, self.elevator_height*0.70))
        self.avatar_position = (0, 0)  # Define la posición del avatar
        self.avatar_visible = False

    def draw_elevator(self):
        '''Dibujamos el Ascensor y su posicion'''
        if self.elevator.status == 'static':
            elevator_image = self.static_elevator_image
        elif self.elevator.status == 'moving':
            elevator_image = self.moving_elevator_image        
        self.window.blit(elevator_image, (290, int(self.elevator.floor * 70)+self.max_height, self.elevator_width, self.elevator_height))
        
    def move_elevator(self):
        '''Movemos el elevador segun se presione una tecla o llegue a la capacidad maxima'''
        if self.target_floor != self.elevator.floor :
            if self.elevator.floor < self.target_floor:
                '''Posicion elevador mas abajo que el target -> abajo'''
                #print('self.elevator.floor antes de la resta: ', self.elevator.floor)
                self.elevator.floor += self.elevator_speed
                #print('self.elevator.floor dsps de la resta: ', self.elevator.floor)
                self.elevator.status = 'moving'
                #print('abs(round(self.elevator.floor, 0) == self.target_floor)',abs(round(self.elevator.floor, 0) == self.target_floor))
                #print('target_floor dsps de la resta: ', self.target_floor)
                if abs(round(self.elevator.floor, 0) == self.target_floor) > 0.1:
                    self.elevator.status = 'static'
                    self.elevator.floor == self.target_floor
                    #print('si va abajo, aparece aca')
                    #print('abs elevaor.floor - target_floor',abs(round(self.elevator.floor, 0) == self.target_floor) )
                    self.hide_avatar()
                    self.elevator.arrive(floor=self.target_floor, moment = (self.elevator.moment + timedelta(minutes=4)))  #Takes 4 minutes to reach the floor
                    
            elif self.elevator.floor > self.target_floor:
                '''Posicion elevador mas arriba que el target -> voy abajo'''
                #print('self.elevator.floor: ', self.elevator.floor)
                self.elevator.floor += -self.elevator_speed
                self.elevator.status = 'static'
                #print('si va arriba, aparece aca')
                if abs(round(self.elevator.floor, 0) == self.target_floor) < 0.1:
                    self.elevator.status = 'moving'
                    self.elevator.floor == self.target_floor
                    
    def subir_gente(self, event_key):
        '''Cuando presionen 0 -> PB -> se vacia'''
        if (self.ascensor_con_gente < self.max_capacity) and (event_key != 48) :
            self.ascensor_con_gente +=1
            self.elevator.status = 'moving'
        elif event_key == 48 or (self.ascensor_con_gente == self.max_capacity) :
            self.target_floor = 9  #el piso 0 es el 9, la diferencia del integer dado por las teclas K_0 y K_9
            self.ascensor_con_gente =0         

    def handle_user_input(self):
        '''Escuchamos si hay evento de presiona de tecla que hace de trigger para mover el ascensor'''
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if K_0 <= event.key <= K_9:
                    '''K_0 = 48 y K_9 = 57'''
                    self.target_floor = K_9 - event.key
                    elevator.demand(floor = self.target_floor, moment = (self.elevator.moment))
                    self.avatar_visible = True
                    #print('target_floor del handle user input: ',self.target_floor)
                    self.show_avatar()
                    self.subir_gente(event.key)#Contador de cuanta gente va subiendo
                
    def show_avatar(self):
        '''Mostramos el evotar del personaje'''
        avatar = self.avatar  # Obtiene el avatar correspondiente a la tecla presionada
        if self.avatar_visible:
            # Calcula la posición en la ventana donde se mostrará el avatar
            self.avatar_position = (180, self.target_floor*71+self.max_height)  
            self.window.blit(avatar, self.avatar_position)  # Dibuja el avatar en la ventana
            
    def hide_avatar(self):
        '''Para que aparezca o no el Evotar'''
        if self.avatar_visible == True:
            self.avatar_visible = False  # Oculta el avatar

    def draw_text(self, text, position):
        '''Dibuja texto en la pantalla'''
        text_surface = self.font.render(text, True, (255, 255, 255))  # Renderiza el texto en una superficie
        # Calcula el tamaño del rectángulo del fondo
        text_background_rect = text_surface.get_rect()
        # Ajusta la posición del rectángulo del fondo
        text_background_rect.topleft = position
        pygame.draw.rect(self.window, (115, 28, 229), text_background_rect)
        self.window.blit(text_surface, position)  # Blit (dibuja) la superficie de texto en la ventana en la posición especificada

'''    def run_simulation(self):
        while True:
            self.handle_user_input()
            self.move_elevator()
            self.window.blit(self.background, (0, 0))  # Dibujamos el fondo
            self.draw_elevator()
            self.draw_text(f"Personas en el ascensor: {self.ascensor_con_gente} de {self.max_capacity}", (30, 20))  # Dibuja el texto en la esquina superior izquierda
            self.draw_text(f"Fecha: {self.elevator.moment.day}/{self.elevator.moment.month}/{self.elevator.moment.year} {self.elevator.moment.hour}:{self.elevator.moment.minute}", (30, 40))  # Dibuja el texto en la esquina superior izquierda
            self.show_avatar()
            pygame.display.flip()
            self.clock.tick(30)
'''

async def main():
    while True:
        await asyncio.sleep(0.1)  # Espera 1 segundo (simulación de un paso de tiempo)
        simulation.handle_user_input()
        simulation.move_elevator()
        simulation.window.blit(simulation.background, (0, 0))
        simulation.draw_elevator()
        simulation.draw_text(f"Personas en el ascensor: {simulation.ascensor_con_gente} de {simulation.max_capacity}", (30, 20))
        simulation.draw_text(f"Fecha: {simulation.elevator.moment.day}/{simulation.elevator.moment.month}/{simulation.elevator.moment.year} {simulation.elevator.moment.hour}:{simulation.elevator.moment.minute}", (30, 40))
        simulation.show_avatar()
        pygame.display.flip()
        simulation.clock.tick(30)

if __name__ == '__main__':
    elevator = Elevator('static', 9)  # Piso de la posición inicial es la PB o 0
    simulation = ElevatorSimulation(elevator)
    asyncio.run(main())
