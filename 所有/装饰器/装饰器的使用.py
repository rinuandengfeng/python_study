# 产品经理：提需求 / 改需求

#如果超过22点不让玩儿游戏，如果不告诉时间，默认不让玩儿游戏

#开放封闭原则

def can_play(fn):
    def inner(x, y, *args, **kwargs):
        # print(args)
        # clock = kwargs['clock']
        clock = kwargs.get("clock", 23)
        if clock <= 22:

            fn(x, y)
        else:
            print('太晚了，赶紧睡')

    return inner


# 开放封闭原则
@can_play
def play_game(name, game):
    print('{}正在玩儿{}'.format(name, game))


play_game('张三', '王者荣耀', clock=18)
play_game('李四', '绝地求生', clock=23)
