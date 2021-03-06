import os,sys
import pygame
from pygame.locals import *
from pygame.sprite import Sprite
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'
import random
class PyManMain:
    def __init__(self, width=610,height=610):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
    def spawn_new_item(self,box_list):
        free_list = []
        for i in range(len(box_list)):
            for j in range(len(box_list[0])):
                if box_list[i][j].value == 0:
                    free_list.append([i,j])
        if len(free_list) == 0:
            return box_list
        random_location = random.randrange(len(free_list))
        row_column = free_list[random_location]
        random_row = row_column[0]
        random_column = row_column[1]
        value_random = random.randrange(100)
        if value_random > 10:
            box_list[random_row][random_column].value = 2
        else:
            box_list[random_row][random_column].value = 4
        return box_list
    def initialize_matrix(self,box_list):
        random_row_1 = random.randrange(4)
        random_column_1 = random.randrange(4)
        box_list[random_row_1][random_column_1].value = 2
        while True:
            random_row_2 = random.randrange(4)
            random_column_2 = random.randrange(4)
            if random_column_2!= random_column_1 or random_row_1!=random_row_2:
                box_list[random_row_2][random_column_2].value = 2
                break
        return box_list
    def transpose_matrix(self,matrix):
        mat_dim = len(matrix)
        transposed_matrix = []
        for i in range(mat_dim):
            column = [row[i] for row in matrix]
            transposed_matrix.append(column)
        return transposed_matrix
    def get_column(self,matrix,i):
        column = [row[i] for row in matrix]
        return column
    #def print_line():
        #print('-   -   -   -   -   -   -   -   -')
    #def display_matrix(matrix):
        print_line()
        for row in matrix:
            rowstring = '|   '
            for item in row:
                rowstring += str(item)
                rowstring += '   |   '
            print rowstring
            print_line()
    def push_left_row(self,row):
        for i in range(len(row)):
            index = i - 1
            if row[i].value == 0:
                continue
            while index >= 0:
                if row[index].value == 0:
                    row[index].value = row[index+1].value
                    row[index+1].value = 0
                else:
                    break
                index = index-1
        return row
    def check_merge(self,row):
        for i in range(len(row)-1):
            if row[i].value == row[i+1].value:
                row[i].value = 2*row[i].value
                row[i+1].value = 0
                row = self.push_left_row(row)
        return row
    def get_matrix_values(self,matrix):
        matrix_values = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix_values.append(matrix[i][j].value)
        return matrix_values
    def move_left(self,box_list):
        temp_matrix = []
        matrix_values = self.get_matrix_values(box_list)
        for row in box_list:
            row = self.push_left_row(row)
            row = self.check_merge(row)
            temp_matrix.append(row)
        final_matrix_values = self.get_matrix_values(temp_matrix)
        if final_matrix_values == matrix_values:
            return temp_matrix,False
        else:
            return temp_matrix,True
    def move_right(self,box_list):
        temp_matrix = []
        matrix_values = self.get_matrix_values(box_list)
        for row in box_list:
            row.reverse()
            row = self.push_left_row(row)
            row = self.check_merge(row)
            row.reverse()
            temp_matrix.append(row)
        final_matrix_values = self.get_matrix_values(temp_matrix)
        if final_matrix_values == matrix_values:
            return temp_matrix,False
        else:
            return temp_matrix,True
    def move_up(self,box_list):
        temp_matrix = []
        matrix_values = self.get_matrix_values(box_list)
        for i in range(len(box_list)):
            column = self.get_column(box_list,i)
            column = self.push_left_row(column)
            column = self.check_merge(column)
            temp_matrix.append(column)
        temp_matrix = self.transpose_matrix(temp_matrix)
        final_matrix_values = self.get_matrix_values(temp_matrix)
        if final_matrix_values == matrix_values:
            return temp_matrix,False
        else:
            return temp_matrix,True
    def move_down(self,box_list):
        temp_matrix = []
        matrix_values = self.get_matrix_values(box_list)
        for i in range(len(box_list)):
            column = self.get_column(box_list,i)
            column.reverse()
            column = self.push_left_row(column)
            column = self.check_merge(column)
            column.reverse()
            temp_matrix.append(column)
        temp_matrix = self.transpose_matrix(temp_matrix)
        final_matrix_values = self.get_matrix_values(temp_matrix)
        if final_matrix_values == matrix_values:
            return temp_matrix,False
        else:
            return temp_matrix,True
    def check_for_win_condition(self,box_list):
        checkflag = 0
        for i in range(len(box_list)):
            for j in range(len(box_list[0])):
                if box_list[i][j].value == 2048:
                    checkflag = 1
        if checkflag == 1:
            return True
        else:
            return False
    def check_for_change(self,box_list_old,box_list_new):
        box_list_old_array = get_matrix_values(box_list_old)
        box_list_new_array = get_matrix_values(box_list_new)
        if box_list_new_array == box_list_old_array:
            return False
        else:
            return True
    def check_for_lose_condition(self,box_list):
        def get_matrix_values(matrix):
            matrix_values = []
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    matrix_values.append(matrix[i][j].value)
            return matrix_values
        check_left = 0
        check_right = 0
        check_up = 0
        check_down = 0
        box_list_values = []
        matrix_values = []
        for i in range(len(box_list)):
            for j in range(len(box_list[0])):
                box_list_values.append(box_list[i][j].value)
        left_matrix = self.move_left(box_list)
        matrix_values = get_matrix_values(left_matrix)
        if matrix_values == box_list_values:
            check_left = 1
        right_matrix = self.move_right(box_list)
        matrix_values = get_matrix_values(right_matrix)
        if matrix_values == box_list_values:
            check_right = 1
        up_matrix = self.move_up(box_list)
        matrix_values = get_matrix_values(up_matrix)
        if matrix_values == box_list_values:
            check_up = 1
        down_matrix = self.move_down(box_list)
        matrix_values = get_matrix_values(down_matrix)
        if matrix_values == box_list_values:
            check_down = 1
        if check_down == 1 and check_up == 1 and check_left == 1 and check_right == 1:
            return True
        else:
            return False
    def MainLoop(self):
        BG_COLOUR = 0, 0, 0
        box_list = []
        temp_box_list = []
        for i in range(4):
            temp_box_list = []
            for j in range(4):
                temp_box_list.append(Box(self.screen,'data/EMPTY.png',(10+150*j,10+150*i)))
            box_list.append(temp_box_list)
        box_list = self.initialize_matrix(box_list)
        for i in range(len(box_list)):
            for j  in range(len(box_list[0])):
                box_list[i][j].update(self.screen,(10+150*j,10+150*i),box_list[i][j].value)
            #self.box_sprites = pygame.sprite.RenderPlain((self.box))
        while 1:
            pygame.time.wait(20)
            modified_box_list = []
            temp_box_list = box_list
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT) or (event.key == K_LEFT) or (event.key == K_UP) or (event.key == K_DOWN)):
                        if event.key == K_LEFT:
                            modified_box_list,result = self.move_left(box_list)
                        elif event.key == K_RIGHT:
                            modified_box_list,result = self.move_right(box_list)
                        elif event.key == K_DOWN:
                            modified_box_list,result = self.move_down(box_list)
                        elif event.key == K_UP:
                            modified_box_list,result = self.move_up(box_list)
                        for i in range(len(modified_box_list)):
                            for j  in range(len(modified_box_list[0])):
                                modified_box_list[i][j].update(self.screen,(10+150*j,10+150*i),modified_box_list[i][j].value)
                        if result == True:
                            modified_box_list = self.spawn_new_item(modified_box_list)
                        for i in range(len(modified_box_list)):
                            for j  in range(len(modified_box_list[0])):
                                modified_box_list[i][j].update(self.screen,(10+150*j,10+150*i),modified_box_list[i][j].value)
            #Abrupt Win/Lose Conditions. Must fix.
            #if self.check_for_lose_condition(modified_box_list):
            #    continue
            if self.check_for_win_condition(modified_box_list):
                exit()
            for row in box_list:
                for box in row:
                    box.blitme()
            pygame.display.flip()
            self.screen.fill(BG_COLOUR)
