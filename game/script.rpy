# 生日派对的 Ren'Py 游戏框架

# 定义角色
define s = Character("云云",image="yunyun")
define d = Character("戴戴",who_color="#cfacd0",image="daidai")
define q = Character("云帆",image="yunfan")

# 定义图像
define config.screen_width = 1920
define config.screen_height = 1080
image bg room_1 = Transform("images/room_1.png", fit="cover")
image bg room_2 = Transform("images/room_2.jpg", fit="cover")
image bg room_3 = Transform("images/room_3.png", fit="cover")
image bg room_4 = Transform("images/room_4.jpg", fit="cover")
image bg room_5 = Transform("images/room_5.png", fit="cover")
image bg room_6 = Transform("images/room_6.jpg", fit="cover")
image bg room_7 = Transform("images/room_7.jpg", fit="cover")
image bg happy = Transform("images/happy.png", fit="cover")
image bg room_8 = Transform("images/room_8.png", fit="cover")
image bg room_9 = Transform("images/room_9.jpg", fit="cover")
image bg room_10 = Transform("images/room_10.png", fit="cover")
image bg end = Transform("images/end.png", fit="cover")
image bg nice = Transform("images/nice.png", fit="cover")
image side yunfan :
    "images/yunfan.png"
    zoom 0.3
image side daidai ="images/daidai.png"
image side yunyun:
    "images/yunyun.png"
    zoom 0.4
image card :
    "images/card.png"
    zoom 0.8
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image cake = "images/cake.png"
image computer = "items/computer.png"
image boy_1 :
    "images/boy_1.jpg"
    zoom 0.6
image book_1 :
    "images/book_1.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）

image book_2 :
    "images/book_2.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）

image qq_1 :
    "images/qq_1.png"
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）

image book_3 :
    "images/book_3.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image book_4 :
    "images/book_4.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image qs_1 :
    "images/qs_1.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image qs_2 :
    "images/qs_2.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）

image qs_3 :
    "images/qs_3.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image qs_4 :
    "images/qs_4.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image qs_5 :
    "images/qs_5.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image as_1 :
    "images/as_1.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image as_2 :
    "images/as_2.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image as_3 :
    "images/as_3.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）

image as_41 :
    "images/as_41.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image as_42 :
    "images/as_42.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image as_5 :
    "images/as_5.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）

image gift :
    "images/gift.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image gi_3 :
    "images/gi_3.jpg"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image gi_41 :
    "images/gi_41.jpg"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image gi_42 :
    "images/gi_42.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image gi_5 :
    "images/gi_5.jpg"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image soft :
    "images/soft.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image bi :
    "images/bi.jpg"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image yue :
    "images/yue.jpg"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image gai :
    "images/gai.jpg"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image luo :
    "images/luo.jpg"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）
image dangao :
    "images/dangao.png"
    zoom 0.6
    xalign 0.5  # 水平居中
    yalign 0.45  # 稍微向上移动（默认0.5是垂直居中）

    
# 定义音乐
define bgm_music_1 = "audio/sanye.mp3"
define bgm_music_2 = "audio/hua.mp3"




# 初始变量
default has_gift_1 = False  # 判断是否准备好礼物
default has_gift_2 = False  # 礼物是否被揭开
default year = 1  # 当前是第几年
default code_done = False  # 判断第三年代码是否完成
default first_card=False #判断扉页的封面是否完成
default second_card=False #判断扉页其余内容是否完成
default q_1=False
default q_2=False
default q_3=False
default q_4=False
default q_5=False
default answer=True
# 开始场景
define gui.text_font = "simsun.ttc"
define gui.name_text_font = "simsun.ttc"
define gui.text_size = 40
define gui.name_text_size = 40
label start:
    scene bg room_1 with fade
    play music bgm_music_1 loop

    "深夜的空气带着一丝微凉，窗外的世界已经沉寂。街道上的路灯投下淡淡的光斑，寂静而宁远。屋内，只有电脑屏幕散发出的微光，在黑暗中显得尤为孤单。"
    "男孩坐在桌前，眼神专注而深邃。指尖在键盘上轻轻舞动，思绪却早已飘向远方。"
    "思考着如何为他的好朋友准备一份生日礼物，心中充满了迷茫与期待。思绪像是随风飘散的叶片，偶尔飘然落地，忽而又在他指尖间纷飞开来。"
    "前两年，他激发了最真挚的创造力，创造了两份意义非凡的礼物。但今年，不知是什么原因，他的创造力似乎已经耗尽。"
    "电脑前的光影在他的脸庞上舞动，偶尔折射出些许疲惫，却依旧有一种执着的坚韧。夜深了，但他知道，直到找到那个完美的礼物，他的心才会安定下来。"
    scene bg room_2 with fade

    s "今年再给戴戴准备出别样的生日礼物怕是一件难事了。"
    s "不过回想一下两年前送给她的生日礼物，或许会给我提供一些灵感。"

    menu:
        "回忆第一年的生日礼物":
            jump year_1_gift
        "回忆第二年的生日礼物":
            jump year_2_gift

