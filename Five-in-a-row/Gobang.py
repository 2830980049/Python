# 序列化和反序列化
import pickle
import test.py

#游戏类
class Save_Load():
    def __init__(self, maxx, maxy):
        self.maxx = maxx
        self.maxy = maxy
        self.color = False

    def Save(self, Checkboard, color):
        fpath = input('请输入棋盘保存路径：')
        # 以写的方式打开
        file = open(fpath, 'wb')
        self.color = color
        pickle.dump(self, file)

    def Load(self):
        fpath = input('请打开棋盘路径：')
        import os
        #F_OK表示是否找到文件
        if os.access(fpath, os.F_OK):
            #以读的方式打开
            file = open(fpath, 'rb')
            status = pickle.load(file)
            file.close()
        else:
            print('文件不存在！')


#记录棋局状态
def Play(Checkboard):
    End_chess = False
    color = True #表示黑方下
    while not End_chess:


# 主程序

# 表示被调用的时候，程序入口
if __name__ == '__main__':
    maxx = 10
    maxy = 10
    Checkboard = [[0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0]]
    Begin_End = Save_Load(maxx, maxy)
    Play(Checkboard)