class Box(pygame.sprite.Sprite):
    image = None
    def __init__(
        self, screen, img_filename, init_position):
        """Initialise the ball"""
        Sprite.__init__(self)
        self.screen = screen
        self.position = init_position
        self.x_dist = 150
        self.y_dist = 150
        self.value = 0
        if Box.image is None:
            Box.image =  pygame.image.load(img_filename)
            Box.image = pygame.transform.scale(Box.image,(140,140))
        self.image = Box.image
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(init_position)
    def update(self,screen,init_position,value):
        self.screen = screen
        self.position = init_position
        self.value = value
        if self.value == 0:
            Box.image =  pygame.image.load('data/EMPTY.png')
            Box.image = pygame.transform.scale(Box.image,(140,140))
        elif self.value == 2:
            Box.image =  pygame.image.load('data/SSN.jpg')
            Box.image = pygame.transform.scale(Box.image,(140,140))
        elif self.value == 4:
            Box.image =  pygame.image.load('data/BITS.jpg')
            Box.image = pygame.transform.scale(Box.image,(140,140))
        elif self.value == 8:
            Box.image =  pygame.image.load('data/IITM.jpg')
            Box.image = pygame.transform.scale(Box.image,(140,140))
        elif self.value == 16:
            Box.image =  pygame.image.load('data/IISC.jpg')
            Box.image = pygame.transform.scale(Box.image,(140,140))
        elif self.value == 32:
            Box.image =  pygame.image.load('data/TIFR.jpg')
            Box.image = pygame.transform.scale(Box.image,(140,140))
        elif self.value == 64:
            Box.image =  pygame.image.load('data/IIIT.jpg')
            Box.image = pygame.transform.scale(Box.image,(140,140))
        elif self.value == 128:
            Box.image =  pygame.image.load('data/SRM.jpg')
            Box.image = pygame.transform.scale(Box.image,(140,140))
        elif self.value == 256:
            Box.image =  pygame.image.load('data/SASTRA.png')
            Box.image = pygame.transform.scale(Box.image,(140,140))
        elif self.value == 512:
            Box.image =  pygame.image.load('data/NITT.jpg')
            Box.image = pygame.transform.scale(Box.image,(140,140))
        elif self.value == 1024:
            Box.image =  pygame.image.load('data/ANNA.jpg')
            Box.image = pygame.transform.scale(Box.image,(140,140))
        elif self.value == 2048:
            Box.image =  pygame.image.load('data/VIT.png')
            Box.image = pygame.transform.scale(Box.image,(140,140))
        self.image = Box.image
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(init_position)
    def move(self,xMove,yMove):
        self.rect.move_ip(xMove,yMove)
    def blitme(self):
        self.screen.blit(self.image, self.rect.topleft)
if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.MainLoop()
