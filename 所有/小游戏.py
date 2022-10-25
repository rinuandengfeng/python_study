print('=' * 20 + '欢迎来到游戏《唐僧大战白骨精》' +  '=' * 20)
print("请选择你的身份：")
print('\t 1.唐僧')
print('\t 2.白骨精')

num = int(input('请选择（1-2）：'))

if num == 1:
    print('你已经选择唐僧，恭喜你将以唐僧的身份进行游戏！')

elif num==2:
    print('什么你竟然选择了白骨精？太不要脸了，系统将自动分配你以唐僧的身份进行游戏')
else:
    print('你输入错误，统将自动分配你以唐僧的身份进行游戏')
print('你的攻击力为2，防御力为2')
boss_lift = 10
boss_gongjili = 10

gongjili = 2
fanyuli = 2
while True:
    print('请选择你要做的操作：')
    print('\t 1、练级')
    print('\t 2、打BOSS')
    print('\t 3、逃跑')
    shuzi = int(input('请选择（1-3）：'))
    #gongjili = 2
    #fanyuli = 2
    if shuzi == 1:
        gongjili = gongjili + 2
        fanyuli = fanyuli + 2

        print('='*65)
        print('恭喜你升级了，你现在的攻击力是{},生命值力是{}'.format(gongjili,fanyuli) )
        print('=' * 65)
    elif shuzi == 2:
        boss_lift = boss_lift - gongjili
        if boss_lift <= 0:
            print('白骨精受到了{}了伤害，重伤不治死了，唐僧赢得胜利了'.format(gongjili))
            break
        else:
            fanyuli = fanyuli - boss_gongjili
            print('唐僧受到了{}伤害，重视不治死了'.format(boss_gongjili))
            break
    elif shuzi == 3:
        print('游戏结束')
        break
    else:
        print('输入有误，请重新输入！')

