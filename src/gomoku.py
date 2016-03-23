#!/usr/bin/env python3
# coding=utf-8

__author__ = 'Chi Qingjun'

import re
import pdb

class Gomoku(object):
    '''使用矩阵坐标进行表示和运算的五子棋类'''

    def __init__(self, size=[15, 15]):
        '''初始化类：确定棋盘大小，棋子代码，棋子显示符号，判赢方法检测方向'''
        self.size = size    # 初始化棋盘大小
        self.piece = {'BLACK': 1, 'WHITE': -1}      # 黑棋和白棋内部表示值
        self.symbol = ['·', 'X', 'O']   # 代码为1用X显示，代码为-1用O显示
        self.directions = {(-1, 1), (0, 1), (1, 1), (1, 0)} # 判赢方法的检测方向
        self.reset()    # 调用reset方法初始化其他参数

    def reset(self):
        '''重置棋局方法：重置棋盘，最新一手落子位置和最新一手棋色'''
        self.board = [[0 for y in range(self.size[1])] for x in range(self.size[0])]    # 棋盘，从0开始的矩阵坐标系
        self.current_go = tuple()   # 最新一手的位置
        self.current_piece = self.piece['BLACK'] # 最新一手的颜色，黑棋先行
        print('Gomoku 五子棋 v0.2')
        self.print_board()

    def coordinate_calc(self, coord_a, coord_b):
        '''对两个点的坐标进行运算'''
        coord_sum = [0, 0]
        for i in range(2):
            coord_sum[i] = coord_a[i] + coord_b[i]
        return coord_sum

    def check_one_direction(self, direction):
        '''对一个方向进行检测方法'''
        pieces_num = 1      # 这一方向上的同色棋子总数
        check_ref = self.current_go   # 检测参考点
        check_direction = direction     # 当前检测方向
        reverse_direciton_flag = True   # 检测方向标志位

        # 检测过程
        while pieces_num < 5:
            # 计算当前检测棋子位置
            check_pos = self.coordinate_calc(check_ref, check_direction)
            # 如果当前检测棋子位置超出棋盘位置，则不检测该方向
            if check_pos[0] < 0 or check_pos[0] >= len(self.board) or check_pos[1] < 0 or check_pos[1] >= len(self.board[0]):
                # 如果检测方向标志位为True，则检测反方向，同时设置标志位为False
                if reverse_direciton_flag:
                    reverse_direciton_flag = False
                    check_direction = (-direction[0], -direction[1])
                    check_ref = self.current_go
                # 否则，结束检测
                else:
                    break
            # 如果检测棋子位置在棋盘内
            else:
                # 判断当前检测棋子与最新一手棋子是否同色
                # 如果同色，本方向上同色棋子总数加一，当前检测棋子位置成为新的检测参考点
                if self.board[check_pos[0]][check_pos[1]] == self.current_piece:
                    pieces_num += 1
                    check_ref = check_pos
                # 如果不同色，判断检测方向标志位
                else:
                    # 如果检测方向标志位为True，则检测反方向，同时设置标志位为False
                    if reverse_direciton_flag:
                        reverse_direciton_flag = False
                        check_direction = (-direction[0], -direction[1])
                        check_ref = self.current_go
                    # 如果不同色且标志位为False，那么说明两个方向上的检测都完成了，退出循环
                    else:
                        break
        # 如果是因为5棋子相连退出循环，那么返回True，否则返回False
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
        '''落子方法，参数为空格隔开的位置坐标字符串，如“3 5”'''
        go_pos_list = re.split(r'\s+', go_pos_str.strip())
        go_pos_x, go_pos_y = int(go_pos_list[0]), int(go_pos_list[1])   # 把字符串转化为棋盘上的坐标值
        # 判断落子坐标是否没有棋子
        if self.board[go_pos_x][go_pos_y] == 0:
            self.current_go = (go_pos_x, go_pos_y)
            self.board[self.current_go[0]][self.current_go[1]] = self.current_piece
            self.print_board()  # 输出棋盘
            # 判赢
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
        '''输出棋盘到终端'''
        for line in self.board:
            print(' '.join(self.symbol[element] for element in line))


if __name__ == '__main__':
    g = Gomoku([10, 10])
    result = g.go_piece(input('请落子，请执黑方下第一手：'))
    while result is not True:
        result = g.go_piece(input('请落子：'))
