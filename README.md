此项目已停止维护，全新版本请前往[https://gitee.com/lkteam/ring-robot-x](https://gitee.com/lkteam/ring-robot-x)

# 灵空机器人介绍

灵空机器人是一个灵活可配的中文语音对话机器人，并根据wukong-robot进行改编（改编部分较多，主要借鉴了悟空后台端）制作。灵空机器人可以做到语音唤醒，语音对话，正常的闲聊，以及查询天气等实用工具

# 运行方式：

图灵+技能+snowboy+baidu\_tts、asr

# 最新版本：

目前更新到0.5.9.200321(057200316)

# 有关技能的说明
## 目前这个版本可能除闲聊外其他的技能会比较弱，因为没加语义理解，所以一定要和他的触发词对应，只能多，不能少（比如笑话技能的触发词是笑话，你说的话内就必须要有笑话两个字，你可以说“讲个笑话”，加上“讲个”两个字，但你不能说“笑”，因为里面没有“笑话”两个字），后续会在近2.0版本完善好大部分的体验，争取有和xiaolan（蓝之酱作品）、wukong（wzpan作品）一样的体验


# 运行环境

使用者如是win平台，那么请去deepin官网和virtualbox官网下载deepin的镜像和virtualbox的安装包，然后进行安装、装载镜像

如果你刚安装好deepin，请执行


## sudo apt update


## sudo apt-get install git


安装git，然后自行确定你的deepin有没有python3环境（正常来说是有的）

使用者如是Mac平台，那么可以直接开始安装了

使用者如果是deepin平台，那么参考win平台的方法

使用者如是非deepin的linux平台，那你可以暂时参考一下debian的安装方法，如有问题，欢迎通过下面的联系方式，联系作者



# 联系作者

如果你有问题，请你通过以下方式联系Epeiuss（作者）

- 作者钉钉：15392006285（加好友请说明来历）

- 作者qq：2822603942（加好友请说明来历）


# 安装环境（Mac）


### 首先你要下载好0.5.9.200321版的灵空机器人
~~~
git clone https://gitee.com/lingkonggzs/lingkong-robot-bata.git
~~~


## 开始安装：
### 首先你要保证你已经安装了python3和pip3，没安装的可以百度
## 必做的第一步：

```
cd lingkong-robot
```


### 执行：

```
./install.sh

```

### 并且中途如果出现Press RETURN to continue or any other key to abort需要按一下回车，如果出现password：需要输入密码

## 到这里你的环境安装就完成了

## 如果你安装出现了问题，欢迎你去介绍页找到作者的联系方式以联系作者


# 安装环境（deepin）

#### 此安装部分已在deepin、debian、rasbian上测试成功，如出现安装失败的情况，请联系Epeiuss，qq:2822603942

### 首先你要下载好0.5.9.200321版的灵空机器人
~~~
git clone https://gitee.com/lingkonggzs/lingkong-robot-bata.git
~~~

## 开始安装：

### 首先你要保证你已经安装了python3和pip3，没安装的可以百度

### 如果你想要换源可执行
~~~
sudo curl -L http://download.lingkong-robot.online/change.sh | bash
~~~

## 必做的第一步：

```
cd lingkong-robot
```


### 执行：

```
./install.sh

```

## 到这里你的环境安装就完成了

## 如果你安装不成功，那么请去文档的介绍页联系作者

## 适配

#### 第一步：

### 用终端cd进lingkong-robot版本号

#### 第二步：

### 在终端输入：cd pei

### 以进入配置so包的文件夹

#### 第三步：

### 在终端输入：

```
git clone https://github.com/Kitt-AI/snowboy.git
```

### 上面这是一行哈（窗口小的会分行，但终端里不要分行写）

#### 第四步：

### 在终端输入

```
cd snowboy/swig/Python3
```
### 再输入：
```
make
```

### 等待完成，完成之后确认Python3文件夹下是否有一个py文件和一个so文件，有那么说明配置完成，没有请去文档的介绍页联系作者

## 运行

### 如果你刚刚配置完，那么请重复输入几次`cd ../`直到回到lingkong-robot版本号

### 回到lingkong-robot版本号之后运行：python3 lingkong.py


## 技能

### 闲聊（图灵）：

 

通过api接入图灵，以作为灵空的主要闲聊部分

请图灵已经认证好的，不要使用我提供的api\_key，请自行修改自己的api\_key和api\_id到文件中，不会的可以去文档的介绍页找作者

#### 调用方法：

闲聊向的话均可（如你说的话不符其他技能的调用条件，那么你的话也会传到这来）


### 笑话（全自制）：



通过调用本地的笑话库，获取笑话

经过我和znx的寻找，目前已经找到了40条的笑话，日常使用基本足够（我不相信你每天都要喊40次“讲个笑话”）

#### 调用方法：

“讲个笑话”、“说个笑话吧”等语句中含“笑话”二字的词


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

### 0.5.7.200316版本的后台目前已有以下功能：

介绍：灵空机器人的基本介绍和文档跳转

日志：本地的运行日志

修改配置项教程：教你0.5.7.200316版怎么修改配置项（将在1或2版本改为直接更改配置）

打赏：对作者Epeiuss的打赏（厚颜无耻，手动滑稽）

对话：与灵空机器人的文字对话，以便出门使用（在线版的雏形）

清单：自己开发的技能“代办”的技能页（尚未开发完成）



### 手机端无左侧的菜单？

方案一：部分手机横屏就可以出现左侧菜单

方案二：记住路径（"/"为介绍页，"/ds"是打赏页,"/log"是日志页,"/study"是修改配置项教程页,"/dh"是对话页,"/list"是清单页，此路径适用于0.5.7.200316版）



# 在线版与本地版的区别

### ①

在线版：所有都无调用限制

本地版：前期因紧急，所以用的都是有限制次数的，在线版完工后本地版也会做无调用限制

### ②

在线版：支持win、安卓、ios、mac、linux等所有支持浏览器的平台，但体验到的东西比本地版少

本地版：仅支持mac、linux（目前只测试到了deepin，按常理debian也是相同道理，所以debian有可能也能用）平台，但是体验到的东西是最多的，作者的维护力度和更新力度也比在线版大

### 在线版目前已有内测版，有兴趣的可以联系作者


## 在线版功能

基本与灵空机器人本地版的后台相同，只不过做了一些适配和加了一些在线版必须的一些功能