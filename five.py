"""
    判断输赢函数
"""
def checkWin(x,y):
    flag = False
    count = 1                #保存共有相同颜色多少棋子相连
    color =map[x][y]

    #横向判断
    i =1
    while color == map[x + i][y]:   #向右判断
        count += 1
        i += 1
    i=1
    while color == map[x - i][y]:   #向左判断
        count += 1
        i += 1
    if count >= 5:
        flag = True

    #纵向判断
    i2 = 1
    count2 = 1
    while color == map[x][y + i2]:  # 向上判断
        count2 += 1
        i2 += 1
    i2 = 1
    while color == map[x][y - i2]:  # 向下判断
        count2 += 1
        i2 += 1
    if count2 >= 5:
        flag = True

    #右上和左下判断
    i3 = 1
    count3 = 1
    while color == map[x + i3][y + i3]:  # 右上判断
        count3 += 1
        i3 += 1
    i3 = 1
    while color == map[x - i3][y - i3]:  # 左下判断
        count3 += 1
        i3 += 1
    if count3 >= 5:
        flag = True

    #右下和左上判断
    i4 = 1
    count4 = 1
    while color == map[x + i4][y - i4]:  # 右下判断
        count4 += 1
        i4 += 1
    i3 = 1
    while color == map[x - i4][y + i4]:  # 左上判断
        count4 += 1
        i4 += 1
    if count4 >= 5:
        flag = True

    return flag


"""
    走棋函数
"""
def callback(event):
    global turn
    x = (event.x)//40
    y = (event.y)//40
    print("click at",x,y,turn)
    if map[x][y] != "":
        showinfo(title= "提示",message = "已有棋子！")
    else:
        img1 = pics[turn]
        id = cv.create_image((x * 40 + 20, y * 40 + 20),image = img1)
        back.append((id,x,y))
        cv.pack()
        map[x][y] = str(turn)
        print_map()
        if checkWin(x,y):
            if turn == 0:
                showinfo(title= "提示",message = "黑方赢了！")
            else:
                showinfo(title= "提示",message = "白方赢了！")
          # 换下一方走棋
        if turn == 0:
            turn = 1
        else:
            turn = 0

"""
    悔棋函数
"""
def huiqi(event):
    global turn
    if len(back) == 0:
        showinfo(title= "提示",message = "已没有任何棋子！")
        return
    m = back.pop()
    id = m[0]
    x = m[1]
    y = m[2]
    map[x][y] = ''
    cv.delete(id)   # 删除棋子

    #换上一方走棋
    if turn == 0:
        turn = 1
    else:
        turn = 0


"""
    绘制棋盘函数
"""
def drawQipan():
    for i in range(0,15):
        cv.create_line(20,20+40*i,580,20+40*i,width = 2)
    for i in range(0,15):
        cv.create_line(20+40*i,20,20+40*i,580,width = 2)
    cv.pack


"""
    输出走棋信息
"""
def print_map():
    for i in range(0, 15):
        for j in range(0, 15):
            print(map[i][j],end='')
        print('w')


"""
    主函数
"""
from tkinter import *
from tkinter.messagebox import *


turn = 0
map = [[""for y in range(15)]for x in range(15)]
root = Tk()

pics = [PhotoImage(file = 'E:\Python file\\blacK.gif'),
        PhotoImage(file = 'E:\Python file\\white.gif')]  #调取棋子图片  格式为gif

root.title("五子棋v1.0")
back = []
cv = Canvas(root,bg = 'green',width = 610,height = 610) #棋盘
drawQipan()
cv.bind("<Button-1>",callback)   #走棋
cv.bind("<Button-3>",huiqi)      #悔棋
cv.pack()
root.mainloop()
