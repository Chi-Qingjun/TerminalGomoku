#!/usr/bin/env python3
# coding=utf-8

__author__ = 'Chi Qingjun'

class Gomoku(object):
    '''使用矩阵坐标进行表示和运算的五子棋类'''
    def __init__(self, size=[15, 15]):
        self.size = size
        self.piece = {'BLACK': 1, 'WHITE': -1}
        self.directions = {(-1, 1), (0, 1), (1, 1), (1, 0)}

    def reset(self):
        self.board = [[0 for y in range(self.size[1])] for x in range(self.size[0])]    # 棋盘
        self.current_go = tuple()   # 上一手的位置
        self.current_piece = self.piece['BLACK'] # 上一手的颜色，黑棋先行

    # def check_win(self, go_piece):
    #     pass
    def coordinate_calc(self, coord_a, coord_b):
        '''对两个点的坐标进行运算'''
        coord_sum = []
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
            check_pos = coordinate_calc(check_ref, check_direction)
            # 判断当前检测棋子与上一手棋子同色
            if board[check_pos[0]][check_pos[1]] == self.current_piece:
                # 如果同色，本方向上同色棋子总数加一，当前检测棋子位置成为新的检测参考点
                pieces_num += 1
                check_ref ＝ check_pos
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
        for item in self.directions:
            check_result = check_one_direction(item)
            if check_result:
                return True
        return False

    def go_piece(self, go_pos):
        pass


if __name__ == '__main__':
    g = Gomoku([3, 5])
    g.reset()
    g.board[2][3] = 1
    print(g.board)
