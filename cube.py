from random import randint
import pygame as pg
import numpy as np
from math import radians, sin, cos

from translate import translate

class RubicsCube:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.state = [
            [
                [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
                [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
                [(255, 255, 255), (255, 255, 255), (255, 255, 255)]
            ],
            [
                [(0, 0, 255), (0, 0, 255), (0, 0, 255)],
                [(0, 0, 255), (0, 0, 255), (0, 0, 255)],
                [(0, 0, 255), (0, 0, 255), (0, 0, 255)]
            ],
            [
                [(255, 128, 0), (255, 128, 0), (255, 128, 0)],
                [(255, 128, 0), (255, 128, 0), (255, 128, 0)],
                [(255, 128, 0), (255, 128, 0), (255, 128, 0)]
            ],
            [
                [(0, 255, 0), (0, 255, 0), (0, 255, 0)],
                [(0, 255, 0), (0, 255, 0), (0, 255, 0)],
                [(0, 255, 0), (0, 255, 0), (0, 255, 0)]
            ],
            [
                [(255, 0, 0), (255, 0, 0), (255, 0, 0)],
                [(255, 0, 0), (255, 0, 0), (255, 0, 0)],
                [(255, 0, 0), (255, 0, 0), (255, 0, 0)]
            ],
            [
                [(255, 255, 0), (255, 255, 0), (255, 255, 0)],
                [(255, 255, 0), (255, 255, 0), (255, 255, 0)],
                [(255, 255, 0), (255, 255, 0), (255, 255, 0)]
            ]
        ]


    def draw_side(self, screen, index, x, y):
        rect_size = int(screen.get_height() / 15)
        for l in range(3):
            for p in range(3):
                pg.draw.rect(
                    screen,
                    self.state[index][l][p],
                    (
                        int(p * rect_size * 1.1 + rect_size * 3.4 * x + screen.get_width() / 4),
                        int(l * rect_size * 1.1 + rect_size * 3.4 * y),
                        rect_size,
                        rect_size
                    )
                )

    def draw_cube(self, screen):
        self.draw_side(screen, 0, 1, 0)
        self.draw_side(screen, 4, 0, 1)
        self.draw_side(screen, 1, 1, 1)
        self.draw_side(screen, 2, 2, 1)
        self.draw_side(screen, 3, 3, 1)
        self.draw_side(screen, 5, 1, 2)

    
    def project_cube(self, screen):
        self.project_element(screen, 0, 0, 0)

    def project_element(self, screen, off_x, off_y, off_z):
        scale = 150

        pos = [screen.get_width() / 2, screen.get_height() / 2.5]

        angle_x = radians(22.5)
        angle_y = radians(45)
        angle_z = radians(0)

        points = []

        points.append(np.matrix([-1.5, -1.5, 1.5]))
        points.append(np.matrix([1.5, -1.5, 1.5]))
        points.append(np.matrix([1.5, 1.5, 1.5]))
        points.append(np.matrix([-1.5, 1.5, 1.5]))
        points.append(np.matrix([-1.5, -1.5, -1.5]))
        points.append(np.matrix([1.5, -1.5, -1.5]))
        points.append(np.matrix([1.5, 1.5, -1.5]))
        points.append(np.matrix([-1.5, 1.5, -1.5]))

        projection_matrix = np.matrix([
            [1, 0, 0],
            [0, 1, 0]
        ])

        projected_points = [ [n, n] for n in range(len(points)) ]

        i = 0
        for point in points:
            rotated2d = np.dot(self.calc_rot_y(angle_y), point.reshape((3, 1)))
            rotated2d = np.dot(self.calc_rot_x(angle_x), rotated2d)
            rotated2d = np.dot(self.calc_rot_z(angle_z), rotated2d)
            projected2d = np.dot(projection_matrix, rotated2d)

            x = int(projected2d[0][0] * scale) + pos[0]
            y = int(projected2d[1][0] * scale) + pos[1]

            projected_points[i] = [x, y]

            pg.draw.circle(screen, (255, 0, 0), (x, y), 5)

            i += 1

        # for p in range(4):
        #     self.connect_points(screen, p, (p + 1) % 4, projected_points)
        #     self.connect_points(screen, p, p + 4, projected_points)
        #     self.connect_points(screen, p + 4, (p + 1) % 4 + 4, projected_points)

    def connect_points(self, screen, i, j, points):
        pg.draw.line(screen, (0, 0, 255), (points[i][0], points[i][1]), (points[j][0], points[j][1]), 3)

    def calc_rot_x(self, angle):
        return np.matrix([
            [1, 0, 0],
            [0, cos(angle), -sin(angle)],
            [0, sin(angle), cos(angle)]
        ])
    
    def calc_rot_y(self, angle):
        return np.matrix([
            [cos(angle), 0, sin(angle)],
            [0, 1, 0],
            [-sin(angle), 0, cos(angle)]
        ])
    
    def calc_rot_z(self, angle):
        return np.matrix([
            [cos(angle), -sin(angle), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1]
        ])


    def horizontal_turn(self, row, direction):
        if (row >= 0 and row <= 2) and (direction == 0 or direction == 1):
            if direction == 0: # Left
                self.state[1][row], self.state[2][row], self.state[3][row], self.state[4][row] = self.state[2][row], self.state[3][row], self.state[4][row], self.state[1][row]
                if row == 0:
                    self.state[0][0][0], self.state[0][0][1], self.state[0][0][2], self.state[0][1][2], self.state[0][2][2], self.state[0][2][1], self.state[0][2][0], self.state[0][1][0] = self.state[0][2][0], self.state[0][1][0], self.state[0][0][0], self.state[0][0][1], self.state[0][0][2], self.state[0][1][2], self.state[0][2][2], self.state[0][2][1]
                elif row == 2:
                    self.state[5][0][0], self.state[5][0][1], self.state[5][0][2], self.state[5][1][2], self.state[5][2][2], self.state[5][2][1], self.state[5][2][0], self.state[5][1][0] = self.state[5][0][2], self.state[5][1][2], self.state[5][2][2], self.state[5][2][1], self.state[5][2][0], self.state[5][1][0], self.state[5][0][0], self.state[5][0][1]

            elif direction == 1: # Right
                self.state[1][row], self.state[2][row], self.state[3][row], self.state[4][row] = self.state[4][row], self.state[1][row], self.state[2][row], self.state[3][row]
                if row == 0:
                    self.state[0][0][0], self.state[0][0][1], self.state[0][0][2], self.state[0][1][2], self.state[0][2][2], self.state[0][2][1], self.state[0][2][0], self.state[0][1][0] = self.state[0][0][2], self.state[0][1][2], self.state[0][2][2], self.state[0][2][1], self.state[0][2][0], self.state[0][1][0], self.state[0][0][0], self.state[0][0][1]
                elif row == 2:
                    self.state[5][0][0], self.state[5][0][1], self.state[5][0][2], self.state[5][1][2], self.state[5][2][2], self.state[5][2][1], self.state[5][2][0], self.state[5][1][0] = self.state[5][2][0], self.state[5][1][0], self.state[5][0][0], self.state[5][0][1], self.state[5][0][2], self.state[5][1][2], self.state[5][2][2], self.state[5][2][1]


    def vertical_turn(self, row, direction):
        if (row >= 0 and row <= 2) and (direction == 0 or direction == 1):
            if direction == 0: # Up
                self.state[0][0][row], self.state[0][1][row], self.state[0][2][row], self.state[1][0][row], self.state[1][1][row], self.state[1][2][row], self.state[5][0][row], self.state[5][1][row], self.state[5][2][row], self.state[3][0][2 - row], self.state[3][1][2 - row], self.state[3][2][2 - row] = self.state[1][0][row], self.state[1][1][row], self.state[1][2][row], self.state[5][0][row], self.state[5][1][row], self.state[5][2][row], self.state[3][2][2 - row], self.state[3][1][2 - row], self.state[3][0][2 - row], self.state[0][2][row], self.state[0][1][row], self.state[0][0][row]
                if row == 0:
                    self.state[4][0][0], self.state[4][0][1], self.state[4][0][2], self.state[4][1][2], self.state[4][2][2], self.state[4][2][1], self.state[4][2][0], self.state[4][1][0] = self.state[4][0][2], self.state[4][1][2], self.state[4][2][2], self.state[4][2][1], self.state[4][2][0], self.state[4][1][0], self.state[4][0][0], self.state[4][0][1]
                elif row == 2:
                    self.state[2][0][0], self.state[2][0][1], self.state[2][0][2], self.state[2][1][2], self.state[2][2][2], self.state[2][2][1], self.state[2][2][0], self.state[2][1][0] = self.state[2][2][0], self.state[2][1][0], self.state[2][0][0], self.state[2][0][1], self.state[2][0][2], self.state[2][1][2], self.state[2][2][2], self.state[2][2][1]
                
            elif direction == 1: # Down
                self.state[0][0][row], self.state[0][1][row], self.state[0][2][row], self.state[1][0][row], self.state[1][1][row], self.state[1][2][row], self.state[5][0][row], self.state[5][1][row], self.state[5][2][row], self.state[3][0][2 - row], self.state[3][1][2 - row], self.state[3][2][2 - row] = self.state[3][2][2 - row], self.state[3][1][2 - row], self.state[3][0][2 - row], self.state[0][0][row], self.state[0][1][row], self.state[0][2][row], self.state[1][0][row], self.state[1][1][row], self.state[1][2][row], self.state[5][2][row], self.state[5][1][row], self.state[5][0][row]
                if row == 0:
                    self.state[4][0][0], self.state[4][0][1], self.state[4][0][2], self.state[4][1][2], self.state[4][2][2], self.state[4][2][1], self.state[4][2][0], self.state[4][1][0] = self.state[4][2][0], self.state[4][1][0], self.state[4][0][0], self.state[4][0][1], self.state[4][0][2], self.state[4][1][2], self.state[4][2][2], self.state[4][2][1]
                elif row == 2:
                    self.state[2][0][0], self.state[2][0][1], self.state[2][0][2], self.state[2][1][2], self.state[2][2][2], self.state[2][2][1], self.state[2][2][0], self.state[2][1][0] = self.state[2][0][2], self.state[2][1][2], self.state[2][2][2], self.state[2][2][1], self.state[2][2][0], self.state[2][1][0], self.state[2][0][0], self.state[2][0][1]
                    

    def side_turn(self, row, direction):
        if (row >= 0 and row <= 2) and (direction == 0 or direction == 1):
            if direction == 0: # Clockwise
                self.state[0][2 - row][0], self.state[0][2 - row][1], self.state[0][2 - row][2], self.state[2][0][row], self.state[2][1][row], self.state[2][2][row], self.state[5][row][0], self.state[5][row][1], self.state[5][row][2], self.state[4][0][2 - row], self.state[4][1][2 - row], self.state[4][2][2 - row] = self.state[4][2][2 - row], self.state[4][1][2 - row], self.state[4][0][2 - row], self.state[0][2 - row][0], self.state[0][2 - row][1], self.state[0][2 - row][2], self.state[2][2][row], self.state[2][1][row], self.state[2][0][row], self.state[5][row][0], self.state[5][row][1], self.state[5][row][2]
                if row == 0:
                    self.state[1][0][0], self.state[1][0][1], self.state[1][0][2], self.state[1][1][2], self.state[1][2][2], self.state[1][2][1], self.state[1][2][0], self.state[1][1][0] = self.state[1][2][0], self.state[1][1][0], self.state[1][0][0], self.state[1][0][1], self.state[1][0][2], self.state[1][1][2], self.state[1][2][2], self.state[1][2][1]
                elif row == 2:
                    self.state[3][0][0], self.state[3][0][1], self.state[3][0][2], self.state[3][1][2], self.state[3][2][2], self.state[3][2][1], self.state[3][2][0], self.state[3][1][0] = self.state[3][0][2], self.state[3][1][2], self.state[3][2][2], self.state[3][2][1], self.state[3][2][0], self.state[3][1][0], self.state[3][0][0], self.state[3][0][1]
            
            elif direction == 1: #Counter clockwise
                self.state[0][2 - row][0], self.state[0][2 - row][1], self.state[0][2 - row][2], self.state[2][0][row], self.state[2][1][row], self.state[2][2][row],self.state[5][row][0], self.state[5][row][1], self.state[5][row][2],self.state[4][0][2 - row], self.state[4][1][2 - row], self.state[4][2][2 - row] = self.state[2][0][row], self.state[2][1][row], self.state[2][2][row], self.state[5][row][2], self.state[5][row][1], self.state[5][row][0], self.state[4][0][2 - row], self.state[4][1][2 - row], self.state[4][2][2 - row], self.state[0][2 - row][2], self.state[0][2 - row][1], self.state[0][2 - row][0]
                if row == 0:
                    self.state[1][0][0], self.state[1][0][1], self.state[1][0][2], self.state[1][1][2], self.state[1][2][2], self.state[1][2][1], self.state[1][2][0], self.state[1][1][0] = self.state[1][0][2], self.state[1][1][2], self.state[1][2][2], self.state[1][2][1], self.state[1][2][0], self.state[1][1][0], self.state[1][0][0], self.state[1][0][1]
                elif row == 2:
                    self.state[3][0][0], self.state[3][0][1], self.state[3][0][2], self.state[3][1][2], self.state[3][2][2], self.state[3][2][1], self.state[3][2][0], self.state[3][1][0] = self.state[3][2][0], self.state[3][1][0], self.state[3][0][0], self.state[3][0][1], self.state[3][0][2], self.state[3][1][2], self.state[3][2][2], self.state[3][2][1]


    def scramble(self):
        moves = ""
        for i in range(0, 20):
            x = randint(0, 2)
            y = randint(0, 2)
            z = randint(0, 1)
            if x == 0:
                self.horizontal_turn(y, z)
                moves += translate("horizontal", y, z) + " "
            elif x == 1:
                self.vertical_turn(y, z)
                moves += translate("vertical", y, z) + " "
            elif x == 2:
                self.side_turn(y, z)
                moves += translate("side", y, z) + " "

        return moves


    def U(self):
        self.horizontal_turn(0, 0)

    def Up(self):
        self.horizontal_turn(0, 1)

    def E(self):
        self.horizontal_turn(1, 1)

    def Ep(self):
        self.horizontal_turn(1, 0)

    def D(self):
        self.horizontal_turn(2, 1)

    def Dp(self):
        self.horizontal_turn(2, 0)

    def L(self):
        self.vertical_turn(0, 1)

    def Lp(self):
        self.vertical_turn(0, 0)

    def M(self):
        self.vertical_turn(1, 1)

    def Mp(self):
        self.vertical_turn(1, 0)

    def R(self):
        self.vertical_turn(2, 0)

    def Rp(self):
        self.vertical_turn(2, 1)

    def F(self):
        self.side_turn(0, 0)

    def Fp(self):
        self.side_turn(0, 1)

    def S(self):
        self.side_turn(1, 0)

    def Sp(self):
        self.side_turn(1, 1)

    def B(self):
        self.side_turn(2, 1)

    def Bp(self):
        self.side_turn(2, 0)