label year_1_gift:
    if has_gift_2:
        scene bg room_2 with fade
    "高二年级，这是云云与戴戴相识的第一年，也是云云第一次为戴戴准备生日礼物。此刻，他正在思考给戴戴制作什么样的礼物。"
    "作为学生的他们，每天要做大量的笔记。此时，云云无意间瞥见了桌上的活页本，心里拿定了主意。"
    s "那就送她一个活页本吧，活页本里面的扉页，用定制款。"
    "决定之后，云云去了小区里的商店，买了一本他认为最好看的活页本。不仅如此，手感也十分不错，非常软的本子~"
    show book_1 with dissolve
    s "接下来来到扉页了，我应该如何定制呢。"
    hide book_1 with dissolve

    menu:
        "在微信里找戴戴要一些图片作为内容":
            jump find
        "在可画网站上为她亲手做一张符合她性格的图片来当做封面":
            jump self_make

label self_make:
    s"设计的第一步，寻找一些可用的元素。梅花，云朵，田野等都可以当做一些意向。"
    s"设计的第二步，添加一些字。“烟雨江南”，“不负盛世，顶峰相见”……这些寓意不错，也加上。再添加上对她的寄语：‘愿你趟过世俗浑水，也不染那一身的世故’。"
    s"最后，添加一些独属于她的东西。"
    show book_2 with dissolve
    "云云决定从知乎上寻找一些线索。打开知乎，云云把戴戴的知乎头像和名字放到了图片上。"
    s"再加上一些诗句吧，加上哪一句好呢？"

    # 创建一个循环，让用户不断选择直到选择正确的选项
    label choose_poem:
        menu:
            "梦里不知身是客，一晌贪欢。":
                # 用户选择正确，跳转或继续
                jump correct_choice
            "飞流直下三千尺，疑是银河落九天。":
                # 用户选择错误，给出提示并重新选择
                s"这句话好像不那么符合戴戴的性格，要不要再想想看呢？"
                jump choose_poem  # 重新回到选择


label correct_choice:
    s"这句话貌似更加符合戴戴的性格一些，那就这句吧！"
    hide book_2 with dissolve
    show book_3 with dissolve
    s"最后署个名： “打杂的zyj” ，大功告成！"

    hide book_3 with dissolve
    $ first_card=True
    if second_card==False:
        s"只有一张图片貌似过于单调了一点，要不再找戴戴要几张她喜欢的图片吧。"
        menu:
            "找戴戴要图片。":
                jump find
    else:
        s"终于把扉页选好了，发给淘宝商家定制吧！"
        menu:
            "交给商家":
                jump first_year_end
label find :
    show qq_1 with dissolve
    "此时云云打开了QQ，点击戴戴的头像，开始了聊天。"
    s"你有喜欢的风景照吗?"
    d"有呀，不过你要干什么呢？"
    s"secret!"
    hide qq_1 with dissolve
    "戴戴虽然疑惑，但还是发了几张照片过去。"
    show book_4 with dissolve
    s"ok!这下图片够了。"
    hide book_4 with dissolve
    $ second_card=True
    if first_card==False:
        s"仅有几张风景图的话，体现不出特殊感，我还是为她定制一张封面吧。"
        menu:
            "在可画网站上为她亲手做一张符合她性格的图片来当做封面":
                jump self_make
    else:
        s"终于把扉页选好了，发给淘宝商家定制吧！"
        menu:
            "交给商家":
                jump first_year_end

