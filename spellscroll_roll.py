# import re
import random

# ##################
# # 以下是导入和解析数据的部分
#
# file = open('spelllist.txt')
#
# lines = file.readlines()
# bard = []
# cleric = []
# druid = []
# paladin = []
# ranger = []
# sorcerer = []
# warlock = []
# wizard = []
#
# class_dict = {'吟游诗人':bard,'牧师':cleric,'德鲁伊':druid,'圣骑士':paladin,'游侠':ranger,'术士':sorcerer,'邪术师':warlock,'法师':wizard}
# # level_dict = {'0环 戏法':0,'1环':1,'2环':2,'3环':3,'4环':4,'5环':5,'6环':6,'7环':7,'8环':8,'9环':9}
# number_dict = []
# for i in range(0,10):
#     number_dict.append(str(i))
#     bard.append([i])
#     cleric.append([i])
#     druid.append([i])
#     paladin.append([i])
#     ranger.append([i])
#     sorcerer.append([i])
#     warlock.append([i])
#     wizard.append([i])
#
# listOfClass = ''
# spellLevel = 0
#
# for line in lines :
#     if line.isspace() :
#         lines.remove(line)
#
# for line in lines :
#     line = re.sub('\n', '', line)
#     if line in class_dict:
#         listOfClass = line
#     elif line in number_dict:
#         spellLevel = int(line)
#         # class_dict[listOfClass].append([spellLevel])
#     elif line == '':
#         continue
#     else:
#         class_dict[listOfClass][spellLevel].append(line)
#
# file.close()
#
# keys = list(class_dict.keys())
# string = ''
# for key in keys :
#     string += (key+':\n')
#     for level in class_dict[key] :
#         string += ''.join(str(level))
#         string += '\n'
# file = open('spelllist_m.txt',mode='w')
# file.write(string)
#
# file.flush()
# file.close()
#
# print(class_dict)

