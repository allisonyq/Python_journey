import turtle

def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
#circle：沿圆形轨迹爬行，rad：位置，angle：弧度值
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
#fd：直线爬行，参数是距离
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
#窗口的大小，起点是屏幕左上角
    turtle.setup(1300,800,0,0)
#运行轨迹宽度
    pythonsize=30
    turtle.pensize(pythonsize)
    turtle.pencolor("lightblue")
#启动时运行的方向
    turtle.seth(-40)
    drawSnake(40,80,5,pythonsize/2)

main()