label first_year_end:
    # 展示定制礼物图像
    scene bg room_3 with fade
    "快递终于送到了。此时来到了2月18日，云云来到了班级。体育课即将上课，班里没什么人。"
    "云云走近戴戴的座位，发现她正在整理上节课的笔记。"
    "她的眉头微微皱起，似乎在思索着每一个知识点的深意，笔尖在纸上飞快地舞动，时而停顿，时而跃动。笔记本的每一页都被她写得井井有条，字迹清秀，笔迹流畅，仿佛每一个字都承载着她对学习的专注与热情。"
    s"戴戴，这是送你的生日礼物！"
    show card with dissolve
    d"哇，好漂亮的本子！"
    "戴戴十分惊喜，打开了本子。"
    d"居然是定制的！"
    hide card  with dissolve
    "体育课的铃声此时响了起来，由于云云选的课是查迟到较严格的武术，所以他急忙去上课了。"
    "于是，戴戴收到礼物的表情和想法，也成了谜。"
    
    

    $ has_gift_1 = True  # 礼物已经准备好
    if has_gift_2==False:
        scene bg room_4 with fade
        s"第一年的回忆就此结束，不过没有找到太多的灵感。我们仍未知道戴戴当时的心情，也不知道她是否还珍藏着那个本子。"
        menu:
            "继续回忆第二年的礼物，看看还能不能找出更多的灵感。":
                jump year_2_gift
    else:
        scene bg room_4 with fade
        s"我们仍未知道戴戴当时的心情，也不知道她是否还珍藏着那个本子。不过回忆了两年的礼物选择，今年送什么礼物我已经有了眉目！"
        menu:
            "开始第三年的准备。":
                jump year_3_effort

label year_2_gift:
    scene bg room_5 with fade
    "这是云云与戴戴相识的第二年，也是高三的重要时刻。本来，戴戴和云云说好的是不要互相送礼物的。"
    "大年三十的晚上，云云在房间里做“圆梦杯”高考模拟题。此时看到QQ群里有人聊到了刘谦的“洗牌”魔术，他突然临机一动。"
    s "我可以出一套具有情景特征的数学试卷，就以“戴戴的生日会”为标题，以数学元素为主线，讲述一个故事。"
    "此时，云云又打开了QQ。"
    show qq_1 with dissolve
    s"既然不送礼物，那我就送你一套数学试卷吧。"
    d"这个可以有（偷笑）。"
    d"不会是洗牌题吧？"
    s"（自信满满）不会，这套卷子绝对出乎你的意料"
    hide qq_1 with dissolve
    "那么，该如何出这套卷子就成了当前的挑战。"
    scene bg room_6 with fade
    "大年三十的夜晚，家里的灯光透过窗帘微微洒在屋内，柔和而温暖。厨房里传来锅碗瓢盆的轻响，远处亲戚们的笑声和聊天声交织在一起，带着节日的热闹氛围。"
    "然而，云云坐在自己房间的桌前，面前摆着一张白纸和几本翻开的书。窗外的烟花声偶尔炸响，却似乎与他无关，他的目光专注而深邃，整个人沉浸在那份安静的思考之中。"
    
    s"标题已经选定，接下来该考虑内容了，首先决定选择几个题目。"
label self_made:

    # 让玩家选择题目数
    menu:
        "选择4个题目":
            $ num_topics = 4
            jump check_topics
        "选择5个题目":
            $ num_topics = 5
            jump check_topics
        "选择6个题目":
            $ num_topics = 6
            jump check_topics

label check_topics:
    # 判断选择的题目数
    if num_topics == 5:
        s"选择了5个题目，这个数量刚好，既能涵盖足够的内容，又不显得过于繁琐。"
        jump started
    elif num_topics==6:
        s"6个题目貌似太多了点，选少一点吧。"
        jump self_made  # 重新跳回选择界面
    else :
        s"4个题目可能无法涵盖全面的剧情，选多一些吧！"
        jump self_made

