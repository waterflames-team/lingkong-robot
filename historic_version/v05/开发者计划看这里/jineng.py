import random

class chengyu:
    # 成语接龙为CSDN博主「李孟笛」的原创代码，经过二次改编。
    def get_list():
        with open("chengyu.txt", "r+", encoding="utf-8") as f:
            content = f.read()
            url_list = content[:-1].split(',')
        return url_list

    def get_first_word(url_list):
        randoms = random.choice(url_list)
        print('我先说一个：', randoms)
        return randoms


    def zhurenjie():
        zhuren = input('我接：\n')
        return zhuren


    def jiqijie(url_list, zhuren):
        chengyus = []

        for url in url_list:
            if url[0] == zhuren[-1]:
                chengyus.append(url)

        a = random.choice(chengyus)
        print('俺接：', a)
        return a

    if __name__ == '__main__':
        print('成语接龙游戏，请接成语或俗语，接的第一个字要跟上面的成语最后一个字相同哦\n当你不想玩的时候可以输入"我不玩了"结束\n当你玩不过我的时候可以输入"我认输"哈哈哈哈')
        url_list = get_list()
        randoms = get_first_word(url_list)

        while True:
            zhuren = zhurenjie()
            if zhuren == '我不玩了':
                print('切，是不是玩不起！！拜拜')
                break
            if zhuren == '我认输':
                print('哈哈，我赢了！！')
                break
            if zhuren not in url_list:
                print('耍赖，这不是个成语或俗语,重新说')

            elif zhuren[0] != randoms[-1]:
                print('耍赖,你没有接最后一个字，重说')
                print('最后一个字是：', randoms[-1])
            else:
                try:
                    jiqi = jiqijie(url_list, zhuren)
                except:
                    print('俺接不出来，你赢了！')
                    break
                randoms = jiqi