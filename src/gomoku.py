#!/usr/bin/env python3
# coding=utf-8

__author__ = 'Chi Qingjun'

import re
import pdb

class Gomoku(object):
    '''使用矩阵坐标进行表示和运算的五子棋类'''
    def __init__(self, size=[15, 15]):
        self.size = size
        self.piece = {'BLACK': 1, 'WHITE': -1}
        self.symbol = ['·', 'X', 'O']   # 代码为1用X表示，代码为-1用O表示
        self.directions = {(-1, 1), (0, 1), (1, 1), (1, 0)}
        self.reset()

    def reset(self):
        self.board = [[0 for y in range(self.size[1])] for x in range(self.size[0])]    # 棋盘
        self.current_go = tuple()   # 上一手的位置
        self.current_piece = self.piece['BLACK'] # 上一手的颜色，黑棋先行
        self.print_board()

    def coordinate_calc(self, coord_a, coord_b):
        '''对两个点的坐标进行运算'''
        coord_sum = [0, 0]
        for i in range(2):
            coord_sum[i] = coord_a[i] + coord_b[i]
        return coord_sum

    def check_one_direction(self, direction):
        pieces_num = 1      # 这一方向上的同色棋子总数
        check_ref = self.current_go   # 检测参考点
        check_direction = direction     # 当前检测方向
        reverse_direciton_flag = True   # 检测方向标志位

        while pieces_num < 5:
            # 计算当前检测棋子位置
            check_pos = self.coordinate_calc(check_ref, check_direction)
            # 如果当前检测棋子位置超出棋盘位置，则不检测该方向，根据检测方向标志位来决定是否检测反方向，或直接结束：
            if check_pos[0] < 0 or check_pos[0] >= len(self.board) or check_pos[1] < 0 or check_pos[1] >= len(self.board[0]):
                if reverse_direciton_flag:
                    reverse_direciton_flag = False
                    check_direction = (-direction[0], -direction[1])
                    check_ref = self.current_go
                else:
                    break
            else:
                # 判断当前检测棋子与上一手棋子同色
                if self.board[check_pos[0]][check_pos[1]] == self.current_piece:
                    # 如果同色，本方向上同色棋子总数加一，当前检测棋子位置成为新的检测参考点
                    pieces_num += 1
                    check_ref = check_pos
                else:
                    if reverse_direciton_flag:
                        # 如果不同色且标志位为True，则进行反方向的检测，同时设置标志位为False
                        reverse_direciton_flag = False
                        check_direction = (-direction[0], -direction[1])
                        check_ref = self.current_go
                    else:
                        # 如果不同色且标志位为False，那么说明两个方向上的检测都完成了，退出循环
                        break
        if pieces_num == 5:
            return True
        else:
            return False

    def check_win(self):
        '''判赢需要检测所有方向上的五子连珠情况，如果有任何一个五子连珠，则返回True；否则返回False'''
        for item in self.directions:
            check_result = self.check_one_direction(item)
            if check_result:
                return True
        return False

    def go_piece(self, go_pos_str):
        go_pos_list = re.split(r'\s+', go_pos_str.strip())
        go_pos_x, go_pos_y = int(go_pos_list[0]), int(go_pos_list[1])
        if self.board[go_pos_x][go_pos_y] == 0:
            self.current_go = (go_pos_x, go_pos_y)
            self.board[self.current_go[0]][self.current_go[1]] = self.current_piece
            self.print_board()
            if self.check_win():
                print('五子连珠，胜利！')
                return True
            else:
                if self.current_piece == self.piece['BLACK']:
                    self.current_piece = self.piece['WHITE']
                else:
                    self.current_piece = self.piece['BLACK']
        else:
            print('你不能在已经有棋子的位置落子！')
        return False

    def print_board(self):
        for line in self.board:
            print(' '.join(self.symbol[element] for element in line))


if __name__ == '__main__':
    g = Gomoku([10, 10])
    result = g.go_piece(input('请落子，黑子先行：'))
    while result is not True:
        result = g.go_piece(input('请落子：'))