label started:
    s"现在我们需要考虑五个题目，考虑哪一题呢？"

    menu:
        "考虑第一题":
            jump question_1
        "考虑第二题":
            jump question_2
        "考虑第三题":
            jump question_3
        "考虑第四题":
            jump question_4
        "考虑第五题":
            jump question_5

label question_1:
    if not q_1:
        s"开头可以放一个“判断戴戴受欢迎程度的题目”，那么可以找一道什么样的题目呢？"
        menu:
            "泛函分析题。":
                s"感觉有点不太符合，要不重新选选？"
                jump question_1
            "比较大小题。":
                show qs_1 with dissolve
                s"这个挺不错，可以选择2021年全国乙卷的选择压轴，来比较戴戴生日会某指标的增长率，进而判断受欢迎程度。"
                hide qs_1 with dissolve
        $ q_1 = True  # 设置第一题已考虑过
    else:
        "你已经考虑过第一题，重新选择题目。"
        jump started  # 跳回开始界面
    
    jump check_all_done

label question_2:
    if not q_2:
        show qs_2 with dissolve
        s"第二题，可以考虑一个和礼物相关的题，那么2023新高考一卷多选压轴的题目就最适合不过了，4个选项可以看做四种礼物。"
        hide qs_2 with dissolve
        $ q_2 = True  # 设置第二题已考虑过
    else:
        "你已经考虑过第二题，重新选择题目。"
        jump started  # 跳回开始界面
    
    jump check_all_done

label question_3:
    if not q_3:
        s"第三题，也可以思考和礼物相关的题，可以设置成蛋糕和贺卡，这里考虑贺卡上写什么，进而出一道题。写什么比较好呢？"
        menu:
            "拉格朗日中值定理。":
                s"感觉没有什么特别的寓意，要不重新选选？"
                jump question_3
            "函数图像。":
                show qs_3 with dissolve
                s"这个挺不错，可以选择前些年北京卷的选择题，画一个好看的图像来表达寓意。"
        hide qs_3 with dissolve
        $ q_3 = True  # 设置第三题已考虑过
    else:
        "你已经考虑过第三题，重新选择题目。"
        jump started  # 跳回开始界面
    
    jump check_all_done

label question_4:
    if not q_4:
        show qs_4 with dissolve
        s"第四题可以选择生日蛋糕了，那么自然圆锥曲线题就成了不二之选。"
        hide qs_4 with dissolve
        $ q_4 = True  # 设置第四题已考虑过
    else:
        "你已经考虑过第四题，重新选择题目。"
        jump started  # 跳回开始界面
    
    jump check_all_done

label question_5:
    if not q_5:
        show qs_5 with dissolve
        s"最后一个题可以考虑一下派对的活动，可以选择比较火热的宁波一模打结问题。"
        hide qs_5 with dissolve
        $ q_5 = True  # 设置第五题已考虑过
    else:
        "你已经考虑过第五题，重新选择题目。"
        jump started  # 跳回开始界面
    
    jump check_all_done

label check_all_done:
    # 检查所有题目是否都已考虑过
    if q_1 and q_2 and q_3 and q_4 and q_5:
        s"所有题目都已考虑完毕！"
        # 进行后续环节
        jump next_step  # 假设后续环节在 `next_step` 标签里
    else:
        "请选择一个剩下未考虑过的题目。"
        jump started  # 跳回开始界面

label next_step:
    scene bg room_7 with fade
    s"现在所有题目都已考虑完毕，接下来进行下一步————串联剧情！"
    ".......（历经长时间的思考，云云已经把生日派对的元素融入至题目，并加入了“环节”和“事件”的小标签）......"
    menu:
        "开启“戴夕悦的生日会”。":
            jump start_1
label start_1:
    "背景概要：2024年2月18日，戴戴在家举行成年生日会，请你协助她完成相关事宜。"
    
    menu:
        "环节一：点人数":
            jump point_count

