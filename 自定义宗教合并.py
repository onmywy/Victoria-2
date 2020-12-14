# -*- coding: utf-8 -*-
#codedby 逸之鹤 维多利亚2吧
#不建议使用
import os
file_path = []
main_path = os.getcwd()

tobemerged = []
global merged
global mergedCN

print("当前路径:"+main_path)

def getname():
    global merged
    global mergedCN
    print("输入一个待合并宗教代码后，按下回车继续输入下一个。全部输完请直接按回车")
    while True:
        tempname=input("请输入待合并的宗教代码：")
        if tempname == "":
            break
        tobemerged.append(tempname)
        #判空,若输入为空，跳出循环，否则继续输入 codedby 逸之鹤 维多利亚2吧
    merged = input("请输入合并后的宗教代码：")
    mergedCN = input("请输入合并后的宗教名称：")

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
    tempdir = os.path.join(tempdir,"MergingReligions.csv")
    tempname = merged+';'+ mergedCN+";;;;;;;;;;X\n"
    with open(tempdir,'a+') as f:
        f.write(tempname)
#追加一行汉化文本 codedby 逸之鹤 维多利亚2吧

if __name__ == "__main__":
    getname()

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
            replace_keyword(item,"religion = "+former,"religion = "+merged)
    #替换 codedby 逸之鹤 维多利亚2吧

    replace_keyword(os.path.join(main_path,"common\\religion.txt"),tobemerged[0],merged)
    #修改religion.txt codedby 逸之鹤 维多利亚2吧

    Localisationcn(dir_localisation)
    #生成汉化文件 codedby 逸之鹤 维多利亚2吧

    for i in tobemerged:print(i+',',end='')
    print("已全部替换为"+merged+mergedCN+"，请进入游戏检查")
    os.system("pause")