bard = [
    [0, '剑刃防护Blade Ward', '舞光术Dancing Lights', '交友术Friend', '光亮术Light', '法师之手Mage Hand', '修复术Mending', '传讯术Message', '次级幻影Minor Illusion', '魔法伎俩Prestidigitation', '克敌机先True Strike', '恶毒嘲笑Vicious Mockery'],
    [1, '化兽为友Animal Friendship', '灾祸术Bane', '魅惑人类Charm Person', '通晓语言Comprehend Languages', '疗伤术Cure Wounds', '侦测魔法Detect Magic', '易容术Disguise Self', '不谐低语Dissonant Whispers', '妖火Faerie Fire', '羽落术Feather Fall', '治愈真言Healing Word', '英雄气概Heroism', '鉴定术Identify', '迷幻手稿Illusory Script', '大步奔行Longstrider', '无声幻影Silent Image', '睡眠术Sleep', '动物交谈术Speak With Animal', '塔莎狂笑术Tasha’s Hideous Laughter', '雷鸣波Thunderwave', '隐形仆役Unseen Servant'],
    [2, '动物信使Animal Messenger', '目盲/耳聋术 Blindness/Deafness', '安定心神Calm Emotions', '匕首之云Cloud of Daggers', '疯狂冠冕Crown of Madness', '侦测思想Detect Thoughts', '强化属性Enhance Ability', '注目术Enthrall', '灼热金属Heat Metal', '人类定身术Hold Person', '隐形术Invisibility', '敲击术Knock', '次级复原术Lesser Restoration', '动植物定位术Locate Animals or Plants', '物件定位术Locate Object', '魔嘴术Magic Mouth', '魅影之力Phantasmal Force', '识破隐形See Invisibility', '粉碎音波Shatter', '沉默术Silence', '暗示术Suggestion', '诚实之域Zone of Truth'],
    [3, '降咒Bestow Curse', '鹰眼术Clairvoyance', '解除魔法Dispel Magic', '恐惧术Fear', '假死术Feign Death', '守卫刻文Glyph of Warding', '催眠图纹Hypnotic Pattern', '李欧蒙小屋Leomund’s Tiny Hut', '高等幻影Major Image', '回避侦测Nondetection', '植物滋长Plant Growth', '短讯术Sending', '死者交谈Speak With Dead', '植物交谈Speak With Plants', '臭云术Stinking Cloud', '巧言术Tongues'],
    [4, '强迫术Compulsion', '困惑术Confusion', '任意门Dimension Door', '行动自如Freedom of Movement', '高等隐形术Greater Invisibility', '幻景Hallucinatory Terrain', '生物定位术Locate Creature', '变形术Polymorph'],
    [5, '活化物件Animate Objects', '启蒙术Awaken', '支配人类Dominate Person', '托梦术Dream', '指使术Geas', '高等复原术Greater Restoration', '怪物定身术Hold Monster', '通晓传奇Legend Lore', '群体疗伤术Mass Cure Wounds', '假象术Mislead', '篡改记忆Modify Memory', '异界誓缚Planar Binding', '死者复活Raise Dead', '探知Scrying', '伪装术Seeming', '传送法阵Teleportation Circle'],
    [6, '摄心目光Eyebite', '寻路术Find the Path', '铜墙铁壁Guards and Wards', '群体暗示术Mass Suggestion', '奥图迷舞Otto’s Irresistible Dance', '预置幻影Programmed Illusion', '真知术True Seeing'],
    [7, '以太化Etherealness', '魔力监牢Forcecage', '海市蜃楼Mirage Arcana', "摩登肯豪宅术Mordenkainen's Magnificent Mansion", '摩登肯之剑Mordenkainen’s Sword', '投影术Project Image', '再生术Regenerate', '复生术Resurrection', '魔法徽记Symbol', '传送术Teleport'],
    [8, '支配怪物Dominate Monster', '弱智术Feeblemind', '花言巧语Glibness', '心灵屏障Mind Blank', '律令震慑Power Word Stun'],
    [9, '预警术Foresight', '律令医疗Power Word Heal', '律令死亡Power Word Kill', '完全变形术True Polymorph']
]
cleric = [
    [0, '神导术Guidance', '光亮术Light', '修复术Mending', '提升抗性Resistance', '圣火术Sacred Flame', '维生术Spare the Dying', '奇术Thaumaturgy']
    ,[1, '灾祸术Bane', '祝福术Bless', '命令术Command', '造水/枯水术Create or Destroy Water', '疗伤术Cure Wounds', '侦测善恶Detect Evil and Good', '侦测魔法Detect Magic', '侦测毒性和疾病Detect Poison and DIsease', '曳光弹Guiding Bolt', '治愈真言Healing Word', '致伤术Inflict Wounds', '防护善恶Protection from Evil and Good', '净化食粮Purify Food and Drink', '庇护术Sanctuary', '虔诚护盾Shield of Faith']
    ,[2, '援助术Aid', '卜筮术Augury', '目盲/耳聋术Blindness/Deafness', '安定心神Calm Emotions', '不灭明焰Continual Flame', '强化属性Enhance Ability', '寻找陷阱Find Traps', '遗体防腐Gentle Repose', '人类定身术Hold Person', '次级复原术Lesser Restoration', '物件定位术Locate Object', '治疗祷言Prayer of Healing', '防护毒素Protection from Poison', '沉默术Silence', '灵体武器Spiritual Weapon', '守护之链Warding Bond', '诚实之域Zone of Truth']
    ,[3, '操纵死尸Animate Dead', '希望信标Beacon of Hope', '降咒Bestow Curse', '鹰眼术Clairvoyance', '造粮术Create Food and Water', '昼明术Daylight', '解除魔法Dispel Magic', '假死术Feign Death', '守卫刻文Glyph of Warding', '防护法阵Magic Circle', '群体治愈真言Mass Healing Word', '融身入石Meld into Stone', '防护能量伤害Protection from Energy', '移除诅咒Remove Curse', '回生术Revivify', '短讯术Sending', '死者交谈Speak With Dead', '灵体卫士Spirit Guardians', '巧言术Tongues', '水上行走Water Walk']
    ,[4, '放逐术Banishment', '操控水体Control Water', '防死结界Death Ward', '预言术Divination', '行动自如Freedom of Movement', '信仰守卫Guardian of Faith', '生物定位术Locate Creature', '塑石术Stone Shape']
    ,[5, '通神术Commune', '疫病术Contagion', '反制善恶Dispel Evil and Good', '焰击术Flame Strike', '指使术Geas', '高等复原术Greater Restoration', '圣居Hallow', '疫病虫群Insect Plague', '通晓传奇Legend Lore', '群体疗伤术Mass Cure Wounds', '异界誓缚Planar Binding', '死者复活Raise Dead', '探知Scrying']
    ,[6, '剑刃护壁Blade Barrier', '唤起死灵Create Undead', '寻路术Find the Path', '禁制术Forbiddance', '重伤术Harm', '医疗术Heal', "英雄宴Heroes' Feast", '异界盟誓Planar Ally', '真知术True Seeing', '回返真言Word of Recall']
    ,[7, '召唤天界生物Conjure Celestial', '圣言术Divine Word', '以太化Etherealness', '火焰风暴Fire Storm', '异界传送Plane Shift', '再生术Regenerate', '复生术Resurrection', '魔法徽记Symbol']
    ,[8, '反魔法力场Antimagic Field', '操控天气Control Weather', '地震术Earthquake', '圣洁灵光Holy Aura']
    ,[9, '星界投影Astral Projection', '异界之门Gate', '群体医疗术Mass Heal', '完全复生术True Resurrection']
]
druid = [
    [0, '德鲁伊伎俩Druidcraft', '神导术Guidance', '修复术Mending', '毒液喷溅Poison Spray', '燃火术Produce Flame', '提升抗性Resistance', '橡棍术Shillelagh', '荆棘之鞭Thorn Whip']
    ,[1, '化兽为友Animal Friendship', '魅惑人类Charm Person', '造水/枯水术Create or Destroy Water', '疗伤术Cure Wounds', '侦测魔法Detect Magic', '侦测毒性和疾病Detect Poison and DIsease', '纠缠术Entangle', '妖火Faerie Fire', '云雾术Fog Cloud', '神莓术Goodberry', '治愈真言Healing Word', '跳跃术Jump', '大步奔行Longstrider', '净化食粮Purify Food and Drink', '动物交谈术Speak With Animals', '雷鸣波Thunderwave']
    ,[2, '动物信使Animal Messenger', '树肤术Barkskin', '野兽知觉Beast Sense', '黑暗视觉Darkvision', '强化属性Enhance Ability', '寻找陷阱Find Traps', '火焰刀Flame Blade', '炽焰法球Flaming Sphere', '造风术Gust of Wind', '灼热金属Heat Metal', '人类定身术Hold Person', '次级复原术Lesser Restoration', '动植物定位术Locate Animals or Plants', '物件定位术Locate Object', '月华之光Moonbeam', '行动无踪Pass without Trace', '防护毒素Protection from Poison', '荆棘丛生Spike Growth']
    ,[3, '召雷术Call Lightning', '召唤动物Conjure Animals', '昼明术Daylight', '解除魔法Dispel Magic', '假死术Feign Death', '融身入石Meld into Stone', '植物滋长Plant Growth', '防护能量伤害Protection from Energy', '雪雨暴Sleet Storm', '植物交谈术Speak With Plants', '水下呼吸Water Breathing', '水上行走Water Walk', '风墙术Wind Wall']
    ,[4, '枯萎术Blight', '困惑术Confusion', '召唤次级元素生物Conjure Minor Elementals', '召唤林地之精Conjure Woodland Beings', '操控水体Control Water', '支配野兽Dominate Beast', '行动自如Freedom of Movement', '巨虫术Giant Insect', '擒抱藤Grasping Vine', '幻景Hallucinatory Terrain', '冰风暴Ice Storm', '生物定位术Locate Creature', '变形术Polymorph', '塑石术Stone Shape', '石肤术Stoneskin', '火墙术Wall of Fire']
    ,[5, '防活物护罩Antilife Shell', '启蒙术Awaken', '问道自然Commune with Nature', '召唤元素生物Conjure Elemental', '疫病术Contagion', '指使术Geas', '高等复原术Greater Restoration', '疫病虫群Insect Plague', '群体疗伤术Mass Cure Wounds', '异界誓缚Planar Binding', '转生术Reincarnate', '探知Scrying', '树跃术Tree Stride', '石墙术Wall of Stone']
    ,[6, '召唤精类生物Conjure Fey', '寻路术Find the Path', '医疗术Heal', "英雄宴Heroes' Feast", '地动术Move Earth', '阳炎射线Sunbeam', '木遁术Transport via Plants', '棘墙术Wall of Throns', '御风而行Wind Walk']
    ,[7, '火焰风暴Fire Storm', '海市蜃楼Mirage Arcana', '异界传送Plane Shift', '再生术Regenerate', '反重力Reverse Gravity']
    ,[8, '动物形态Animal Shapes', '嫌恶/关怀术 Antipathy/Sympathy', '操控天气Control Weather', '地震术Earthquake', '弱智术Feeblemind', '阳炎爆Sunburst', '海啸术Tsunami']
    ,[9, '预警术Foresight', '形体变化Shapechange', '复仇风暴Storm of Vengeance', '完全复生术True Resurrection']
]
paladin = [
    [0]
    ,[1, '祝福术Bless', '命令术Command', '强令对决Compelled Duel', '疗伤术Cure Wounds', '侦测善恶Detect Evil and Good', '侦测魔法Detect Magic', '侦测毒性和疾病Detect Poison and Disease', '神恩Divine Favor', '英雄气概Heroism', '防护善恶Protection from Evil and Good', '净化食粮Purify Food and Drink', '炽焰斩Searing Smite', '虔诚护盾Shield of Faith', '雷鸣斩Thunderous Smite', '激愤斩Wrathful Smite']
    ,[2, '援助术Aid', '印记斩Branding Smite', '召唤坐骑Find Steed', '次级复原术Lesser Restoration', '物件定位术Locate Object', '魔化武器Magic Weapon', '防护毒素Protection from Poison', '诚实之域Zone of Truth']
    ,[3, '活力灵光Aura of Vitality', '致盲斩Blinding Smite', '造粮术Create Food and Water', '十字军披风Crusader’s Mantle', '昼明术Daylight', '解除魔法Dispel Magic', '元素武器Elemental Weapon', '防护法阵Magic Circle', '移除诅咒Remove Curse', '回生术Revivify']
    ,[4, '生命灵光Aura of Life', '净化灵光Aura of Purity', '放逐术Banishment', '防死结界Death Ward', '生物定位术Locate Creature', '惊惧斩Staggering Smite']
    ,[5, '放逐斩Banishing Smite', '原力法阵Circle of Power', '湮灭波Destructive Wave', '反制善恶Dispel Evil and Good', '指使术Geas', '死者复活Raise Dead']
    ,[6]
    ,[7]
    ,[8]
    ,[9]
]
ranger = [[0]
    ,[1, '警报术Alarm', '化兽为友Animal Friendship', '疗伤术Cure Wounds', '侦测魔法Detect Magic', '侦测毒性和疾病Detect Poison and Disease', '诱捕打击Ensnaring Strike', '云雾术Fog Cloud', '神莓术Goodberry', '棘雹术Hail of Thorns', '猎人印记Hunter’s Mark', '跳跃术Jump', '大步奔行Longstrider', '动物交谈术Speak With Animals']
    ,[2, '动物信使Animal Messenger', '树肤术Barkskin', '野兽知觉Beast Sense', '警戒之箭Cordon of Arrows', '黑暗视觉Darkvision', '寻找陷阱Find Traps', '次级复原术Lesser Restoration', '动植物定位术Locate Animals or Plants', '物件定位术Locate Object', '行动无踪Pass without Trace', '防护毒素Protection from Poison', '沉默术Silence', '荆棘丛生Spike Growth']
    ,[3, '召唤动物Conjure Animals', '召唤箭雨Conjure Barrage', '昼明术Daylight', '闪电箭Lightning Arrow', '回避侦测Nondetection', '植物滋长Plant Growth', '防护能量伤害Protection from Energy', '植物交谈术Speak With Plants', '水下呼吸Water Breathing', '水上行走Water Walk', '风墙术Wind Wall']
    ,[4, '召唤林地之精Conjure Woodland Beings', '行动自如Freedom of Movement', '擒抱藤Grasping Vine', '生物定位术Locate Creature', '石肤术Stoneskin']
    ,[5, '问道自然Commune with Nature', '万箭齐发Conjure Volley', '迅捷箭袋Swift Quiver', '树跃术Tree Stride']
    ,[6]
    ,[7]
    ,[8]
    ,[9]
]
sorcerer = [
    [0, '酸液飞溅Acid Splash', '剑刃防护Blade Ward', '冻寒之触Chill Touch', '舞光术Dancing Lights', '火焰箭Fire Bolt', '交友术Friends', '光亮术Light', '法师之手Mage Hand', '修复术Mending', '传讯术Message', '次级幻影Minor Illusion', '毒液喷溅Poison Spray', '魔法伎俩Prestidigitation', '冷冻射线Ray of Frost', '电爪Shocking Grasp', '克敌机先True Strike']
    ,[1, '燃烧之手Burning Hands', '魅惑人类Charm Person', '繁彩球Chromatic Orb', '七彩喷射Color Spray', '通晓语言Comprehend Languages', '侦测魔法Detect Magic', '易容术Disguise Self', '脚底摸油Expeditious Retreat', '虚假生命False Life', '羽落术Feather Fall', '云雾术Fog Cloud', '跳跃术Jump', '法师护甲Mage Armor', '魔法飞弹Magic Missile', '致病射线Ray of Sickness', '护盾术Shield', '无声幻影Silent Image', '睡眠术Sleep', '雷鸣波Thunderwave', '巫术箭Witch Bolt']
    ,[2, '变身术Alter Self', '目盲/耳聋术 Blindness/Deafness', '朦胧术Blur', '匕首之云Cloud of Daggers', '疯狂冠冕Crown of Madness', '黑暗术Darkness', '黑暗视觉Darkvision', '侦测思想Detect Thoughts', '强化属性Enhance Ability', '变巨/缩小术 Enlarge/Reduce', '造风术Gust of Wind', '人类定身术Hold Person', '隐形术Invisibility', '敲击术Knock', '浮空术Levitate', '镜影术Mirror Image', '迷踪步Misty Step', '魅影之力Phantasmal Force', '灼热射线Scorching Ray', '识破隐形See Invisibility', '粉碎音波Shatter', '蛛行术Spider Climb', '暗示术Suggestion', '蛛网术Web']
    ,[3, '闪现术Blink', '鹰眼术Clairvoyance', '法术反制Counterspell', '昼明术Daylight', '解除魔法Dispel Magic', '恐惧术Fear', '火球术Fireball', '飞行术Fly', '气化形体Gaseous Form', '加速术Haste', '催眠图纹Hypnotic Pattern', '闪电束Lightning Bolt', '高等幻影Major Image', '防护能量伤害Protection from Energy', '雪雨暴Sleet Storm', '缓慢术Slow', '臭云术Stinking Cloud', '巧言术Tongues', '水下呼吸Water Breathing', '水上行走Water Walk']
    ,[4, '放逐术Banishment', '枯萎术Blight', '困惑术Confusion', '任意门Dimension Door', '支配野兽Dominate Beast', '高等隐形术Greater Invisibility', '冰风暴Ice Storm', '变形术Polymorph', '石肤术Stoneskin', '火墙术Wall of Fire']
    ,[5, '活化物件Animate Objects', '死云术Cloudkill', '寒冰锥Cone of Cold', '造物术Creation', '支配人类Dominate Person', '怪物定身术Hold Monster', '疫病虫群Insect Plague', '伪装术Seeming', '心灵遥控Telekinesis', '传送法阵Teleportation Circle', '石墙术Wall of Stone']
    ,[6, '秘法门Arcane Gate', '连锁闪电Chain Lightning', '死亡法阵Circle of Death', '解离术Disintegrate', '摄心目光Eyebite', '法术无效结界Globe of Invulnerability', '群体暗示术Mass Suggestion', '地动术Move Earth', '阳炎射线Sunbeam', '真知术True Seeing']
    ,[7, '延迟爆裂火球Delayed Blast Fireball', '以太化Etherealness', '死亡一指Finger of Death', '火焰风暴Fire Storm', '异界传送Plane Shift', '虹光喷射Prismatic Spray', '反重力Reverse Gravity', '传送术Teleport']
    ,[8, '支配怪物Dominate Monster', '地震术Earthquake', '焚云术Incendiary Cloud', '律令震慑Power Word Stun   ', '阳炎爆Sunburst']
    ,[9, '异界之门Gate', '流星爆Meteor Swarm', '律令死亡Power Word Kill', '时间停止Time Stop', '祈愿术Wish']
]
warlock = [
    [0, '剑刃防护Blade Ward', '冻寒之触Chill Touch', '魔能爆Eldritch Blast', '交友术Friends', '法师之手Mage Hand', '次级幻影Minor Illusion', '毒液喷溅Poison Spray', '魔法伎俩Prestidigitation', '克敌机先True Strike']
    ,[1, '艾嘉西斯之铠Armor of Agathys', '哈达之臂Arms of Hadar', '魅惑人类Charm Person', '通晓语言Comprehend Languages', '脚底摸油Expeditious Retreat', '炼狱叱喝Hellish Rebuke', '脆弱诅咒Hex', '迷幻手稿Illusory Script', '防护善恶Protection from Evil and Good', '隐形仆役Unseen Servant', '巫术箭Witch Bolt']
    ,[2, '匕首之云Cloud of Daggers', '疯狂冠冕Crown of Madness', '黑暗术Darkness', '注目术Enthrall', '人类定身术Hold Person', '隐形术Invisibility', '镜影术Mirror Image', '迷踪步Misty Step', '衰弱射线Ray of Enfeeblement', '粉碎音波Shatter', '蛛行术Spider Climb', '暗示术Suggestion']
    ,[3, '法术反制Counterspell', '解除魔法Dispel Magic', '恐惧术Fear', '飞行术Fly', '气化形体Gaseous Form', '哈达之欲Hunger of Hadar', '催眠图纹Hypnotic Pattern', '防护法阵Magic Circle', '高等幻影Major Image', '移除诅咒Remove Curse', '巧言术Tongues', '吸血鬼之触Vampiric Touch']
    ,[4, '放逐术Banishment', '枯萎术Blight', '任意门Dimension Door', '幻景Hallucinatory Terrain']
    ,[5, '异界探知Contact Other Plane', '托梦术Dream', '怪物定身术Hold Monster', '探知Scrying']
    ,[6, '秘法门Arcane Gate', '死亡法阵Circle of Death', '召唤精类生物Conjure Fey', '唤起死灵Create Undead', '摄心目光Eyebite', '石化术Flesh to Stone', '群体暗示术Mass Suggestion', '真知术True Seeing']
    ,[7, '以太化Etherealness', '死亡一指Finger of Death', '魔力监牢Forcecage', '异界传送Plane Shift']
    ,[8, '创造半位面Demiplane', '支配怪物Dominate Monster', '弱智术Feeblemind', '花言巧语Glibness', '律令震慑Power Word Stun']
    ,[9, '星界投影Astral Projection', '预警术Foresight', '禁锢术Imprisonment', '律令死亡Power Word Kill', '完全变形术True Polymorph']
]
wizard = [
    [0, '酸液飞溅Acid Splash', '剑刃防护Blade Ward', '冻寒之触Chill Touch', '舞光术Dancing Lights', '火焰箭Fire Bolt', '交友术Friends', '光亮术Light', '法师之手Mage Hand', '修复术Mending', '传讯术Message', '次级幻影Minor Illusion', '毒液喷溅Poison Spray', '魔法伎俩Prestidigitation', '冷冻射线Ray of Frost', '电爪Shocking Grasp', '克敌机先True Strike']
    ,[1, '警报术Alarm', '燃烧之手Burning Hands', '魅惑人类Charm Person', '繁彩球Chromatic Orb', '七彩喷射Color Spray', '通晓语言Comprehend Languages', '侦测魔法Detect Magic', '易容术Disguise Self', '脚底摸油Expeditious Retreat', '虚假生命False Life', '羽落术Feather Fall', '获得魔宠Find Familiar', '云雾术Fog Cloud', '油腻术Grease', '鉴定术Identify', '迷幻手稿Illusory Script', '跳跃术Jump', '大步奔行Longstrider', '法师护甲Mage Armor', '魔法飞弹Magic Missile', '防护善恶Protection from Evil and Good', '致病射线Ray of Sickness', '护盾术Shield', '无声幻影Silent Image', '睡眠术Sleep', '塔莎狂笑术Tasha’s Hideous Laughter', '谭森浮碟术Tenser’s Floating Disk', '雷鸣波Thunderwave', '隐形仆役Unseen Servant', '巫术箭Witch Bolt']
    ,[2, '变身术Alter Self', '秘法锁Arcane Lock', '目盲/耳聋术 Blindness/Deafness', '朦胧术Blur', '匕首之云Cloud of Daggers', '不灭明焰Continual Flame', '疯狂冠冕Crown of Madness', '黑暗术Darkness', '黑暗视觉Darkvision', '侦测思想Detect Thoughts', '变巨/缩小术 Enlarge/Reduce', '炽焰法球Flaming Sphere', '遗体防腐Gentle Repose', '造风术Gust of Wind', '人类定身术Hold Person', '隐形术Invisibility', '敲击术Knock', '浮空术Levitate', '物件定位术Locate Object', '魔嘴术Magic Mouth', '魔化武器Magic Weapon', '马友夫强酸箭Melf’s Acid Arrow', '镜影术Mirror Image', '迷踪步Misty Step', '涅斯图魔法灵光Nystul’s Magic Aura', '魅影之力Phantasmal Force', '衰弱射线Ray of Enfeeblement', '魔绳术Rope Trick', '灼热射线Scorching Ray', '识破隐形See Invisibility', '粉碎音波Shatter', '蛛行术Spider Climb', '暗示术Suggestion', '蛛网术Web']
    ,[3, '操纵死尸Animate Dead', '降咒Bestow Curse', '闪现术Blink', '鹰眼术Clairvoyance', '法术反制Counterspell', '解除魔法Dispel Magic', '恐惧术Fear', '假死术Feign Death', '火球术Fireball', '飞行术Fly', '气化形体Gaseous Form', '守卫刻文Glyph of Warding', '加速术Haste', '催眠图纹Hypnotic Pattern', '李欧蒙小屋Leomund’s Tiny Hut', '闪电束Lightning Bolt', '防护法阵Magic Circle', '高等幻影Major Image', '回避侦测Nondetection', '魅影驹Phantom Steed', '防护能量伤害Protection from Energy', '移除诅咒Remove Curse', '短讯术Sending', '雪雨暴Sleet Storm', '缓慢术Slow', '臭云术Stinking Cloud', '巧言术Tongues', '吸血鬼之触Vampiric Touch', '水下呼吸Water Breathing']
    ,[4, '秘法眼Arcane Eye', '放逐术Banishment', '枯萎术Blight', '困惑术Confusion', '召唤次级元素生物Conjure Minor Elementals', '操控水体Control Water', '任意门Dimension Door', '艾伐黑触手Evard’s Black Tentacles', '鬼斧神工Fabricate', '火焰护盾Fire Shield', '高等隐形术Greater Invisibility', '幻景Hallucinatory Terrain', '冰风暴Ice Storm', '李欧蒙秘藏箱Leomund’s Secret Chest', '生物定位术Locate Creature', '摩登肯忠犬Mordenkainen’s Faithful Hound', '摩登肯私人密室Mordenkainen’s Private Sanctum', '欧提路克弹力法球Otiluke’s Resilient Sphere', '魅影杀手Phantasmal Killer', '变形术Polymorph', '塑石术Stone Shape', '石肤术Stoneskin', '火墙术Wall of Fire']
    ,[5, '活化物件Animate Objects', '毕格比之手Bigby’s Hand', '死云术Cloudkill', '寒冰锥Cone of Cold', '召唤元素生物Conjure Elemental', '异界探知Contact Other Plane', '造物术Creation', '支配人类Dominate Person', '托梦术Dream', '指使术Geas', '怪物定身术Hold Monster', '通晓传奇Legend Lore', '假象术Mislead', '篡改记忆Modify Memory', '穿墙术Passwall', '异界誓缚Planar Binding', '拉瑞心灵联结Rary’s Telepathic Bond', '探知Scrying', '伪装术Seeming', '心灵遥控Telekinesis', '传送法阵Teleportation Circle', '力场墙Wall of Force', '石墙术Wall of Stone']
    ,[6, '秘法门Arcane Gate', '连锁闪电Chain Lightning', '死亡法阵Circle of Death', '触发术Contingency', '唤起死灵Create Undead', '解离术Disintegrate', '卓姆吉瞬间召唤Drawmij’s Instant Summons', '摄心目光Eyebite', '石化术Flesh to Stone', '法术无效结界Globe of Invulnerability', '铜墙铁壁Guards and Wards', '魔魂壶Magic Jar', '群体暗示术Mass Suggestion', '地动术Move Earth', '欧提路克冰封法球Otiluke’s Freezing Sphere', '奥图迷舞Otto’s Irresistible Dance', '预置幻影Programmed Illusion', '阳炎射线Sunbeam', '真知术True Seeing', '冰墙术Wall of Ice']
    ,[7, '延迟爆裂火球Delayed Blast Fireball', '以太化Etherealness', '死亡一指Finger of Death', '魔力监牢Forcecage', '海市蜃楼Mirage Arcana', '摩登肯豪宅术Mordenkainen’s Magnificent Mansion', '摩登肯之剑Mordenkainen’s Sword', '异界传送Plane Shift', '虹光喷射Prismatic Spray', '投影术Project Image', '反重力Reverse Gravity', '隔离术Sequester', '拟像术Simulacrum', '魔法徽记Symbol', '传送术Teleport']
    ,[8, '反魔法力场Antimagic Field', '嫌恶/关怀术 Antipathy/Sympathy', '克隆术Clone', '操控天气Control Weather', '创造半位面Demiplane', '支配怪物Dominate Monster', '弱智术Feeblemind', '焚云术Incendiary Cloud', '迷宫术Maze', '心灵屏障Mind Blank', '律令震慑Power Word Stun', '阳炎爆Sunburst', '心灵感应Telepathy']
    ,[9, '星界投影Astral Projection', '预警术Foresight', '异界之门Gate', '禁锢术Imprisonment', '流星爆Meteor Swarm', '律令死亡Power Word Kill', '虹光法墙Prismatic Wall', '形体变化Shapechange', '时间停止Time Stop', '完全变形术True Polymorph', '怪影杀手Weird', '祈愿术Wish']
]
level_choices = ["0环", "1环", "2环", "3环", "4环", "5环", "6环", "7环", "8环", "9环"]
number_choices = [str(i) for i in range(1,10)]
class_choices = ['全部','吟游诗人','牧师','德鲁伊','圣骑士','游侠','术士','邪术师','法师']
# 概率：法师30% 牧师30% 德15% 诗人15% 邪术师3% 术士3% 圣骑士2% 游侠2% 仅限选择全部选项时的概率
probability = {0:wizard, 15:bard, 45:cleric, 60:druid, 62:paladin, 64:ranger, 67:sorcerer, 70:warlock, 100:wizard}