label point_count:
    "环节一：戴戴清点了一下今年来参加生日宴会的人数，发现相比去年，同学到来人数有所提升。"
    "其中小学同学提升的百分数值约为a，初中同学提升的百分数值约为b，高中同学提升的百分数值约为c。"
    "你能判断出戴戴今年更受哪个时期的同学欢迎吗？(a=2ln1.01,b=ln1.02,c=根号下1.04-1)"
    menu:
        "查看解答":
            pass
    show as_1 with dissolve
    "看来还是更受小学同学欢迎啊。"
    hide as_1 with dissolve
    menu:
        "事件一：神秘人的礼物":
            jump mystery_gift

label mystery_gift:
    show gi_3 with dissolve
    "事件一：宴会进行中，突然一个神秘人送来了礼物，包装是一个棱长为1m的正方体盒子。"
    
    menu:
        "环节二：猜礼物":
            jump guess_gift

label guess_gift:
    "环节二：大家纷纷猜测礼物的内容。"
    "小程说：‘可能是一个皮球？’（直径为0.99m）"
    "小孟说：‘难道是一个金字塔形装饰？’（所有棱长均为1.4m的四面体）"
    "小蔡说：‘我想不到啥，我猜是一根金箍棒。’（底面直径为0.01m，高为1.8m的圆柱体）"
    "小缪说：‘听说戴戴最近在保持苗条的身材，这肯定是一个体重称！’（底面直径为1.2m，高为0.01m的圆柱体）"
    "仅从礼物能否放下的角度，谁的猜测是合理的？"
    hide gi_3 with dissolve
    menu:
        "查看解答":
            pass
    show as_2 with dissolve
    "小程，小蔡，小缪都是合理的！"
    hide as_2 with dissolve
    menu:
        "事件二：拆礼物":
            jump unwrap_gift

label unwrap_gift:
    "事件二：戴戴满怀期待地拆开包装，发现里面是一个草莓蛋糕和一张贺卡，贺卡上有一句‘生日快乐’和一个爱心图案。"
    show gi_42 with dissolve
    "大家的注意力集中在这张贺卡上的数学图案上。"
    hide gi_42 with dissolve
    menu:
        "环节三：看贺卡":
            jump check_card

label check_card:
    "环节三：喜欢数学的同学们研究起了这个图案，他们发现方程满足C：x^2 + y^2 = 1 + |x|y。"
    "小章提出了三个结论。"
    "①曲线C恰好经过6个整点（即横、纵坐标均为整数的点）；"
    "②曲线C上任意一点到原点的距离都不超过根号2；"
    "③曲线C所围成的‘心形’区域的面积小于3。"
    "一旁的数学课代表小牛反驳道：“你有个结论是错的！”"
    "请问是哪一个？"
    menu:
        "查看解答":
            pass
    show as_3 with dissolve
    "结论③原来是错的啊！"
    hide as_3 with dissolve
    menu:
        "事件三：研究蛋糕":
            jump research_cake

label research_cake:
    show gi_41 with dissolve
    "事件三：大家把关注度转移到了蛋糕上。蛋糕是圆形的，中间的草莓部分是椭圆形。"
    "蛋糕盒外面标注：椭圆长轴为40cm，离心率为0.5，但没有圆形蛋糕的规格。"
    hide gi_41 with dissolve
    menu:
        "环节四：切蛋糕":
            jump cut_cake

label cut_cake:
    "环节四：大家开始切蛋糕。"
    show dangao with dissolve
    "他们惊奇地发现，如果按如图所示这样切蛋糕，切出来的永远是个矩形！"
    hide dangao with dissolve
    "此时小唐惊呼：“我知道蛋糕的规格了！”大家纷纷夸小唐聪明。"
    "戴戴十分开心，决定按照这种切法给喜欢草莓的小唐切下一块最大的这样的蛋糕。"
    "小唐谦虚地说：“我只需要最小的一块就行了。”"
    "请问蛋糕的半径大小以及如何切出一块最大和最小的蛋糕？"
    menu:
        "查看解答":
            pass
    show as_41 with dissolve
    "原来是蒙日圆的结论！"
    hide as_41 with dissolve
    show as_42 with dissolve
    "原来是蒙日圆的结论！"
    hide as_42 with dissolve
    menu:
        "环节五：做游戏":
            jump play_game

