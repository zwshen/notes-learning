# |  56 | 623 | 张江·复杂科学前沿27讲              |张江·北京师范大学系统科学教授
# |  58 | 596 | 顾衡·西方美术100讲 |顾衡·读书人
# |  59 | 352 | 薄世宁·医学通识50讲 | 薄世宁·北医三院ICU医生

# |  61 | 512 | 熊逸讲透资治通鉴    |熊逸·思想隐士   |
# |  36 | 603 | 熊逸讲透资治通鉴2（年度日更）       |熊逸·思想隐士

# | 65 | 462 | 熊逸·唐诗进阶20讲  |熊逸·思想隐士   |
# |  66 | 478 | 给忙碌者的骨科医学课 | 赵辉·骨科副主任医师
# |  67 | 519 | 吴军·阅读与写作50讲 | 吴军·计算机科学家                |
# |  68 | 391 | 怎样升级你的说服力  |李南南·得到专职老师，作家
# |  75 | 458 | 吴军·数学通识50讲  |吴军·计算机科学家
# |  78 | 449 | 给忙碌者的个人保险课 | 李璞·特许金融分析师

# |  79 | 118 | 卓克·科学思维课    |卓克·科技观察家 |

# |  80 | 433 | 贾行家说武侠        |贾行家·著名作家，得到专职作者

# |  81 | 515 | 中国产业格局·李丰猜想              |李丰·峰瑞资本创始合伙人
# |  82 | 503 | 王立铭·病毒科学9讲 |王立铭·生物学家
# |  84 | 465 | 跟张弛学市场调研    |张弛·中国市场研究行业协会副会长
# |  85 | 410 | 刘晗·法律思维30讲  |刘晗·清华大学法学院博士生导师
# | 110 | 359 | 卓克·密码学30讲    |卓克·科技观察家 |
# | 111 | 349 | 陆蓉·行为金融学    |陆蓉·上海财经大学金融学讲席教授
# | 107 | 376 | 熊太行·职场关系课  |熊太行·人际关系洞察家
# | 103 | 411 | 巨富之路：洛克菲勒  |李翔·得到总编辑 |
# | 105 | 354 | 众病之王的解决方案  |王立铭·生物学家 |
# |  97 | 451 | 跟贾伟学设计        |贾伟·中国著名设计师              |
# |  99 | 412 | 孙亚飞·化学通识30讲 | 孙亚飞·化学工程师                |
# |  83 | 502 | 科学人物课：冯·诺伊曼              |卓克·科技观察家 |

# | 100 | 442 | 科学人物课：霍金    |卓克·科技观察家 |
# | 101 | 268 | 六神磊磊读唐诗（合集）              |六神磊磊·作家
# | 102 | 368 | 吴军·科技史纲60讲  |吴军·计算机科学家                |
#  | 93 | 347 | 贾宁·财务思维课    |贾宁·清华大学经管学院会计系博士生导师
#  | 94 | 418 | 吴军·信息论40讲    |吴军·计算机科学家                |
#  |  9 | 390 | 张潇雨·个人投资课  |张潇雨·对冲基金管理人            |
#  | 26 | 415 | 科学人物课：杨振宁  |卓克·科技观察家 |
#  | 27 | 132 | 梁宁·产品思维30讲  |梁宁·著名产品人 |
#  | 28 | 296 | 怎样快速提升英语口语能力            |马徐骏·资深翻译、新知守望者
#  | 30 | 373 | 贾行家说老舍        |贾行家·著名作家，得到专职作者
#  | 31 | 574 | 脱不花·怎样成为高效学习的人        |脱不花·得到App联合创始人&CEO
#  | 41 | 138 | 王立铭·生命科学50讲 | 王立铭·生物学家 |
#  | 42 | 113 | 宁向东的管理学课    |宁向东·清华大学经管学院教授
#  | 43 | 123 | 香帅的北大金融学课  |香帅·著名金融学者                |
#  | 48 | 587 | 陈海贤·家庭关系21讲 | 陈海贤·心理学博士                |
#  | 49 | 505 | 张明楷·刑法学100讲 |张明楷·刑法学者，清华大学法学院教授
#  | 53 | 558 | 卓克·科技参考      |卓克·科技观察家 |

# DOWNLOAD_LIST = [512, 603, 462, 478, 519, 391, 458, 449, 118, 433, 558, 505, 587, 123, 113, 138, 574, 373, 296, 132, 415, 390, 418, 347, 368, 268, 442, 502, 412, 451, 354, 411, 376, 349, 359, 410, 465, 503, 515, 623, 596, 352 ]

# for id in DOWNLOAD_LIST:
#     print("dedao-dl dl {0} -t 2".format(id))

# URL = "https://fapello.com/content/y/u/yui-xin/1000/yui-xin_0{0:03d}.jpg"
# URL = "https://fapachi.com/models/z/e/zenny/1/full/zenny_0{0:03d}.jpeg"
URL = "https://fapello.com/content/s/p/sprite-fang-qi-yuan/1000/sprite-fang-qi-yuan_00{0:02d}.jpg" # 88
for i in range(1, 89):
    target = URL.format(i)
    print( "wget {0}".format( target ))


# wget -U "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0" -nd -r --level=1  -e robots=off -A jpg,jpeg -H