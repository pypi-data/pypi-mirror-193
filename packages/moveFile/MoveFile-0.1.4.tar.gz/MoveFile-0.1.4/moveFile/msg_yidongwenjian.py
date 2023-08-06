'''

移动文件到层级文件夹的功能实现

'''
# coding=utf-8
import os
# path1 = os.getcwd()
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'E:\000工作\NewPDfSplit\pyhton3864\Lib\site-packages\PyQt5\Qt5\plugins'
import settings
print(settings.__file__)
print(os.path.join(settings.__file__.replace('settings.py', "database"), "url.db"))
from PyQt5.QtWidgets import *
import sys, os
import traceback
import requests
import json
import sqlite3
import random
from clazz import demo
import os,shutil,re, time
try:
    from find_file_return_path_m1 import search
    from Ui.moveFileUi import Ui_MoveFile
    from optionDb import InsertDb, getOption
except:
    from .find_file_return_path_m1 import search
    from .Ui.moveFileUi import Ui_MoveFile
    from .optionDb import InsertDb, getOption
from PyQt5 import QtWidgets
from PyQt5.QtCore import *


def get_now():
    return time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))

class MoveFile(QWidget, Ui_MoveFile,demo.TableObject):
    style = '''
        QPushButton#btn1 {
        height: 50px;
        background-color: qlineargradient(x1:1, y1:0, x2:1, y2:1, stop:0 #8a9195, stop: 1 balck);
        color: white;
        border-radius: 5px;
        font-size: 20px;
        font-weight:bold;
    }

    QPushButton#btn1:hover {
        background-color: qlineargradient(x1:1, y1:0, x2:1, y2:1, stop:0 #7d8488, stop: 1 balck);
    }

    QPushButton#btn1:pressed {
        background-color: qlineargradient(x1:1, y1:0, x2:1, y2:1, stop:0 #6a7073, stop: 1 balck);
    }

    QPushButton#btn2 {
        height: 50px;
        background-color: qlineargradient(x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #47a7ed, stop: 1 #a967b2);
        color: white;
        border-radius: 25px;
        font-size: 20px;
        font-weight:bold;

    }

    QPushButton#btn2:hover {
        background-color: qlineargradient(x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #459ee0, stop: 1 #995da1);
    }

    QPushButton#btn2:pressed {
        background-color: qlineargradient(x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #4093d1, stop: 1 #87538e);
    }
QTabWidget::pane {
    border-top: 1px solid #E5E5E5;
    background-color:#FFFFFF;
}

QTabWidget QTabBar::tab {
    border-bottom: 2px solid rgba(0,0,0,0);
    min-width: 70px; /*不要太大就可以使得border宽度和字体一样宽*/
    margin-left:25px; /*用来隔开每个tab*/
    margin-right-25px;
    padding-top: 14px;
    padding-bottom:14px;
    color:#444;
    background-color:#fafafa;
}

QTabBar::tab:hover{
    color:rgb(198, 47, 47);
}

QTabBar::tab:selected {
    color:rgb(198, 47, 47);
    background-color:#fafafa;
    border-bottom: 2px solid rgb(198, 47, 47);
    /*border-bottom: 2px solid #2080F7;*/
    /*font-weight:bold;*/
}

QTabWidget::tab-bar {
    border-top: 2px solid #E5E5E5;
    border-bottom: 2px solid #E5E5E5;
    border-left:1px solid #E5E5E5;
    alignment: center;
    font-size: 17px;
    background-color:#fafafa;
}


QScrollArea{
    border:0px;
}

#Main_widget{
    font-family:Microsoft YaHei;
    background-color:#fafafa;
}
    '''
    ProcessbarSignal = pyqtSignal(float)
    def __init__(self, communication=None):
        super(MoveFile, self).__init__(communication)
        self.setupUi(self)
        self.communication = communication
        self.token = ""
        self.user = ""
        self.run_code = 1
        self.StartBtn.clicked.connect(self.startMove)
        self.UiInit()
        self.ProcessbarSignal.connect(self.ProcessBarFun)
        # self.BarText.setVisible(False)
        self.setStyleSheet(self.style)
        self.urldb = os.path.join(settings.__file__.replace('settings.py', "database"), "url.db")
        self.FilesBtn.clicked.connect(self.setFilePath)
        self.DirsBtn.clicked.connect(self.setDirPath)
        self.FunctionName = "这是移动文件到层级文件夹"
        self.describetion = '''
=================================================
这是移动文件到层级文件夹
=================================================
'''


    def setFilePath(self ):
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self, "浏览", "./")
        if download_path:
            self.FilePathEdit.clear()
            self.FilePathEdit.setText(download_path)

    def setDirPath(self):
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self, "浏览", "./")
        if download_path:
            self.DirsPathEdit.clear()
            self.DirsPathEdit.setText(download_path)
    #进度条
    def ProcessBarFun(self, num):
        if num < 1.1:
            self.progressBar.setValue(int(num * 100))
        else:
            self.BarText.setVisible(True)
            self.progressBar.setValue(100)
            self.progressBar.setTextVisible(False)


    def StartBtnDis(self):
        self.StartBtn.setDisabled(True)
        self.StartBtn.setText("正在执行")

    def StartBtnEnb(self):
        self.StartBtn.setDisabled(False)
        self.StartBtn.setText("移动文件")

    def UiInit(self):
        ui_list = getOption("move")
        # 判断类型
        if isinstance(ui_list, list):
            if len(ui_list) == 1:
                ui_tuple = ui_list[0]
                self.FilePathEdit.setText(ui_tuple[1])
                self.DirsPathEdit.setText(ui_tuple[2])
        elif isinstance(ui_list, str):
            pass
        else:
            self.textEdit.setText(str(ui_list))

    def showmsg(self,t,msg):
        if(t == "warning"):
            # QMessageBox.warning(self,"Warining","没有需要保存的内容",QMessageBox.Ok)
            QMessageBox.warning(self,"Warining",msg,QMessageBox.Ok)
        if(t == "info"):
            QMessageBox.information(self,"info",msg,QMessageBox.Yes,QMessageBox.Yes)

    def getparam(self):
        # print("get params")
        self.文件位置 = self.FilePathEdit.text()
        self.待插入的文件夹位置 = self.DirsPathEdit.text()

    def write_DB(self):
        checkTuple = ("move", self.文件位置, self.待插入的文件夹位置)
        g = InsertDb(checkTuple)

    def get_url(self,urlName):
        conn = sqlite3.connect(self.urldb)
        cursor = conn.cursor()
        sql = "select * from urldb where url_name = '{}'".format(urlName)
        cursor.execute(sql)
        g = cursor.fetchall()
        return g

    #开始执行时传递的id，和所需要记录的文本
    def checkToken(self,id,comments):
        try:
            self.urldb = os.path.join(settings.__file__.replace('settings.py', "database"), "url.db")
            # self.urldb = os.path.join("./database", "url.db")
            if not os.path.exists(self.urldb):
                self.showmsg("warning","保存URl表不存在")
                self.run_code = 0
                return False
            headers = {
                "token": self.token
            }
            dbText = self.get_url("commit")
            if dbText:
                url = dbText[0][1]
                body = {
                    "id": id,
                    "comments": "【开始执行：】  {}".format(comments),
                    "pid": 0
                }
                response = requests.post(url=url, data=json.dumps(body), headers=headers)
                if response.status_code != 200:

                    num = 0
                    while num < 3:
                        time.sleep(random.uniform(0.5, 1))
                        response = requests.post(url=url, data=json.dumps(body), headers=headers)
                        if response.status_code == 200:
                            break

                        if num == 2:
                            # self.communication.token_singal.emit()
                            self.run_code = 0
                        num += 1
                else:
                    print("更新成功")

        except:
            traceback.print_exc()


    #隐藏所有文件tip
    def AllDisVisible(self):
        self.filePathTip.setVisible(False)
        self.DirPathTip.setVisible(False)

    #实现startMove函数，textEdit是我们放上去的文本框的id
    def startMove(self):

        self.AllDisVisible()

        self.BarText.setVisible(False)
        self.ProcessbarSignal.emit(0)
        self.checkToken(8, "移动文件夹")
        start_time = get_now()
        if not os.path.exists("./logging"):
            os.mkdir('./logging')
        copy_files_to_folders_name = './logging/底稿批量复制转移文件运行日志_' + str(start_time)
        if self.run_code:
            self.getparam()
            print(self.文件位置, self.待插入的文件夹位置)
            self.write_DB()
            if not self.文件位置:
                self.filePathTip.setText("保存PDF位置为空")
                self.filePathTip.setVisible(True)
                return False
            if not os.path.exists(self.文件位置):
                self.filePathTip.setText("保存PDF位置不存在")
                self.filePathTip.setVisible(True)
                return False
            if not self.待插入的文件夹位置:
                self.DirPathTip.setText("层级文件夹为空")
                self.DirPathTip.setVisible(True)
                return False
            if not os.path.exists(self.待插入的文件夹位置):
                self.DirPathTip.setText("层级文件夹不在存在")
                self.DirPathTip.setVisible(True)
                return False
            with open(copy_files_to_folders_name + '.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                file.write('[开始处理]' + str(get_now()) + "\n")
            self.StartBtnDis()
            self.Thread1 = RunThread(self, self.token, copy_files_to_folders_name)
            self.Thread1.文件位置 = self.文件位置
            self.Thread1.待插入的文件夹位置 = self.待插入的文件夹位置
            self.Thread1.start()
    # def ture_run(self):

class RunThread(QThread):
    def __init__(self, communication=None, token = "", loggingName = ""):
        super(RunThread, self).__init__()
        self.communication = communication
        self.token = token
        self.copy_files_to_folders_name = loggingName
        self.titlepattern = re.compile('第(\s)*([一,二,三,四,五,六,七,八,九,十]{1,3})(\s)*章')
        self.chineseNumList = ['一', '二', '三', '四', '五', '六', '七', '八', "九"]
        self.urldb  = os.path.join(settings.__file__.replace('settings.py', "database"), "url.db")


    def chineseNum(self, chineseIndex):
        # 判断中文的索引是否是以中文的十为开始
        if chineseIndex.startswith("十"):
            if chineseIndex != "十":
                wordIndex = 10 + self.chineseNumList.index(chineseIndex.replace("十", "")) + 1
            else:
                wordIndex = 10
            return wordIndex

        elif "十" in chineseIndex:
            numIndex = chineseIndex.replace("十", "")
            wordIndex = (self.chineseNumList.index(numIndex[0]) + 1) * 10 + self.chineseNumList.index(numIndex[1]) + 1
            return wordIndex

        else:
            wordIndex = self.chineseNumList.index(chineseIndex[0]) + 1
            return wordIndex

    def run(self):
        try:
            copy_files_to_folders_name = self.copy_files_to_folders_name
            root_path = self.待插入的文件夹位置 + '\\'  # 已存在的底稿文件夹目录 注：需要与auto_build_file_tree中建立的文件目录匹配
            pathRFS = self.文件位置 + '\\'  # 待移动状态且命名符合规范的PDF文件所在路径
            print(pathRFS)
            def mymovefile(srcfile, dstfile):
                if not os.path.isfile(srcfile) :
                    print(srcfile + 'not exist!')
                else:
                    fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
                    if not os.path.exists(fpath):
                        os.makedirs(fpath)  # 创建路径
                    shutil.move(srcfile, dstfile)  # 移动文件
                    # print("move %s -> %s"%( srcfile,dstfile))

            def mycopyfile(srcfile, dstfile):
                if not os.path.isfile(srcfile):
                    print(srcfile + 'not exist!')
                else:
                    fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
                    if not os.path.exists(fpath):
                        os.makedirs(fpath)  # 创建路径
                    shutil.copyfile(srcfile, dstfile)  # 复制文件
                    # print("copy %s -> %s"%( srcfile,dstfile))

            def mycopydst(srcfile, dstfile):
                if not os.path.isdir(srcfile):
                    print(srcfile + 'not exist!')
                else:
                    if os.path.isdir(dstfile):
                        print(dstfile + ' is exist!')
                    else:
                        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
                        print(fpath, fname)
                        if not os.path.exists(fpath):
                            os.makedirs(fpath)  # 创建路径
                        shutil.copytree(srcfile, dstfile)  # 复制文件
                        print(111111111111111111111111111)
                        print("copy %s -> %s" % (srcfile, dstfile))

            dict_file = {}
            ChineseDirDIct = {}
            for root, dirs, files in os.walk(root_path):
                for dir in dirs:
                    # 获取目录的名称
                    print(dir)
                    if re.match('(\d+(?:-\d+)*)', dir) is not None:
                        key = re.match('(\d+(?:-\d+)*)', dir).group(1)
                        # print('主键是'+key)
                        # 获取目录的路径
                        # goal_path=os.path.join(root,dir)
                        # dict_file.update({key: goal_path})
                        dict_file.update({key: dir})
                    if re.match(self.titlepattern, dir) is not None:
                        key = re.match(self.titlepattern, dir).group()
                        print(key)
                        ChineseDirDIct[key] = os.path.join(root, dir)

            #获取底稿目录
            pathsd = dict_file
            print(pathsd)
            f = os.listdir(pathRFS)
            print(f)
            with open(copy_files_to_folders_name + '.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                file.write('[正在处理]_参数成功读取' + str(get_now()) + "\n")
            num = 0
            for i in f:
                with open(copy_files_to_folders_name + '.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                    file.write('[正在处理]_正在读入'+str(i) + '  ' + str(get_now()) + "\n")
                print(re.match('(\d+(?:-\d+)*)', i))
                print(re.match('(\d+(?:-\d+)*)', i).group(1))
                matchText = re.match('(\d+(?:-\d+)*)', i).group(1)
                #判断是否匹配到的文本为1级
                if "-" not in matchText:
                    try:
                        NameIndex = "第{}章".format(self.chineseNumList[int(matchText)-1])
                        old_file_path = os.path.join(pathRFS, i)
                        print(old_file_path)
                        new_file_path = ChineseDirDIct[NameIndex]
                        print(new_file_path)
                        if os.path.isfile(old_file_path):
                            # mycopyfile(old_file_path, new_file_path)
                            fpath, fname = os.path.split(old_file_path)
                            print("ggggggg")
                            print(os.path.join(new_file_path, fname))
                            shutil.copyfile(old_file_path, os.path.join(new_file_path, fname))
                            with open(copy_files_to_folders_name + '.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                                file.write('[正在处理]_完成复制，从’' + old_file_path + '复制到' + new_file_path + '  ' + str(get_now()) + "\n")
                            continue
                    except:
                        pass
                if re.match('(\d+(?:-\d+)*)', i):
                    try:
                        key = re.match('(\d+(?:-\d+)*)', i).group(1)  #
                        print(key)
                        flag_remove = 0
                        while flag_remove == 0:
                            if pathsd.__contains__(key):
                                # print(pathsd[key])
                                # path_last = search(root_path, key + ' ' + pathsd[key])#文件夹名字有空格版
                                path_last = search(root_path, pathsd[key])  # 文件夹名字无空格版
                                # print('here')

                                if path_last != -1:
                                    # new_file_name=i.split('糳')[1] #w文件名分隔符为糳
                                    new_file_name = i  # 文件名分隔符为空格
                                    # print(new_file_name)
                                    old_file_path = pathRFS + i
                                    # print(old_file_path)
                                    new_file_path = path_last + '\\' + new_file_name
                                    if os.path.isfile(old_file_path):
                                        mycopyfile(old_file_path, new_file_path)
                                        with open(copy_files_to_folders_name + '.txt',"a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                                            file.write('[正在处理]_完成复制，从’' + old_file_path + '复制到'+ new_file_path+ '  '+str(get_now()) + "\n")
                                    if os.path.isdir(old_file_path):
                                        mycopydst(old_file_path, new_file_path)
                                        with open(copy_files_to_folders_name + '.txt',
                                                  "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                                            file.write('[正在处理]_完成复制，从’' + old_file_path + '复制到'+ new_file_path+ '  '+str(get_now()) + "\n")
                                    # print(new_file_path + '文件已移动')
                                    flag_remove = 1
                                    print(key + '复制成功')

                            else:
                                print(key + '无指定目录，尝试上一级目录')
                                key = re.match('((\d+(?:-\d+)*))-\d+', key).group(1)
                                # print(key)
                    except:
                        self.communication.showmsg("warning", "文件复制失败，该文件为"+str(i))
                        with open(copy_files_to_folders_name + '.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                            file.write('[正在处理]_文件复制失败，该文件为' + str(i) + '  ' + str(get_now()) + "\n")

                else:
                    if re.match(self.titlepattern, i):
                        try:
                            ChineseIndex = re.match(self.titlepattern, i).group(2)
                            ChineseTitle = re.match(self.titlepattern, i).group(0)
                            key = str(self.chineseNum(ChineseIndex))
                            print(ChineseDirDIct)
                            print(key)
                            print(pathsd)
                            if ChineseDirDIct.__contains__(ChineseTitle):
                                old_file_path = os.path.join(pathRFS,i)
                                print(old_file_path)
                                new_file_path = ChineseDirDIct[ChineseTitle]
                                print(new_file_path)
                                if os.path.isfile(old_file_path):
                                    # mycopyfile(old_file_path, new_file_path)
                                    fpath, fname = os.path.split(old_file_path)
                                    print("zzzzzzzzzzzzz")
                                    print(os.path.join(new_file_path, fname))
                                    shutil.copyfile(old_file_path, os.path.join(new_file_path, fname))
                                    with open(copy_files_to_folders_name + '.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                                        file.write('[正在处理]_完成复制，从’' + old_file_path + '复制到' + new_file_path + '  ' + str(get_now()) + "\n")
                                    continue
                            if pathsd.__contains__(key):
                                # print(pathsd[key])
                                # path_last = search(root_path, key + ' ' + pathsd[key])#文件夹名字有空格版
                                path_last = search(root_path, pathsd[key])  # 文件夹名字无空格版
                                # print('here')
                                if path_last != -1:
                                    # new_file_name=i.split('糳')[1] #w文件名分隔符为糳
                                    new_file_name = i  # 文件名分隔符为空格
                                    # print(new_file_name)
                                    old_file_path = pathRFS + i
                                    # print(old_file_path)
                                    new_file_path = path_last + '\\' + new_file_name
                                    if os.path.isfile(old_file_path):
                                        mycopyfile(old_file_path, new_file_path)
                                        with open(copy_files_to_folders_name + '.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                                            file.write('[正在处理]_完成复制，从’' + old_file_path + '复制到' + new_file_path + '  ' + str(get_now()) + "\n")
                                    if os.path.isdir(old_file_path):
                                        mycopydst(old_file_path, new_file_path)
                                        with open(copy_files_to_folders_name + '.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                                            file.write('[正在处理]_完成复制，从’' + old_file_path + '复制到' + new_file_path + '  ' + str(get_now()) + "\n")
                            else:
                                print(key + '无指定目录，尝试上一级目录')
                        except:
                            traceback.print_exc()
                            self.showmsg("warning", "文件复制失败，该文件为"+str(i))
                            with open(copy_files_to_folders_name + '.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                                file.write('[正在处理]_文件复制失败，该文件为' + str(i) + '  ' + str(get_now()) + "\n")
                    else:
                        print(i+' 没找到索引')
                        with open(copy_files_to_folders_name + '.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                            file.write('[正在处理]_匹配索引失败' + str(i) + '  ' + str(get_now()) + "\n")

                print("进度为", end="")
                num += 1
                print(num)
                print(len(f))
                print(num/len(f))
                self.communication.ProcessbarSignal.emit(num/len(f))
            self.communication.ProcessbarSignal.emit(2)
        except Exception as e:
            traceback.print_exc()
            # self.communication.showmsg("warning", "异常终止")
            self.communication.textEdit.setPlainText('程序参数错误')
            with open(copy_files_to_folders_name + '.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                file.write('[Error]' + str(get_now()) + "\n")
                file.write('[报错内容]' + str(e) + "\n")
                file.write('[报错源文件位置]' + str(e.__traceback__.tb_frame.f_globals["__file__"]) + "\n")
                file.write('[报错源码行数]' + str(e.__traceback__.tb_lineno) + "\n")

        else:
            self.communication.textEdit.setPlainText('PDF复制移动可能成功了')
            with open(copy_files_to_folders_name + '.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                file.write('[处理完成]'+ str(get_now()) + "\n")
        self.checkToken1(8, "移动文件夹")
        self.communication.StartBtnEnb()

    # 完成执行时传递的id，和所需要记录的文本
    def checkToken1(self,id,comments):
        try:

            # self.urldb = os.path.join("./database", "url.db")
            if not os.path.exists(self.urldb):
                self.showmsg("warning", "保存URl表不存在")
                self.run_code = 0
                return False
            headers = {
                "token": self.token
            }
            dbText = self.communication.get_url("commit")
            if dbText:
                url = dbText[0][1]
                body = {
                    "id": id,
                    "comments": "【执行完成：】 {}".format(comments),
                    "pid": 0
                }
                response = requests.post(url=url, data=json.dumps(body), headers=headers)

                #判断响应的状态码是否为200， 不为200会进行三次尝试
                if response.status_code != 200:
                    num = 0
                    while num < 3:
                        time.sleep(random.uniform(0.5, 1))
                        response = requests.post(url=url, data=json.dumps(body), headers=headers)
                        if response.status_code == 200:
                            break
                        if num == 2:
                            # self.communication.token_singal.emit()
                            self.run_code = 0
                        num += 1
                else:
                    print("更新成功")

        except:
            traceback.print_exc()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    myWin = MoveFile()
    myWin.show()
    sys.exit(app.exec_())