label play_game:
    "环节五：宴会的最后一项是做游戏。"
    show gi_5 with dissolve
    "大家决定比给绳子打结的速度。"
    "经过激烈的比拼，心灵手巧的戴戴赢得了最终的冠军。"
    "打结速度最慢的是小杨。小杨有些不好意思。他说："
    "“虽然我打结速度慢，但我知道这些绳子能打多少种不同的结。这n根绳子恰好能围成一个圈的概率为(2^(2n-1)n!(n-1)!)/((2n)!)”"
    "大家震惊了，纷纷对小杨的发现表示赞许。"
    "最后的问题，请验证小杨的观点。"
    hide gi_5 with dissolve
    menu:
        "查看解答":
            pass
    show as_5 with dissolve
    "原来如此，小杨也太聪明了！"
    hide as_5 with dissolve
    menu:
        "完（作者：云帆）。":
            jump if_end
label if_end:
    s"这下终于把礼物做完咯！"
    menu:
        "非常完美！":
            jump school
        "貌似还缺少了点什么......":
            jump if_next
label if_next:
    s"要不我加上个意外发现的彩蛋呗！"
    menu:
        "继续事件四：意外发现":
            jump unexpected_discovery

label unexpected_discovery:
    scene bg happy with fade
    "事件四：同学们走后，戴戴突然发现，贺卡下面还有一行小字：“愿金榜题名，顶峰相见。”"
    "她眉头一紧，关于神秘人是谁，心中已经有了答案。"
    s"这才算是最终版！"
    "之后，云云又在文件最后加上了他亲手做的贺卡————有着第三题函数图像的，爱心贺卡。"
    jump school

label school:
    scene bg room_8 with fade
    "此时静待开学吧~"# 后续的剧情或流程
    "开学恰好是戴戴生日的这一天，同学们要返校上晚自习。"
    s"等了半天，戴戴都不来，她不会生病了吧？"
    "云云十分焦急，等到了上课戴戴也没来。"
    "云云坐在教室的角落，目光不时扫向门口，心跳愈发急促。他时而低头看手中的礼物盒，时而又焦急地抬起头，仿佛每一分每一秒的等待都在拉扯着他的心。时间如同流沙般悄无声息地从指缝间溜走，他的心却被那份沉甸甸的期盼紧紧攥住。"
    "正当此时，戴戴终于来了，坐到了自己的座位上开始自习，云云看到后长舒一口气。"
    "终于熬到了晚自习下课，云云来到了戴戴的座位旁。"
    show gift with dissolve
    s"这是送你的礼物！"
    d"真是一张卷子？"
    "戴戴十分吃惊。"
    s"生日快乐，戴戴。"
    "云云送完礼物后就急匆匆地回去刷题了。他不敢看戴戴的反应，不知道是什么原因。"
    "至于最后戴戴有没有打开卷子看，看了之后是什么反应，都无法得知了，只能让云云和电脑前的作者自行脑补。"
    $ has_gift_2 = True  # 礼物已经揭开

    if has_gift_1==False:
        scene bg room_4 with fade
        s"第二年的回忆就此结束，不过没有找到太多的灵感。我们仍未知道戴戴当时的心情，也不知道她是否仔细地看了那每一道题。"
        menu:
            "继续回忆第一年的礼物，看看还能不能找出更多的灵感。":
                jump year_1_gift
    else:
        scene bg room_4 with fade
        s"我们仍未知道戴戴当时的心情，也不知道她是否仔细地看了那每一道题。不过回忆了两年的礼物选择，今年送什么礼物我已经有了眉目！"
        menu:
            "开始第三年的准备。":
                jump year_3_effort


