import turtle

# 計算二次貝塞爾曲線的點
def quadratic_bezier(t, p0, p1, p2):
    x = (1 - t)**2 * p0[0] + 2 * (1 - t) * t * p1[0] + t**2 * p2[0]
    y = (1 - t)**2 * p0[1] + 2 * (1 - t) * t * p1[1] + t**2 * p2[1]
    return (x, y)

#繪製初音未來
'''
/*
 * _______________#########_______________________ 
 * ______________############_____________________ 
 * ______________#############____________________ 
 * _____________##__###########___________________ 
 * ____________###__######_#####__________________ 
 * ____________###_#######___####_________________ 
 * ___________###__##########_####________________ 
 * __________####__###########_####_______________ 
 * ________#####___###########__#####_____________ 
 * _______######___###_########___#####___________ 
 * _______#####___###___########___######_________ 
 * ______######___###__###########___######_______ 
 * _____######___####_##############__######______ 
 * ____#######__#####################_#######_____ 
 * ____#######__##############################____ 
 * ___#######__######_#################_#######___ 
 * ___#######__######_######_#########___######___ 
 * ___#######____##__######___######_____######___ 
 * ___#######________######____#####_____#####____ 
 * ____######________#####_____#####_____####_____ 
 * _____#####________####______#####_____###______ 
 * ______#####______;###________###______#________ 
 * ________##_______####________####______________ 
 */
'''

# 繪製二次貝塞爾曲線
def draw_quadratic_bezier(p0, p1, p2):
    turtle.speed(0)
    turtle.pensize(2)  # 每次繪製前顯式設置筆畫大小
    points = []  # 儲存所有計算出的點
    t = 0
    step = 0.01
    
    while t <= 1:
        point = quadratic_bezier(t, p0, p1, p2)
        points.append(point)
        t += step
    

    # 移到起始點
    turtle.penup()
    turtle.goto(points[0])  
    turtle.pendown()
    
    # 一次性畫出所有點
    for point in points:
        turtle.goto(point)
 
# 設定畫布大小為 1280x720
turtle.setup(1280, 720)

#設定視窗標題
turtle.title("雷姆...是誰?")
# 設定畫布背景顏色
turtle.bgcolor("white")

# 隱藏圖標
turtle.hideturtle()


"""
/*
 *                        _oo0oo_
 *                       o8888888o
 *                       88" . "88
 *                       (| -_- |)
 *                       0\  =  /0
 *                     ___/`---'\___
 *                   .' \\|     |// '.
 *                  / \\|||  :  |||// \
 *                 / _||||| -:- |||||- \
 *                |   | \\\  - /// |   |
 *                | \_|  ''\---/''  |_/ |
 *                \  .-\__  '-'  ___/-. /
 *              ___'. .'  /--.--\  `. .'___
 *           ."" '<  `.___\_<|>_/___.' >' "".
 *          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
 *          \  \ `_.   \_ __\ /__ _/   .-` /  /
 *      =====`-.____`.___ \_____/___.-`___.-'=====
 *                        `=---='
 * 
 * 
 *      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * 
 *            佛祖保佑       永不當機     永無BUG
 */
"""


##############繪製圖案輪廓#############
# 從datas.txt讀取座標
data = []#儲存座標
try:
    with open("datas.txt", "r") as f:
        for line in f:
            try:
                line_data = eval(line)
                if line_data is not None:
                    data.append(line_data)
            except (SyntaxError, NameError) as e:
                print(f"Error evaluating line: {line.strip()} - {e}")
except FileNotFoundError:
    print("Error: 'datas.txt' file not found.")
except IOError as e:
    print(f"Error reading file: {e}")

#!!!!!!!!!!務必背誦全文!!!!!!!!!
'''
蕾姆知道，昴是哪怕身處無邊的黑暗中，也會伸出手的勇敢之人。
蕾姆喜歡昴摸我的頭，彷彿能透過手掌與頭髮的接觸，與昴心意相通。
蕾姆喜歡昴的聲音，每聽到你的話，就彷彿心被溫暖了；
蕾姆喜歡昴的眼神，雖然平常很銳利，但我喜歡那溫柔待人時柔軟下來的目光；
蕾姆喜歡昴的手指，明明是男孩子卻又著修長的手指，但牽手的時候能感到這果然是男孩子的手，手指強力又纖細；
蕾姆喜歡昴的行走方式，結伴行走的時候，偶然會像確認蕾姆有沒有跟上一般回頭，蕾姆喜歡這樣的行走方式。
蕾姆喜歡昴的睡顏，像嬰兒一樣毫無防備，睫毛稍微有點長。
被觸碰臉頰的話，表情會變得相當平靜。
壞心眼的摸唇也不會察覺到，讓蕾姆感到心裡滿滿的喜歡你。昴如果要討厭自己的話。
蕾姆就希望你知道蕾姆了解昴的那麼多優點。
蕾姆昴只明白自己的事情，蕾姆所看到的昴，昴又知道多少呢？
因為昴是蕾姆的英雄，在那昏暗的森林裡，在那迷失了自我的世界中，你救了橫衝直撞的蕾姆。
剛醒來動彈不得的蕾姆，魔法使用過度疲憊的姊姊。
為了讓我們逃走而做誘餌，正面應戰魔獸。
完全沒有勝算，可能輕易威脅到生命，即使如此你還是活下來了，還是那麼溫暖地回到了蕾姆的懷抱中。
醒來，微笑著把蕾姆最需要的話再最想聽的時候，由最渴望的人說出來。
蕾姆的時間一直是停止的，那個大火之夜，從失去了姐姐以外的所有事物那晚開始，蕾姆的時間就一直停止著。
停止的時間，冰凍的心。
被昴甜美地融化，溫柔地推動。
那個瞬間，那個早晨，蕾姆獲得了巨大的救贖。
昴一定不知道，當時的蕾姆有多高興。
所以蕾姆相信昴，就算在艱苦痛苦，就算昴堅持不下去，就算世上的人都不相信昴，就連昴自己都不相信自己，蕾姆也相信你。
因為拯救了蕾姆的昴才是真正的英雄
'''
# 繪製二次貝塞爾曲線
for i in range(len(data)):
    # 定義二次貝塞爾曲線的控制點
    p0_quad = (data[i][0], data[i][1])  # 起點
    p1_quad = (data[i][2], data[i][3])  # 控制點
    p2_quad = (data[i][4], data[i][5])  # 終點
    
    draw_quadratic_bezier(p0_quad, p1_quad, p2_quad)  # 繪製二次貝塞爾曲線  
#####################################


# 完成畫圖
turtle.done()