import wx
###########################################################################
## 界面架构
###########################################################################
class ScrollRoll(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'随机法术',size=(500,400))
        # 左右分块布局
        left_panel = wx.Panel(self,-1)
        left_panel.SetSize(185,340)
        left_panel.SetPosition((10,10))
        left_panel.SetBackgroundColour('light blue')
        right_panel = wx.Panel(self,-1)
        right_panel.SetSize(270,340)
        right_panel.SetPosition((205,10))
        right_panel.SetBackgroundColour('light grey')

        # 左侧操作面板
        # 标签组
        label1 = wx.StaticText(left_panel, -1, '环级：', (10, 12))
        label2 = wx.StaticText(left_panel, -1, '职业：', (10, 47))
        label3 = wx.StaticText(left_panel, -1, '数量：', (10, 82))
        # 组合框
        self.level_combox = wx.ComboBox(left_panel, -1, value=level_choices[0], choices=level_choices, pos=(50, 10), size=(125, 40))
        self.class_combox = wx.ComboBox(left_panel, -1, value=class_choices[0], choices=class_choices, pos=(50, 45), size=(125, 40))
        self.number_combox = wx.ComboBox(left_panel, -1, value=number_choices[0], choices=number_choices, pos=(50, 80), size=(125, 40))
        # 组合框设置初始选项，防止初始-1报错
        self.level_combox.SetSelection(0)
        self.class_combox.SetSelection(0)
        self.number_combox.SetSelection(0)
        # 按钮
        self.random_button = wx.Button(left_panel, -1, '随机抽取', (10, 300), (165, 30))

        # 右侧输出结果面板
        # 文本框
        self.output = wx.TextCtrl(right_panel, -1, '', (10, 10), (250, 320), style=wx.TE_MULTILINE)

        # 事件绑定
        self.Bind(wx.EVT_BUTTON, self.random, self.random_button)

    def random(self, event):
        # self.output.SetValue('clicked')
        level_choice = self.level_combox.GetCurrentSelection()
        class_choice = class_choices[self.class_combox.GetCurrentSelection()]
        number_choice = self.number_combox.GetCurrentSelection()+1
        random_list =[]
        text = ''

        # 获取职业列表
        if class_choice == "全部" :
            # 如果选择的是全部，则随机方法如下
            r = random.uniform(0,100)
            for key in probability.keys():
                if r <= key:
                    random_list = probability[key][level_choice]
                    break
        elif class_choice == '吟游诗人' :
            random_list = bard[level_choice]
        elif class_choice == '牧师':
            random_list = cleric[level_choice]
        elif class_choice == '德鲁伊':
            random_list = druid[level_choice]
        elif class_choice == '圣骑士':
            random_list = paladin[level_choice]
        elif class_choice == '游侠':
            random_list = ranger[level_choice]
        elif class_choice == '术士':
            random_list = sorcerer[level_choice]
        elif class_choice == '邪术师':
            random_list = warlock[level_choice]
        elif class_choice == '法师':
            random_list = wizard[level_choice]

        # 选择相应的环级
        # list_com = list[level_choice]

        # 随机抽取函数
        for i in range(number_choice):
            text += random.choice(random_list[1:])+'\n'

        # 设置输出框
        self.output.SetValue(text)

        # self.output.SetValue(level_choice+'\n'+class_choice+'\n'+number_choice)

if __name__ == '__main__' :
    app = wx.App()
    frame = ScrollRoll()
    frame.Show()
    app.MainLoop()