label year_3_effort:
    scene bg room_9 with fade
    "2025年，进入兰州大学信息学院的云云，积累了许多Python的知识。"
    s "今年，我可以用Python做一个手机软件来当做生日礼物，让戴戴把其留存于手机中，予以纪念。"
    "云云的初步想法是回忆前两年给戴戴准备礼物的场景的游戏。主要视角是云云自己。"

    "那么要以什么顺序来编写这个程序呢？"
    
    menu:
        "配置环境，框架设计，内容填写，细节优化":
            $ selected_order = ["配置环境", "框架设计", "内容填写", "细节优化"]
            jump check_order
        "框架设计，配置环境，内容填写，细节优化":
            $ selected_order = ["框架设计", "配置环境", "内容填写", "细节优化"]
            jump check_order
        "内容填写，框架设计，配置环境，细节优化":
            $ selected_order = ["内容填写", "框架设计", "配置环境", "细节优化"]
            jump check_order
        "细节优化，配置环境，框架设计，内容填写":
            $ selected_order = ["细节优化", "配置环境", "框架设计", "内容填写"]
            jump check_order
        # 其他排列组合选项同理...

label check_order:
    # 检查是否选择了正确的顺序
    if selected_order == ["配置环境", "框架设计", "内容填写", "细节优化"]:
        s "你选择了正确的顺序，接下来进入程序的下一环节。"
        jump new_step  # 进入下一步环节
    else:
        s "顺序不对，请重新选择。"
        jump year_3_effort  # 跳回开始标签，重新选择顺序

label new_step:
    s "程序编写的下一步已经开始了……"
    "通过大量地调试代码，云云完成了基本的框架编写。现在他想在程序里面加入一些有趣的问题。"
    "此时作者也想起来前几天密室最后一关的趣味小问题。"

    # 第一个问题
    "问题1：哪种动物的心脏跳动次数最多？"
    menu:
        "鲸鱼":
            s "鲸鱼的心脏跳动次数并不是最多，答错了哦！"
            $ answer=False
            jump new_step  # 错误跳回重新选择
        "兔子":
            s "恭喜你，答对了！兔子的心脏跳动次数确实最多！"
            $ correct1 = True
            jump question_2a  # 正确跳到第二个问题
        "乌龟":
            s "乌龟的心脏跳动次数比较少，不是最多哦！"
            $ answer=False
            jump new_step  # 错误跳回重新选择
        "老虎":
            s "老虎的心脏跳动次数也不是最多的哦！"
            $ answer=False
            jump new_step  # 错误跳回重新选择

label question_2a:
    "问题2：下面哪个人最美？"
    menu:    
        "戴夕悦":
            s "恭喜你，答对了！戴戴永远是最美的~"
            $ correct2 = True
            jump question_3a  # 正确跳到第三个问题
        "费马":
            s "这尼玛是男的！"
            $ answer=False
            jump new_step  # 错误跳回重新选择
        "工藤有希子":
            s "相信自己！"
            $ answer=False
            jump new_step  # 错误跳回重新选择
        "高木同学":
            s "相信自己！"
            $ answer=False
            jump new_step  # 错误跳回重新选择

label question_3a:
    "问题3：太阳是如何产生光和热的？"
    menu:
        
        "通过核融合反应":
            s "恭喜你，答对了！太阳的光和热正是通过核融合反应产生的！"
            $ correct3 = True
            jump question_4a  # 正确跳到第四个问题
        "通过化学反应":
            s "化学反应并不是太阳光热的来源哦，答错了！"
            $ answer=False
            jump new_step  # 错误跳回重新选择
        "通过电能转换":
            s "太阳并不是通过电能转换来产生光热的，答错了！"
            $ answer=False
            jump new_step  # 错误跳回重新选择
        "通过风能转换":
            s "风能并不是太阳产生光热的方式，答错了！"
            $ answer=False
            jump new_step  # 错误跳回重新选择

label question_4a:
    "问题4：世界上最长的河流是哪条？"
    menu:
        
        "长江":
            s "长江虽然很长，但不是世界最长的河流哦，答错了！"
            $ answer=False
            jump new_step  # 错误跳回重新选择
        "尼罗河":
            s "恭喜你，答对了！尼罗河是世界上最长的河流！"
            $ correct4 = True
            jump question_5a  # 正确跳到第五个问题
        "亚马逊河":
            s "亚马逊河虽然很长，但不是最长的，答错了！"
            $ answer=False
            jump new_step  # 错误跳回重新选择
        "密西西比河":
            s "密西西比河也不是世界最长的河流哦，答错了！"
            $ answer=False
            jump new_step  # 错误跳回重新选择

