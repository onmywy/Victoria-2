# -*- coding: utf-8 -*-
#codedby 逸之鹤 维多利亚2吧
import os
file_path = []
main_path = os.getcwd()

tobemerged = []
tobemerged.append("maghrebi")
tobemerged.append("mashriqi")
tobemerged.append("bedouin")
merged="arabian"
mergedCN="阿拉伯人"

print("当前路径:"+main_path)

def getname():
    while True:
        tempname=input("请输入待合并的民族代码，如beifaren。输入完毕请按回车")
        if not(tempname==""):
            tobemerged.append(tempname)
        else:
            break
    merged=input("请输入合并后的民族代码，如hanren。")
    mergedCN=input("请输入合并后的民族名称，如汉人")

def Traversal(tempdir):
    for root, __, files in os.walk(tempdir):  
        for fileitem in files:
            file_path.append(os.path.join(root,fileitem))
#遍历上述几个文件夹下的文件 codedby 逸之鹤 维多利亚2吧

def replace_keyword(file,old_str,new_str):
    file_data = ""
    with open(file, encoding="utf-8", errors="surrogateescape") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,'w',encoding="utf-8", errors="surrogateescape") as f:
        f.write(file_data)


def Localisationcn(tempdir):
    tempdir = os.path.join(tempdir,"MergingNations.csv")
    tempname = merged+';'+ mergedCN+";;;;;;;;;;X\n"
    with open(tempdir,'a+') as f:
        f.write(tempname)
#追加一行汉化文本 codedby 逸之鹤 维多利亚2吧

if __name__ == "__main__":
    
    dir_pops = os.path.join(main_path,"history\\pops")
    dir_countries = os.path.join(main_path,"history\\countries")
    dir_events = os.path.join(main_path,"events")
    dir_decisions = os.path.join(main_path,"decisions")
    dir_localisation = os.path.join(main_path,"localisation")
    #可能遍历的次级文件夹，参考了贴吧大神远古贴 codedby 逸之鹤 维多利亚2吧

    for tempdir in dir_pops,dir_countries,dir_events,dir_decisions:
        Traversal(tempdir)
    #遍历 codedby 逸之鹤 维多利亚2吧
    for item in file_path:
        print("正在替换...====",item)
        for former in tobemerged:
            replace_keyword(item,"culture = "+former,"culture = "+merged)
    #替换 codedby 逸之鹤 维多利亚2吧

    replace_keyword(os.path.join(main_path,"common\\cultures.txt"),tobemerged[0],merged)
    #修改cultures.txt codedby 逸之鹤 维多利亚2吧

    Localisationcn(dir_localisation)
    #生成汉化文件 codedby 逸之鹤 维多利亚2吧

    for i in tobemerged:print(i+',',end='')
    print("已全部替换为"+merged+mergedCN+"，请进入游戏检查")
    os.system("pause")