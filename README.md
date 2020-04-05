# 灵空机器人[![star](https://gitee.com/lingkonggzs/lingkong-robot/badge/star.svg?theme=gray)](https://gitee.com/lingkonggzs/lingkong-robot/stargazers)[![fork](https://gitee.com/lingkonggzs/lingkong-robot/badge/fork.svg?theme=gray)](https://gitee.com/lingkonggzs/lingkong-robot/members)![主要语言](https://img.shields.io/badge/语言-python3-lightgrey.svg)![版本](https://img.shields.io/badge/版本-V0.5.9.200321-lightgrey.svg)

----
* 灵空机器人是一个由非凡小王开发、折腾调协助维护的灵活可配的中文语音对话机器人，并根据    wukong-robot进行改编（改编部分较多，主要借鉴了悟空后台端）。
* 灵空机器人可以做到语音唤醒，语音对话，正常的闲聊，以及查询天气等实用工具
# 跳转
----
[灵空完整版文档](http://docs.lingkong-robot.cn)(包括灵空在线和灵空本地的使用说明)/[灵空在线](http://server.lingkong.store:88/)（账号随意，密码12345）
# 目录
----
- [运行方式](#运行方式)
- [更新时间](#更新时间)
- [有关技能的说明](#有关技能的说明)
- [运行环境](#运行环境)
- [联系作者](#联系作者)
- [灵空生态介绍](#灵空生态介绍)
- [安装环境（Mac）](#安装环境mac)
- [安装环境（deepin）](#安装环境deepin)
- [适配](#适配)
- [运行](#运行)
- [技能](#技能)
- [开发者计划](https://gitee.com/lingkonggzs/lingkong-robot/tree/master/%E5%BC%80%E5%8F%91%E8%80%85%E8%AE%A1%E5%88%92%E7%9C%8B%E8%BF%99%E9%87%8C)
- [后台](#后台)


# 运行方式：
----
* snowboy→baidu_asr→技能库→baidu_tts
# 更新时间：
----
* 本项目节假日、周末几乎每天都更新，除非遇到瓶颈或有个人上的事


# 有关技能的说明
----
> * 目前这个版本可能除闲聊外其他的技能会比较弱，因为没加语义理解，所以一定要和他的触发词对应，只能多，不能少（比如笑话技能的触发词是笑话，你说的话内就必须要有笑话两个字，你可以说“讲个笑话”，加上“讲个”两个字，但你不能说“笑”，因为里面没有“笑话”两个字）

> * 后续会在近2.0版本完善好大部分的体验，争取有和xiaolan（蓝之酱作品）、wukong（wzpan作品）一样的体验


# 联系作者
----

> 如果你有问题，请你通过以下方式联系非凡小王（作者）

* 作者钉钉：15392006285（加好友请说明来历）

* 作者qq：2822603942（加好友请说明来历）

# 灵空生态介绍
----

灵空生态分为以下五个方面

#### \* 灵空宠物
（可移动，可对话）

#### \* 灵空伴侣
（在手机上运行）

#### \* 灵空在线版
 (在web上用，使用win的人可以使用）

#### \* 灵空本地版
（使用Linux和MacOS的可以使用）

#### \* 灵空技能
（进仓库里的开发者计划的文件夹里看详细介绍）


# 运行环境
----
> * 1.使用者如是win平台，那么请去deepin官网和virtualbox官网下载deepin的镜像和virtualbox的安装包，然后进行安装、装载镜像
>> * 2.如果你刚安装好deepin，请执行
```shell
    sudo apt update
    sudo apt-get install git
```
安装git，然后自行确定你的deepin有没有python3环境（正常来说是有的）


* 使用者如是Mac平台，那么可以直接开始安装了

* 使用者如果是deepin平台，那么参考win平台的方法

* 使用者如是非deepin的linux平台，那你可以暂时参考一下debian的安装方法，如有问题，欢迎通过下面的联系方式，联系作者


# 安装环境（Mac）
---

* 首先你要下载好0.5.9.200321版的灵空机器人
```shell
git clone https://gitee.com/lingkonggzs/lingkong-robot.git
```

### 开始安装：
----
**首先你要保证你已经安装了python3和pip3，没安装的可以百度**

1.
```shell
cd lingkong-robot
```
2.
```shell
./install.sh
```
**并且中途如果出现Press RETURN to continue or any other key to abort需要按一下回车，如果出现password：需要输入密码**

* 到这里你的环境安装就完成了
* 如果你安装出现了问题，欢迎你去介绍页找到作者的联系方式以联系作者
----

# 安装环境（deepin）
----
* 此安装部分已在deepin、debian、rasbian上测试成功，如出现安装失败的情况，请联系非凡小王，qq:2822603942


1. 首先你要下载好0.5.9.200321版的灵空机器人
```shell
git clone https://gitee.com/lingkonggzs/lingkong-robot.git
```
2. 首先你要保证你已经安装了python3和pip3，没安装的可以百度


* 如果你想要换源可执行
```shell
sudo curl -L http://download.lingkong-robot.online/change.sh | sudo bash
```
3.
```shell
cd lingkong-robot
./install.sh
```

* 到这里你的环境安装就完成了

***（如果换源时长时间没有动静，那么是需要密码的，执行完一键命令后输入用户密码再按下回车就可以换源啦）***

***(如果换源时出现“need root”或者没有更换成功，那么请手动下载：***
```shell
wget http://download.lingkong-robot.online/change.sh
sudo sh change.sh
```
***注意：这两条是需要分别执行的！！！在执行第二句时可能需要密码！输入并按下回车即可！！！）***
### 如果你安装不成功，那么请去文档的介绍页联系作者

## 适配
----
### 第一步：

#### 用终端cd进lingkong-robot

### 第二步：

#### 在终端输入：
```shell
cd pei
```
#### 以进入配置so包的文件夹

### 第三步：

#### 在终端输入：
```
git clone https://github.com/Kitt-AI/snowboy.git
```
#### 上面这是一行哈（窗口小的会分行，但终端里不要分行写）

### 第四步：

#### 在终端输入
```
cd snowboy/swig/Python3
make
```
#### 等待完成，完成之后确认Python3文件夹下是否有一个py文件和一个so文件，有那么说明配置完成，没有请去文档的介绍页联系作者

## 运行
----
### 如果你刚刚配置完，那么请重复输入几次`cd ../`直到回到lingkong-robot版本号

### 回到lingkong-robot之后运行：
```shell
python3 lingkong.py
```
### 然后说出唤醒词“snowboy”即可唤醒
## 唤醒反馈
###### 你可以修改'import'部分下的'model = 1'为1或2
1代表唤醒后说ding，然后录完音说dong
2代表唤醒后说在呢或干嘛，录完音啥都不说
默认为1

## 技能
----
### 闲聊（图灵）：

 

通过api接入图灵，以作为灵空的主要闲聊部分

请图灵已经认证好的，不要使用我提供的api\_key，请自行修改自己的5个api\_key和1个api\_id到配置文件（config.json）的tuling，下的id、key1、2.....中，不会的可以去文档的介绍页找作者

#### 调用方法：

闲聊向的话均可（如你说的话不符其他技能的调用条件，那么你的话也会传到这来）

### 数学计算（图灵）：
通过api接入图灵，利用里面的自带技能库满足灵空的部分功能
此功能可进行加减乘除、乘方、开方、指数、对数、统计等多种运算
请图灵已经认证好的，不要使用我提供的api\_key，请自行修改自己的5个api\_key和1个api\_id到配置文件（config.json）的tuling，下的id、key1、2.....中，不会的可以去文档的介绍页找作者
#### 调用方法：
所有涉及计算的均可

### 中英互译（图灵）：
通过api接入图灵，利用里面的自带技能库满足灵空的部分功能
此功能提供优质的中文和英语的在线互译服务
请图灵已经认证好的，不要使用我提供的api\_key，请自行修改自己的5个api\_key和1个api\_id到配置文件（config.json）的tuling，下的id、key1、2.....中，不会的可以去文档的介绍页找作者
#### 调用方法：
中→英：XXX的英文是啥（如：苹果的英语是啥）
英→中：直接拼英文字母（如：a-p-p-l-e）

### 疫情防控（图灵）【临时性技能】：
通过api接入图灵，利用里面的自带技能库满足灵空的部分功能
此功能包含新型冠状病毒肺炎的基础知识（如主要症状、传播途径、隔离方式等）、预防措施（如消毒方式、口罩、洗手的正确方式等）和相关医疗人员、医疗药物等信息。
请图灵已经认证好的，不要使用我提供的api\_key，请自行修改自己的5个api\_key和1个api\_id到配置文件（config.json）的tuling，下的id、key1、2.....中，不会的可以去文档的介绍页找作者
#### 调用方法：
按介绍中所说的即可（如“如何正确洗手”“个人如何自我防护”等）

### 讲故事（图灵）：
通过api接入图灵，利用里面的自带技能库满足灵空的部分功能
可随机提供成语故事、寓言故事、童话故事等多种类的故事内容。
请图灵已经认证好的，不要使用我提供的api\_key，请自行修改自己的5个api\_key和1个api\_id到配置文件（config.json）的tuling，下的id、key1、2.....中，不会的可以去文档的介绍页找作者
#### 调用方法：
按介绍的描述所说即可（如：“讲个故事”“讲个故事吧”“讲个白雪公主的故事吧”等）

### 星座运势（图灵）：
通过api接入图灵，利用里面的自带技能库满足灵空的部分功能
提供十二星座查询，每个星座的今天、明天、本周、本月、本年星座运势查询，时刻掌握星运动向。开发者使用图灵机器人API既可直接使用，无需进行功能的开发，便捷易用。
请图灵已经认证好的，不要使用我提供的api\_key，请自行修改自己的5个api\_key和1个api\_id到配置文件（config.json）的tuling，下的id、key1、2.....中，不会的可以去文档的介绍页找作者
#### 调用方法：
按介绍的描述所说即可（如：“处女座资料”“处女座运势”“处女座性格”等）

### 脑筋急转弯（图灵）：
通过api接入图灵，利用里面的自带技能库满足灵空的部分功能
随机返回脑筋急转弯数据，脑筋急转弯最早起源于古代印度。就是指当思维遇到特殊的阻碍时，要很快的离开习惯的思路，从别的方面来思考问题。现在泛指一些不能用通常的思路来回答的智力问答题。
请图灵已经认证好的，不要使用我提供的api\_key，请自行修改自己的5个api\_key和1个api\_id到配置文件（config.json）的tuling，下的id、key1、2.....中，不会的可以去文档的介绍页找作者
#### 调用方法：
脑筋急转弯（建议一字都不要改）

### 歇后语（图灵）：
通过api接入图灵，利用里面的自带技能库满足灵空的部分功能
歇后语是中国劳动人民自古以来在生活实践中创造的一种特殊语言形式，是一种短小、风趣、形象的语句。它由前后两部分组成：前一部分起“引子”作用，像谜面，后一部分起“后衬”的作用，像谜底，十分自然贴切。此功能数据种类齐全，包含节气、季节、动物、昆虫、人物、谐音、等方面，应有尽有。
请图灵已经认证好的，不要使用我提供的api\_key，请自行修改自己的api\_key和api\_id到文件中，不会的可以去文档的介绍页找作者
#### 调用方法：
歇后语、说个歇后语

### 绕口令（图灵）：
通过api接入图灵，利用里面的自带技能库满足灵空的部分功能
随机快速返回绕口令数据，绕口令又称急口令、吃口令、拗口令等。是一种汉族传统的语言游戏，由于它是将若干双声、叠词词汇或发音相同、相近的语、词有意集中在一起，组成简单、有趣的语韵，要求快速念出，所以读起来使人感到节奏感强，妙趣横生。
请图灵已经认证好的，不要使用我提供的api\_key，请自行修改自己的5个api\_key和1个api\_id到配置文件（config.json）的tuling，下的id、key1、2.....中，不会的可以去文档的介绍页找作者
#### 调用方法：
绕口令、说个绕口令

### 顺口溜（图灵）：
通过api接入图灵，利用里面的自带技能库满足灵空的部分功能
顺口溜，是民间流行的一种口头韵文，句子长短不齐，纯用口语，念起来很顺口。我们把当代流行的这种语言现象称作“新民谣”，也就是顺口溜。无需开发功能，便捷易用。
请图灵已经认证好的，不要使用我提供的api\_key，请自行修改自己的5个api\_key和1个api\_id到配置文件（config.json）的tuling，下的id、key1、2.....中，不会的可以去文档的介绍页找作者
#### 调用方法：
顺口溜、给我讲个顺口溜

### 天气（心知天气）：
利用心知天气的天气数据，进行分析当天天气（只有当天天气数据）
使用时请确定你是否已经把自己的城市填到config.json的city下的引号里了，不然会是作者的城市
#### 调用方法：
“今天天气怎么样”等含“天气”二字的句子

### 笑话（全自制）：



通过调用本地的笑话库，获取笑话

经过我和znx的寻找，目前已经找到了40条的笑话，日常使用基本足够（我不相信你每天都要喊40次“讲个笑话”）

#### 调用方法：

“讲个笑话”、“说个笑话吧”等语句中含“笑话”二字的词

### 鹦鹉学说话（全自制）：



通过存储用户说的话
然后做tts输出
以达到鹦鹉学说话的效果

#### 调用方法：

学我说XXXX

### 代办（全自制）：



通过os模块往本地放代办的相关日志文件

通过os模块，往本地创建/删除本地的代办日志文件，以达到代办的效果

因本技能不那么完善，暂时没有查看代办的功能，所以，用户如果要查看代办，可以去lingkong-robot下的daiban\_log的文件夹查看自己已经创建的代办（请不要删除名为ceshi的文件，否则可能报错）

#### 调用方法：

“添加代办 XXX”、“删除代办 XXX”



### 语料库（全自制）：



通过调用语料库里的指定语料，来触发指定语录

#### 调用方法：

因0.5.7.200316版内自带一些语录，所以可以调用以下指定语录：“你爸爸是谁”、“你会做啥”，使用者可以通过研究代码自行添加属于自己的语料，也可以去文档的介绍页找到作者的联系方式，以联系作者，获取添加语料的方法。


### 贡献技能：



因为灵空的技能库真的太少啦，所以欢迎给位开发者为灵空做技能贡献

#### 要求：

最后给我的文件可以用文字交互，（就拿讲笑话这个技能为例，你给我的技能最后要能呈现以下效果：终端输入讲笑话，然后文字反馈给我一个笑话，以此类推，制作技能）然后我要是觉得这个技能可以，就会做适配，如果我觉得可能需要做图形化的时候，我会把它放到后台和文档中哦！

## 后台
----
### 0.5.7.200316以上版本的后台目前已有以下功能：

介绍：灵空机器人的基本介绍和文档跳转

日志：本地的运行日志

修改配置项教程：教你0.5.7.200316以上版怎么修改配置项（将在1或2版本改为直接更改配置）

打赏：对作者非凡小王的打赏（厚颜无耻，手动滑稽）

对话：与灵空机器人的文字对话，以便出门使用（在线版的雏形）

清单：自己开发的技能“代办”的技能页（尚未开发完成）



### 手机端无左侧的菜单？

方案一：部分手机横屏就可以出现左侧菜单

方案二：记住路径（"/"为介绍页，"/ds"是打赏页,"/log"是日志页,"/study"是修改配置项教程页,"/dh"是对话页,"/list"是清单页，此路径适用于0.5.7.200316以上版）

# 文档更多内容请访问最开头写的'灵空完整版文档'