label question_5a:
    "问题5：在“戴夕悦的生日会”中，事件三的标签名是什么？"
    menu:

        "看贺卡":
            s "别把事件和环节搞混了！"
            $ answer=False
            jump new_step  # 错误跳回重新选择
        "切蛋糕":
            s "还没到事件四呢，就想着切蛋糕了，是不是没吃夜宵肚子饿了？"
            $ answer=False
            jump new_step  # 错误跳回重新选择
        "讨论蛋糕":
            s "很像，就差一点点了~"
            $ answer=False
            jump new_step  # 错误跳回重新选择
        "研究蛋糕":
            s "终于答对了，我就知道你还记得~"
            $ correct5 = True
            jump all_corre  # 正确跳到所有问题答对后的环节

label all_corre:
    s "太棒了！你成功回答了所有的问题，程序也进入了下一步！"
    # 可以在这里加入你后续的环节    # 后续环节的代码
    show soft with dissolve
    "历经千辛万苦，云云终于完成了软件。"
    hide soft with dissolve
    scene bg nice with fade
    "在软件的最后，他也给戴戴画了一幅新的贺卡，祝贺戴戴生日快乐，同时对未来表示愿景。"
    

    # 展示第三年敲代码的努力情景
    $ code_done = True  # 表示代码完成
    s "每一行代码，都是我对她的祝福，每一个页面，都是我对我们友谊的见证。"
    if answer:
        menu:
            "完成软件并发送":
                jump software_done
            "???":
                jump gift_given_3
    menu:
        "完成软件并发送":
            jump software_done

label gift_given_3:
    s"恭喜你，一次性答对上述的五道题目，获得了彩蛋2！"
    "沉默已久的程序员从电脑背后现身。"
    q"除了这个具有纪念意义的游戏，我还会送你一个其他的附赠品，敬请期待哟~"
    jump caice
label caice:
    "猜猜它是什么？"
    menu:
        "《概率论与数理统计》":
            show gai with dissolve
            "知道明天会不会中奖？想了解生活中的每一份幸运背后的数学奥秘？《概率论与数理统计》告诉你：别总想着中彩票，能活到明天就已经很幸运了！"
            hide gai with dissolve
            jump caice
        "月光镜":
            show yue with dissolve
            "照亮每一个黑夜，反射每一份光辉。月光镜，让你看见的不只是自己，还有星辰大海——更重要的是，看到你人生中的美好瞬间！"
            hide yue with dissolve
            jump caice
        "bilibili年度大会员":
            show bi with dissolve
            "一年365天，一颗追剧的心！Bilibili年度大会员，别让你的快乐止步于一分钟，解锁无广告，超清画质，你的追剧利器，只差你一个‘大会员’！"
            hide bi with dissolve 
            jump caice
        "兰州大学骆驼证":
            show luo with dissolve
            "当你站在黄河边，看到那座骆驼，它不只是一只骆驼，它是兰州大学的象征！拿到骆驼证，你就拥有了通往知识的‘无限沙漠绿洲’。"
            hide luo with dissolve
            jump caice
        "不猜了，继续":
            jump software_done

label software_done:
    scene bg end with fade
    "软件最后发送成功了，戴戴的反应如何，最后也不得而知。"
    q "故事到这里就要结束了"
    q"每年，给戴戴准备礼物，我都花了很多心思。每一次送出礼物的时候，她都让我觉得这份友谊特别有意义。"
    q"谢谢你，戴戴，感谢你这三年来的陪伴，有缘再会咯~"

    "完结撒花，感谢陪伴。（PS：游戏中的两个彩蛋你都找到了吗？）"
    menu:
        "重新开始游戏，寻找彩蛋":
            jump start
        "结束游戏，请作者喝一杯下午茶。":
            return
    return
