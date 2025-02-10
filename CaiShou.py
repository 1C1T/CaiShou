# -*- coding: utf-8 -*-
#    作者  :  Limit
#    企鹅  :  599772335
#    群聊  :  928286446
#    日期  :  2025.2.10
# ---------------------

import time
import tkinter.messagebox
import tkinter as tk
import threading
import ctypes
import sys
import os
import configparser
from random import randint


hotkey_cfg = configparser.ConfigParser()
hotkey_cfg.read('./配置文件/hotkey.ini', encoding='utf-8')
config = {
          'MOUSE_X' : 0,                      # 全局 记录鼠标x轴坐标
          'MOUSE_Y' : 0,                      # 全局 记录鼠标y轴坐标
          'SIGN_1' : 1,                       # 全局 主界面 显示或隐藏信号
          'SIGN_2' : 0,                       # 全局 配置文件切换 信号
          'SIGN_3' : 1,                       # 全局 状态栏背景 显示或隐藏信号
          'SIGN_4' : 1,                       # 全局 状态栏前景 显/隐信号 使晚于状态栏背景显示 达到覆盖效果
          'SIGN_6' : 0,                       # 全局 宏开关 信号
          'SIGN_7' : 0,                       # 修改状态栏 模式名字
          'SIGN_8' : 0,                       # 修改状态栏 配置名字
          'SIGN_16' : 0,                      # 全局 计时器 信号
          'SIGN_26' : 0,                      # 全局 自定义按键 更换信号
          'DESKTOP_RESOLUTION' : [1920, 1080],# 桌面分辨率
          'ERROR_LOG' : '',                   # 错误日志记录
          'HOOK_SWITCH': 1,                   # 鼠标和键盘监听 开启：1 关闭：0
          'WM_LBUTTON_STATE' : 0,             # 鼠标左键状态 弹起：0  按下：1
          'WM_RBUTTON_STATE' : 0,             # 鼠标右键状态
          'WM_MBUTTON_STATE' : 0,             # 鼠标中键状态
          'WM_SBUTTON_STATE' : 0,             # 鼠标侧键状态
          'WM_LBUTTON_CLICK' : 0,             # 鼠标左键单击 按下：0 弹起：1
          'WM_RBUTTON_CLICK' : 0,             # 鼠标右键单击 按下：0 弹起：1
          'UI_BG' : '#373737',                # UI界面背景颜色
          'UI_BG_2' : '#5e5e5e',              # UI界面背景颜色二
          'UI_FG' : '#bfbfbf',                # UI界面前景颜色
          'BTN_MENU_ENTER_BG' : '#7a119e',    # 菜单按钮背景颜色
          'BTN_MENU_ACTIVE_BG' : '#530b6b',   # 菜单按钮活动时背景颜色
          'BTN_MENU_ACTIVE_FG' : 'white',     # 菜单按钮活动时前景颜色
          'BTN_MENU_CHOOSE_BG' : '#a418d2',   # 菜单按钮选定时背景颜色
          'BTN_MENU_CHOOSE_FG' : 'white',     # 菜单按钮选定时前景颜色
          'BTN_FUNC_FG' : '#ffdb00',          # 功能按钮前景颜色
          'BTN_FUNC_ENTER_BG' : '#727272',    # 功能按钮进入时背景颜色
          'BTN_FUNC_ACTIVE_BG' : '#ccb000',   # 功能按钮活动时背景颜色
          'BTN_FUNC_ACTIVE_FG' : 'black',     # 功能按钮活动时前景颜色
          'BTN_FUNC_CHOOSE_BG' : '#ffdb00',   # 功能按钮选定时背景颜色
          'BTN_FUNC_CHOOSE_FG' : 'black',     # 功能按钮选定时前景颜色
          'ENTRY_BG' : '#1dba8d',             # 输入框背景颜色
          'ENTRY_FG' : 'black',               # 输入框前景颜色
          'ENTRY_FOCUSIN_BG' : '#a881db',     # 输入框获得焦点时背景颜色
          'ENTRY_DISABLED_BG' : '#4c4c4c',    # 输入框禁用时背景颜色
          'ENTRY_DISABLED_FG' : 'black',      # 输入框禁用时前景颜色
          'SCALE_BG' : '#ffdb00',             # 刻度块背景颜色
          'LABEL_CUSTOM_KEY' : 0,             # 自定义按键显示文本
          'CUSTOM_KEY' : '',                  # 自定义按键
          'STATUS_BAR_FG' : '#ff00ff',        # 状态显示颜色
          'MARCO_SWITCH' : 'OFF',             # 宏开关 开启：ON 关闭：OFF
          'CONFIGURATION_NAME' : '配置一',     # 当前配置名
          'MARCO_MODE' : 1,                   # 配置指定的宏运行模式
          'ANOTHER_NAME' : '默认配置',         # 配置别名
          'MACRO_DURATION' : 5000,            # 配置文件中的宏时长
          'MACRO_SECTION' : 10,               # 配置文件中的宏段数
          'MACRO_SECTION_ONE_TIME' : 0,       # 用于模式二 配置文件宏平均每段的时间 单位：秒
          'MACRO_SECTION_ONE_TIME_FLAOT' : 0, # 用于模式三 配置文件宏平均每段的时间 单位：毫秒
          'MACRO_STEP_LIST' : [[],[]],        # 整数拆分前 配置文件中的宏数据
          'MACRO_COUNT' : 0,                  # 模式一、二时 的宏计数器一
          'MACRO_CONVERT' : [[],[]],          # 整数拆分后的宏数据
          'UI_DISPLAY' : 'SHOW',              # 主界面 隐藏：HIDE 显示：SHOW
          'STATUS_DISPLAY' : 'SHOW',          # 顶部状态栏 隐藏：HIDE 显示：SHOW
          'LBUTTON_PRESS_TIME' : 0,           # 左键按下时间
          'HOTKEY_MACRO_SWITCH' : 20,         # 彩手高级设置 热键:宏开/关 默认:大写键
          'HOTKEY_UI_DISPLAY' : 36,           # 彩手高级设置 热键:主界面显/隐 默认:Home键
          'HOTKEY_STATUS_DISPLAY' : 35,       # 彩手高级设置 热键:状态栏显/隐 默认:End键
          'HOTKEY_CLICKER' : 86,              # 彩手高级设置 热键:连点器触发键 默认:V键
          'MOUSE_ACCELERATION' : '关',        # 彩手功能设置 鼠标加速度开关
          'MOUSE_SPEED' : 10,                 # 彩手功能设置 鼠标灵敏度 鼠标速度 1 - 20 之间 默认10
          'CLICKER_SWITCH' : '关',            # 彩手高级设置 连点器开关 开启：1 关闭：0
          'CLICKER_INTERVAL' : 0.1,           # 连点器间隔 单位：秒
          'CLICKER_BREAK_LIMIT' : '关',       # 连点器 极限点击 开启：1 关闭：0
          'CLICKER_SIGN' : '关',              # 连点器启动信号 启动：1 暂停：0
          'SOUND_EFFECT_SWITCH' : '开',       # 彩手高级设置 音效开关 开启：1 关闭：0
          'STYLE_CHANGE' : '明',              # 彩手高级设置 风格切换按钮
          'SELF_START' : '关',                # 彩手高级设置 开机自启开关 开启：1 关闭：0
          'L_R_P_T' : '关',                   # 彩手高级设置 左右键触发宏 开启：1 关闭：0
          'HOTKEY_CONFIGURE_1' : 112,         # 热键 配置一 默认: F1
          'HOTKEY_CONFIGURE_2' : 113,         # 热键 配置二 默认: F2
          'HOTKEY_CONFIGURE_3' : 114,         # 热键 配置三 默认: F3
          'HOTKEY_CONFIGURE_4' : 115,         # 热键 配置四 默认: F4
          'HOTKEY_CONFIGURE_5' : 116,         # 热键 配置五 默认: F5
          'HOTKEY_CONFIGURE_6' : 117,         # 热键 配置六 默认: F6
          'HOTKEY_CONFIGURE_7' : 118,         # 热键 配置七 默认: F7
          'HOTKEY_CONFIGURE_8' : 119,         # 热键 配置八 默认: F8
          'HOTKEY_CONFIGURE_9' : 120,         # 热键 配置九 默认: F9
          'HOTKEY_CONFIGURE_10' : 121,        # 热键 配置十一 默认: F10
          'HOTKEY_CONFIGURE_11' : 122,        # 热键 配置十一 默认: F11
          'HOTKEY_CONFIGURE_12' : 123,        # 热键 配置十二 默认: F12
          'RANDOM_BALLISTIC_1' : 0,           # 随机弹道功能 间隔时间A
          'RANDOM_BALLISTIC_2' : 0,           # 随机弹道功能 间隔时间B
          'RANDOM_BALLISTIC_3' : 0,           # 随机弹道功能 X轴随机偏移A
          'RANDOM_BALLISTIC_4' : 0,           # 随机弹道功能 X轴随机偏移B
          'RANDOM_BALLISTIC_5' : 0,           # 随机弹道功能 Y轴随机偏移A
          'RANDOM_BALLISTIC_6' : 0,           # 随机弹道功能 Y轴随机偏移B
          'LGS_GHUB_STATE' : 0,               # 对接罗技驱动 成功1  失败-1
          'SELECT_DRIVE' : 0,                 # 驱动选择 SendInput 0  罗技驱动 1
                }

ctypes.windll.kernel32.SetDllDirectoryW(None)# 重置dll搜索路径，从当前目录加载dll
ctypes.windll.LoadLibrary('winmm').timeBeginPeriod(1)# 链接winmm动态库 设置sleep精度为1毫秒
sleep_100us = ctypes.windll.LoadLibrary('./DLLs/Sleep100us_32.dll')# 休眠100微妙 32位dll动态库
# 对接罗技-  罗技蓝驱-LGS_9.02.65_x64_Logitech   罗技黑驱-lghub_installer_2021.3.5164
LGS_GHUB = ctypes.windll.LoadLibrary('./DLLs/LGS_GHUB_32.dll') # 32位dll动态库
config['LGS_GHUB_STATE'] = LGS_GHUB.mouse_open()


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]


class Input_I(ctypes.Union):
    _fields_ = [("mi", MouseInput),]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]


class SendInputApi:#键盘鼠标模拟API
    def __init__(self):
        self.SendInput = ctypes.windll.user32.SendInput

    def position(self):#获取鼠标准确坐标
        cursor = POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
        return cursor.x, cursor.y

    def mouseDown(self):#按下 鼠标左键
        ii_ = Input_I()
        ii_.mi = MouseInput(0, 0, 0, 0x0002, 0, ctypes.pointer(ctypes.c_ulong(0)))
        command = Input(ctypes.c_ulong(0), ii_)
        self.SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))

    def mouseUp(self):#弹起 鼠标左键
        ii_ = Input_I()
        ii_.mi = MouseInput(0, 0, 0, 0x0004, 0, ctypes.pointer(ctypes.c_ulong(0)))
        command = Input(ctypes.c_ulong(0), ii_)
        self.SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))

    def moveRel(self, x, y):#鼠标相对移动 相对当前鼠标位置
        ii_ = Input_I()
        ii_.mi = MouseInput(x, y, 0, 0x0001, 0, ctypes.pointer(ctypes.c_ulong(0)))
        command = Input(ctypes.c_ulong(0), ii_)
        self.SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))


def call_func(func_name, *args):
    def ui_display():         # 主界面显示或隐藏
        try:
            if config['UI_DISPLAY'] == 'SHOW':
                config['UI_DISPLAY'] = 'HIDE'
            else:
                config['UI_DISPLAY'] = 'SHOW'
            config['SIGN_1'] = 1
        except Exception as e:
            if '0x010103：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x010103：' + str(e) + '\n'
            print('0x010103:ERROR!',e)


    def macro_switch():       # 宏开关
        try:
            if config['MARCO_SWITCH'] == 'OFF':
                config['MARCO_SWITCH'] = 'ON'
                config['STATUS_BAR_FG'] = '#eff3ef'
            else:
                config['MARCO_SWITCH'] = 'OFF'
                config['STATUS_BAR_FG'] = '#ff00ff'
            config['SIGN_6'] = 1
        except Exception as e:
            if '0x010104：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x010104：' + str(e) + '\n'
            print('0x010104:ERROR!',e)


    def status_display():     # 状态栏显示或隐藏
        try:
            if config['STATUS_DISPLAY'] == 'SHOW':
                config['STATUS_DISPLAY'] = 'HIDE'
            else:
                config['STATUS_DISPLAY'] = 'SHOW'
            config['SIGN_3'] = 1
            config['SIGN_4'] = 1
        except Exception as e:
            if '0x010105：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x010105：' + str(e) + '\n'
            print('0x010105:ERROR!',e)


    def macro_off():          # 关闭宏
        try:
            config['MARCO_SWITCH'] = 'OFF'
            config['STATUS_BAR_FG'] = '#ff00ff'
            config['SIGN_6'] = 1
        except Exception as e:
            if '0x010106：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x010106：' + str(e) + '\n'
            print('0x010106:ERROR!',e)


    def macro_on():           # 开启宏
        try:
            config['MARCO_SWITCH'] = 'ON'
            config['STATUS_BAR_FG'] = '#eff3ef'
            config['SIGN_6'] = 1
        except Exception as e:
            if '0x010107：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x010107：' + str(e) + '\n'
            print('0x010107:ERROR!',e)


    def continuous_clicker(key_action):     # 连点器
        try:
            if key_action == 'press':
                if config['CLICKER_SIGN'] != '开':
                    config['CLICKER_SIGN'] = '开'
            elif key_action == 'up':
                if config['CLICKER_SIGN'] != '关':
                    config['CLICKER_SIGN'] = '关'
        except Exception as e:
            if '0x010124：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x010124：' + str(e) + '\n'
            print('0x010124:ERROR!',e)


    func_dict = {
                'ui_display':ui_display,
                'macro_switch':macro_switch,
                'status_display':status_display,
                'macro_off':macro_off,
                'macro_on':macro_on,
                'continuous_clicker':continuous_clicker,
                    }
    
    func_dict.get(func_name)(*args)


def CaiShouM1():#UI界面
    ###    变量赋值    ###
    b1_time = 0                                                 # 记录点击可以移动窗口顶部时的时间
    entry_name = [[],[]]                                        # 用于强度输入框的组件名称
    btn_name = [[],[],[],[]]                                    # 用于强度输入框旁边上下左右按钮名称
    label_name = []                                             # 用于‘第...段’标签名称
    Button_1_x = 0                                              # 在窗体顶部小部件按下左键时的event.x值
    Button_1_y = 0                                              # 在窗体顶部小部件按下左键时的event.y值
    box_num = 10                                                # 预设强度输入框的值
    scroll_height = 0                                           # 预设滚动条的高度
    recover_sign = 0                                            # 重置信号
    hotkey_macro_switch = 20                                    # 彩手高级设置 热键:宏开/关 默认:大写键
    hotkey_ui_display = 36                                      # 彩手高级设置 热键:主界面显/隐 默认:Home键
    hotkey_status_display = 35                                  # 彩手高级设置 热键:状态栏显/隐 默认:End键
    hotkey_clicker = 86                                         # 彩手高级设置 热键:连点器触发键 默认:V键
    clicker_switch = '关'                                       # 彩手高级设置 连点器开/关 开启：1 关闭：0
    mouse_acceleration = '关'                                   # 彩手功能设置 鼠标加速度开关
    mouse_speed = 10                                            # 彩手功能设置 鼠标速度 1 - 20 之间 默认10
    random_ballistic_1 = 0                                      # 随机弹道功能 间隔时间A
    random_ballistic_2 = 0                                      # 随机弹道功能 间隔时间B
    random_ballistic_3 = 0                                      # 随机弹道功能 X轴随机偏移A
    random_ballistic_4 = 0                                      # 随机弹道功能 X轴随机偏移B
    random_ballistic_5 = 0                                      # 随机弹道功能 Y轴随机偏移A
    random_ballistic_6 = 0                                      # 随机弹道功能 Y轴随机偏移B
    clicker_interval = 100                                      # 彩手高级设置 连点器间隔 单位：毫秒
    clicker_break_limit = '关'                                  # 彩手高级设置 连点器极限点击 开启：1 关闭：0
    sound_effect_switch = '开'                                  # 彩手高级设置 音效开关 开启：1 关闭：0
    style_change = '明'                                         # 彩手高级设置 风格切换按钮
    self_start = '关'                                           # 彩手高级设置 开机自启开关 开启：1 关闭：0
    left_right_press_trigger = '关'                             # 彩手高级设置 左右键触发宏 开启：1 关闭：0
    hotkey_Configure_1 = 112,                                   # 热键 配置一 默认: F1
    hotkey_Configure_2 = 113,                                   # 热键 配置二 默认: F2
    hotkey_Configure_3 = 114,                                   # 热键 配置三 默认: F3
    hotkey_Configure_4 = 115,                                   # 热键 配置四 默认: F4
    hotkey_Configure_5 = 116,                                   # 热键 配置五 默认: F5
    hotkey_Configure_6 = 117,                                   # 热键 配置六 默认: F6
    hotkey_Configure_7 = 118,                                   # 热键 配置七 默认: F7
    hotkey_Configure_8 = 119,                                   # 热键 配置八 默认: F8
    hotkey_Configure_9 = 120,                                   # 热键 配置九 默认: F9
    hotkey_Configure_10 = 121,                                  # 热键 配置十一 默认: F10
    hotkey_Configure_11 = 122,                                  # 热键 配置十一 默认: F11
    hotkey_Configure_12 = 123,                                  # 热键 配置十二 默认: F12
    configuration_all = []                                      # 保存配置数据
    configuration_another_name = '默认配置'                      # 配置别名
    configuration_mode = 1                                      # 宏运行模式
    configuration_duration = 5000                               # 时间值
    configuration_section = 10                                  # 段数值
    configuration_strong = [[],[]]                              # 强度值
    strong_convert = [[],[]]                                    # 转换强度值用于宏执行


    ###    函数定义    ###
    def get_hotkey():                                     # 获取、设置快捷键数据
        try:
            nonlocal hotkey_macro_switch, hotkey_ui_display, hotkey_status_display\
            , clicker_switch, clicker_interval, hotkey_clicker, clicker_break_limit\
            , sound_effect_switch, style_change, self_start, left_right_press_trigger\
            , hotkey_Configure_1, hotkey_Configure_2, hotkey_Configure_3\
            , hotkey_Configure_4, hotkey_Configure_5, hotkey_Configure_6\
            , hotkey_Configure_7, hotkey_Configure_8, hotkey_Configure_9\
            , hotkey_Configure_10, hotkey_Configure_11, hotkey_Configure_12\
            , mouse_acceleration, mouse_speed, random_ballistic_1, random_ballistic_2\
            , random_ballistic_3, random_ballistic_4, random_ballistic_5\
            , random_ballistic_6
            
            hotkey_macro_switch = int(hotkey_cfg.get('设置','宏开/关热键'))
            hotkey_ui_display = int(hotkey_cfg.get('设置','主界面显/隐热键'))
            hotkey_status_display = int(hotkey_cfg.get('设置','指示栏显/隐热键'))
            sound_effect_switch = str(hotkey_cfg.get('设置','音效提示开/关'))
            style_change = str(hotkey_cfg.get('设置','风格切换'))
            self_start = str(hotkey_cfg.get('设置','开机自启'))
            
            try:
                mouse_acceleration = str(hotkey_cfg.get('设置','鼠标加速度'))
            except:
                hotkey_cfg.set('设置','鼠标加速度','关')
                mouse_acceleration = '关'
            try:
                mouse_speed = int(hotkey_cfg.get('设置','鼠标灵敏度'))
            except:
                hotkey_cfg.set('设置','鼠标灵敏度','10')
                mouse_speed = 10
            try:
                random_ballistic_1 = int(hotkey_cfg.get('设置','随机弹道间隔时间A'))
                if random_ballistic_1 < 0:
                    hotkey_cfg.set('设置','随机弹道间隔时间A','0')
                    random_ballistic_1 = 0
            except:
                hotkey_cfg.set('设置','随机弹道间隔时间A','0')
                random_ballistic_1 = 0
            try:
                random_ballistic_2 = int(hotkey_cfg.get('设置','随机弹道间隔时间B'))
                if random_ballistic_2 < 0:
                    hotkey_cfg.set('设置','随机弹道间隔时间B','0')
                    random_ballistic_2 = 0
            except:
                hotkey_cfg.set('设置','随机弹道间隔时间B','0')
                random_ballistic_2 = 0
            try:
                random_ballistic_3 = int(hotkey_cfg.get('设置','X轴随机偏移A'))
            except:
                hotkey_cfg.set('设置','X轴随机偏移A','0')
                random_ballistic_3 = 0
            try:
                random_ballistic_4 = int(hotkey_cfg.get('设置','X轴随机偏移B'))
            except:
                hotkey_cfg.set('设置','X轴随机偏移B','0')
                random_ballistic_4 = 0
            try:
                random_ballistic_5 = int(hotkey_cfg.get('设置','Y轴随机偏移A'))
            except:
                hotkey_cfg.set('设置','Y轴随机偏移A','0')
                random_ballistic_5 = 0
            try:
                random_ballistic_6 = int(hotkey_cfg.get('设置','Y轴随机偏移B'))
            except:
                hotkey_cfg.set('设置','Y轴随机偏移B','0')
                random_ballistic_6 = 0
            
            try:
                if hotkey_cfg.get('设置','驱动') == "SendInput":
                    config["SELECT_DRIVE"] = 0
                elif hotkey_cfg.get('设置','驱动') == "罗技":
                    config["SELECT_DRIVE"] = 1
                else:
                    config["SELECT_DRIVE"] = 0
            except:
                config["SELECT_DRIVE"] = 0
                hotkey_cfg.set('设置','驱动','SendInput')
                with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                    hotkey_cfg.write(f)
            
            clicker_switch = str(hotkey_cfg.get('设置','连点器开/关'))
            clicker_interval = int(hotkey_cfg.get('设置','连点器间隔时间'))
            hotkey_clicker = int(hotkey_cfg.get('设置','连点器触发热键'))
            clicker_break_limit = str(hotkey_cfg.get('设置','极限点击开/关'))
            left_right_press_trigger = str(hotkey_cfg.get('设置','左右键触发宏'))
            hotkey_Configure_1 = int(hotkey_cfg.get('设置','配置一热键'))
            hotkey_Configure_2 = int(hotkey_cfg.get('设置','配置二热键'))
            hotkey_Configure_3 = int(hotkey_cfg.get('设置','配置三热键'))
            hotkey_Configure_4 = int(hotkey_cfg.get('设置','配置四热键'))
            hotkey_Configure_5 = int(hotkey_cfg.get('设置','配置五热键'))
            hotkey_Configure_6 = int(hotkey_cfg.get('设置','配置六热键'))
            hotkey_Configure_7 = int(hotkey_cfg.get('设置','配置七热键'))
            hotkey_Configure_8 = int(hotkey_cfg.get('设置','配置八热键'))
            hotkey_Configure_9 = int(hotkey_cfg.get('设置','配置九热键'))
            hotkey_Configure_10 = int(hotkey_cfg.get('设置','配置十热键'))
            hotkey_Configure_11 = int(hotkey_cfg.get('设置','配置十一热键'))
            hotkey_Configure_12 = int(hotkey_cfg.get('设置','配置十二热键'))
            hotkey_updata()
        except Exception as e:
            if '0x0301：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0301：' + str(e) + '\n'
            print('0x0301:ERROR!',e)


    def configuration(way, name, *args):                        # 获取、设置配置
        try:
            nonlocal configuration_all, configuration_another_name, configuration_mode, configuration_duration, configuration_section, configuration_strong, strong_convert
            if way == 'get':
                configuration_list = []
                try:
                    with open('./配置文件/{}.txt'.format(name), 'r', encoding='utf-8') as f:
                        configuration_list.extend(f.read().split('\n'))
                        configuration_another_name = str(configuration_list[1].split(':')[1])
                        configuration_mode = int(configuration_list[2].split(':')[1])
                        configuration_duration = time_num_check1(configuration_list[3].split(':')[1])
                        configuration_section = section_num_check(configuration_list[4].split(':')[1])
                        configuration_list[1] = '标题:' + str(configuration_another_name)
                        configuration_list[2] = '模式:' + str(configuration_mode)
                        configuration_list[3] = '时间:' + str(configuration_duration)
                        configuration_list[4] = '段数:' + str(configuration_section)
                        for i in range(configuration_section):
                            x = strong_num_check(configuration_list[i+5].split(':')[1].split(',')[0])
                            y = strong_num_check(configuration_list[i+5].split(':')[1].split(',')[1])
                            configuration_list[i+5] = '第'+str(i+1)+'段:' + str(x)+','+str(y)
                            configuration_strong[0].append(x)
                            configuration_strong[1].append(y)
                except Exception as e:
                    if '0x010201：' not in config['ERROR_LOG']:
                        config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x010201：' + str(e) + '\n'
                    name_path = './配置文件/{}.txt'.format(name)
                    if os.path.exists(name_path) == True:
                        time_tuple = time.localtime(time.time()) 
                        file_name_path = './配置文件/{}.txt'.format('{}_[原文件备份]_此文件内有错误_{}年{}月{}日{}时{}分{}秒'.format(name,time_tuple[0],time_tuple[1],time_tuple[2],time_tuple[3],time_tuple[4],time_tuple[5]))
                        with open(name_path, 'r', encoding='utf-8') as f_r, open(file_name_path, 'w', encoding='utf-8') as f_w:
                            f_w.write(f_r.read())
                    configuration_list=['注释:模式只有1 2 3,时间不可低于段数的10倍,段数最低为1,冒号和逗号为英文字符', \
                    '标题:{}'.format(name), '模式:1', '时间:5000', '段数:10', \
                    '第1段:0,0', '第2段:0,0', '第3段:0,0', '第4段:0,0', '第5段:0,0', \
                    '第6段:0,0', '第7段:0,0', '第8段:0,0', '第9段:0,0', '第10段:0,0']
                    configuration_strong = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
                    with open(name_path, 'w', encoding='utf-8') as f:
                        f.write(str(configuration_list).replace("', '", "\n").replace("['", "").replace("']", ""))
                finally:
                    configuration_another_name = str(configuration_list[1].split(':')[1])
                    configuration_mode = int(configuration_list[2].split(':')[1])
                    duration = time_num_check1(configuration_list[3].split(':')[1])
                    section_num = section_num_check(configuration_list[4].split(':')[1])
                    configuration_section = section_num_check(configuration_list[4].split(':')[1])
                    configuration_duration = time_num_check2(duration)
                    configuration_another_name_updata()
                    configuration_mode_updata()
                    configuration_duration_updata()
                    configuration_section_updata()
                    configuration_strong_updata()
                    strong_convert_updata()
                    return configuration_list
            elif way == 'set':
                set_values = dict(*args)
                configuration_name_path = './配置文件/{}.txt'.format(config['CONFIGURATION_NAME'])
                if '模式' in set_values:
                    configuration_all.pop(2)
                    configuration_all.insert(2,'模式:{}'.format(set_values.get('模式')))
                    with open(configuration_name_path, 'w', encoding='utf-8') as f:
                        f.write(str(configuration_all).replace("', '", "\n").replace("['", "").replace("']", ""))
                elif '时间' in set_values:
                    configuration_all.pop(3)
                    configuration_all.insert(3,'时间:{}'.format(set_values.get('时间')))
                    with open(configuration_name_path, 'w', encoding='utf-8') as f:
                        f.write(str(configuration_all).replace("', '", "\n").replace("['", "").replace("']", ""))
                elif '段数' in set_values:
                    configuration_all.pop(4)
                    configuration_all.insert(4,'段数:{}'.format(set_values.get('段数')))
                    with open(configuration_name_path, 'w', encoding='utf-8') as f:
                        f.write(str(configuration_all).replace("', '", "\n").replace("['", "").replace("']", ""))
                else:
                    row = str(set_values)[2:][:3]                                       # 分出是左右排，还是上下排
                    num = int(str(set_values)[6:].split("'")[0])                        # 第几段
                    value = int(str(set_values).split(':')[1].split('}')[0])            # 传递的数值
                    old_value = str(configuration_all[num+4]).split(':')[1].split(',')
                    new_value = ''
                    if row == 'one':
                        new_value = '第{}段:'.format(num)+str(value)+','+str(old_value[1])
                    elif row == 'two':
                        new_value = '第{}段:'.format(num)+str(old_value[0])+','+str(value)
                    configuration_all.pop(num+4)
                    configuration_all.insert(num+4, new_value)
                    with open(configuration_name_path, 'w', encoding='utf-8') as f:
                        f.write(str(configuration_all).replace("', '", "\n").replace("['", "").replace("']", ""))
        except Exception as e:
            if '0x0102：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0102：' + str(e) + '\n'
            print('0x0102:ERROR!',e)


    def kill_all_process():                                     # 关闭所有相关进程
        try:
            ui.withdraw()
            if config['LGS_GHUB_STATE']:
                LGS_GHUB.mouse_close()                          # 关闭罗技驱动端口
            f_r_content = ''
            if os.path.exists('./配置文件/ErrorLog.txt') == True:
                with open('./配置文件/ErrorLog.txt', 'r', encoding='utf-8') as f_r:
                    f_r_content = f_r.read()
            with open('./配置文件/ErrorLog.txt', 'w', encoding='utf-8') as f_w:
                f_w.write(config['ERROR_LOG'] + f_r_content)
            os.kill(os.getpid(), 9)
        except Exception as e:
            if '0x0106：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0106：' + str(e) + '\n'
            print('0x0106:ERROR!',e)


    def split_integer(m, n):                                    # 拆分整数
        try:
            assert n > 0
            quotient = int(m / n)
            remainder = m % n
            if remainder > 0:
                if m < 0:
                    quotient = int((0-m) / n)
                    remainder = (0-m) % n
                    if n > 0-m:
                        return [quotient] * (n - remainder) + [-1 - quotient] * remainder
                    else:
                        return [-quotient] * (n - remainder) + [-1 - quotient] * remainder
                else:
                    return [quotient] * (n - remainder) + [quotient + 1] * remainder
            return [quotient] * n
        except Exception as e:
            if '0x0107：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0107：' + str(e) + '\n'
            print('0x0107:ERROR!',e)


    def hotkey_updata():                                        # 更新快捷键
        try:
            config['HOTKEY_MACRO_SWITCH'] = hotkey_macro_switch
            config['HOTKEY_UI_DISPLAY'] = hotkey_ui_display
            config['HOTKEY_STATUS_DISPLAY'] = hotkey_status_display
            config['CLICKER_SWITCH'] = clicker_switch
            config['MOUSE_ACCELERATION'] = mouse_acceleration
            config['MOUSE_SPEED'] = mouse_speed
            config['CLICKER_INTERVAL'] = round(clicker_interval/1000, 3)
            config['HOTKEY_CLICKER'] = hotkey_clicker
            config['CLICKER_BREAK_LIMIT'] = clicker_break_limit
            config['SOUND_EFFECT_SWITCH'] = sound_effect_switch
            config['STYLE_CHANGE'] = style_change
            config['SELF_START'] = self_start
            config['L_R_P_T'] = left_right_press_trigger
            config['HOTKEY_CONFIGURE_1'] = hotkey_Configure_1
            config['HOTKEY_CONFIGURE_2'] = hotkey_Configure_2
            config['HOTKEY_CONFIGURE_3'] = hotkey_Configure_3
            config['HOTKEY_CONFIGURE_4'] = hotkey_Configure_4
            config['HOTKEY_CONFIGURE_5'] = hotkey_Configure_5
            config['HOTKEY_CONFIGURE_6'] = hotkey_Configure_6
            config['HOTKEY_CONFIGURE_7'] = hotkey_Configure_7
            config['HOTKEY_CONFIGURE_8'] = hotkey_Configure_8
            config['HOTKEY_CONFIGURE_9'] = hotkey_Configure_9
            config['HOTKEY_CONFIGURE_10'] = hotkey_Configure_10
            config['HOTKEY_CONFIGURE_11'] = hotkey_Configure_11
            config['HOTKEY_CONFIGURE_12'] = hotkey_Configure_12
            config['RANDOM_BALLISTIC_1'] = random_ballistic_1
            config['RANDOM_BALLISTIC_2'] = random_ballistic_2
            config['RANDOM_BALLISTIC_3'] = random_ballistic_3
            config['RANDOM_BALLISTIC_4'] = random_ballistic_4
            config['RANDOM_BALLISTIC_5'] = random_ballistic_5
            config['RANDOM_BALLISTIC_6'] = random_ballistic_6
            if style_change == '明':
                config['STYLE_CHANGE'] = '明'
                config['UI_BG'] = '#e7e6e6'                # UI界面背景颜色
                config['UI_BG_2'] = '#c1c1c1'              # UI界面背景颜色二
                config['UI_FG'] = 'black'                  # UI界面前景颜色
                config['BTN_MENU_ENTER_BG'] = '#aaa7a7'    # 菜单按钮进入时背景颜色
                config['BTN_MENU_ACTIVE_BG'] = '#3f3d3d'   # 菜单按钮活动时背景颜色
                config['BTN_MENU_ACTIVE_FG'] = 'white'     # 菜单按钮活动时前景颜色
                config['BTN_MENU_CHOOSE_BG'] = '#757171'   # 菜单按钮选定时背景颜色
                config['BTN_MENU_CHOOSE_FG'] = 'white'     # 菜单按钮选定时前景颜色
                config['BTN_FUNC_FG'] = '#131414'          # 功能按钮前景颜色
                config['BTN_FUNC_ENTER_BG'] = '#aaa7a7'    # 功能按钮进入时背景颜色
                config['BTN_FUNC_ACTIVE_BG'] = '#01018e'   # 功能按钮活动时背景颜色
                config['BTN_FUNC_ACTIVE_FG'] = 'white'     # 功能按钮活动时前景颜色
                config['BTN_FUNC_CHOOSE_BG'] = '#2357a0'   # 功能按钮选定时背景颜色
                config['BTN_FUNC_CHOOSE_FG'] = 'white'     # 功能按钮选定时前景颜色
                config['ENTRY_BG'] = '#1dba8d'             # 输入框背景颜色
                config['ENTRY_FG'] = 'black'               # 输入框前景颜色
                config['ENTRY_FOCUSIN_BG'] = '#a881db'     # 输入框获得焦点时背景颜色
                config['ENTRY_DISABLED_BG'] = '#C0C0C0'    # 输入框禁用时背景颜色
                config['ENTRY_DISABLED_FG'] = 'black'      # 输入框禁用时前景颜色
                config['SCALE_BG'] = '#2357a0'             # 刻度块背景颜色
            elif style_change == '暗':
                config['STYLE_CHANGE'] = '暗'
                config['UI_BG'] = '#373737'                # UI界面背景颜色
                config['UI_BG_2'] = '#5e5e5e'              # UI界面背景颜色二
                config['UI_FG'] = '#bfbfbf'                # UI界面前景颜色
                config['BTN_MENU_ENTER_BG'] = '#7a119e'    # 菜单按钮背景颜色
                config['BTN_MENU_ACTIVE_BG'] = '#530b6b'   # 菜单按钮活动时背景颜色
                config['BTN_MENU_ACTIVE_FG'] = 'white'     # 菜单按钮活动时前景颜色
                config['BTN_MENU_CHOOSE_BG'] = '#a418d2'   # 菜单按钮选定时背景颜色
                config['BTN_MENU_CHOOSE_FG'] = 'white'     # 菜单按钮选定时前景颜色
                config['BTN_FUNC_FG'] = '#edcf0e'          # 功能按钮前景颜色
                config['BTN_FUNC_ENTER_BG'] = '#727272'    # 功能按钮进入时背景颜色
                config['BTN_FUNC_ACTIVE_BG'] = '#ccb000'   # 功能按钮活动时背景颜色
                config['BTN_FUNC_ACTIVE_FG'] = 'black'     # 功能按钮活动时前景颜色
                config['BTN_FUNC_CHOOSE_BG'] = '#edcf0e'   # 功能按钮选定时背景颜色
                config['BTN_FUNC_CHOOSE_FG'] = 'black'     # 功能按钮选定时前景颜色
                config['ENTRY_BG'] = '#cccace'             # 输入框背景颜色
                config['ENTRY_FG'] = 'black'               # 输入框前景颜色
                config['ENTRY_FOCUSIN_BG'] = '#ca73dd'     # 输入框获得焦点时背景颜色
                config['ENTRY_DISABLED_BG'] = '#4c4c4c'    # 输入框禁用时背景颜色
                config['ENTRY_DISABLED_FG'] = 'black'      # 输入框禁用时前景颜色
                config['SCALE_BG'] = '#edcf0e'             # 刻度块背景颜色
        except Exception as e:
            if '0x0108：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0108：' + str(e) + '\n'
            print('0x0108:ERROR!',e)


    def configuration_another_name_updata():                    # 更新全局变量config的别名值
        try:
            config['ANOTHER_NAME'] = configuration_another_name
        except Exception as e:
            if '0x0109：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0109：' + str(e) + '\n'
            print('0x0109:ERROR!',e)


    def configuration_mode_updata():                            # 更新全局变量config的模式值
        try:
            config['MARCO_MODE'] = configuration_mode
        except Exception as e:
            if '0x0110：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0110：' + str(e) + '\n'
            print('0x0110:ERROR!',e)


    def configuration_duration_updata():                        # 更新全局变量config的时间值
        try:
            config['MACRO_DURATION'] = configuration_duration
            config['MACRO_COUNT'] = int(config['MACRO_DURATION']/10)# 将宏设置为10毫秒的延迟
            config['MACRO_SECTION_ONE_TIME'] = config['MACRO_DURATION']/config['MACRO_SECTION']
            config['MACRO_SECTION_ONE_TIME_FLAOT'] = round(config['MACRO_SECTION_ONE_TIME']/1000, 3)
        except Exception as e:
            if '0x0101：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0101：' + str(e) + '\n'
            print('0x0111:ERROR!',e)


    def clicker_interval_updata():                              # 更新全局变量clicker_interval的值
        try:
            config['CLICKER_INTERVAL'] = round(clicker_interval/1000, 3)
        except Exception as e:
            if '0x0111：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0111：' + str(e) + '\n'
            print('0x0111:ERROR!',e)


    def random_ballistic_updata(dispenser):                     # 更新全局变量random_ballistic的值
        try:
            if dispenser == 1:
                config['RANDOM_BALLISTIC_1'] = random_ballistic_1
            elif dispenser == 2:
                config['RANDOM_BALLISTIC_2'] = random_ballistic_2
            elif dispenser == 3:
                config['RANDOM_BALLISTIC_3'] = random_ballistic_3
            elif dispenser == 4:
                config['RANDOM_BALLISTIC_4'] = random_ballistic_4
            elif dispenser == 5:
                config['RANDOM_BALLISTIC_5'] = random_ballistic_5
            elif dispenser == 6:
                config['RANDOM_BALLISTIC_6'] = random_ballistic_6
        except Exception as e:
            if '0x011101：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x011101：' + str(e) + '\n'
            print('0x011101:ERROR!',e)


    def configuration_section_updata():                         # 更新全局变量config的段数值
        try:
            config['MACRO_SECTION'] = configuration_section
            config['MACRO_SECTION_ONE_TIME'] = config['MACRO_DURATION']/config['MACRO_SECTION']
            config['MACRO_SECTION_ONE_TIME_FLAOT'] = round(config['MACRO_SECTION_ONE_TIME']/1000, 3)
        except Exception as e:
            if '0x0112：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0112：' + str(e) + '\n'
            print('0x0112:ERROR!',e)


    def configuration_strong_updata():                          # 更新全局变量config的强度值
        try:
            config['MACRO_STEP_LIST'] = configuration_strong
        except Exception as e:
            if '0x0113：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0113：' + str(e) + '\n'
            print('0x0113:ERROR!',e)


    def strong_convert_updata():                                # 更新全局变量config的强度最终执行值
        try:
            nonlocal strong_convert
            strong_convert = [[],[]]
            macro_count = split_integer(int(config['MACRO_DURATION']/10), config['MACRO_SECTION'])# 将宏设置为10毫秒的延迟
            for i in range(2):
                for j in range(config['MACRO_SECTION']):
                    strong_convert[i].extend(split_integer(configuration_strong[i][j], macro_count[j]))
            config['MACRO_CONVERT'] = strong_convert
        except Exception as e:
            if '0x0114：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0114：' + str(e) + '\n'
            print('0x0114:ERROR!',e)


    def configuration_ui_display():                             # ui最小化按钮功能
        try:
            config['UI_DISPLAY'] = 'HIDE'
            ui.withdraw()
        except Exception as e:
            if '0x0115：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0115：' + str(e) + '\n'
            print('0x0115:ERROR!',e)


    def mouse_wheel(event):                                     # 强度设置区域的鼠标滚轮事件
        try:
            canvas_content_two.config(yscrollincrement=180)         # 滚轮开始，设置滚动条步长为100，鼠标滚轮滑动页面的速度加快100倍
            number = int(-event.delta / 120)
            canvas_content_two.yview_scroll(number, 'units')
            canvas_content_two.config(yscrollincrement=18)          # 滚轮完毕，还原滚动条步长设置为18
        except Exception as e:
            if '0x0116：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0116：' + str(e) + '\n'
            print('0x0116:ERROR!',e)


    def mouse_wheel_two(event):                                 # 设置页面的鼠标滚轮事件
        try:
            number = int(-event.delta / 120)
            canvas_advanced.yview_scroll(number, 'units')
        except Exception as e:
            if '0x011601：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x011601：' + str(e) + '\n'
            print('0x011601:ERROR!',e)


    def duration_set(receive_value):                            # 修改时间
        try:
            nonlocal entry_1
            entry_1.delete(0, 'end')
            entry_1.insert(0, receive_value)
            kw={'时间':receive_value}
            configuration('set', config['CONFIGURATION_NAME'], kw)
        except Exception as e:
            if '0x0117：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0117：' + str(e) + '\n'
            print('0x0117:ERROR!',e)


    def clicker_interval_set(receive_value):                    # 修改连点器的间隔时间
        try:
            nonlocal entry_3
            entry_3.delete(0, 'end')
            entry_3.insert(0, receive_value)
            hotkey_cfg.set('设置','连点器间隔时间', str(receive_value))
            with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                hotkey_cfg.write(f)
        except Exception as e:
            if '0x011701：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x011701：' + str(e) + '\n'
            print('0x011701:ERROR!',e)


    def random_ballistic_set(dispenser, receive_value):         # 修改随机弹道的数据
        try:
            if dispenser == 1:
                entry_4.delete(0, 'end')
                entry_4.insert(0, receive_value)
                hotkey_cfg.set('设置','随机弹道间隔时间A', str(receive_value))
            elif dispenser == 2:
                entry_5.delete(0, 'end')
                entry_5.insert(0, receive_value)
                hotkey_cfg.set('设置','随机弹道间隔时间B', str(receive_value))
            elif dispenser == 3:
                entry_6.delete(0, 'end')
                entry_6.insert(0, receive_value)
                hotkey_cfg.set('设置','X轴随机偏移A', str(receive_value))
            elif dispenser == 4:
                entry_7.delete(0, 'end')
                entry_7.insert(0, receive_value)
                hotkey_cfg.set('设置','X轴随机偏移B', str(receive_value))
            elif dispenser == 5:
                entry_8.delete(0, 'end')
                entry_8.insert(0, receive_value)
                hotkey_cfg.set('设置','Y轴随机偏移A', str(receive_value))
            elif dispenser == 6:
                entry_9.delete(0, 'end')
                entry_9.insert(0, receive_value)
                hotkey_cfg.set('设置','Y轴随机偏移B', str(receive_value))
            
            
            with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                hotkey_cfg.write(f)
        except Exception as e:
            if '0x011701：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x011701：' + str(e) + '\n'
            print('0x011701:ERROR!',e)


    def time_num_check1(time_num):                              # 检查配置内的时间设置值
        try:
            try:
                if int(time_num):
                    if int(time_num)>=0:
                        time_num = int(time_num)
                    else:
                        time_num = 5000
                else:
                    time_num = 5000
            except Exception as e:
                time_num = 5000
            return time_num
        except Exception as e:
            if '0x0118：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0118：' + str(e) + '\n'
            print('0x0118:ERROR!',e)


    def time_num_check2(receive_value):                         # 时间最低只能为段数的10倍，设置合理值
        try:
            nonlocal configuration_section
            right_value = 10*configuration_section # 将宏设置为10毫秒的延迟
            while int(receive_value) < right_value:
                receive_value += 1
            return int(receive_value)
        except Exception as e:
            if '0x0119：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0119：' + str(e) + '\n'
            print('0x0119:ERROR!',e)


    def time_num_check3(receive_value):                         # 检查段数输入值，并给时间设置合理值
        try:
            nonlocal configuration_duration
            right_value = receive_value*10# 将宏设置为10毫秒的延迟
            if right_value > configuration_duration:
                if right_value > int(right_value):
                    right_value = int(right_value+1)
                configuration_duration = int(right_value)
                configuration_duration_updata()
                duration_set(configuration_duration)
        except Exception as e:
            if '0x0120：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0120：' + str(e) + '\n'
            print('0x0120:ERROR!',e)


    def section_num_check(section_num):                         # 检查配置内的段数设置值
        try:
            try:
                section_num = int(section_num)
            except Exception as e:
                if '0x012101：' not in config['ERROR_LOG']:
                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x012101：' + str(e) + '\n'
                section_num = 10
            return section_num
        except Exception as e:
            if '0x0121：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0121：' + str(e) + '\n'
            print('0x0121:ERROR!',e)


    def strong_num_check(strong_num):                           # 检查配置内的强度设置值
        try:
            try:
                strong_num = int(strong_num)
            except Exception as e:
                if '0x012201：' not in config['ERROR_LOG']:
                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x012201：' + str(e) + '\n'
                strong_num = 0
            return strong_num
        except Exception as e:
            if '0x0122：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0122：' + str(e) + '\n'
            print('0x0122:ERROR!',e)


    def box_num_check(box_num):                                 # 检查界面的段数设置值，计算画布滚动高度
        try:
            scroll_height = 180                                   # 180是画布二的高度
            try:
                if int(box_num):
                    if int(box_num)>10:
                        scroll_height = 180 + 18*(int(box_num)-10)
                        scrollbar.place(relx=0.96, rely=0, relwidth=0.04-0.0025, relheight=1-0.005)        # 当box_num大于10，放置垂直滚动条
                    else:
                        box_num=10
                else:
                    box_num=10
            except Exception as e:
                box_num=10
            return box_num, scroll_height
        except Exception as e:
            if '0x0123：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0123：' + str(e) + '\n'
            print('0x0123:ERROR!',e)


    def btn_enter(event):                                       # 鼠标进入按钮范围触发事件
        try:
            if str(event.widget) == '.!button':
                btn1.config(bg='#508cbe', fg='black')
            elif str(event.widget) == '.!button2':
                btn2.config(bg='#950000', fg='black')
            elif str(event.widget) == '.!button3' and btn3.config('bg')[4] != config['BTN_MENU_CHOOSE_BG']:
                btn3.config(bg=config['BTN_MENU_ENTER_BG'])
            elif str(event.widget) == '.!button4' and btn4.config('bg')[4] != config['BTN_MENU_CHOOSE_BG']:
                btn4.config(bg=config['BTN_MENU_ENTER_BG'])
            elif str(event.widget) == '.!button5' and btn5.config('bg')[4] != config['BTN_MENU_CHOOSE_BG']:
                btn5.config(bg=config['BTN_MENU_ENTER_BG'])
            elif str(event.widget) == '.!button6' and btn6.config('bg')[4] != config['BTN_MENU_CHOOSE_BG']:
                btn6.config(bg=config['BTN_MENU_ENTER_BG'])
            elif str(event.widget) == '.!button7' and btn55.config('bg')[4] != config['BTN_MENU_CHOOSE_BG']:
                btn55.config(bg=config['BTN_MENU_ENTER_BG'])
            elif str(event.widget) == '.!frame.!canvas.!button' and btn13.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:# 鼠标加速度
                if btn13['state'] != 'disabled':
                    btn13.config(bg=config['BTN_FUNC_ENTER_BG'])
            elif str(event.widget) == '.!frame2.!canvas.!button4' and btn36.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:# 连点器
                if btn36['state'] != 'disabled':
                    btn36.config(bg=config['BTN_FUNC_ENTER_BG'])
            elif str(event.widget) == '.!frame2.!canvas.!button6' and btn38.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:# 音效提示
                if btn38['state'] != 'disabled':
                    btn38.config(bg=config['BTN_FUNC_ENTER_BG'])
            elif str(event.widget) == '.!frame2.!canvas.!button7' and btn39.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:# 极限点击
                if btn39['state'] != 'disabled':
                    btn39.config(bg=config['BTN_FUNC_ENTER_BG'])
            elif str(event.widget) == '.!frame2.!canvas.!button9' and btn41.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:# 开机自启
                if btn41['state'] != 'disabled':
                    btn41.config(bg=config['BTN_FUNC_ENTER_BG'])
            elif str(event.widget) == '.!frame2.!canvas.!button10' and btn42.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:# 左右键触发宏
                if btn42['state'] != 'disabled':
                    btn42.config(bg=config['BTN_FUNC_ENTER_BG'])
            elif str(event.widget) == '.!frame4.!canvas.!button' and btn56.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:
                if btn56['state'] != 'disabled':
                    btn56.config(bg=config['BTN_FUNC_ENTER_BG'])
            elif str(event.widget) == '.!frame4.!canvas.!button2' and btn57.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:
                if btn57['state'] != 'disabled':
                    btn57.config(bg=config['BTN_FUNC_ENTER_BG'])
        except Exception as e:
            if '0x0124：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0124：' + str(e) + '\n'
            print('0x0124:ERROR!',e)


    def btn_leave(event):                                       # 鼠标离开按钮范围触发事件
        try:
            if str(event.widget) == '.!button':
                btn1.config(bg='black', fg='#1bcbeb')
            elif str(event.widget) == '.!button2':
                btn2.config(bg='black', fg='#1bcbeb')
            elif str(event.widget) == '.!button3' and btn3.config('bg')[4] != config['BTN_MENU_CHOOSE_BG']:
                btn3.config(bg=config['UI_BG'])
            elif str(event.widget) == '.!button4' and btn4.config('bg')[4] != config['BTN_MENU_CHOOSE_BG']:
                btn4.config(bg=config['UI_BG'])
            elif str(event.widget) == '.!button5' and btn5.config('bg')[4] != config['BTN_MENU_CHOOSE_BG']:
                btn5.config(bg=config['UI_BG'])
            elif str(event.widget) == '.!button6' and btn6.config('bg')[4] != config['BTN_MENU_CHOOSE_BG']:
                btn6.config(bg=config['UI_BG'])
            elif str(event.widget) == '.!button7' and btn55.config('bg')[4] != config['BTN_MENU_CHOOSE_BG']:
                btn55.config(bg=config['UI_BG'])
            elif str(event.widget) == '.!frame.!canvas.!button' and btn13.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:# 鼠标加速度
                if btn13['state'] != 'disabled':
                    btn13.config(bg=config['UI_BG_2'])
            elif str(event.widget) == '.!frame2.!canvas.!button4' and btn36.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:# 连点器
                if btn36['state'] != 'disabled':
                    btn36.config(bg=config['UI_BG'])
            elif str(event.widget) == '.!frame2.!canvas.!button6' and btn38.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:# 音效提示
                if btn38['state'] != 'disabled':
                    btn38.config(bg=config['UI_BG'])
            elif str(event.widget) == '.!frame2.!canvas.!button7' and btn39.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:# 极限点击
                if btn39['state'] != 'disabled':
                    btn39.config(bg=config['UI_BG'])
            elif str(event.widget) == '.!frame2.!canvas.!button9' and btn41.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:# 开机自启
                if btn41['state'] != 'disabled':
                    btn41.config(bg=config['UI_BG'])
            elif str(event.widget) == '.!frame2.!canvas.!button10' and btn42.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:# 左右键触发宏
                if btn42['state'] != 'disabled':
                    btn42.config(bg=config['UI_BG'])
            elif str(event.widget) == '.!frame4.!canvas.!button' and btn56.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:
                if btn56['state'] != 'disabled':
                    btn56.config(bg=config['UI_BG'])
            elif str(event.widget) == '.!frame4.!canvas.!button2' and btn57.config('bg')[4] != config['BTN_FUNC_CHOOSE_BG']:
                if btn57['state'] != 'disabled':
                    btn57.config(bg=config['UI_BG'])
        except Exception as e:
            if '0x0125：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0125：' + str(e) + '\n'
            print('0x0125:ERROR!',e)


    def hotkey_set(event):                                      # 鼠标点击自定义按钮触发事件
        try:
            config['SIGN_26'] = 1
            label_dict = {
                         35 : label_35,        # 设置页面 宏开/关 显示当前热键
                         36 : label_36,        # 设置页面 主界面显/隐 显示当前热键
                         37 : label_37,        # 设置页面 状态栏显/隐 显示当前热键
                         53 : label_53,        # 设置页面 触发热键 显示当前热键
                         69 : label_69,        # 设置页面 配置一 显示当前热键
                         70 : label_70,        # 设置页面 配置二 显示当前热键
                         71 : label_71,        # 设置页面 配置三 显示当前热键
                         72 : label_72,        # 设置页面 配置四 显示当前热键
                         73 : label_73,        # 设置页面 配置五 显示当前热键
                         74 : label_74,        # 设置页面 配置六 显示当前热键
                         75 : label_75,        # 设置页面 配置七 显示当前热键
                         76 : label_76,        # 设置页面 配置八 显示当前热键
                         77 : label_77,        # 设置页面 配置九 显示当前热键
                         78 : label_78,        # 设置页面 配置十 显示当前热键
                         79 : label_79,        # 设置页面 配置十一 显示当前热键
                         80 : label_80        # 设置页面 配置十二 显示当前热键
                                      }
            if str(event.widget) == '.!frame2.!canvas.!button':
                config['LABEL_CUSTOM_KEY'] = 35
                label_35['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button2':
                config['LABEL_CUSTOM_KEY'] = 36
                label_36['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button3':
                config['LABEL_CUSTOM_KEY'] = 37
                label_37['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button5':
                config['LABEL_CUSTOM_KEY'] = 53
                label_53['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button11':
                config['LABEL_CUSTOM_KEY'] = 69
                label_69['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button12':
                config['LABEL_CUSTOM_KEY'] = 70
                label_70['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button13':
                config['LABEL_CUSTOM_KEY'] = 71
                label_71['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button14':
                config['LABEL_CUSTOM_KEY'] = 72
                label_72['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button15':
                config['LABEL_CUSTOM_KEY'] = 73
                label_73['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button16':
                config['LABEL_CUSTOM_KEY'] = 74
                label_74['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button17':
                config['LABEL_CUSTOM_KEY'] = 75
                label_75['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button18':
                config['LABEL_CUSTOM_KEY'] = 76
                label_76['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button19':
                config['LABEL_CUSTOM_KEY'] = 77
                label_77['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button20':
                config['LABEL_CUSTOM_KEY'] = 78
                label_78['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button21':
                config['LABEL_CUSTOM_KEY'] = 79
                label_79['bg'] = config['ENTRY_FOCUSIN_BG']
            elif str(event.widget) == '.!frame2.!canvas.!button22':
                config['LABEL_CUSTOM_KEY'] = 80
                label_80['bg'] = config['ENTRY_FOCUSIN_BG']
            for this_label in [35,36,37,53,69,70,71,72,73,74,75,76,77,78,79,80]:
                if this_label != config['LABEL_CUSTOM_KEY']:
                    label_dict.get(this_label)['bg'] = config['ENTRY_BG']
        except Exception as e:
            if '0x0126：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0126：' + str(e) + '\n'
            print('0x0126:ERROR!',e)


    def btn3_command():                                        # 点击‘弹道’按钮触发事件
        try:
            btn3.config(bg=config['BTN_MENU_CHOOSE_BG'], fg=config['BTN_MENU_CHOOSE_FG'])
            btn4.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn5.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn6.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn55.config(bg=config['UI_BG'], fg=config['UI_FG'])
            frame_func.place_forget()
            frame_advanced.place_forget()
            frame_about.place_forget()
            frame_drive.place_forget()
        except Exception as e:
            if '0x0127：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0127：' + str(e) + '\n'
            print('0x0127:ERROR!',e)


    def btn4_command():                                        # 点击‘功能’按钮触发事件
        try:
            btn3.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn4.config(bg=config['BTN_MENU_CHOOSE_BG'], fg=config['BTN_MENU_CHOOSE_FG'])
            btn5.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn6.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn55.config(bg=config['UI_BG'], fg=config['UI_FG'])
            frame_func.place(x=1,y=36)
            canvas_func.place(x=0,y=0, relwidth=1, relheight=1)
            btn13.place(relx=0.2, y=18*3, relwidth=0.6, relheight=0.054*2)      # 鼠标加速度开关
            label_8.place(relx=0.15, y=18*7, relwidth=0.7, relheight=0.054)     # 鼠标灵敏度说明文字
            label_9.place(relx=0.1, y=18*9, relwidth=0.1, relheight=0.054)      # 鼠标灵敏度刻度值显示
            label_93.place(relx=0.05, y=18*12, relwidth=0.2, relheight=0.054)   # 功能页面 文本 '弹道每'
            label_94.place(relx=0.45, y=18*12, relwidth=0.05, relheight=0.054)  # 功能页面 文本 '至'
            label_95.place(relx=0.7, y=18*12, relwidth=0.25, relheight=0.054)   # 功能页面 文本 '毫秒随机执行'
            label_96.place(relx=0.05, y=18*13, relwidth=0.2, relheight=0.054)   # 功能页面 文本 'X轴在'
            label_97.place(relx=0.45, y=18*13, relwidth=0.05, relheight=0.054)  # 功能页面 文本 '至'
            label_98.place(relx=0.7, y=18*13, relwidth=0.25, relheight=0.054)   # 功能页面 文本 '之间随机偏移'
            label_99.place(relx=0.05, y=18*14, relwidth=0.2, relheight=0.054)   # 功能页面 文本 'Y轴在'
            label_100.place(relx=0.45, y=18*14, relwidth=0.05, relheight=0.054) # 功能页面 文本 '至'
            label_101.place(relx=0.7, y=18*14, relwidth=0.25, relheight=0.054)  # 功能页面 文本 '之间随机偏移'
            scale_1.place(relx=0.2, y=18*9, relwidth=0.6, relheight=0.06)       # 鼠标灵敏度刻度条
            entry_4.place(relx=0.25, y=18*12, relwidth=0.2, relheight=0.054)    # 功能页面 文本框 首 随机毫秒
            entry_5.place(relx=0.5, y=18*12, relwidth=0.2, relheight=0.054)     # 功能页面 文本框 尾 随机毫秒
            entry_6.place(relx=0.25, y=18*13, relwidth=0.2, relheight=0.054)    # 功能页面 文本框 首 X轴随机偏移
            entry_7.place(relx=0.5, y=18*13, relwidth=0.2, relheight=0.054)     # 功能页面 文本框 尾 X轴随机毫秒
            entry_8.place(relx=0.25, y=18*14, relwidth=0.2, relheight=0.054)    # 功能页面 文本框 首 Y轴随机偏移
            entry_9.place(relx=0.5, y=18*14, relwidth=0.2, relheight=0.054)     # 功能页面 文本框 尾 Y轴随机毫秒
            
            frame_advanced.place_forget()
            frame_about.place_forget()
            frame_drive.place_forget()
        except Exception as e:
            if '0x0128：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0128：' + str(e) + '\n'
            print('0x0128:ERROR!',e)


    def btn5_command():                                        # 点击‘设置’按钮触发事件
        try:
            btn3.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn4.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn5.config(bg=config['BTN_MENU_CHOOSE_BG'], fg=config['BTN_MENU_CHOOSE_FG'])
            btn6.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn55.config(bg=config['UI_BG'], fg=config['UI_FG'])
            frame_advanced.place(x=1,y=36)
            canvas_advanced.place(x=0,y=0, relwidth=1, relheight=1)
            scrollbar_two.place(relx=0.96, rely=0, relwidth=0.04-0.0025, relheight=1-0.005) # 放置垂直滚动条
            
            canvas_advanced.create_window((280,18*4), window=btn26, width=79.6, height=17.442, anchor='w')# 按键自定义 '宏开/关：'
            canvas_advanced.create_window((280,18*5), window=btn27, width=79.6, height=17.442, anchor='w')# 按键自定义 '主界面显/隐：'
            canvas_advanced.create_window((280,18*6), window=btn28, width=79.6, height=17.442, anchor='w')# 按键自定义 '状态栏显/隐：'
            canvas_advanced.create_window((80,18*8), window=btn36, width=79.6, height=17.442, anchor='w')# 设置页面 连点器开关
            canvas_advanced.create_window((280,18*11), window=btn37, width=79.6, height=17.442, anchor='w')# 按键自定义 连点器'触发热键'
            canvas_advanced.create_window((80,18*2), window=btn38, width=79.6, height=17.442, anchor='w')# 设置页面 音效提示开关
            canvas_advanced.create_window((240,18*8), window=btn39, width=79.6, height=17.442, anchor='w')# 设置页面 极限点击开关
            canvas_advanced.create_window((240,18*2), window=btn40, width=79.6, height=17.442, anchor='w')# 设置页面 风格切换按钮
            canvas_advanced.create_window((80,18*13), window=btn41, width=79.6, height=17.442, anchor='w')# 设置页面 开机自启开关
            canvas_advanced.create_window((232,18*13), window=btn42, width=119.4, height=17.442, anchor='w')# 设置页面 左右键触发宏
            canvas_advanced.create_window((280,18*15), window=btn43, width=79.6, height=17.442, anchor='w')# 按键自定义 配置一
            canvas_advanced.create_window((280,18*16), window=btn44, width=79.6, height=17.442, anchor='w')# 按键自定义 配置二
            canvas_advanced.create_window((280,18*17), window=btn45, width=79.6, height=17.442, anchor='w')# 按键自定义 配置三
            canvas_advanced.create_window((280,18*18), window=btn46, width=79.6, height=17.442, anchor='w')# 按键自定义 配置四
            canvas_advanced.create_window((280,18*19), window=btn47, width=79.6, height=17.442, anchor='w')# 按键自定义 配置五
            canvas_advanced.create_window((280,18*20), window=btn48, width=79.6, height=17.442, anchor='w')# 按键自定义 配置六
            canvas_advanced.create_window((280,18*21), window=btn49, width=79.6, height=17.442, anchor='w')# 按键自定义 配置七
            canvas_advanced.create_window((280,18*22), window=btn50, width=79.6, height=17.442, anchor='w')# 按键自定义 配置八
            canvas_advanced.create_window((280,18*23), window=btn51, width=79.6, height=17.442, anchor='w')# 按键自定义 配置九
            canvas_advanced.create_window((280,18*24), window=btn52, width=79.6, height=17.442, anchor='w')# 按键自定义 配置十
            canvas_advanced.create_window((280,18*25), window=btn53, width=79.6, height=17.442, anchor='w')# 按键自定义 配置十一
            canvas_advanced.create_window((280,18*26), window=btn54, width=79.6, height=17.442, anchor='w')# 按键自定义 配置十二
            
            
            canvas_advanced.create_window((0,18*4), window=label_32, width=118, height=17.442, anchor='w')# 文本 '宏开/关：'
            canvas_advanced.create_window((0,18*5), window=label_33, width=118, height=17.442, anchor='w')# 文本 '主界面显/隐：'
            canvas_advanced.create_window((0,18*6), window=label_34, width=118, height=17.442, anchor='w')# 文本 '状态栏显/隐：'
            canvas_advanced.create_window((120,18*4), window=label_35, width=159.2, height=17.442, anchor='w')# 宏开/关 显示当前热键
            canvas_advanced.create_window((120,18*5), window=label_36, width=159.2, height=17.442, anchor='w')# 主界面显/隐 显示当前热键
            canvas_advanced.create_window((120,18*6), window=label_37, width=159.2, height=17.442, anchor='w')# 状态栏显/隐 显示当前热键
            canvas_advanced.create_window((0,18*10), window=label_50, width=118, height=17.442, anchor='w')# 文本 连点器 '间隔：'
            canvas_advanced.create_window((280,18*10), window=label_51, width=79.6, height=17.442, anchor='w')# 文本 连点器 '毫秒'
            canvas_advanced.create_window((0,18*11), window=label_52, width=118, height=17.442, anchor='w')# 文本 连点器 '触发热键'
            canvas_advanced.create_window((120,18*11), window=label_53, width=159.2, height=17.442, anchor='w')# 触发热键 显示当前热键
            canvas_advanced.create_window((120,18*10), window=entry_3, width=159.2, height=17.442, anchor='w')# 连点器 间隔 输入框
            
            
            canvas_advanced.create_window((120,18*15), window=label_69, width=159.2, height=17.442, anchor='w')# 设置页面 配置一 显示当前热键
            canvas_advanced.create_window((120,18*16), window=label_70, width=159.2, height=17.442, anchor='w')# 设置页面 配置二 显示当前热键
            canvas_advanced.create_window((120,18*17), window=label_71, width=159.2, height=17.442, anchor='w')# 设置页面 配置三 显示当前热键
            canvas_advanced.create_window((120,18*18), window=label_72, width=159.2, height=17.442, anchor='w')# 设置页面 配置四 显示当前热键
            canvas_advanced.create_window((120,18*19), window=label_73, width=159.2, height=17.442, anchor='w')# 设置页面 配置五 显示当前热键
            canvas_advanced.create_window((120,18*20), window=label_74, width=159.2, height=17.442, anchor='w')# 设置页面 配置六 显示当前热键
            canvas_advanced.create_window((120,18*21), window=label_75, width=159.2, height=17.442, anchor='w')# 设置页面 配置七 显示当前热键
            canvas_advanced.create_window((120,18*22), window=label_76, width=159.2, height=17.442, anchor='w')# 设置页面 配置八 显示当前热键
            canvas_advanced.create_window((120,18*23), window=label_77, width=159.2, height=17.442, anchor='w')# 设置页面 配置九 显示当前热键
            canvas_advanced.create_window((120,18*24), window=label_78, width=159.2, height=17.442, anchor='w')# 设置页面 配置十 显示当前热键
            canvas_advanced.create_window((120,18*25), window=label_79, width=159.2, height=17.442, anchor='w')# 设置页面 配置十一 显示当前热键
            canvas_advanced.create_window((120,18*26), window=label_80, width=159.2, height=17.442, anchor='w')# 设置页面 配置十二 显示当前热键
            canvas_advanced.create_window((0,18*15), window=label_81, width=118, height=17.442, anchor='w')# 设置页面 文本 '配置一'
            canvas_advanced.create_window((0,18*16), window=label_82, width=118, height=17.442, anchor='w')# 设置页面 文本 '配置二'
            canvas_advanced.create_window((0,18*17), window=label_83, width=118, height=17.442, anchor='w')# 设置页面 文本 '配置三'
            canvas_advanced.create_window((0,18*18), window=label_84, width=118, height=17.442, anchor='w')# 设置页面 文本 '配置四'
            canvas_advanced.create_window((0,18*19), window=label_85, width=118, height=17.442, anchor='w')# 设置页面 文本 '配置五'
            canvas_advanced.create_window((0,18*20), window=label_86, width=118, height=17.442, anchor='w')# 设置页面 文本 '配置六'
            canvas_advanced.create_window((0,18*21), window=label_87, width=118, height=17.442, anchor='w')# 设置页面 文本 '配置七'
            canvas_advanced.create_window((0,18*22), window=label_88, width=118, height=17.442, anchor='w')# 设置页面 文本 '配置八'
            canvas_advanced.create_window((0,18*23), window=label_89, width=118, height=17.442, anchor='w')# 设置页面 文本 '配置九'
            canvas_advanced.create_window((0,18*24), window=label_90, width=118, height=17.442, anchor='w')# 设置页面 文本 '配置十'
            canvas_advanced.create_window((0,18*25), window=label_91, width=118, height=17.442, anchor='w')# 设置页面 文本 '配置十一'
            canvas_advanced.create_window((0,18*26), window=label_92, width=118, height=17.442, anchor='w')# 设置页面 文本 '配置十二'
            
            
            
            
            
            
            
            frame_func.place_forget()
            frame_about.place_forget()
            frame_drive.place_forget()
        except Exception as e:
            if '0x0129：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0129：' + str(e) + '\n'
            print('0x0129:ERROR!',e)


    def btn6_command():                                        # 点击‘关于’按钮触发事件
        try:
            btn3.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn4.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn5.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn6.config(bg=config['BTN_MENU_CHOOSE_BG'], fg=config['BTN_MENU_CHOOSE_FG'])
            btn55.config(bg=config['UI_BG'], fg=config['UI_FG'])
            frame_about.place(x=1,y=36)
            canvas_about.place(x=0,y=0, relwidth=1, relheight=1)
            label_38.place(x=159, y=16*2, relwidth=0.2, relheight=0.054)        # 文字 '使用教程'
            label_39.place(x=79, y=16*4, relwidth=0.6, relheight=0.054)         # 文本 '版本号：1.47'
            label_42.place(x=79, y=16*6, relwidth=0.6, relheight=0.054)         # 文本 'QQ交流群：928286446'
            label_40.place(x=20, y=16*8, relwidth=0.9, relheight=0.054)         # 文本 '开源地址：https://github.com/1C1T/CaiShou'
            label_63.place(x=39, y=18*9, relwidth=0.8, relheight=0.054*3)       # 文本 '永久免费'
            btn30.place(x=80, y=18*13, relwidth=0.6, relheight=0.054*3)         # 关于页面 检查版本更新按钮
            frame_func.place_forget()
            frame_advanced.place_forget()
            frame_drive.place_forget()
        except Exception as e:
            if '0x0130：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0130：' + str(e) + '\n'
            print('0x0130:ERROR!',e)


    def btn55_command():                                       # 点击‘驱动’按钮触发事件
        try:
            btn3.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn4.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn5.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn6.config(bg=config['UI_BG'], fg=config['UI_FG'])
            btn55.config(bg=config['BTN_MENU_CHOOSE_BG'], fg=config['BTN_MENU_CHOOSE_FG'])
            frame_drive.place(x=1,y=36)
            canvas_drive.place(x=0,y=0, relwidth=1, relheight=1)
            btn56.place(relx=0.1, y=18*5, relwidth=0.35, relheight=0.054*7)   #  SendInput驱动按钮
            btn57.place(relx=0.55, y=18*5, relwidth=0.35, relheight=0.054*7)  #  罗技驱动按钮
            frame_func.place_forget()
            frame_advanced.place_forget()
            frame_about.place_forget()
        except Exception as e:
            if '0x013001：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x013001：' + str(e) + '\n'
            print('0x013001:ERROR!')


    def btn7_command():                                        # 点击‘模式’按钮触发事件
        try:
            if btn7['text'] == '模式1':
                config['MARCO_MODE'] = 2
                btn7.config(text='模式2')
                kw={'模式':'2'}
            elif btn7['text'] == '模式2':
                config['MARCO_MODE'] = 3
                btn7.config(text='模式3')
                kw={'模式':'3'}
            else:
                config['MARCO_MODE'] = 1
                btn7.config(text='模式1')
                kw={'模式':'1'}
            configuration('set', config['CONFIGURATION_NAME'], kw)
            config['SIGN_7'] = 1 # 修改状态栏 模式名字
        except Exception as e:
            if '0x0131：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0131：' + str(e) + '\n'
            print('0x0131:ERROR!',e)


    def btn8_command():                                        # 点击弹道页面‘重置’按钮触发事件
        try:
            nonlocal configuration_another_name, recover_sign
            if tkinter.messagebox.askokcancel('提示', '点击重置将清空已设置的数据，请确认'):
                recover_path = './配置文件/recover'
                if not os.path.exists(recover_path):
                    os.mkdir(recover_path)
                configuration_name_path = './配置文件/{}.txt'.format(config['CONFIGURATION_NAME'])
                if os.path.exists(configuration_name_path) == True:
                    file_name = '{}_[最近一次重置前数据]'.format(config['CONFIGURATION_NAME'])
                    with open(configuration_name_path, 'r', encoding='utf-8') as f_r, open(recover_path + '/{}.txt'.format(file_name), 'w', encoding='utf-8') as f_w:
                        f_w.write(f_r.read())
                configuration_list=['注释:模式只有1 2 3,时间不可低于段数的10倍,段数最低为1,冒号和逗号为英文字符', \
                '标题:{}'.format(configuration_another_name), '模式:1', '时间:5000', '段数:10', \
                '第1段:0,0', '第2段:0,0', '第3段:0,0', '第4段:0,0', '第5段:0,0', \
                '第6段:0,0', '第7段:0,0', '第8段:0,0', '第9段:0,0', '第10段:0,0']
                with open(configuration_name_path, 'w', encoding='utf-8') as f:
                    f.write(str(configuration_list).replace("', '", "\n").replace("['", "").replace("']", ""))
                recover_sign = 1
                config['SIGN_2'] = 1
        except Exception as e:
            if '0x0132：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0132：' + str(e) + '\n'
            print('0x0132:ERROR!',e)


    def btn9_command():                                        # 点击‘左’按钮 所有强度输入值-1
        try:
            srtong_count = int(len(configuration_strong[0]))
            for i in range(srtong_count):
                num = int(entry_name[0][i].get())-1
                configuration_strong[0][i] = num
                entry_name[0][i].delete(0, 'end')
                entry_name[0][i].insert(0, num)
                old_value = str(configuration_all[i+5]).split(':')[1].split(',')
                new_value = '第{}段:'.format(i+1)+str(num)+','+str(old_value[1])
                configuration_all.pop(i+5)
                configuration_all.insert(i+5, new_value)
            with open('./配置文件/{}.txt'.format(config['CONFIGURATION_NAME']), 'w', encoding='utf-8') as f:
                f.write(str(configuration_all).replace("', '", "\n").replace("['", "").replace("']", ""))
            configuration_strong_updata()
            strong_convert_updata()
        except Exception as e:
            if '0x0133：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0133：' + str(e) + '\n'
            print('0x0133:ERROR!',e)


    def btn10_command():                                       # 点击‘右’按钮 所有强度输入值+1
        try:
            srtong_count = int(len(configuration_strong[1]))
            for i in range(srtong_count):
                num = int(entry_name[0][i].get())+1
                configuration_strong[0][i] = num
                entry_name[0][i].delete(0, 'end')
                entry_name[0][i].insert(0, num)
                old_value = str(configuration_all[i+5]).split(':')[1].split(',')
                new_value = '第{}段:'.format(i+1)+str(num)+','+str(old_value[1])
                configuration_all.pop(i+5)
                configuration_all.insert(i+5, new_value)
            with open('./配置文件/{}.txt'.format(config['CONFIGURATION_NAME']), 'w', encoding='utf-8') as f:
                f.write(str(configuration_all).replace("', '", "\n").replace("['", "").replace("']", ""))
            configuration_strong_updata()
            strong_convert_updata()
        except Exception as e:
            if '0x0134：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0134：' + str(e) + '\n'
            print('0x0134:ERROR!',e)


    def btn11_command():                                       # 点击‘上’按钮 所有强度输入值-1
        try:
            srtong_count = int(len(configuration_strong[0]))
            for i in range(srtong_count):
                num = int(entry_name[1][i].get())-1
                configuration_strong[1][i] = num
                entry_name[1][i].delete(0, 'end')
                entry_name[1][i].insert(0, num)
                old_value = str(configuration_all[i+5]).split(':')[1].split(',')
                new_value = '第{}段:'.format(i+1)+str(old_value[0])+','+str(num)
                configuration_all.pop(i+5)
                configuration_all.insert(i+5, new_value)
            with open('./配置文件/{}.txt'.format(config['CONFIGURATION_NAME']), 'w', encoding='utf-8') as f:
                f.write(str(configuration_all).replace("', '", "\n").replace("['", "").replace("']", ""))
            configuration_strong_updata()
            strong_convert_updata()
        except Exception as e:
            if '0x0135：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0135：' + str(e) + '\n'
            print('0x0135:ERROR!',e)


    def btn12_command():                                       # 点击‘下’按钮 所有强度输入值+1
        try:
            srtong_count = int(len(configuration_strong[1]))
            for i in range(srtong_count):
                num = int(entry_name[1][i].get())+1
                configuration_strong[1][i] = num
                entry_name[1][i].delete(0, 'end')
                entry_name[1][i].insert(0, num)
                old_value = str(configuration_all[i+5]).split(':')[1].split(',')
                new_value = '第{}段:'.format(i+1)+str(old_value[0])+','+str(num)
                configuration_all.pop(i+5)
                configuration_all.insert(i+5, new_value)
            with open('./配置文件/{}.txt'.format(config['CONFIGURATION_NAME']), 'w', encoding='utf-8') as f:
                f.write(str(configuration_all).replace("', '", "\n").replace("['", "").replace("']", ""))
            configuration_strong_updata()
            strong_convert_updata()
        except Exception as e:
            if '0x0136：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0136：' + str(e) + '\n'
            print('0x0136:ERROR!',e)


    def btn30_command():                                       # 点击关于页面‘检查版本更新’按钮触发事件
        try:
            btn30['text'] = '已删除联网更新代码'
        except Exception as e:
            if '0x0140：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0140：' + str(e) + '\n'
            print('0x0140:ERROR!',e)


    def btn13_command(*args):                                  # 点击功能页面‘鼠标加速度开关’按钮触发事件
        try:
            nonlocal mouse_acceleration
            if args:
                if get_mouse_acceleration():#如果鼠标加速度开启
                    config['MOUSE_ACCELERATION'] = '开'
                    mouse_acceleration = '开'
                else:
                    config['MOUSE_ACCELERATION'] = '关'
                    mouse_acceleration = '关'
            else:
                if mouse_acceleration == '开':
                    config['MOUSE_ACCELERATION'] = '关'
                    mouse_acceleration = '关'
                else:
                    config['MOUSE_ACCELERATION'] = '开'
                    mouse_acceleration = '开'
            if config['MOUSE_ACCELERATION'] == '开':
                hotkey_cfg.set('设置','鼠标加速度', '开')
                btn13['bg'] = config['BTN_FUNC_CHOOSE_BG']
                btn13['fg'] = config['BTN_FUNC_CHOOSE_FG']
                set_mouse_acceleration(1)
            else:
                hotkey_cfg.set('设置','鼠标加速度', '关')
                btn13['bg'] = config['UI_BG_2']
                btn13['fg'] = config['BTN_FUNC_FG']
                set_mouse_acceleration(0)
            with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                hotkey_cfg.write(f)
        except Exception as e:
            if '0x014203：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014203：' + str(e) + '\n'
            print('0x014203:ERROR!',e)


    def btn36_command(*args):                                  # 点击设置页面‘连点器开关’按钮触发事件
        try:
            nonlocal clicker_switch
            if args:
                config['CLICKER_SWITCH'] = clicker_switch
            else:
                if clicker_switch == '开':
                    config['CLICKER_SWITCH'] = '关'
                    clicker_switch = '关'
                else:
                    config['CLICKER_SWITCH'] = '开'
                    clicker_switch = '开'
            if config['CLICKER_SWITCH'] == '开':
                hotkey_cfg.set('设置','连点器开/关', '开')
                btn36['bg'] = config['BTN_FUNC_CHOOSE_BG']
                btn36['fg'] = config['BTN_FUNC_CHOOSE_FG']
                btn39['state'] = 'normal'
            else:
                hotkey_cfg.set('设置','连点器开/关', '关')
                btn36['bg'] = config['UI_BG']
                btn36['fg'] = config['BTN_FUNC_FG']
                btn39['state'] = 'disabled'
            with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                hotkey_cfg.write(f)
        except Exception as e:
            if '0x014203：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014203：' + str(e) + '\n'
            print('0x014203:ERROR!',e)


    def btn38_command(*args):                                  # 点击设置页面‘音效开关’按钮触发事件
        try:
            nonlocal sound_effect_switch
            if args:
                config['SOUND_EFFECT_SWITCH'] = sound_effect_switch
            else:
                if sound_effect_switch == '开':
                    config['SOUND_EFFECT_SWITCH'] = '关'
                    sound_effect_switch = '关'
                else:
                    config['SOUND_EFFECT_SWITCH'] = '开'
                    sound_effect_switch = '开'
            if config['SOUND_EFFECT_SWITCH'] == '开':
                hotkey_cfg.set('设置','音效提示开/关', '开')
                btn38['bg'] = config['BTN_FUNC_CHOOSE_BG']
                btn38['fg'] = config['BTN_FUNC_CHOOSE_FG']
            else:
                hotkey_cfg.set('设置','音效提示开/关', '关')
                btn38['bg'] = config['UI_BG']
                btn38['fg'] = config['BTN_FUNC_FG']
            with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                hotkey_cfg.write(f)
        except Exception as e:
            if '0x014204：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014204：' + str(e) + '\n'
            print('0x014204:ERROR!',e)


    def btn39_command(*args):                                  # 点击设置页面‘极限点击’按钮触发事件
        try:
            nonlocal clicker_break_limit
            if args:
                config['CLICKER_BREAK_LIMIT'] = clicker_break_limit
            else:
                if clicker_break_limit == '开':
                    config['CLICKER_BREAK_LIMIT'] = '关'
                    clicker_break_limit = '关'
                else:
                    config['CLICKER_BREAK_LIMIT'] = '开'
                    clicker_break_limit = '开'
            if config['CLICKER_BREAK_LIMIT'] == '开':
                hotkey_cfg.set('设置','极限点击开/关', '开')
                btn39['bg'] = config['BTN_FUNC_CHOOSE_BG']
                btn39['fg'] = config['BTN_FUNC_CHOOSE_FG']
            else:
                hotkey_cfg.set('设置','极限点击开/关', '关')
                btn39['bg'] = config['UI_BG']
                btn39['fg'] = config['BTN_FUNC_FG']
            with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                hotkey_cfg.write(f)
        except Exception as e:
            if '0x014204：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014204：' + str(e) + '\n'
            print('0x014204:ERROR!',e)


    def restart_program():                                     # 重启程序
        try:
            CaiShou = sys.executable
            os.execl(CaiShou, CaiShou, * sys.argv)
        except Exception as e:
            if '0x014205：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014205：' + str(e) + '\n'
            print('0x014205:ERROR!',e)


    def btn40_command():                                       # 点击设置页面‘风格切换’按钮触发事件
        try:
            nonlocal style_change
            if style_change == '暗':
                style_change = '明'
                config['STYLE_CHANGE'] = style_change
                config['UI_BG'] = '#e7e6e6'                # UI界面背景颜色
                config['UI_BG_2'] = '#c1c1c1'              # UI界面背景颜色
                config['UI_FG'] = 'black'                  # UI界面前景颜色
                config['BTN_MENU_ENTER_BG'] = '#aaa7a7'    # 菜单按钮进入时背景颜色
                config['BTN_MENU_ACTIVE_BG'] = '#3f3d3d'   # 菜单按钮活动时背景颜色
                config['BTN_MENU_ACTIVE_FG'] = 'white'     # 菜单按钮活动时前景颜色
                config['BTN_MENU_CHOOSE_BG'] = '#757171'   # 菜单按钮选定时背景颜色
                config['BTN_MENU_CHOOSE_FG'] = 'white'     # 菜单按钮选定时前景颜色
                config['BTN_FUNC_FG'] = '#131414'          # 功能按钮前景颜色
                config['BTN_FUNC_ENTER_BG'] = '#aaa7a7'    # 功能按钮进入时背景颜色
                config['BTN_FUNC_ACTIVE_BG'] = '#01018e'   # 功能按钮活动时背景颜色
                config['BTN_FUNC_ACTIVE_FG'] = 'white'     # 功能按钮活动时前景颜色
                config['BTN_FUNC_CHOOSE_BG'] = '#2357a0'   # 功能按钮选定时背景颜色
                config['BTN_FUNC_CHOOSE_FG'] = 'white'     # 功能按钮选定时前景颜色
                config['ENTRY_BG'] = '#1dba8d'             # 输入框背景颜色
                config['ENTRY_FG'] = 'black'               # 输入框前景颜色
                config['ENTRY_FOCUSIN_BG'] = '#a881db'     # 输入框获得焦点时背景颜色
                config['ENTRY_DISABLED_BG'] = '#C0C0C0'    # 输入框禁用时背景颜色
                config['ENTRY_DISABLED_FG'] = 'black'      # 输入框禁用时前景颜色
                config['SCALE_BG'] = '#2357a0'             # 刻度块背景颜色
                hotkey_cfg.set('设置','风格切换', '明')
            else:
                style_change = '暗'
                config['STYLE_CHANGE'] = style_change
                config['UI_BG'] = '#373737'                # UI界面背景颜色
                config['UI_BG_2'] = '#5e5e5e'              # UI界面背景颜色二
                config['UI_FG'] = '#bfbfbf'                # UI界面前景颜色
                config['BTN_MENU_ENTER_BG'] = '#7a119e'    # 菜单按钮背景颜色
                config['BTN_MENU_ACTIVE_BG'] = '#530b6b'   # 菜单按钮活动时背景颜色
                config['BTN_MENU_ACTIVE_FG'] = 'white'     # 菜单按钮活动时前景颜色
                config['BTN_MENU_CHOOSE_BG'] = '#a418d2'   # 菜单按钮选定时背景颜色
                config['BTN_MENU_CHOOSE_FG'] = 'white'     # 菜单按钮选定时前景颜色
                config['BTN_FUNC_FG'] = '#ffdb00'          # 功能按钮前景颜色
                config['BTN_FUNC_ENTER_BG'] = '#727272'    # 功能按钮进入时背景颜色
                config['BTN_FUNC_ACTIVE_BG'] = '#ccb000'   # 功能按钮活动时背景颜色
                config['BTN_FUNC_ACTIVE_FG'] = 'black'     # 功能按钮活动时前景颜色
                config['BTN_FUNC_CHOOSE_BG'] = '#ffdb00'   # 功能按钮选定时背景颜色
                config['BTN_FUNC_CHOOSE_FG'] = 'black'     # 功能按钮选定时前景颜色
                config['ENTRY_BG'] = '#cccace'             # 输入框背景颜色
                config['ENTRY_FG'] = 'black'               # 输入框前景颜色
                config['ENTRY_FOCUSIN_BG'] = '#d3d137'     # 输入框获得焦点时背景颜色
                config['ENTRY_DISABLED_BG'] = '#4c4c4c'    # 输入框禁用时背景颜色
                config['ENTRY_DISABLED_FG'] = 'black'      # 输入框禁用时前景颜色
                config['SCALE_BG'] = '#ffdb00'             # 刻度块背景颜色
                hotkey_cfg.set('设置','风格切换', '暗')
            with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                hotkey_cfg.write(f)
            restart_program()
        except Exception as e:
            if '0x014206：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014206：' + str(e) + '\n'
            print('0x014206:ERROR!',e)


    def btn41_command(*args):                                  # 点击设置页面‘开机自启’按钮触发事件
        try:
            nonlocal self_start
            if args:
                config['SELF_START'] = self_start
            else:
                if self_start == '开':
                    config['SELF_START'] = '关'
                    self_start = '关'
                elif self_start == '关':
                    config['SELF_START'] = '开'
                    self_start = '开'
            if config['SELF_START'] == '开':
                hotkey_cfg.set('设置','开机自启', '开')
                btn41['bg'] = config['BTN_FUNC_CHOOSE_BG']
                btn41['fg'] = config['BTN_FUNC_CHOOSE_FG']
            else:
                hotkey_cfg.set('设置','开机自启', '关')
                btn41['bg'] = config['UI_BG']
                btn41['fg'] = config['BTN_FUNC_FG']
            with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                hotkey_cfg.write(f)
        except Exception as e:
            if '0x014208：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014208：' + str(e) + '\n'
            print('0x014208:ERROR!',e)


    def btn42_command(*args):                                  # 点击设置页面‘左右键触发宏’按钮触发事件
        try:
            nonlocal left_right_press_trigger
            if args:
                config['L_R_P_T'] = left_right_press_trigger
            else:
                if left_right_press_trigger == '开':
                    config['L_R_P_T'] = '关'
                    left_right_press_trigger = '关'
                elif left_right_press_trigger == '关':
                    config['L_R_P_T'] = '开'
                    left_right_press_trigger = '开'
            if config['L_R_P_T'] == '开':
                hotkey_cfg.set('设置','左右键触发宏', '开')
                btn42['bg'] = config['BTN_FUNC_CHOOSE_BG']
                btn42['fg'] = config['BTN_FUNC_CHOOSE_FG']
            else:
                hotkey_cfg.set('设置','左右键触发宏', '关')
                btn42['bg'] = config['UI_BG']
                btn42['fg'] = config['BTN_FUNC_FG']
            with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                hotkey_cfg.write(f)
        except Exception as e:
            if '0x014209：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014209：' + str(e) + '\n'
            print('0x014209:ERROR!',e)


    def btn56_command(*args):                                  # 点击驱动页面‘SendInput’按钮触发事件
        moveRel = SendInput.moveRel
        try:
            if args:
                if config["SELECT_DRIVE"] == 0:
                    btn56['bg'] = config['BTN_FUNC_CHOOSE_BG']
                    btn56['fg'] = config['BTN_FUNC_CHOOSE_FG']
            else:#手动点击
                if config["SELECT_DRIVE"] == 1:
                    config["SELECT_DRIVE"] = 0
                    btn56['bg'] = config['BTN_FUNC_CHOOSE_BG']
                    btn56['fg'] = config['BTN_FUNC_CHOOSE_FG']
                    btn57['bg'] = config['UI_BG']
                    btn57['fg'] = config['BTN_FUNC_FG']
                    hotkey_cfg.set('设置','驱动',"SendInput")
                    with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                        hotkey_cfg.write(f)
                    time.sleep(0.1)
                    for i in range(50):
                        moveRel(0, 5)
                        time.sleep(0.01)
                else:
                    time.sleep(0.1)
                    for i in range(50):
                        moveRel(0, 5)
                        time.sleep(0.01)
        except Exception as e:
            if '0x014214：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014214：' + str(e) + '\n'
            print('0x014214:ERROR!')


    def btn57_command(*args):                                  # 点击驱动页面‘罗技’按钮触发事件
        try:
            if args:
                if config["SELECT_DRIVE"] == 1:
                    if config['LGS_GHUB_STATE'] :# 如果检测到罗技驱动
                        btn57['bg'] = config['BTN_FUNC_CHOOSE_BG']
                        btn57['fg'] = config['BTN_FUNC_CHOOSE_FG']
                    else:
                        config["SELECT_DRIVE"] = 0
                        btn56['bg'] = config['BTN_FUNC_CHOOSE_BG']
                        btn56['fg'] = config['BTN_FUNC_CHOOSE_FG']
                        hotkey_cfg.set('设置','驱动',"SendInput")
                        with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                            hotkey_cfg.write(f)
            else:#手动点击
                if config['SELECT_DRIVE'] == 0:
                    if config['LGS_GHUB_STATE']:
                        config["SELECT_DRIVE"] = 1
                        btn56['bg'] = config['UI_BG']
                        btn56['fg'] = config['BTN_FUNC_FG']
                        btn57['bg'] = config['BTN_FUNC_CHOOSE_BG']
                        btn57['fg'] = config['BTN_FUNC_CHOOSE_FG']
                        hotkey_cfg.set('设置','驱动',"罗技")
                        with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                            hotkey_cfg.write(f)
                        time.sleep(0.1)
                        for i in range(50):
                            LGS_GHUB.moveR(0, 5)
                            time.sleep(0.01)
                    else:
                        tkinter.messagebox.showinfo('提示', '未安装罗技驱动')
                else:
                    time.sleep(0.1)
                    for i in range(50):
                        LGS_GHUB.moveR(0, 5)
                        time.sleep(0.01)
        except Exception as e:
            if '0x014215：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014215：' + str(e) + '\n'
            print('0x014215:ERROR!')


    def scale_1_command(event):                                # 点击功能页面 ‘鼠标灵敏度’刻度条 触发事件
        try:
            nonlocal mouse_speed
            mouse_speed = scale_1.get()
            set_mouse_speed(mouse_speed)
            label_9['text'] = str(mouse_speed)
            hotkey_cfg.set('设置','鼠标灵敏度', str(mouse_speed))
            with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                hotkey_cfg.write(f)
        except Exception as e:
            if '0x014209：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014209：' + str(e) + '\n'
            print('0x014209:ERROR!',e)


    def entry_FocusIn(event):                                  # 时间、段数输入框 得到焦点 触发事件
        try:
            if str(event.widget) == '.!canvas2.!entry':
                entry_1.config(bg=config['ENTRY_FOCUSIN_BG'])
            elif str(event.widget) == '.!canvas2.!entry2':
                entry_2.config(bg=config['ENTRY_FOCUSIN_BG'])
            elif str(event.widget) == '.!frame2.!canvas.!entry':
                entry_3.config(bg=config['ENTRY_FOCUSIN_BG'])
            elif str(event.widget) == '.!frame.!canvas.!entry':
                entry_4.config(bg=config['ENTRY_FOCUSIN_BG'])
            elif str(event.widget) == '.!frame.!canvas.!entry2':
                entry_5.config(bg=config['ENTRY_FOCUSIN_BG'])
            elif str(event.widget) == '.!frame.!canvas.!entry3':
                entry_6.config(bg=config['ENTRY_FOCUSIN_BG'])
            elif str(event.widget) == '.!frame.!canvas.!entry4':
                entry_7.config(bg=config['ENTRY_FOCUSIN_BG'])
            elif str(event.widget) == '.!frame.!canvas.!entry5':
                entry_8.config(bg=config['ENTRY_FOCUSIN_BG'])
            elif str(event.widget) == '.!frame.!canvas.!entry6':
                entry_9.config(bg=config['ENTRY_FOCUSIN_BG'])
        except Exception as e:
            if '0x0144：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0144：' + str(e) + '\n'
            print('0x0144:ERROR!',e)


    def entry_FocusOut(event):                                 # 时间、段数输入框 失去焦点 触发事件
        try:
            nonlocal box_num, scroll_height, configuration_all, configuration_duration\
            , configuration_section, configuration_strong, recover_sign, clicker_interval\
            , random_ballistic_1, random_ballistic_2, random_ballistic_3, random_ballistic_4\
            , random_ballistic_5, random_ballistic_6
            if str(event.widget) == '.!canvas2.!entry':
                entry_1.config(bg=config['ENTRY_BG'])
                num = 5000
                try:
                    entry_1_get = int(entry_1.get())
                    if entry_1_get and entry_1_get > 0:
                        num = entry_1_get
                    else:
                        num = 5000
                except Exception as e:
                    if '0x014501：' not in config['ERROR_LOG']:
                        config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014501：' + str(e) + '\n'
                    num = 5000
                configuration_duration = time_num_check2(num)
                configuration_duration_updata()
                duration_set(num)
                strong_convert_updata()
            elif str(event.widget) == '.!canvas2.!entry2':
                entry_2.config(bg=config['ENTRY_BG'])
                for i in range(10):                               # 修改强度输入框的背景颜色
                    entry_name[0][i].config(state='normal')
                    entry_name[1][i].config(state='normal')
                num = 10
                entry_2_get = entry_2.get()
                if 'hf' in entry_2_get or 'HF' in entry_2_get or 'hF' in entry_2_get or 'Hf' in entry_2_get or '恢复' in entry_2_get:
                    entry_2.delete(0, 'end')
                    entry_2.insert(0, config['MACRO_SECTION'])
                    if tkinter.messagebox.askokcancel('提示', '将恢复该配置最近一次重置前的数据，请确认'):
                        if not os.path.exists('./配置文件/recover'):
                            os.mkdir('./配置文件/recover')
                        else:
                            file_name = '{}_[最近一次重置前数据]'.format(config['CONFIGURATION_NAME'])
                            if os.path.exists('./配置文件/recover/{}.txt'.format(file_name)) == True:
                                with open('./配置文件/recover/{}.txt'.format(file_name), 'r', encoding='utf-8') as f_r_recover\
                                , open('./配置文件/{}.txt'.format(config['CONFIGURATION_NAME']), 'r', encoding='utf-8') as f_r_now:
                                    f_r_now, f_r_recover = f_r_now.read(), f_r_recover.read()
                                with open('./配置文件/recover/{}.txt'.format(file_name), 'w', encoding='utf-8') as f_w_recover\
                                , open('./配置文件/{}.txt'.format(config['CONFIGURATION_NAME']), 'w', encoding='utf-8') as f_w_now:
                                    f_w_recover.write(f_r_now)
                                    f_w_now.write(f_r_recover)
                                recover_sign = 1
                                config['SIGN_2'] = 1
                            else:
                                tkinter.messagebox.showinfo('提示', '没有该配置最近一次重置前的数据')
                else:
                    try:
                        if int(entry_2_get) and num > 0:
                            num = int(entry_2_get)
                            time_num_check3(num)
                            if num < 10:
                                for i in range(num, 10):
                                    entry_name[0][i].config(state='disabled')
                                    entry_name[1][i].config(state='disabled')
                        else:
                            num = 10
                    except Exception as e:
                        if '0x014502：' not in config['ERROR_LOG']:
                            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014502：' + str(e) + '\n'
                        num = 10
                    configuration_section = num
                    configuration_section_updata()
                    entry_2.delete(0, 'end')
                    entry_2.insert(0, num)
                    kw={'段数':num}
                    configuration('set', config['CONFIGURATION_NAME'], kw)       # 修改配置文件中的段数
                    configuration_strong = [[],[]]
                    box_num, scroll_height = box_num_check(configuration_all[4].split(':')[1])    # 对输入的段数进行检查，并计算scroll_height值
                    canvas_content_two.config(scrollregion=(0, 0, 400, scroll_height))            # 设置画布可以滚动的范围
                    change_canvas_content_two(int(num))
                    for i in range(5, num+5):
                        x = strong_num_check(configuration_all[i].split(':')[1].split(',')[0])
                        y = strong_num_check(configuration_all[i].split(':')[1].split(',')[1])
                        configuration_strong[0].append(x)
                        configuration_strong[1].append(y)
                    configuration_strong_updata()
                    strong_convert_updata()
            elif str(event.widget) == '.!frame2.!canvas.!entry':
                entry_3.config(bg=config['ENTRY_BG'])
                num = 100
                try:
                    entry_3_get = int(entry_3.get())
                    if entry_3_get and entry_3_get > 0:
                        num = entry_3_get
                    else:
                        num = 100
                except Exception as e:
                    if '0x014503：' not in config['ERROR_LOG']:
                        config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014503：' + str(e) + '\n'
                    num = 100
                clicker_interval = num
                clicker_interval_updata()
                clicker_interval_set(num)
            elif str(event.widget) == '.!frame.!canvas.!entry':
                entry_4.config(bg=config['ENTRY_BG'])
                num = 0
                try:
                    int_entry_4 = int(entry_4.get())
                    if int_entry_4 and int_entry_4 >= 0:
                        num = int_entry_4
                    else:
                        num = 0
                except Exception as e:
                    if '0x014504：' not in config['ERROR_LOG']:
                        config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014504：' + str(e) + '\n'
                    num = 0
                random_ballistic_1 = num
                random_ballistic_updata(1)
                random_ballistic_set(1, num)
            elif str(event.widget) == '.!frame.!canvas.!entry2':
                entry_5.config(bg=config['ENTRY_BG'])
                num = 0
                try:
                    int_entry_5 = int(entry_5.get())
                    if int_entry_5 and int_entry_5 >= 0:
                        num = int_entry_5
                    else:
                        num = 0
                except Exception as e:
                    if '0x014505：' not in config['ERROR_LOG']:
                        config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014505：' + str(e) + '\n'
                    num = 0
                random_ballistic_2 = num
                random_ballistic_updata(2)
                random_ballistic_set(2, num)
            elif str(event.widget) == '.!frame.!canvas.!entry3':
                entry_6.config(bg=config['ENTRY_BG'])
                num = 0
                try:
                    if int(entry_6.get()):
                        num = int(entry_6.get())
                except Exception as e:
                    if '0x014506：' not in config['ERROR_LOG']:
                        config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014506：' + str(e) + '\n'
                    num = 0
                random_ballistic_3 = num
                random_ballistic_updata(3)
                random_ballistic_set(3, num)
            elif str(event.widget) == '.!frame.!canvas.!entry4':
                entry_7.config(bg=config['ENTRY_BG'])
                num = 0
                try:
                    if int(entry_7.get()):
                        num = int(entry_7.get())
                except Exception as e:
                    if '0x014507：' not in config['ERROR_LOG']:
                        config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014507：' + str(e) + '\n'
                    num = 0
                random_ballistic_4 = num
                random_ballistic_updata(4)
                random_ballistic_set(4, num)
            elif str(event.widget) == '.!frame.!canvas.!entry5':
                entry_8.config(bg=config['ENTRY_BG'])
                num = 0
                try:
                    if int(entry_8.get()):
                        num = int(entry_8.get())
                except Exception as e:
                    if '0x014508：' not in config['ERROR_LOG']:
                        config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014508：' + str(e) + '\n'
                    num = 0
                random_ballistic_5 = num
                random_ballistic_updata(5)
                random_ballistic_set(5, num)
            elif str(event.widget) == '.!frame.!canvas.!entry6':
                entry_9.config(bg=config['ENTRY_BG'])
                num = 0
                try:
                    if int(entry_9.get()):
                        num = int(entry_9.get())
                except Exception as e:
                    if '0x014509：' not in config['ERROR_LOG']:
                        config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014509：' + str(e) + '\n'
                    num = 0
                random_ballistic_6 = num
                random_ballistic_updata(6)
                random_ballistic_set(6, num)
        except Exception as e:
            if '0x0145：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0145：' + str(e) + '\n'
            print('0x0145:ERROR!',e)


    def entry_return(event):                                   # 时间、段数输入框 按下回车 触发事件
        try:
            label_5.focus_set()
        except Exception as e:
            if '0x0146：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0146：' + str(e) + '\n'
            print('0x0146:ERROR!',e)


    def ui_move(event):                                        # 移动窗口功能
        try:
            nonlocal b1_time
            if time.time() - b1_time > 0.015:
                ui.geometry('400x360+{}+{}'.format(event.x_root-Button_1_x, event.y_root-Button_1_y))
                b1_time = time.time()
        except Exception as e:
            if '0x0147：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0147：' + str(e) + '\n'
            print('0x0147:ERROR!',e)


    def get_b1_time(event):                                    # 获取点击窗口的时间
        try:
            nonlocal b1_time
            b1_time = time.time()
        except Exception as e:
            if '0x014701：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x014701：' + str(e) + '\n'
            print('0x014701:ERROR!',e)


    def get_mouse_xy(event):                                   # 保存鼠标在窗体顶部按下时的位置
        try:
            nonlocal Button_1_x, Button_1_y
            if str(event.widget) == '.!label':
                Button_1_x = event.x+1
                Button_1_y = event.y+1
            elif str(event.widget) == '.!label2':
                Button_1_x = event.x+20
                Button_1_y = event.y
            elif str(event.widget) == '.!label3':
                Button_1_x = event.x+48
                Button_1_y = event.y
        except Exception as e:
            if '0x0148：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0148：' + str(e) + '\n'
            print('0x0148:ERROR!',e)


    def open_tutorial(event):                                  # 打开使用教程
        try:
            if os.path.exists('.\使用教程.txt') == True:
                os.startfile('.\使用教程.txt')
        except Exception as e:
            if '0x0149：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0149：' + str(e) + '\n'
            print('0x0149:ERROR!',e)


    def open_url(event):                                       # 打开开源地址
        try:
            if os.path.exists('彩手开源地址.url') == True:
                os.startfile('彩手开源地址.url')
        except Exception as e:
            if '0x0150：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0150：' + str(e) + '\n'
            print('0x0150:ERROR!',e)


    def change_canvas_content_two(num):
        try:
            item_id = canvas_content_two.find_all()
            item_count = int(len(item_id)/7)
            if int(box_num) > 10:
                if num < item_count:
                    for i in range(num+1, item_count):
                        label_name[i].place_forget()
                        entry_name[0][i].place_forget()
                        entry_name[1][i].place_forget()
                        btn_name[0][i].place_forget()
                        btn_name[1][i].place_forget()
                        btn_name[2][i].place_forget()
                        btn_name[3][i].place_forget()
            elif int(box_num) == 10:
                if num < item_count:
                    for i in range(10, item_count):
                        label_name[i].place_forget()
                        entry_name[0][i].place_forget()
                        entry_name[1][i].place_forget()
                        btn_name[0][i].place_forget()
                        btn_name[1][i].place_forget()
                        btn_name[2][i].place_forget()
                        btn_name[3][i].place_forget()
            if num > item_count:
                create_canvas_content_two_widget('add', config['CONFIGURATION_NAME'])
            else:
                create_canvas_content_two_widget('new', config['CONFIGURATION_NAME'])
        except Exception as e:
            if '0x0151：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0151：' + str(e) + '\n'
            print('0x0151:ERROR!',e)


    def create_canvas_content_two_widget(way, name):           # 创建‘第几段’标签、强度输入框和控制按钮，根据box_num值创建控件
        try:
            nonlocal configuration_all, label_name, entry_name, btn_name
            if way == 'add':
                start_num = int(len(canvas_content_two.find_all())/7)
                end_num = int(box_num)
            else:
                start_num = 0
                end_num = int(box_num)
            for i in range(start_num, end_num):
                def canvas_content_two_button_up_count(i=i):
                    try:
                        if entry_name[1][i]['state'] != 'disabled':
                            num = int(entry_name[1][i].get())-1
                            configuration_strong[1][i] = num
                            configuration_strong_updata()
                            strong_convert_updata()
                            entry_name[1][i].delete(0, 'end')
                            entry_name[1][i].insert(0, num)
                            kw={'two_'+str(i+1):num}
                            configuration('set', name, kw)                 # 上，强度值-1
                    except Exception as e:
                        if '0x015201：' not in config['ERROR_LOG']:
                            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x015201：' + str(e) + '\n'
                        print('0x015201:ERROR!',e)


                def canvas_content_two_button_down_count(i=i):
                    try:
                        if entry_name[1][i]['state'] != 'disabled':
                            num = int(entry_name[1][i].get())+1
                            configuration_strong[1][i] = num
                            configuration_strong_updata()
                            strong_convert_updata()
                            entry_name[1][i].delete(0, 'end')
                            entry_name[1][i].insert(0, num)
                            kw={'two_'+str(i+1):num}
                            configuration('set', name, kw)                 # 下，强度值+1
                    except Exception as e:
                        if '0x015202：' not in config['ERROR_LOG']:
                            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x015202：' + str(e) + '\n'
                        print('0x015202:ERROR!',e)


                def canvas_content_two_button_left_count(i=i):
                    try:
                        if entry_name[0][i]['state'] != 'disabled':
                            num = int(entry_name[0][i].get())-1
                            configuration_strong[0][i] = num
                            configuration_strong_updata()
                            strong_convert_updata()
                            entry_name[0][i].delete(0, 'end')
                            entry_name[0][i].insert(0, num)
                            kw={'one_'+str(i+1):num}
                            configuration('set', name, kw)                 # 左，强度值-1
                    except Exception as e:
                        if '0x015203：' not in config['ERROR_LOG']:
                            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x015203：' + str(e) + '\n'
                        print('0x015203:ERROR!',e)


                def canvas_content_two_button_right_count(i=i):
                    try:
                        if entry_name[0][i]['state'] != 'disabled':
                            num = int(entry_name[0][i].get())+1
                            configuration_strong[0][i] = num
                            configuration_strong_updata()
                            strong_convert_updata()
                            entry_name[0][i].delete(0, 'end')
                            entry_name[0][i].insert(0, num)
                            kw={'one_'+str(i+1):num}
                            configuration('set', name, kw)                 # 右，强度值+1
                    except Exception as e:
                        if '0x015204：' not in config['ERROR_LOG']:
                            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x015204：' + str(e) + '\n'
                        print('0x015204:ERROR!',e)


                len_configuration_all = len(configuration_all)
                if len_configuration_all < i+5:
                    range_num = (i+5) - len_configuration_all
                    for s in range(range_num):
                        index = s+len_configuration_all-5
                        configuration_all.append('第{}段:0,0'.format(index+1))
                        entry_name[0][index].config(state='normal')
                        entry_name[1][index].config(state='normal')
                        entry_name[0][index].delete(0, 'end')
                        entry_name[1][index].delete(0, 'end')
                        entry_name[0][index].insert(0, 0)
                        entry_name[1][index].insert(0, 0)
                if len(configuration_all) == i+5:
                    configuration_all.append('第{}段:0,0'.format(i+1))
                    entry_name[0][-1].config(state='normal')
                    entry_name[1][-1].config(state='normal')
                    entry_name[0][-1].delete(0, 'end')
                    entry_name[1][-1].delete(0, 'end')
                    entry_name[0][-1].insert(0, 0)
                    entry_name[1][-1].insert(0, 0)
                if len(label_name) < end_num:
                    if len(label_name) < i+1:
                        label_name.append('label')
                        entry_name[0].append('entry_name')
                        entry_name[1].append('entry_name')
                        btn_name[0].append('btn_name')
                        btn_name[1].append('btn_name')
                        btn_name[2].append('btn_name')
                        btn_name[3].append('btn_name')
                        label_name[i] = tk.Label(canvas_content_two,                   # 挂在内容区域二上
                                            text='第{}段：'.format(i+1),               # 显示文本，第i段”
                                            bg=config['UI_BG'],                        # 背景颜色
                                            fg=config['UI_FG'],                        # 前景颜色
                                            font=('宋体', 11)                          # 字体、字号设置
                                            )
                        entry_name[0][i] = tk.Entry(canvas_content_two, bd=0, bg=config['ENTRY_BG'], fg=config['ENTRY_FG'],
                                               selectbackground='#556677', selectforeground='white',
                                               font=('宋体', 11), justify='center',
                                               disabledbackground=config['ENTRY_DISABLED_BG'], disabledforeground=config['ENTRY_DISABLED_FG'])
                        entry_name[1][i] = tk.Entry(canvas_content_two, bd=0, bg=config['ENTRY_BG'], fg=config['ENTRY_FG'],
                                               selectbackground='#556677', selectforeground='white',
                                               font=('宋体', 11), justify='center',
                                               disabledbackground=config['ENTRY_DISABLED_BG'], disabledforeground=config['ENTRY_DISABLED_FG'])
                        btn_name[0][i] = tk.Button(canvas_content_two, image=up_png, bd=1, bg=config['UI_BG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], width=16, height=16, takefocus=False, relief='flat', overrelief='raised', repeatdelay=250, repeatinterval=16, command=canvas_content_two_button_up_count)
                        btn_name[1][i] = tk.Button(canvas_content_two, image=down_png, bd=1, bg=config['UI_BG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], width=16, height=16, takefocus=False, relief='flat', overrelief='raised', repeatdelay=250, repeatinterval=16, command=canvas_content_two_button_down_count)
                        btn_name[2][i] = tk.Button(canvas_content_two, image=left_png, bd=1, bg=config['UI_BG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], width=16, height=16, takefocus=False, relief='flat', overrelief='raised', repeatdelay=250, repeatinterval=16, command=canvas_content_two_button_left_count)
                        btn_name[3][i] = tk.Button(canvas_content_two, image=right_png, bd=1, bg=config['UI_BG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], width=16, height=16, takefocus=False, relief='flat', overrelief='raised', repeatdelay=250, repeatinterval=16, command=canvas_content_two_button_right_count)
                        label_window=canvas_content_two.create_window((0, i*18),                             # 像素坐标
                                                                      window=label_name[i],                  # 设置为画布小部件
                                                                      anchor="nw"                            # 锚点，文字贴靠方向：nw代表西北
                                                                      )                                      # 第几段标签，                   ID: 1*i
                        entry_window_left_right=canvas_content_two.create_window((121, i*18), window=entry_name[0][i],
                                                                                 width=79, height=17, anchor="nw",
                                                                                 state='normal')             # 左右 输入框，                  ID: 2*i
                        entry_window_up_down=canvas_content_two.create_window((281, i*18), window=entry_name[1][i],
                                                                              width=79, height=17, anchor="nw",
                                                                              state='normal')                # 上下 输入框，                  ID: 3*i
                        button_window_up=canvas_content_two.create_window((260, i*18), window=btn_name[0][i], anchor="nw")         # 按钮 ↑，  ID: 6*i
                        button_window_down=canvas_content_two.create_window((361, i*18), window=btn_name[1][i], anchor='nw')       # 按钮 ↓，  ID: 7*i
                        button_window_left=canvas_content_two.create_window((100, i*18), window=btn_name[2][i], anchor="nw")       # 按钮 ←，  ID: 8*i
                        button_window_right=canvas_content_two.create_window((201, i*18), window=btn_name[3][i], anchor='nw')      # 按钮 →，  ID: 9*i
                x = configuration_all[i+5].split(':')[1].split(',')[0]
                y = configuration_all[i+5].split(':')[1].split(',')[1]
                entry_name[0][i].config(state='normal')
                entry_name[1][i].config(state='normal')
                entry_name[0][i].delete(0, 'end')
                entry_name[1][i].delete(0, 'end')
                entry_name[0][i].insert(0, x)                           # 将配置缓存中的数据写入文本框
                entry_name[1][i].insert(0, y)
            with open('./配置文件/{}.txt'.format(name), 'w', encoding='utf-8') as f:                          # 修改配置文件的强度值
                f.write(str(configuration_all).replace("', '", "\n").replace("['", "").replace("']", ""))
            canvas_content_two_widget_config()
        except Exception as e:
            if '0x0152：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0152：' + str(e) + '\n'
            print('0x0152:ERROR!',e)


    def canvas_content_two_widget_config():                    # 给画布区域二的组件添加功能
        try:
            nonlocal configuration_all
            for i in range(int(box_num)):
                def canvas_entry_FocusIn(event, i=i):                   # 输入框得到焦点 背景变色  i=i可以强制早期绑定i，将其用作默认参数
                    try:
                        focus_entry_index=str(event.widget).split('.!canvas2.!frame.!canvas.!entry')[1]
                        if focus_entry_index=='':
                            entry_name[0][i].config(bg=config['ENTRY_FOCUSIN_BG'])
                        elif int(focus_entry_index)%2==1:
                            entry_name[0][i].config(bg=config['ENTRY_FOCUSIN_BG'])
                        elif int(focus_entry_index)%2==0:
                            entry_name[1][i].config(bg=config['ENTRY_FOCUSIN_BG'])
                    except Exception as e:
                        if '0x015301：' not in config['ERROR_LOG']:
                            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x015301：' + str(e) + '\n'
                        print('0x015301:ERROR!',e)


                def canvas_entry_FocusOut(event, i=i):                  # 输入框失去焦点 还原背景色
                    try:
                        focus_entry_index=str(event.widget).split('.!canvas2.!frame.!canvas.!entry')[1]
                        num = 0
                        if focus_entry_index=='':
                            entry_name[0][i].config(bg=config['ENTRY_BG'])
                            try:
                                if int(entry_name[0][i].get()):
                                    num = int(entry_name[0][i].get())
                                else:
                                    num = 0
                            except Exception as e:
                                if '0x015302：' not in config['ERROR_LOG']:
                                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x015302：' + str(e) + '\n'
                                num = 0
                            configuration_strong[0][i] = num
                            configuration_strong_updata()
                            strong_convert_updata()
                            entry_name[0][i].delete(0, 'end')
                            entry_name[0][i].insert(0, num)
                            kw={'one_'+str(i+1):num}
                            configuration('set', config['CONFIGURATION_NAME'], kw)                 # 修改强度值
                        elif int(focus_entry_index)%2==1:
                            entry_name[0][i].config(bg=config['ENTRY_BG'])
                            try:
                                if int(entry_name[0][i].get()):
                                    num = int(entry_name[0][i].get())
                                else:
                                    num = 0
                            except Exception as e:
                                if '0x015303：' not in config['ERROR_LOG']:
                                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x015303：' + str(e) + '\n'
                                num = 0
                            configuration_strong[0][i] = num
                            configuration_strong_updata()
                            strong_convert_updata()
                            entry_name[0][i].delete(0, 'end')
                            entry_name[0][i].insert(0, num)
                            kw={'one_'+str(i+1):num}
                            configuration('set', config['CONFIGURATION_NAME'], kw)                 # 修改强度值

                        elif int(focus_entry_index)%2==0:
                            entry_name[1][i].config(bg=config['ENTRY_BG'])
                            try:
                                if int(entry_name[1][i].get()):
                                    num = int(entry_name[1][i].get())
                                else:
                                    num = 0
                            except Exception as e:
                                if '0x015304：' not in config['ERROR_LOG']:
                                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x015304：' + str(e) + '\n'
                                num = 0
                            configuration_strong[1][i] = num
                            configuration_strong_updata()
                            strong_convert_updata()
                            entry_name[1][i].delete(0, 'end')
                            entry_name[1][i].insert(0, num)
                            kw={'two_'+str(i+1):num}
                            configuration('set', config['CONFIGURATION_NAME'], kw)                 # 修改强度值
                    except Exception as e:
                        if '0x015305：' not in config['ERROR_LOG']:
                            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x015305：' + str(e) + '\n'
                        print('0x015305:ERROR!',e)


                def canvas_entry_return(event, i=i):
                    try:
                        label_name[i].focus_set()
                        canvas_entry_FocusOut(event, i=i)
                    except Exception as e:
                        if '0x015306：' not in config['ERROR_LOG']:
                            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x015306：' + str(e) + '\n'
                        print('0x015306:ERROR!',e)


                def canvas_content_two_button_press(event, i=i):
                    try:
                        button_index=str(event.widget).split('.!canvas2.!frame.!canvas.!button')[1]
                        if button_index=='':
                            entry_name[1][i].config(bg=config['ENTRY_FOCUSIN_BG'])
                        elif int(button_index)%4==0:                # 右+1
                            entry_name[0][i].config(bg=config['ENTRY_FOCUSIN_BG'])
                        elif int(button_index)%4==1:                # 上-1
                            entry_name[1][i].config(bg=config['ENTRY_FOCUSIN_BG'])
                        elif int(button_index)%4==2:                # 下+1
                            entry_name[1][i].config(bg=config['ENTRY_FOCUSIN_BG'])
                        elif int(button_index)%4==3:                # 左-1
                            entry_name[0][i].config(bg=config['ENTRY_FOCUSIN_BG'])
                    except Exception as e:
                        if '0x015307：' not in config['ERROR_LOG']:
                            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x015307：' + str(e) + '\n'
                        print('0x015307:ERROR!',e)


                def canvas_content_two_button_Release(event, i=i):
                    try:
                        button_index=str(event.widget).split('.!canvas2.!frame.!canvas.!button')[1]
                        if button_index=='':
                            entry_name[1][i].config(bg=config['ENTRY_BG'])
                        elif int(button_index)%4==0:                # 右+1
                            entry_name[0][i].config(bg=config['ENTRY_BG'])
                        elif int(button_index)%4==1:                # 上-1
                            entry_name[1][i].config(bg=config['ENTRY_BG'])
                        elif int(button_index)%4==2:                # 下+1
                            entry_name[1][i].config(bg=config['ENTRY_BG'])
                        elif int(button_index)%4==3:                # 左-1
                            entry_name[0][i].config(bg=config['ENTRY_BG'])
                    except Exception as e:
                        if '0x015308：' not in config['ERROR_LOG']:
                            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x015308：' + str(e) + '\n'
                        print('0x015308:ERROR!',e)


                entry_name[0][i].bind('<FocusIn>', canvas_entry_FocusIn)            # 绑定焦点变色功能
                entry_name[1][i].bind('<FocusIn>', canvas_entry_FocusIn)
                entry_name[0][i].bind('<FocusOut>', canvas_entry_FocusOut)
                entry_name[1][i].bind('<FocusOut>', canvas_entry_FocusOut)
                entry_name[0][i].bind('<Return>', canvas_entry_return)
                entry_name[1][i].bind('<Return>', canvas_entry_return)
                label_name[i].bind("<MouseWheel>", mouse_wheel)                     # 给canvas_content_two所有组件绑定滚轮控制滚动条功能
                entry_name[0][i].bind("<MouseWheel>", mouse_wheel)
                entry_name[1][i].bind("<MouseWheel>", mouse_wheel)
                btn_name[0][i].bind("<MouseWheel>", mouse_wheel)
                btn_name[1][i].bind("<MouseWheel>", mouse_wheel)
                btn_name[2][i].bind("<MouseWheel>", mouse_wheel)
                btn_name[3][i].bind("<MouseWheel>", mouse_wheel)
                btn_name[0][i].bind("<Button-1>", canvas_content_two_button_press)           # 左键按下后变背景色
                btn_name[1][i].bind("<Button-1>", canvas_content_two_button_press)
                btn_name[2][i].bind("<Button-1>", canvas_content_two_button_press)
                btn_name[3][i].bind("<Button-1>", canvas_content_two_button_press)
                btn_name[0][i].bind("<ButtonRelease-1>", canvas_content_two_button_Release)  # 左键释放后变背景色
                btn_name[1][i].bind("<ButtonRelease-1>", canvas_content_two_button_Release)
                btn_name[2][i].bind("<ButtonRelease-1>", canvas_content_two_button_Release)
                btn_name[3][i].bind("<ButtonRelease-1>", canvas_content_two_button_Release)
            section_num = int(configuration_all[4].split(':')[1])                            # 段数小于10，强度输入框状态、背景色修改
            if section_num < 10:
                for i in range(section_num, 10):
                    entry_name[0][i].config(state='disabled')
                    entry_name[1][i].config(state='disabled')
        except Exception as e:
            if '0x0153：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0153：' + str(e) + '\n'
            print('0x0153:ERROR!',e)


    def get_mouse_acceleration():
        # 获取是否勾选提升鼠标精确度 勾选为1 不勾选为None
        try:
            p_epp = ctypes.c_void_p()
            ctypes.windll.user32.SystemParametersInfoA(0x0003, 0, ctypes.pointer(p_epp), 0)
            epp_value = p_epp.value
            return epp_value
        except:
            return None


    def get_mouse_speed():
        # 获取鼠标灵敏度
        try:
            p_mouse_speed = ctypes.c_void_p()
            ctypes.windll.user32.SystemParametersInfoA(0x0070, 0, ctypes.pointer(p_mouse_speed), 0)
            mouseSpeed = int(p_mouse_speed.value)
            if mouseSpeed:
                return mouseSpeed
            else:
                return 10
        except:
            return 10


    def set_mouse_acceleration(arg):
        # 设置是否勾选提升鼠标精确度
        try:
            if arg: # 勾选
                EPP_ON = [1,1,1]
                ctypes.windll.user32.SystemParametersInfoA(0x0004, 0, (ctypes.c_int * 3)(*EPP_ON), 0)
            else: # 取消勾选
                EPP_OFF = [0,0,0]
                ctypes.windll.user32.SystemParametersInfoA(0x0004, 0, (ctypes.c_int * 3)(*EPP_OFF), 0)
        except:
            pass


    def set_mouse_speed(mouseSpeed):
        # 设置鼠标灵敏度为10档 范围在1 - 20之间
        try:
            ctypes.windll.user32.SystemParametersInfoA(0x0071, 0, mouseSpeed, 0)
        except:
            pass


    try:
        ### 控件 创建 ###
        get_hotkey()                                                               # 获取快捷键设置数据
        ui = tk.Tk()                                                               # 初始化窗口
        canvas_top = tk.Canvas(ui, bg='#000')                                      # 创建顶部区域画布
        canvas_content_one = tk.Canvas(ui, bg=config['UI_BG'])                     # 创建内容区域一画布, 放置时间框、段数框
        frame_one = tk.Frame(canvas_content_one, bg=config['UI_BG'])               # 在内容区域一上设置容器，用来装强度设置区域
        frame_func = tk.Frame(ui, bg=config['UI_BG'], width=398, height=323)       # 创建 功能 页面 框架
        frame_advanced = tk.Frame(ui, bg=config['UI_BG'], width=398, height=323)   # 创建 设置 页面
        frame_about = tk.Frame(ui, bg=config['UI_BG'], width=398, height=323)      # 创建 公告 页面
        frame_drive = tk.Frame(ui, bg=config['UI_BG'], width=398, height=323)      # 创建 驱动 页面
        canvas_func = tk.Canvas(frame_func, bg=config['UI_BG'])                    # 创建 功能 页面 画布
        canvas_advanced = tk.Canvas(frame_advanced, bg=config['UI_BG'])            # 创建 设置 页面 画布
        canvas_about = tk.Canvas(frame_about, bg=config['UI_BG'])                  # 创建 公告 页面 画布
        canvas_drive = tk.Canvas(frame_drive, bg=config['UI_BG'])                  # 创建 驱动 页面 画布
        scrollbar = tk.Scrollbar(frame_one)                                        # 创建 弹道页面的 垂直滚动条
        scrollbar_two = tk.Scrollbar(frame_advanced)                               # 创建 设置页面的 垂直滚动条
        canvas_content_two = tk.Canvas(frame_one, bg=config['UI_BG'])              # 创建内容区域二画布, 放置强度框，强度设置区域
        configuration_all = configuration('get', config['CONFIGURATION_NAME'])        # 获取配置
        box_num, scroll_height = box_num_check(configuration_all[4].split(':')[1])    # 对输入的段数进行检查，并计算scroll_height值
        favicon = tk.PhotoImage(file='./image/F19x17.png')  # 创建软件图标
        if config['STYLE_CHANGE'] == '暗':
            up_png = tk.PhotoImage(file='./image/anUp.png')              # 创建图片 上
            down_png = tk.PhotoImage(file='./image/anDown.png')          # 创建图片 下
            left_png = tk.PhotoImage(file='./image/anLeft.png')          # 创建图片 左
            right_png = tk.PhotoImage(file='./image/anRight.png')        # 创建图片 右
        elif config['STYLE_CHANGE'] == '明':
            up_png = tk.PhotoImage(file='./image/mingUp.png')              # 创建图片 上
            down_png = tk.PhotoImage(file='./image/mingDown.png')          # 创建图片 下
            left_png = tk.PhotoImage(file='./image/mingLeft.png')          # 创建图片 左
            right_png = tk.PhotoImage(file='./image/mingRight.png')        # 创建图片 右
        create_canvas_content_two_widget('new', config['CONFIGURATION_NAME'])         # 创建‘第几段’标签、强度输入框和控制按钮
        btn1=tk.Button(ui)                         # 最小化按钮
        btn2=tk.Button(ui)                         # 退出按钮
        btn3=tk.Button(ui)                         # 配置按钮
        btn4=tk.Button(ui)                         # 功能按钮
        btn5=tk.Button(ui)                         # 高级按钮
        btn6=tk.Button(ui)                         # 关于按钮
        btn7=tk.Button(canvas_content_one)                         # 配置页面 模式切换按钮
        btn8=tk.Button(canvas_content_one)                         # 配置页面 重置按钮
        btn9=tk.Button(canvas_content_one)                         # 左
        btn10=tk.Button(canvas_content_one)                        # 右
        btn11=tk.Button(canvas_content_one)                        # 上
        btn12=tk.Button(canvas_content_one)                        # 下
        btn13=tk.Button(canvas_func)                               # 功能页面 鼠标加速度按钮
        btn26=tk.Button(canvas_advanced)                           # 设置页面 按键自定义 '宏开/关：'
        btn27=tk.Button(canvas_advanced)                           # 设置页面 按键自定义 '主界面显/隐：'
        btn28=tk.Button(canvas_advanced)                           # 设置页面 按键自定义 '状态栏显/隐：'
        btn30=tk.Button(canvas_about)                              # 关于页面 检查版本更新按钮
        btn36=tk.Button(canvas_advanced)                           # 设置页面 连点器开关
        btn37=tk.Button(canvas_advanced)                           # 按键自定义 连点器'触发热键'
        btn38=tk.Button(canvas_advanced)                           # 设置页面 音效开关
        btn39=tk.Button(canvas_advanced)                           # 设置页面 极限点击开关
        btn40=tk.Button(canvas_advanced)                           # 设置页面 风格切换按钮
        btn41=tk.Button(canvas_advanced)                           # 设置页面 开机自启开关
        btn42=tk.Button(canvas_advanced)                           # 设置页面 左右键触发宏
        btn43=tk.Button(canvas_advanced)                           # 设置页面 配置一 热键
        btn44=tk.Button(canvas_advanced)                           # 设置页面 配置二 热键
        btn45=tk.Button(canvas_advanced)                           # 设置页面 配置三 热键
        btn46=tk.Button(canvas_advanced)                           # 设置页面 配置四 热键
        btn47=tk.Button(canvas_advanced)                           # 设置页面 配置五 热键
        btn48=tk.Button(canvas_advanced)                           # 设置页面 配置六 热键
        btn49=tk.Button(canvas_advanced)                           # 设置页面 配置七 热键
        btn50=tk.Button(canvas_advanced)                           # 设置页面 配置八 热键
        btn51=tk.Button(canvas_advanced)                           # 设置页面 配置九 热键
        btn52=tk.Button(canvas_advanced)                           # 设置页面 配置十 热键
        btn53=tk.Button(canvas_advanced)                           # 设置页面 配置十一 热键
        btn54=tk.Button(canvas_advanced)                           # 设置页面 配置十二 热键
        btn55=tk.Button(ui)                                        # 驱动按钮
        btn56=tk.Button(canvas_drive)                              # 驱动页面 SendInput驱动按钮
        btn57=tk.Button(canvas_drive)                              # 驱动页面 罗技驱动按钮
        label_1=tk.Label(ui)                                       # 文字 图标
        label_2=tk.Label(ui)                                       # 文字 图标旁的‘彩手’
        label_3=tk.Label(ui)                                       # 文字 配置名称
        label_4=tk.Label(canvas_content_one)                       # 文字 ‘时间：’
        label_5=tk.Label(canvas_content_one)                       # 文字 ‘毫秒’
        label_6=tk.Label(canvas_content_one)                       # 文字 ‘段数：’
        label_7=tk.Label(canvas_content_one)                       # 文字 ‘段’
        label_8=tk.Label(canvas_func)                              # 文字 鼠标灵敏度说明文字
        label_9=tk.Label(canvas_func)                              # 文字 鼠标灵敏度刻度值显示
        label_32=tk.Label(canvas_advanced)                         # 文字 '宏开/关：'
        label_33=tk.Label(canvas_advanced)                         # 文字 '主界面显/隐：'
        label_34=tk.Label(canvas_advanced)                         # 文字 '状态栏显/隐：'
        label_35=tk.Label(canvas_advanced)                         # 文本 显示 '宏开/关：' 快捷键
        label_36=tk.Label(canvas_advanced)                         # 文本 显示 '主界面显/隐：' 快捷键
        label_37=tk.Label(canvas_advanced)                         # 文本 显示 '状态栏显/隐：' 快捷键
        label_38=tk.Label(canvas_about)                            # 文字 '使用教程'
        label_39=tk.Label(canvas_about)                            # 文本 '版本号：1.47'
        label_40=tk.Label(canvas_about)                            # 文本 '开源地址：https://github.com/1C1T/CaiShou'
        label_42=tk.Label(canvas_about)                            # 文本 'QQ交流群：928286446'
        label_49=tk.Label(canvas_advanced)                         # 文字 '连点器'
        label_50=tk.Label(canvas_advanced)                         # 文字 连点器 '间隔：'
        label_51=tk.Label(canvas_advanced)                         # 文字 连点器 '毫秒'
        label_52=tk.Label(canvas_advanced)                         # 文字 连点器 '触发热键：'
        label_53=tk.Label(canvas_advanced)                         # 文字 显示 '触发热键' 快捷键
        label_54=tk.Label(canvas_advanced)                         # 文字 '音效'
        label_63=tk.Label(canvas_about)                            # 文字 '永久免费'
        label_64=tk.Label(canvas_advanced)                         # 文字 '极限点击'
        label_69=tk.Label(canvas_advanced)                         # 设置页面 配置一 显示当前热键
        label_70=tk.Label(canvas_advanced)                         # 设置页面 配置二 显示当前热键
        label_71=tk.Label(canvas_advanced)                         # 设置页面 配置三 显示当前热键
        label_72=tk.Label(canvas_advanced)                         # 设置页面 配置四 显示当前热键
        label_73=tk.Label(canvas_advanced)                         # 设置页面 配置五 显示当前热键
        label_74=tk.Label(canvas_advanced)                         # 设置页面 配置六 显示当前热键
        label_75=tk.Label(canvas_advanced)                         # 设置页面 配置七 显示当前热键
        label_76=tk.Label(canvas_advanced)                         # 设置页面 配置八 显示当前热键
        label_77=tk.Label(canvas_advanced)                         # 设置页面 配置九 显示当前热键
        label_78=tk.Label(canvas_advanced)                         # 设置页面 配置十 显示当前热键
        label_79=tk.Label(canvas_advanced)                         # 设置页面 配置十一 显示当前热键
        label_80=tk.Label(canvas_advanced)                         # 设置页面 配置十二 显示当前热键
        label_81=tk.Label(canvas_advanced)                         # 设置页面 文本 '配置一'
        label_82=tk.Label(canvas_advanced)                         # 设置页面 文本 '配置二'
        label_83=tk.Label(canvas_advanced)                         # 设置页面 文本 '配置三'
        label_84=tk.Label(canvas_advanced)                         # 设置页面 文本 '配置四'
        label_85=tk.Label(canvas_advanced)                         # 设置页面 文本 '配置五'
        label_86=tk.Label(canvas_advanced)                         # 设置页面 文本 '配置六'
        label_87=tk.Label(canvas_advanced)                         # 设置页面 文本 '配置七'
        label_88=tk.Label(canvas_advanced)                         # 设置页面 文本 '配置八'
        label_89=tk.Label(canvas_advanced)                         # 设置页面 文本 '配置九'
        label_90=tk.Label(canvas_advanced)                         # 设置页面 文本 '配置十'
        label_91=tk.Label(canvas_advanced)                         # 设置页面 文本 '配置十一'
        label_92=tk.Label(canvas_advanced)                         # 设置页面 文本 '配置十二'
        label_93=tk.Label(canvas_func)                             # 功能页面 文本 '弹道每'
        label_94=tk.Label(canvas_func)                             # 功能页面 文本 '至'
        label_95=tk.Label(canvas_func)                             # 功能页面 文本 '毫秒随机执行'
        label_96=tk.Label(canvas_func)                             # 功能页面 文本 'X轴在'
        label_97=tk.Label(canvas_func)                             # 功能页面 文本 '至'
        label_98=tk.Label(canvas_func)                             # 功能页面 文本 '之间随机偏移'
        label_99=tk.Label(canvas_func)                             # 功能页面 文本 'Y轴在'
        label_100=tk.Label(canvas_func)                            # 功能页面 文本 '至'
        label_101=tk.Label(canvas_func)                            # 功能页面 文本 '之间随机偏移'
        entry_1=tk.Entry(canvas_content_one)                       # 创建填写限制时间的文本框
        entry_2=tk.Entry(canvas_content_one)                       # 创建填写段数的文本框
        entry_3=tk.Entry(canvas_advanced)                          # 创建填写连点器间隔时间的文本框
        entry_4=tk.Entry(canvas_func)                              # 功能页面 文本框 首 随机毫秒
        entry_5=tk.Entry(canvas_func)                              # 功能页面 文本框 尾 随机毫秒
        entry_6=tk.Entry(canvas_func)                              # 功能页面 文本框 首 X轴随机偏移
        entry_7=tk.Entry(canvas_func)                              # 功能页面 文本框 尾 X轴随机毫秒
        entry_8=tk.Entry(canvas_func)                              # 功能页面 文本框 首 Y轴随机偏移
        entry_9=tk.Entry(canvas_func)                              # 功能页面 文本框 尾 Y轴随机毫秒
        scale_1=tk.Scale(canvas_func)                              # 功能页面 鼠标速度刻度条


        ### 控件 配置 ###
        ui.overrideredirect(True)                                   # 去掉windows边框
        ui.attributes('-topmost', True)                             # 在所有应用中置前
        config['DESKTOP_RESOLUTION'][0] = ui.winfo_screenwidth()    # 屏幕横向分辨率
        config['DESKTOP_RESOLUTION'][1] = ui.winfo_screenheight()   # 屏幕纵向分辨率
        ui.geometry('400x360+{}+{}'.format(int((config['DESKTOP_RESOLUTION'][0]-400)/2),
                                           int((config['DESKTOP_RESOLUTION'][1]-360)/2))
                    )                                               # 设置窗口尺寸，并使窗口屏幕置中
        ui.resizable(width=False, height=False)                     # 设置窗口的宽、高：不可变
        canvas_top.config(highlightthickness=0)                     # 去canvas_top白边
        canvas_content_one.config(highlightthickness=0)
        canvas_func.config(highlightthickness=0)
        canvas_about.config(highlightthickness=0)
        canvas_drive.config(highlightthickness=0)
        canvas_content_two.config(highlightthickness=0,             # 去canvas_content_two白边
                                  yscrollcommand=scrollbar.set,     # 滚动条关联到scrollbar
                                  yscrollincrement=18,              # 设置滚动条步长
                                  scrollregion=(0, 0, 400, scroll_height),                  # 设置画布可以滚动的范围
                                  )
        canvas_advanced.config(highlightthickness=0,
                                  yscrollcommand=scrollbar_two.set,     # 滚动条关联到scrollbar
                                  yscrollincrement=36,              # 设置滚动条步长
                                  scrollregion=(0, 0, 400, 500),                  # 设置画布可以滚动的范围
                                  )
        canvas_content_two.bind("<MouseWheel>", mouse_wheel)        # 给画布区域二添加滚轮事件
        canvas_advanced.bind("<MouseWheel>", mouse_wheel_two)       # 给设置页面的画布添加滚轮事件
        scrollbar.config(command=canvas_content_two.yview)          # 设置垂直滚动条的函数与强度设置区域的Y轴滚动条事件绑定
        scrollbar_two.config(command=canvas_advanced.yview)        # 设置垂直滚动条的函数与强度设置区域的Y轴滚动条事件绑定
        btn1.config(text='-',                               # 显示文本
                    bg='black',                             # 背景颜色
                    fg='#1bcbeb',                           # 前景颜色
                    activebackground='steelblue',           # 活动时背景颜色
                    activeforeground='white',               # 活动时前景颜色
                    font=('微软雅黑', 11),                  # 字体、字号设置
                    cursor='hand2',                         # 鼠标停留样式
                    relief='flat',                          # 按钮样式
                    command=configuration_ui_display        # 隐藏窗口， 显示窗口为：deiconify()
                    )                                       # 最小化按钮
        btn2.config(text='x', bg='black', fg='#1bcbeb', activebackground='darkred', activeforeground='white', font=('微软雅黑', 11), cursor='hand2', relief='flat', command=kill_all_process)            # 退出
        btn3.config(text='弹道', bg=config['UI_BG'], fg=config['UI_FG'], activebackground=config['BTN_MENU_ACTIVE_BG'], activeforeground=config['BTN_MENU_ACTIVE_FG'], font=('宋体', 11), cursor='hand2', relief='flat', command=btn3_command)     # '弹道'
        btn4.config(text='功能', bg=config['UI_BG'], fg=config['UI_FG'], activebackground=config['BTN_MENU_ACTIVE_BG'], activeforeground=config['BTN_MENU_ACTIVE_FG'], font=('宋体', 11), cursor='hand2', relief='flat', command=btn4_command)       # '功能'
        btn5.config(text='设置', bg=config['UI_BG'], fg=config['UI_FG'], activebackground=config['BTN_MENU_ACTIVE_BG'], activeforeground=config['BTN_MENU_ACTIVE_FG'], font=('宋体', 11), cursor='hand2', relief='flat', command=btn5_command)       # '设置'
        btn6.config(text='关于', bg=config['UI_BG'], fg=config['UI_FG'], activebackground=config['BTN_MENU_ACTIVE_BG'], activeforeground=config['BTN_MENU_ACTIVE_FG'], font=('宋体', 11), cursor='hand2', relief='flat', command=btn6_command)       # '关于'
        btn55.config(text='驱动', bg=config['UI_BG'], fg=config['UI_FG'], activebackground=config['BTN_MENU_ACTIVE_BG'], activeforeground=config['BTN_MENU_ACTIVE_FG'], font=('宋体', 11), cursor='hand2', relief='flat', command=btn55_command)       # '驱动'
        btn7.config(text='模式'+str(configuration_mode), font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'],cursor='hand2', activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised', command=btn7_command)                                # 配置页面 模式切换按钮
        btn8.config(text='重置', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], cursor='hand2', activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised', command=btn8_command)                                       # 配置页面 重置按钮
        btn9.config(text='左', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised', repeatdelay=250, repeatinterval=16, command=btn9_command)                 # 左
        btn10.config(text='右', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised', repeatdelay=250, repeatinterval=16, command=btn10_command)                 # 右
        btn11.config(text='上', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised', repeatdelay=250, repeatinterval=16, command=btn11_command)                 # 上
        btn12.config(text='下', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised', repeatdelay=250, repeatinterval=16, command=btn12_command)                 # 下
        btn13.config(text='鼠标加速度', bg=config['UI_BG_2'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], font=('宋体', 11), cursor='hand2', relief='flat', command=btn13_command)                                        # 鼠标加速度开关
        btn36.config(text='连点器', bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], font=('宋体', 11), cursor='hand2', relief='flat', command=btn36_command)                                        # 连点器开关
        btn38.config(text='音效提示', bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], font=('宋体', 11), cursor='hand2', relief='flat', command=btn38_command)                                        # 音效提示开关
        btn39.config(text='极限点击', bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], font=('宋体', 11), cursor='hand2', relief='flat', command=btn39_command)                                        # 极限点击开关
        btn40.config(text='风格切换', bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], font=('宋体', 11), cursor='hand2', relief='flat', overrelief='raised', command=btn40_command)                   # 风格切换按钮
        btn41.config(text='开机自启', bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], font=('宋体', 11), cursor='hand2', relief='flat', command=btn41_command)                                        # 开机自启开关
        btn42.config(text='左右键触发宏', bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], font=('宋体', 11), cursor='hand2', relief='flat', command=btn42_command)                                        # 左右键触发宏
        btn56.config(text='SendInput\n\nWindows系统自带', bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], font=('宋体', 11), cursor='hand2', relief='raised', command=btn56_command)               # SendInput按钮
        btn57.config(text='罗技\n\n需装 LGS 或 GHUB\n\n具体请看教程', bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], font=('宋体', 11), cursor='hand2', relief='raised', command=btn57_command)          # 罗技按钮
        #初始化按钮
        btn13_command(1)            # 功能页面 鼠标加速度开关
        btn36_command(1)            # 设置页面 连点器开关
        btn38_command(1)            # 音效提示开关
        btn39_command(1)            # 极限点击开关
        btn41_command(1)            # 开机自启开关
        btn42_command(1)            # 左右键触发宏
        btn56_command(1)            # SendInput按钮
        btn57_command(1)            # 罗技按钮
        btn26.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 按键自定义 '宏开/关：'
        btn27.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 按键自定义 '主界面显/隐：'
        btn28.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 按键自定义 '状态栏显/隐：'
        btn30.config(text='检查版本更新', font=('宋体', 11), bd=3, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], cursor='hand2', activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], disabledforeground=config['UI_FG'], takefocus=False, relief='raised', overrelief='raised', command=btn30_command)                              # 关于页面 检查版本更新按钮
        btn37.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 按键自定义 连点器'触发热键' 按键自定义
        
        btn43.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 设置页面 配置一 热键
        btn44.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 设置页面 配置二 热键
        btn45.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 设置页面 配置三 热键
        btn46.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 设置页面 配置四 热键
        btn47.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 设置页面 配置五 热键
        btn48.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 设置页面 配置六 热键
        btn49.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 设置页面 配置七 热键
        btn50.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 设置页面 配置八 热键
        btn51.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 设置页面 配置九 热键
        btn52.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 设置页面 配置十 热键
        btn53.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 设置页面 配置十一 热键
        btn54.config(text='自定义', font=('宋体', 11), bd=1, bg=config['UI_BG'], fg=config['BTN_FUNC_FG'], activebackground=config['BTN_FUNC_ACTIVE_BG'], activeforeground=config['BTN_FUNC_ACTIVE_FG'], takefocus=False, relief='flat', overrelief='raised')                           # 设置页面 配置十二 热键
        
        
        label_1.config(image=favicon, bg='black', bd=0, cursor='fleur')
        label_2.config(text='彩手', bg='black', fg='#1bcbeb', font=('微软雅黑', 9), cursor='fleur')
        label_3.config(text=configuration_another_name, bg='black', fg='#1bcbeb', font=('宋体', 11), cursor='fleur')
        label_4.config(text='时间：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_5.config(text='毫秒', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_6.config(text='段数：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_7.config(text='段', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        key_dict = {
             513:'鼠标左键',516:'鼠标右键',519:'鼠标中键', 523:'鼠标侧键',
             514:'鼠标左键',517:'鼠标右键',520:'鼠标中键', 524:'鼠标侧键',
             
             1:'鼠标左键',                 12:'清除键',                21:'输入法韩文模式',
             2:'鼠标右键',                 13:'回车键',                23:'IME Junja模式',
             3:'控制中断处理',             16:'转移键',                24:'输入法最终模式',
             4:'鼠标中键',                 17:'控制键',                25:'输入法汉字模式',
             5:'X1鼠标按钮',               18:'Alt',                   '25*':'输入法汉字模式',
             6:'X2鼠标按钮',               19:'中断暂停键',            27:'Esc',
             8:'退格键',                   20:'大写键',                28:'输入法转换',
             9:'Tab',                      21:'IME Hanguel模式',       29:'输入法未转换',
             
             0:'输入法接受',               39:'右方向键',              48:'0',
             31:'IME 模式更改请求',        40:'下方向键',              49:'1',
             32:'空格键',                  41:'选择键',                50:'2',
             33:'PgUp',                    42:'打印键',                51:'3',
             34:'PgDown',                  43:'执行键',                52:'4',
             35:'End',                     44:'快照键',                53:'5',
             36:'Home',                    45:'Insert',                54:'6',
             37:'左方向键',                46:'Delete',                55:'7',
             38:'上方向键',                47:'帮助键',                56:'8',
             
             57:'9',                       73:'I',                     82:'R',
             65:'A',                       74:'J',                     83:'S',
             66:'B',                       75:'K',                     84:'T',
             67:'C',                       76:'L',                     85:'U',
             68:'D',                       77:'M',                     86:'V',
             69:'E',                       78:'N',                     87:'W',
             70:'F',                       79:'O',                     88:'X',
             71:'G',                       80:'P',                     89:'Y',
             72:'H',                       81:'Q',                     90:'Z',
             
             91:'左Windows键',             101:'数字键盘 5',             110:'数字键盘 .',          111:'数字键盘 /',
             92:'右Windows键',             102:'数字键盘 6',             112:'F1',
             93:'应用程序密钥',             103:'数字键盘 7',             113:'F2',
             95:'电脑睡眠键',               104:'数字键盘 8',             114:'F3',
             96:'数字键盘 0',               105:'数字键盘 9',             115:'F4',
             97:'数字键盘 1',               106:'数字键盘 *',             116:'F5',
             98:'数字键盘 2',               107:'数字键盘 +',             117:'F6',
             99:'数字键盘 3',               108:'数字键盘 Enter',         118:'F7',
             100:'数字键盘 4',              109:'数字键盘 -',             119:'F8',
             
             120:'F9',                     129:'F18',                  160:'左 shift',
             121:'F10',                    130:'F19',                  161:'右 shift',
             122:'F11',                    131:'F20',                  162:'左 ctrl',
             123:'F12',                    132:'F21',                  163:'右 ctrl',
             124:'F13',                    133:'F22',                  164:'左 alt',
             125:'F14',                    134:'F23',                  165:'右 alt',
             126:'F15',                    135:'F24',                  166:'浏览器返回键',
             127:'F16',                    144:'Num Lock',             167:'浏览器前进键',
             128:'F17',                    145:'屏幕滚动显示锁定键',   168:'浏览器刷新键',
             
             169:'浏览器停止键',           178:'停止媒体键',           189:'- _',
             170:'浏览器搜索键',           179:'播放/暂停媒体键',      190:'. ',
             171:'浏览器收藏夹键',         180:'开始邮件键',           191:'/ ?',
             172:'浏览器开始和主页键',     181:'选择媒体键',           192:'` ~',
             173:'音量静音键',             182:'1 键',                 219:'[ {',
             174:'降低音量键',             183:'2 键',                 220:'/ |',
             175:'提高音量键',             186:'; :',                  221:'] }',
             176:'下一曲目键',             187:'= +',                  222:"\' \"",
             177:'上一曲目键',             188:', ',                   223:'杂字符',
             
             226:'尖括号或反斜杠键',       247:'选择键',               251:'缩放键',
             231:'传递Unicode字符键',      248:'退出键',               252:'预订键',
             229:'输??入法处理键',           249:'EOF擦除键',            253:'PA1 键',
             246:'收件人键',               250:'播放键',               254:'清除键',
                    }

        label_53.config(text=key_dict.get(hotkey_clicker), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 文本 显示 '触发热键' 快捷键
        
        
        label_69.config(text=key_dict.get(hotkey_Configure_1), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 设置页面 配置一 热键 文字
        label_70.config(text=key_dict.get(hotkey_Configure_2), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 设置页面 配置二 热键 文字
        label_71.config(text=key_dict.get(hotkey_Configure_3), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 设置页面 配置三 热键 文字
        label_72.config(text=key_dict.get(hotkey_Configure_4), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 设置页面 配置四 热键 文字
        label_73.config(text=key_dict.get(hotkey_Configure_5), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 设置页面 配置五 热键 文字
        label_74.config(text=key_dict.get(hotkey_Configure_6), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 设置页面 配置六 热键 文字
        label_75.config(text=key_dict.get(hotkey_Configure_7), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 设置页面 配置七 热键 文字
        label_76.config(text=key_dict.get(hotkey_Configure_8), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 设置页面 配置八 热键 文字
        label_77.config(text=key_dict.get(hotkey_Configure_9), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 设置页面 配置九 热键 文字
        label_78.config(text=key_dict.get(hotkey_Configure_10), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 设置页面 配置十 热键 文字
        label_79.config(text=key_dict.get(hotkey_Configure_11), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 设置页面 配置十一 热键 文字
        label_80.config(text=key_dict.get(hotkey_Configure_12), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 设置页面 配置十二 热键 文字
        
        
        label_81.config(text='配置一：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_82.config(text='配置二：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_83.config(text='配置三：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_84.config(text='配置四：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_85.config(text='配置五：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_86.config(text='配置六：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_87.config(text='配置七：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_88.config(text='配置八：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_89.config(text='配置九：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_90.config(text='配置十：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_91.config(text='配置十一：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_92.config(text='配置十二：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        
        
        label_32.config(text='宏开/关：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_33.config(text='主界面显/隐：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_34.config(text='状态栏显/隐：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_49.config(text='连点器', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11), anchor="w")
        label_50.config(text='间隔：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_51.config(text='毫秒', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_52.config(text='触发热键：', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_54.config(text='音效', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11), anchor="w")
        label_63.config(text='永久免费', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_8.config(text='鼠标灵敏度 越往右拉越快 通常为10档', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_9.config(text=str(mouse_speed), bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_93.config(text='弹道每', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_94.config(text='至', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_95.config(text='毫秒随机执行', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_96.config(text='X 轴在', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_97.config(text='至', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_98.config(text='之间随机偏移', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_99.config(text='Y 轴在', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_100.config(text='至', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_101.config(text='之间随机偏移', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_64.config(text='极限点击', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11), anchor="w")
        label_35.config(text=key_dict.get(hotkey_macro_switch), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 文本 显示 '宏开/关：' 快捷键
        label_36.config(text=key_dict.get(hotkey_ui_display), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 文本 显示 '主界面显/隐：' 快捷键
        label_37.config(text=key_dict.get(hotkey_status_display), bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], font=('宋体', 11)) # 文本 显示 '状态栏显/隐：' 快捷键
        label_38.config(text='使用教程', bg=config['UI_BG'], fg=config['BTN_FUNC_CHOOSE_BG'], font=('宋体', 11), cursor='hand2')
        label_39.config(text='版本号：1.47', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        label_40.config(text='开源地址：https://github.com/1C1T/CaiShou', bg=config['UI_BG'], fg=config['BTN_FUNC_CHOOSE_BG'], font=('宋体', 11), cursor='hand2')
        label_42.config(text='QQ交流群：928286446', bg=config['UI_BG'], fg=config['UI_FG'], font=('宋体', 11))
        entry_1.config(bd=0, bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], selectbackground='#556677', 
                        selectforeground='white', font=('宋体', 11),
                       justify='center')                    # 时间输入框
        entry_2.config(bd=0, bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], selectbackground='#556677', 
                        selectforeground='white', font=('宋体', 11),
                       justify='center')                    # 段数输入框
        entry_3.config(bd=0, bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], selectbackground='#556677', 
                        selectforeground='white', font=('宋体', 11),
                       justify='center')                    # 连点器 间隔 输入框
        entry_4.config(bd=0, bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], selectbackground='#556677', 
                        selectforeground='white', font=('宋体', 11),
                       justify='center')                    # 功能页面 文本框 首 随机毫秒
        entry_5.config(bd=0, bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], selectbackground='#556677', 
                        selectforeground='white', font=('宋体', 11),
                       justify='center')                    # 功能页面 文本框 尾 随机毫秒
        entry_6.config(bd=0, bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], selectbackground='#556677', 
                        selectforeground='white', font=('宋体', 11),
                       justify='center')                    # 功能页面 文本框 首 X轴随机偏移
        entry_7.config(bd=0, bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], selectbackground='#556677', 
                        selectforeground='white', font=('宋体', 11),
                       justify='center')                    # 功能页面 文本框 尾 X轴随机毫秒
        entry_8.config(bd=0, bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], selectbackground='#556677', 
                        selectforeground='white', font=('宋体', 11),
                       justify='center')                    # 功能页面 文本框 首 Y轴随机偏移
        entry_9.config(bd=0, bg=config['ENTRY_BG'], fg=config['ENTRY_FG'], selectbackground='#556677', 
                        selectforeground='white', font=('宋体', 11),
                       justify='center')                    # 功能页面 文本框 尾 Y轴随机毫秒

        scale_1.config(from_=1, to=20, orient='horizontal', bd=0, bg=config['SCALE_BG'], troughcolor=config['BTN_FUNC_ENTER_BG'], showvalue='False', sliderrelief='flat', relief='flat', cursor='hand2', highlightbackground=config['UI_BG'], sliderlength=48, repeatinterval=100000, repeatdelay=100000, command=scale_1_command) # 鼠标灵敏度刻度条
        mouse_speed = get_mouse_speed() # 获取鼠标灵敏度
        scale_1.set(mouse_speed)
        
        btn1.bind('<Enter>', btn_enter)                     # 鼠标进入按钮范围触发事件
        btn2.bind('<Enter>', btn_enter)
        btn3.bind('<Enter>', btn_enter)
        btn4.bind('<Enter>', btn_enter)
        btn5.bind('<Enter>', btn_enter)
        btn6.bind('<Enter>', btn_enter)
        btn13.bind('<Enter>', btn_enter)
        btn36.bind('<Enter>', btn_enter)
        btn38.bind('<Enter>', btn_enter)
        btn39.bind('<Enter>', btn_enter)
        btn41.bind('<Enter>', btn_enter)
        btn42.bind('<Enter>', btn_enter)
        btn55.bind('<Enter>', btn_enter)
        btn56.bind('<Enter>', btn_enter)
        btn57.bind('<Enter>', btn_enter)
        btn1.bind('<Leave>', btn_leave)                     # 鼠标离开按钮范围触发事件
        btn2.bind('<Leave>', btn_leave)
        btn3.bind('<Leave>', btn_leave)
        btn4.bind('<Leave>', btn_leave)
        btn5.bind('<Leave>', btn_leave)
        btn6.bind('<Leave>', btn_leave)
        btn13.bind('<Leave>', btn_leave)
        btn36.bind('<Leave>', btn_leave)
        btn38.bind('<Leave>', btn_leave)
        btn39.bind('<Leave>', btn_leave)
        btn41.bind('<Leave>', btn_leave)
        btn42.bind('<Leave>', btn_leave)
        btn55.bind('<Leave>', btn_leave)
        btn56.bind('<Leave>', btn_leave)
        btn57.bind('<Leave>', btn_leave)
        btn26.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 按键自定义 '宏开/关：'
        btn27.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 按键自定义 '主界面显/隐：'
        btn28.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 按键自定义 '状态栏显/隐：'
        btn37.bind('<ButtonRelease-1>', hotkey_set)           # 按键自定义 连点器'触发热键'
        btn43.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 配置一 热键
        btn44.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 配置二 热键
        btn45.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 配置三 热键
        btn46.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 配置四 热键
        btn47.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 配置五 热键
        btn48.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 配置六 热键
        btn49.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 配置七 热键
        btn50.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 配置八 热键
        btn51.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 配置九 热键
        btn52.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 配置十 热键
        btn53.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 配置十一 热键
        btn54.bind('<ButtonRelease-1>', hotkey_set)           # 设置页面 配置十二 热键
        # 给设置页面的所有组件，绑定滚轮控制滚动条功能
        btn26.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 按键自定义 '宏开/关：'
        btn27.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 按键自定义 '主界面显/隐：'
        btn28.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 按键自定义 '状态栏显/隐：'
        btn36.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 连点器开关
        btn37.bind("<MouseWheel>", mouse_wheel_two)           # 按键自定义 连点器'触发热键'
        btn38.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 音效开关
        btn39.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 极限点击开关
        btn40.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 风格切换按钮
        btn41.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 开机自启开关
        btn42.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 左右键触发宏
        btn43.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 配置一 热键
        btn44.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 配置二 热键
        btn45.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 配置三 热键
        btn46.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 配置四 热键
        btn47.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 配置五 热键
        btn48.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 配置六 热键
        btn49.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 配置七 热键
        btn50.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 配置八 热键
        btn51.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 配置九 热键
        btn52.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 配置十 热键
        btn53.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 配置十一 热键
        btn54.bind("<MouseWheel>", mouse_wheel_two)           # 设置页面 配置十二 热键
        label_32.bind("<MouseWheel>", mouse_wheel_two)        # 文字 '宏开/关：'
        label_33.bind("<MouseWheel>", mouse_wheel_two)        # 文字 '主界面显/隐：'
        label_34.bind("<MouseWheel>", mouse_wheel_two)        # 文字 '状态栏显/隐：'
        label_35.bind("<MouseWheel>", mouse_wheel_two)        # 文本 显示 '宏开/关：' 快捷键
        label_36.bind("<MouseWheel>", mouse_wheel_two)        # 文本 显示 '主界面显/隐：' 快捷键
        label_37.bind("<MouseWheel>", mouse_wheel_two)        # 文本 显示 '状态栏显/隐：' 快捷键
        label_49.bind("<MouseWheel>", mouse_wheel_two)        # 文字 '连点器'
        label_50.bind("<MouseWheel>", mouse_wheel_two)        # 文字 连点器 '间隔：'
        label_51.bind("<MouseWheel>", mouse_wheel_two)        # 文字 连点器 '毫秒'
        label_52.bind("<MouseWheel>", mouse_wheel_two)        # 文字 连点器 '触发热键：'
        label_53.bind("<MouseWheel>", mouse_wheel_two)        # 文字 显示 '触发热键' 快捷键
        label_54.bind("<MouseWheel>", mouse_wheel_two)        # 文字 '音效'
        label_64.bind("<MouseWheel>", mouse_wheel_two)        # 文字 '极限点击'
        
        label_69.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 配置一 显示当前热键
        label_70.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 配置二 显示当前热键
        label_71.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 配置三 显示当前热键
        label_72.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 配置四 显示当前热键
        label_73.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 配置五 显示当前热键
        label_74.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 配置六 显示当前热键
        label_75.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 配置七 显示当前热键
        label_76.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 配置八 显示当前热键
        label_77.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 配置九 显示当前热键
        label_78.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 配置十 显示当前热键
        label_79.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 配置十一 显示当前热键
        label_80.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 配置十二 显示当前热键
        label_81.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 文本 '配置一'
        label_82.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 文本 '配置二'
        label_83.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 文本 '配置三'
        label_84.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 文本 '配置四'
        label_85.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 文本 '配置五'
        label_86.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 文本 '配置六'
        label_87.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 文本 '配置七'
        label_88.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 文本 '配置八'
        label_89.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 文本 '配置九'
        label_90.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 文本 '配置十'
        label_91.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 文本 '配置十一'
        label_92.bind("<MouseWheel>", mouse_wheel_two)        # 设置页面 文本 '配置十二'
        
        entry_3.bind("<MouseWheel>", mouse_wheel_two)         # 创建填写连点器间隔时间的文本框
        
        label_1.bind('<Button-1>', get_mouse_xy)            # 获取点击小部件时的event.x值和event.y值
        label_2.bind('<Button-1>', get_mouse_xy)
        label_3.bind('<Button-1>', get_mouse_xy)
        label_38.bind('<Button-1>', open_tutorial)          # 打开教程
        label_40.bind('<Button-1>', open_url)               # 打开彩手开源地址
        label_1.bind('<B1-Motion>', ui_move)                # 图标   绑定移动窗口功能
        label_2.bind('<B1-Motion>', ui_move)                # 软件名 绑定移动窗口功能
        label_3.bind('<B1-Motion>', ui_move)                # 配置名 绑定移动窗口功能
        label_1.bind('<ButtonRelease-1>', get_b1_time)      # 图标   绑定点击窗口时获取时间功能
        label_2.bind('<ButtonRelease-1>', get_b1_time)      # 软件名 绑定点击窗口时获取时间功能
        label_3.bind('<ButtonRelease-1>', get_b1_time)      # 配置名 绑定点击窗口时获取时间功能
        entry_1.bind('<FocusIn>', entry_FocusIn)            # 得到焦点，背景变天蓝色
        entry_2.bind('<FocusIn>', entry_FocusIn)
        entry_3.bind('<FocusIn>', entry_FocusIn)
        entry_4.bind('<FocusIn>', entry_FocusIn)
        entry_5.bind('<FocusIn>', entry_FocusIn)
        entry_6.bind('<FocusIn>', entry_FocusIn)
        entry_7.bind('<FocusIn>', entry_FocusIn)
        entry_8.bind('<FocusIn>', entry_FocusIn)
        entry_9.bind('<FocusIn>', entry_FocusIn)
        entry_1.bind('<FocusOut>', entry_FocusOut)          # 失去焦点，还原背景色，检查输入值并进行配置
        entry_2.bind('<FocusOut>', entry_FocusOut)
        entry_3.bind('<FocusOut>', entry_FocusOut)
        entry_4.bind('<FocusOut>', entry_FocusOut)
        entry_5.bind('<FocusOut>', entry_FocusOut)
        entry_6.bind('<FocusOut>', entry_FocusOut)
        entry_7.bind('<FocusOut>', entry_FocusOut)
        entry_8.bind('<FocusOut>', entry_FocusOut)
        entry_9.bind('<FocusOut>', entry_FocusOut)
        entry_1.bind('<Return>', entry_return)              # 回车，检查输入值并进行配置
        entry_2.bind('<Return>', entry_return)
        entry_3.bind('<Return>', entry_return)
        entry_4.bind('<Return>', entry_return)
        entry_5.bind('<Return>', entry_return)
        entry_6.bind('<Return>', entry_return)
        entry_7.bind('<Return>', entry_return)
        entry_8.bind('<Return>', entry_return)
        entry_9.bind('<Return>', entry_return)
        entry_1.insert(0, configuration_all[3].split(':')[1])                               # 写入配置文件中的值
        entry_2.insert(0, configuration_all[4].split(':')[1])
        
        entry_3.insert(0, hotkey_cfg.get('设置','连点器间隔时间'))
        entry_4.insert(0, hotkey_cfg.get('设置','随机弹道间隔时间A'))
        entry_5.insert(0, hotkey_cfg.get('设置','随机弹道间隔时间B'))
        entry_6.insert(0, hotkey_cfg.get('设置','X轴随机偏移A'))
        entry_7.insert(0, hotkey_cfg.get('设置','X轴随机偏移B'))
        entry_8.insert(0, hotkey_cfg.get('设置','Y轴随机偏移A'))
        entry_9.insert(0, hotkey_cfg.get('设置','Y轴随机偏移B'))
        btn3_command()# 使启动后第一个页面是弹道页面
        config['SIGN_7'] = 1 # 修改状态栏 模式名字
        config['SIGN_8'] = 1 # 修改状态栏 配置名字


        ### 控件 放置 ###
        canvas_top.place(relx=0, rely=0, relwidth=1, relheight=0.05)                  # 放置画布:顶部区域, master: ui
        canvas_content_one.place(relx=0, rely=0.05, relwidth=1, relheight=1)          # 放置画布:内容区域一, master: ui
        frame_one.place(relx=0, rely=0.45, relwidth=1, relheight=0.5)                 # 放置容器, master: 内容区域一
        canvas_content_two.place(relx=0, rely=0, relwidth=0.96, relheight=1)          # 放置画布:强度设置区域, master: frame_one
        btn1.place(relx=0.6, rely=0, relwidth=0.2, relheight=0.05)                    # 放置 最小化按钮
        btn2.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.05)                    # 放置 退出按钮
        btn3.place(relx=0, rely=0.05, relwidth=0.2, relheight=0.05)                   # 放置 弹道按钮
        btn4.place(relx=0.2, rely=0.05, relwidth=0.2, relheight=0.05)                 # 放置 功能按钮
        btn5.place(relx=0.4, rely=0.05, relwidth=0.2, relheight=0.05)                 # 放置 设置按钮
        btn6.place(relx=0.6, rely=0.05, relwidth=0.2, relheight=0.05)                 # 放置 关于按钮
        btn55.place(relx=0.8, rely=0.05, relwidth=0.2, relheight=0.05)                # 放置 驱动按钮
        btn7.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.05)                   # 放置 弹道页面 模式切换按钮
        btn8.place(relx=0, rely=0.30, relwidth=0.2, relheight=0.05)                   # 放置 弹道页面 重置按钮
        btn9.place(relx=0.3+0.0025, rely=0.4, relwidth=0.1, relheight=0.05)                         # 左
        btn10.place(relx=0.4+0.0025, rely=0.4, relwidth=0.1, relheight=0.05)                        # 右
        btn11.place(relx=0.7+0.0025, rely=0.4, relwidth=0.1, relheight=0.05)                        # 上
        btn12.place(relx=0.8+0.0025, rely=0.4, relwidth=0.1, relheight=0.05)                        # 下
        label_1.place(relx=0+0.0025, rely=0+0.0025, relwidth=0.05, relheight=0.05-0.0025)    # 放置 图标
        label_2.place(relx=0.05, rely=0, relwidth=0.07, relheight=0.05)               # 放置 软件名
        label_3.place(relx=0.12, rely=0, relwidth=0.48, relheight=0.05)               # 放置 配置名
        label_4.place(relx=0.2, rely=0.15, relwidth=0.2, relheight=0.05)              # 放置：‘时间：’
        label_5.place(relx=0.8, rely=0.15, relwidth=0.2, relheight=0.05)              # 放置：‘毫秒’
        label_6.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.05)               # 放置：‘段数：’
        label_7.place(relx=0.8, rely=0.3, relwidth=0.2, relheight=0.05)               # 放置：‘段’
        entry_1.place(relx=0.4, rely=0.15, relwidth=0.4, relheight=0.05)              # 放置时间输入框
        entry_2.place(relx=0.4, rely=0.3, relwidth=0.4, relheight=0.05)               # 放置段数输入框
    except Exception as e:
        if '0x0154：' not in config['ERROR_LOG']:
            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0154：' + str(e) + '\n'
        print('0x0154:ERROR!',e)


    try:
        ### 顶部状态栏 ###
        if config['DESKTOP_RESOLUTION'] == [2560, 1440]:
            statusBar_BG = tk.Toplevel(ui)                                      # 顶部状态栏背景
            statusBar_BG.geometry("987x25+787+1")                               # 窗体尺寸及坐标
            statusBar_BG.overrideredirect(True)                                 # 隐藏窗体边框
            statusBar_BG.attributes('-topmost', 1)                              # 在所有应用中置前
            statusBar_BG.attributes('-alpha',0.2)                               # 透明度
            
            statusBar_FG = tk.Toplevel(ui)                                      # 顶部状态栏前景
            statusBar_FG.geometry("987x25+787+1")
            statusBar_FG.overrideredirect(True)                                 # 去掉windows边框
            statusBar_FG.attributes('-topmost',1)
            statusBar_FG.attributes('-transparentcolor','yellow')
            
            bg_one=tk.Frame(statusBar_BG, bg='black', width=987, height=25)
            bg_two=tk.Frame(statusBar_FG, bg='yellow', width=987, height=25)
            content_switch = tk.Label(bg_two, bg='yellow', text='OFF', fg='#ff00ff', font=("宋体", 11), anchor='center')
            content_weapon_one = tk.Label(bg_two, bg='yellow', text='模式1', fg='#ff00ff', font=("宋体", 11), anchor='w')
            content_weapon_two = tk.Label(bg_two, bg='yellow', text='配置一', fg='#ff00ff', font=("宋体", 11), anchor='w')
            content_timer_one = tk.Label(bg_two, bg='yellow', text='0\t毫秒', fg='#ff00ff', font=("宋体", 11), anchor='w')
            
            bg_one.pack()
            bg_two.pack()
            
            content_switch.place(x=0, y=0, width=67, height=25)
            content_weapon_one.place(x=67, y=0, width=107, height=25)
            content_weapon_two.place(x=174, y=0, width=667, height=25)
            content_timer_one.place(x=841, y=0, width=146, height=25)

        else:
            statusBar_BG = tk.Toplevel(ui)                                      # 顶部状态栏背景
            statusBar_BG.geometry("740x19+590+1")                               # 窗体尺寸及坐标
            statusBar_BG.overrideredirect(True)                                 # 隐藏窗体边框
            statusBar_BG.attributes('-topmost', 1)                              # 在所有应用中置前
            statusBar_BG.attributes('-alpha',0.2)                               # 透明度
            
            statusBar_FG = tk.Toplevel(ui)                                      # 顶部状态栏前景
            statusBar_FG.geometry("740x19+590+1")
            statusBar_FG.overrideredirect(True)                                 # 去掉windows边框
            statusBar_FG.attributes('-topmost',1)
            statusBar_FG.attributes('-transparentcolor','yellow')
            
            bg_one=tk.Frame(statusBar_BG, bg='black', width=740, height=19)
            bg_two=tk.Frame(statusBar_FG, bg='yellow', width=740, height=19)
            content_switch = tk.Label(bg_two, bg='yellow', text='OFF', fg='#ff00ff', font=("宋体", 9), anchor='center')
            content_weapon_one = tk.Label(bg_two, bg='yellow', text='模式1', fg='#ff00ff', font=("宋体", 9))
            content_weapon_two = tk.Label(bg_two, bg='yellow', text='配置一', fg='#ff00ff', font=("宋体", 9))
            content_timer_one = tk.Label(bg_two, bg='yellow', text='0\t毫秒', fg='#ff00ff', font=("宋体", 9))
            
            bg_one.pack()
            bg_two.pack()
            
            content_switch.place(x=0, y=0, width=50, height=19)
            content_weapon_one.place(x=50, y=0, width=80, height=19)
            content_weapon_two.place(x=130, y=0, width=500, height=19)
            content_timer_one.place(x=630, y=0, width=110, height=19)

        ui.withdraw()
        statusBar_BG.withdraw()
        statusBar_FG.withdraw()
    except Exception as e:
        if '0x0155：' not in config['ERROR_LOG']:
            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0155：' + str(e) + '\n'
        print('0x0155:ERROR!',e)


    def thread_switch_configuration():#切换配置 线程
        nonlocal configuration_all, box_num, scroll_height, configuration_another_name, configuration_mode, configuration_duration, configuration_section, configuration_strong, strong_convert, entry_name, btn_name, label_name
        while True:
            try:
                time.sleep(0.1)
                if config['SIGN_1'] == 1:
                    config['SIGN_1'] = 0
                    if config['UI_DISPLAY'] == 'SHOW':
                        ui.deiconify()
                    else:
                        ui.withdraw()
                if config['SIGN_2'] == 1:
                    configuration_name = config['CONFIGURATION_NAME']
                    configuration_another_name = '默认配置'
                    configuration_duration = 5000
                    configuration_section = 10
                    configuration_strong = [[],[]]
                    strong_convert = [[],[]]
                    configuration_all = configuration('get', configuration_name)
                    label_3['text'] = configuration_another_name
                    if btn7['text'] != '模式'+str(configuration_mode):
                        btn7['text'] = '模式'+str(configuration_mode)
                    box_num, scroll_height = box_num_check(configuration_all[4].split(':')[1])
                    canvas_content_two.config(scrollregion=(0, 0, 400, scroll_height))
                    entry_1.delete(0, 'end')
                    entry_2.delete(0, 'end')
                    entry_1.insert(0, configuration_all[3].split(':')[1])
                    entry_2.insert(0, configuration_all[4].split(':')[1])
                    item_id = canvas_content_two.find_all()
                    item_count = int(len(item_id)/7)
                    for i in range(0, item_count):
                        label_name[i].place_forget()
                        entry_name[0][i].place_forget()
                        entry_name[1][i].place_forget()
                        btn_name[0][i].place_forget()
                        btn_name[1][i].place_forget()
                        btn_name[2][i].place_forget()
                        btn_name[3][i].place_forget()
                    create_canvas_content_two_widget('new', configuration_name)
                    config['SIGN_2'] = 0
            except Exception as e:
                if '0x0156：' not in config['ERROR_LOG']:
                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0156：' + str(e) + '\n'
                print('0x0156:ERROR!',e)


    def thread_breathing_light():# 呼吸灯 线程
        # 红色 【RGB】255,   0,   0
        # 橙色 【RGB】255, 165,   0
        # 黄色 【RGB】255, 255,   0
        # 绿色 【RGB】  0, 255,   0
        # 青色 【RGB】  0, 255, 255
        # 蓝色 【RGB】  0,   0, 255
        # 紫色 【RGB】139,   0, 255
        rgb_state = 1
        r = 255
        g = 0
        b = 0
        while True:
            time.sleep(0.1)
            label_1['bg'] = '#%02x%02x%02x'%(r, g, b)
            label_2['fg'] = '#%02x%02x%02x'%(r, g, b)
            if rgb_state == 0:#紫色 到 红色
                r += 4 #139/30
                b -= 9 #255/30
                if r > 251 or b < 9:#255-4
                    rgb_state = 1
            elif rgb_state == 1:#红色 到 橙色
                g += 6 # 165/30
                if g > 165:
                    rgb_state = 2
            elif rgb_state == 2:#橙色 到 黄色
                g += 3 # (255-165)/30
                if g > 252:#255-3
                    rgb_state = 3
            elif rgb_state == 3:#黄色 到 绿色
                r -= 9 # 255/30
                if r < 9:
                    rgb_state = 4
            elif rgb_state == 4:#绿色 到 青色
                b += 9 # 255/30
                if b > 246:#255-9
                    rgb_state = 5
            elif rgb_state == 5:#青色 到 蓝色
                g -= 9 # 255/30
                if g < 9:
                    rgb_state = 6
            elif rgb_state == 6:#蓝色 到 紫色
                r += 5 # 139/30
                if r > 134:#139-5
                    rgb_state = 0


    def thread_key_modification():#快捷键修改 线程
        label_dict = {
                     35 : (label_35,'HOTKEY_MACRO_SWITCH','设置','宏开/关热键'),      # 宏开/关 显示当前热键
                     36 : (label_36,'HOTKEY_UI_DISPLAY','设置','主界面显/隐热键'),     # 主界面显/隐 显示当前热键
                     37 : (label_37,'HOTKEY_STATUS_DISPLAY','设置','指示栏显/隐热键'), # 指示栏显/隐 显示当前热键
                     53 : (label_53,'HOTKEY_CLICKER','设置','连点器触发热键'),         # 连点器触发热键 显示当前热键
                     69 : (label_69,'HOTKEY_CONFIGURE_1','设置','配置一热键'),        # 设置页面 配置一 显示当前热键
                     70 : (label_70,'HOTKEY_CONFIGURE_2','设置','配置二热键'),        # 设置页面 配置二 显示当前热键
                     71 : (label_71,'HOTKEY_CONFIGURE_3','设置','配置三热键'),        # 设置页面 配置三 显示当前热键
                     72 : (label_72,'HOTKEY_CONFIGURE_4','设置','配置四热键'),        # 设置页面 配置四 显示当前热键
                     73 : (label_73,'HOTKEY_CONFIGURE_5','设置','配置五热键'),        # 设置页面 配置五 显示当前热键
                     74 : (label_74,'HOTKEY_CONFIGURE_6','设置','配置六热键'),        # 设置页面 配置六 显示当前热键
                     75 : (label_75,'HOTKEY_CONFIGURE_7','设置','配置七热键'),        # 设置页面 配置七 显示当前热键
                     76 : (label_76,'HOTKEY_CONFIGURE_8','设置','配置八热键'),        # 设置页面 配置八 显示当前热键
                     77 : (label_77,'HOTKEY_CONFIGURE_9','设置','配置九热键'),        # 设置页面 配置九 显示当前热键
                     78 : (label_78,'HOTKEY_CONFIGURE_10','设置','配置十热键'),       # 设置页面 配置十 显示当前热键
                     79 : (label_79,'HOTKEY_CONFIGURE_11','设置','配置十一热键'),     # 设置页面 配置十一 显示当前热键
                     80 : (label_80,'HOTKEY_CONFIGURE_12','设置','配置十二热键')      # 设置页面 配置十二 显示当前热键
                                 }
        key_dict = {
         513:'鼠标左键',516:'鼠标右键',519:'鼠标中键', 523:'鼠标侧键',
         514:'鼠标左键',517:'鼠标右键',520:'鼠标中键', 524:'鼠标侧键',
         
         1:'鼠标左键',                 12:'清除键',                21:'输入法韩文模式',
         2:'鼠标右键',                 13:'回车键',                23:'IME Junja模式',
         3:'控制中断处理',             16:'转移键',                24:'输入法最终模式',
         4:'鼠标中键',                 17:'控制键',                25:'输入法汉字模式',
         5:'X1鼠标按钮',               18:'Alt',                   '25*':'输入法汉字模式',
         6:'X2鼠标按钮',               19:'中断暂停键',            27:'Esc',
         8:'退格键',                   20:'大写键',                28:'输入法转换',
         9:'Tab',                      21:'IME Hanguel模式',       29:'输入法未转换',
         
         0:'输入法接受',               39:'右方向键',              48:'0',
         31:'IME 模式更改请求',        40:'下方向键',              49:'1',
         32:'空格键',                  41:'选择键',                50:'2',
         33:'PgUp',                    42:'打印键',                51:'3',
         34:'PgDown',                  43:'执行键',                52:'4',
         35:'End',                     44:'快照键',                53:'5',
         36:'Home',                    45:'Insert',                54:'6',
         37:'左方向键',                46:'Delete',                55:'7',
         38:'上方向键',                47:'帮助键',                56:'8',
         
         57:'9',                       73:'I',                     82:'R',
         65:'A',                       74:'J',                     83:'S',
         66:'B',                       75:'K',                     84:'T',
         67:'C',                       76:'L',                     85:'U',
         68:'D',                       77:'M',                     86:'V',
         69:'E',                       78:'N',                     87:'W',
         70:'F',                       79:'O',                     88:'X',
         71:'G',                       80:'P',                     89:'Y',
         72:'H',                       81:'Q',                     90:'Z',
         
         91:'左Windows键',             101:'数字键盘 5',             110:'数字键盘 .',          111:'数字键盘 /',
         92:'右Windows键',             102:'数字键盘 6',             112:'F1',
         93:'应用程序密钥',             103:'数字键盘 7',             113:'F2',
         95:'电脑睡眠键',               104:'数字键盘 8',             114:'F3',
         96:'数字键盘 0',               105:'数字键盘 9',             115:'F4',
         97:'数字键盘 1',               106:'数字键盘 *',             116:'F5',
         98:'数字键盘 2',               107:'数字键盘 +',             117:'F6',
         99:'数字键盘 3',               108:'数字键盘 Enter',         118:'F7',
         100:'数字键盘 4',              109:'数字键盘 -',             119:'F8',
         
         120:'F9',                     129:'F18',                  160:'左 shift',
         121:'F10',                    130:'F19',                  161:'右 shift',
         122:'F11',                    131:'F20',                  162:'左 ctrl',
         123:'F12',                    132:'F21',                  163:'右 ctrl',
         124:'F13',                    133:'F22',                  164:'左 alt',
         125:'F14',                    134:'F23',                  165:'右 alt',
         126:'F15',                    135:'F24',                  166:'浏览器返回键',
         127:'F16',                    144:'Num Lock',             167:'浏览器前进键',
         128:'F17',                    145:'屏幕滚动显示锁定键',   168:'浏览器刷新键',
         
         169:'浏览器停止键',           178:'停止媒体键',           189:'- _',
         170:'浏览器搜索键',           179:'播放/暂停媒体键',      190:'. ',
         171:'浏览器收藏夹键',         180:'开始邮件键',           191:'/ ?',
         172:'浏览器开始和主页键',     181:'选择媒体键',           192:'` ~',
         173:'音量静音键',             182:'1 键',                 219:'[ {',
         174:'降低音量键',             183:'2 键',                 220:'/ |',
         175:'提高音量键',             186:'; :',                  221:'] }',
         176:'下一曲目键',             187:'= +',                  222:"\' \"",
         177:'上一曲目键',             188:', ',                   223:'杂字符',
         
         226:'尖括号或反斜杠键',       247:'选择键',               251:'缩放键',
         231:'传递Unicode字符键',      248:'退出键',               252:'预订键',
         229:'输??入法处理键',           249:'EOF擦除键',            253:'PA1 键',
         246:'收件人键',               250:'播放键',               254:'清除键',
                            }
        while True:
            try:
                time.sleep(0.1)
                if config['SIGN_26'] == 2:
                    config['SIGN_26'] = 3
                    if config['LABEL_CUSTOM_KEY'] in [35,36,37,53,69,70,71,72,73,74,75,76,77,78,79,80] and config['CUSTOM_KEY'] in [513, 514, 1]:
                        config['SIGN_26'] = 1
                    if config['SIGN_26'] == 3:
                        dict_get = label_dict.get(config['LABEL_CUSTOM_KEY'], None)
                        dict_get[0]['bg'] = config['ENTRY_BG']
                        dict_get[0]['text'] = key_dict.get(config['CUSTOM_KEY'], '不知名按键···')
                        config[dict_get[1]] = config['CUSTOM_KEY']
                        hotkey_cfg.set(dict_get[2], dict_get[3], str(config['CUSTOM_KEY']))
                        with open('./配置文件/hotkey.ini', 'w', encoding='utf-8') as f:
                            hotkey_cfg.write(f)
                        time.sleep(0.2)
                        config['SIGN_26'] = 0
            except Exception as e:
                if '0x0158：' not in config['ERROR_LOG']:
                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0158：' + str(e) + '\n'
                print('0x0158:ERROR!',e)


    def thread_status_bar_bg():#状态栏背景显示或隐藏 线程
        alpha_state = 1
        if config['DESKTOP_RESOLUTION'] == [1920, 1080]:
            bar_left = 580 # 状态栏左边界 590-10
            bar_right = 1340 # 状态栏右边界 590+740+10
        elif config['DESKTOP_RESOLUTION'] == [2560, 1440]:
            bar_left = 777 # 787-10
            bar_right = 1784 # 787+987+10
        while True:
            try:
                time.sleep(0.1)
                if bar_left < config['MOUSE_X'] < bar_right and config['MOUSE_Y'] < 30: # 防止鼠标点到状态栏，导致切换出游戏外窗口
                    if alpha_state == 1:
                        alpha_state = 0
                        statusBar_BG.attributes('-alpha',0)
                else:
                    if alpha_state == 0:
                        alpha_state = 1
                        statusBar_BG.attributes('-alpha',0.2)
                if config['SIGN_3'] == 1:
                    config['SIGN_3'] = 0
                    if config['STATUS_DISPLAY'] == 'SHOW':
                        statusBar_BG.deiconify()
                    else:
                        statusBar_BG.withdraw()
            except Exception as e:
                if '0x0160：' not in config['ERROR_LOG']:
                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0160：' + str(e) + '\n'
                print('0x0160:ERROR!',e)


    def thread_status_bar_fg():#状态栏前景显示或隐藏 线程
        alpha_state = 1
        if config['DESKTOP_RESOLUTION'] == [1920, 1080]:
            bar_left = 580 # 状态栏左边界 590-10
            bar_right = 1340 # 状态栏右边界 590+740+10
        elif config['DESKTOP_RESOLUTION'] == [2560, 1440]:
            bar_left = 777 # 787-10
            bar_right = 1784 # 787+987+10
        while True:
            try:
                time.sleep(0.1)
                if bar_left < config['MOUSE_X'] < bar_right and config['MOUSE_Y'] < 30:
                    if alpha_state == 1:
                        alpha_state = 0
                        content_switch['fg'] = 'yellow'
                        content_weapon_one['fg'] = 'yellow'
                        content_weapon_two['fg'] = 'yellow'
                        content_timer_one['fg'] = 'yellow'
                else:
                    if alpha_state == 0:
                        alpha_state = 1
                        content_switch['fg'] = config['STATUS_BAR_FG']
                        content_weapon_one['fg'] = config['STATUS_BAR_FG']
                        content_weapon_two['fg'] = config['STATUS_BAR_FG']
                        content_timer_one['fg'] = config['STATUS_BAR_FG']
                if config['SIGN_4'] == 1:
                    config['SIGN_4'] = 0
                    if config['STATUS_DISPLAY'] == 'SHOW':
                        time.sleep(0.1)
                        statusBar_FG.deiconify()
                    else:
                        statusBar_FG.withdraw()
                if config['SIGN_6'] == 1:
                    config['SIGN_6'] = 0
                    content_switch['text'] = config['MARCO_SWITCH']
                    content_switch['fg'] = config['STATUS_BAR_FG']
                    content_weapon_one['fg'] = config['STATUS_BAR_FG']
                    content_weapon_two['fg'] = config['STATUS_BAR_FG']
                    content_timer_one['fg'] = config['STATUS_BAR_FG']
                if config['SIGN_8'] == 1:
                    config['SIGN_8'] = 0
                    new_content = config['ANOTHER_NAME']
                    if content_weapon_two['text'] != new_content:
                        content_weapon_two['text'] = new_content
                        if config['STATUS_DISPLAY'] == 'SHOW':
                            content_weapon_two['bg'] = 'skyblue'
                            time.sleep(0.03)
                            content_weapon_two['bg'] = 'yellow'
                            time.sleep(0.05)
                            content_weapon_two['bg'] = 'skyblue'
                            time.sleep(0.03)
                            content_weapon_two['bg'] = 'yellow'
            except Exception as e:
                if '0x0164：' not in config['ERROR_LOG']:
                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0164：' + str(e) + '\n'
                print('0x0164:ERROR!',e)


    def thread_status_bar_mode():#状态栏模式名修改 线程
        while True:
            try:
                time.sleep(0.1)
                if config['SIGN_7'] == 1:
                    config['SIGN_7'] = 0
                    new_content = '模式' + str(config['MARCO_MODE'])
                    if content_weapon_one['text'] != new_content:
                        content_weapon_one['text'] = new_content
                        if config['STATUS_DISPLAY'] == 'SHOW':
                            content_weapon_one['bg'] = 'skyblue'
                            time.sleep(0.03)
                            content_weapon_one['bg'] = 'yellow'
                            time.sleep(0.05)
                            content_weapon_one['bg'] = 'skyblue'
                            time.sleep(0.03)
                            content_weapon_one['bg'] = 'yellow'
            except Exception as e:
                if '0x0163：' not in config['ERROR_LOG']:
                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0163：' + str(e) + '\n'
                print('0x0163:ERROR!',e)


    def thread_status_bar_time():#状态栏鼠标左键按下时长显示 线程
        position = SendInput.position
        while True:
            time.sleep(0.01)
            try:
                config['MOUSE_X'], config['MOUSE_Y'] = position()
                if config['SIGN_16'] == 1:
                    if config['LBUTTON_PRESS_TIME'] > 0 and config['HOOK_SWITCH'] == 1:
                        press_time = int((time.time() - config['LBUTTON_PRESS_TIME'])*1000)
                        if press_time < 86400000:
                            content_timer_one['text'] = str(press_time) + '\t毫秒'
            except Exception as e:
                if '0x0161：' not in config['ERROR_LOG']:
                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0161：' + str(e) + '\n'
                print('0x0161:ERROR!')


    threading.Thread(target=thread_switch_configuration).start()# 切换配置 线程
    threading.Thread(target=thread_breathing_light).start()# 呼吸灯 线程
    threading.Thread(target=thread_key_modification).start()# 快捷键修改 线程
    threading.Thread(target=thread_status_bar_bg).start()# 状态栏背景显示或隐藏 线程
    threading.Thread(target=thread_status_bar_fg).start()# 状态栏前景显示或隐藏 线程
    threading.Thread(target=thread_status_bar_mode).start()# 状态栏模式名修改 线程
    threading.Thread(target=thread_status_bar_time).start()# 状态栏鼠标左键按下时长显示 线程

    ui.mainloop()# 开启窗体事件循环


def CaiShouM2():#鼠标钩子
    from ctypes import wintypes
    try:
        WH_MOUSE_LL = 14             # 低级鼠标钩子常量
        WM_LBUTTONDOWN = 513         # 左键按下事件常量0x0201
        WM_LBUTTONUP = 514           # 左键回弹0x0202
        WM_RBUTTONDOWN = 516         # 右键按下0x0204
        WM_RBUTTONUP = 517           # 右键回弹0x0205
        WM_MBUTTONDOWN = 519         # 中键按下0x0207
        WM_MBUTTONUP = 520           # 中键回弹0x0208
        WM_SBUTTONDOWN = 523         # 侧键按下0x020b
        WM_SBUTTONUP = 524           # 侧键回弹0x020c
        play_sound = 0               # 提示声音播放信号
        HC_ACTION = 0
        user32 = ctypes.WinDLL('user32', use_last_error=True)
        ULONG_PTR = wintypes.WPARAM
        LRESULT = wintypes.LPARAM
        HOOKPROC = ctypes.WINFUNCTYPE(LRESULT, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)
        LPMSG = ctypes.POINTER(wintypes.MSG)
    except Exception as e:
        if '0x0201：' not in config['ERROR_LOG']:
            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0201：' + str(e) + '\n'
        print('0x0201:ERROR!',e)


    class MSLLHOOKSTRUCT(ctypes.Structure):
        try:
            _fields_ = (
                ('pt',          wintypes.POINT),
                ('mouseData',   wintypes.DWORD),
                ('flags',       wintypes.DWORD),
                ('time',        wintypes.DWORD),
                ('dwExtraInfo', ULONG_PTR),
            )
        except Exception as e:
            if '0x0218：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0218：' + str(e) + '\n'
            print('0x0218:ERROR!',e)


    try:
        LowLevelMouseProc = ctypes.WINFUNCTYPE(LRESULT, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)
        user32.SetWindowsHookExW.restype = wintypes.HHOOK
        user32.SetWindowsHookExW.argtypes = (ctypes.c_int, HOOKPROC, wintypes.HINSTANCE, wintypes.DWORD)
        user32.CallNextHookEx.restype = LRESULT
        user32.CallNextHookEx.argtypes = (wintypes.HHOOK, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)
        user32.GetMessageW.restype = wintypes.BOOL
        user32.GetMessageW.argtypes = (LPMSG, wintypes.HWND, wintypes.UINT, wintypes.UINT)
        user32.TranslateMessage.restype = wintypes.BOOL
        user32.TranslateMessage.argtypes = (LPMSG,)
        user32.DispatchMessageW.restype = LRESULT
        user32.DispatchMessageW.argtypes = (LPMSG,)
    except Exception as e:
        if '0x0219：' not in config['ERROR_LOG']:
            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0219：' + str(e) + '\n'
        print('0x0219:ERROR!',e)


    # 鼠标事件回调函数, wParam是事件类型，lParam是一个MSLLHOOKSTRUCT的结构体，其中包括鼠标坐标等信息
    @LowLevelMouseProc
    def callback_func(nCode, wParam, lParam):
        try:
            if nCode == HC_ACTION:
                if config['SIGN_26'] == 1:
                    if wParam in [514, 517, 520, 524]:
                        config['CUSTOM_KEY'] = wParam
                        config['SIGN_26'] = 2
                elif config['SIGN_26'] == 0:# 在设置自定义按键时，下面的函数都不运行
                    if wParam == WM_LBUTTONDOWN:      # 全局 左键按下
                        config['WM_LBUTTON_STATE'] = 1
                        config['LBUTTON_PRESS_TIME'] = time.time()
                        config['SIGN_16'] = 1
                    elif wParam == WM_LBUTTONUP:      # 全局 左键弹起
                        config['SIGN_16'] = 0
                        config['WM_LBUTTON_STATE'] = 0
                        config['LBUTTON_PRESS_TIME'] = 0
                    elif wParam == WM_RBUTTONDOWN:    # 全局 右键按下
                        config['WM_RBUTTON_STATE'] = 1
                    elif wParam == WM_RBUTTONUP:      # 全局 右键弹起
                        config['WM_RBUTTON_STATE'] = 0
                    elif wParam == WM_MBUTTONDOWN:    # 全局 中键按下
                        config['WM_MBUTTON_STATE'] = 1
                    elif wParam == WM_MBUTTONUP:      # 全局 中键弹起
                        config['WM_MBUTTON_STATE'] = 0
                    elif wParam == WM_SBUTTONDOWN:    # 全局 侧键按下
                        config['WM_SBUTTON_STATE'] = 1
                    elif wParam == WM_SBUTTONUP:      # 全局 侧键弹起
                        config['WM_SBUTTON_STATE'] = 0
                    if wParam in [513, 516, 519, 523]:# 全局按下事件
                        if wParam == config['HOTKEY_CLICKER']: # V键 彩手高级设置 热键:连点器 开启
                            SIGN_1 = 1
                    if wParam in [514, 517, 520, 524]:# 全局弹起事件
                        if wParam == config['HOTKEY_MACRO_SWITCH']:# 彩手高级设置 热键:宏开/关
                            call_func('macro_switch')
                            if config['SOUND_EFFECT_SWITCH'] == '开':
                                if config['MARCO_SWITCH'] == 'ON' :
                                    play_sound = 1
                                else:
                                    play_sound = 2
                        elif wParam == config['HOTKEY_UI_DISPLAY']:# 彩手高级设置 热键:主界面显/隐
                            call_func('ui_display')
                        elif wParam == config['HOTKEY_STATUS_DISPLAY']:# 彩手高级设置 热键:状态栏显/隐
                            call_func('status_display')
                        if wParam == config['HOTKEY_CLICKER']: # V键 彩手高级设置 热键:连点器 关闭
                            call_func('continuous_clicker', 'up')
            return user32.CallNextHookEx(None, nCode, wParam, lParam)
        except Exception as e:
            if '0x0220：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0220：' + str(e) + '\n'
            print('0x0220:ERROR!',e)


    def event_loop():                       # Windows消息循环
        try:
            msg = wintypes.MSG()
            while True:
                try:
                    if user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
                        user32.TranslateMessage(ctypes.byref(msg))
                        user32.DispatchMessageW(ctypes.byref(msg))
                except Exception as e:
                    if '0x022101：' not in config['ERROR_LOG']:
                        config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x022101：' + str(e) + '\n'
                    print('0x022101:ERROR!',e)
        except Exception as e:
            if '0x0221：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0221：' + str(e) + '\n'
            print('0x0221:ERROR!',e)


    def thread_play_sound():#播放提示声音 线程
        import winsound
        nonlocal play_sound
        while True:
            try:
                time.sleep(0.01)
                if config['SOUND_EFFECT_SWITCH'] == '开':
                    if play_sound == 1:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/on.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT) # 启动宏，播放提示声音1
                    elif play_sound == 2:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/off.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT) # 启动宏，播放提示声音2
            except Exception as e:
                if '0x0222：' not in config['ERROR_LOG']:
                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0222：' + str(e) + '\n'
                print('0x0222:ERROR!',e)


    try:
        threading.Thread(target=thread_play_sound).start()
        hMouseHook = user32.SetWindowsHookExW(WH_MOUSE_LL, callback_func, None, 0)      # 注册鼠标钩子
        event_loop()                            # 开启消息循环
    except Exception as e:
        if '0x02：' not in config['ERROR_LOG']:
            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x02：' + str(e) + '\n'
        print('0x02:ERROR!',e)


def CaiShouM3():#键盘钩子
    WH_KEYBOARD = 13
    WM_KEYDOWN = 256                    # 按键按下事件 0x0100
    WM_KEYUP = 257                      # 按键弹起事件 0x0101
    play_sound = 0                      # 提示声音播放信号
    sign_configuration_switch = 0       # 切换配置信号
    HC_ACTION = 0


    def configuration_switch(dis):    # 配置切换
        try:
            nonlocal play_sound, sign_configuration_switch
            if config['SIGN_2'] != 1:
                config['SIGN_2'] = 1
            if sign_configuration_switch != 1:
                sign_configuration_switch = 1
            if config['SOUND_EFFECT_SWITCH'] == '开':
                play_sound = 2 + dis
        except Exception as e:
            if '0x0306：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0306：' + str(e) + '\n'
            print('0x0306:ERROR!',e)


    class JHKeyLogger(object):
        def __init__(self, user32, kernel32):
            self.user32_ = user32
            self.kernel32_ = kernel32
            self.hook_ = None

        def install_hookproc(self, hookproc):
            try:
                self.hook_ = self.user32_.SetWindowsHookExA(
                                              WH_KEYBOARD,
                                              hookproc,
                                              None,
                                              0)
                if not self.hook_:
                    return False
                return True
            except Exception as e:
                if '0x0324：' not in config['ERROR_LOG']:
                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0324：' + str(e) + '\n'
                print('0x0324:ERROR!',e)

        def start(self):
            from ctypes.wintypes import MSG
            try:
                msg = MSG()
                while True:
                    try:
                        if self.user32_.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                            self.user32_.TranslateMessage(ctypes.byref(msg))
                            self.user32_.DispatchMessageA(ctypes.byref(msg))
                    except Exception as e:
                        print('0x032501:ERROR!',e)
                        if '0x032501：' not in config['ERROR_LOG']:
                            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x032501：' + str(e) + '\n'
                        time.sleep(0.1)
            except Exception as e:
                if '0x0325：' not in config['ERROR_LOG']:
                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0325：' + str(e) + '\n'
                print('0x0325:ERROR!',e)


    def hookproc(nCode, wParam, lParam):
        try:
            nonlocal play_sound
            if nCode == HC_ACTION:
                key_code = 0xFFFFFFFF & lParam[0]
                if config['SIGN_26'] == 1:
                    config['CUSTOM_KEY'] = key_code
                    config['SIGN_26'] = 2
                elif config['SIGN_26'] == 0:    # 在设置自定义按键时，下面的函数都不运行
                    if wParam == WM_KEYDOWN:    # 按键按下事件
                        if key_code == config['HOTKEY_CLICKER']: # V键 彩手高级设置 热键:连点器 开启
                            call_func('continuous_clicker', 'press')
                    elif wParam == WM_KEYUP:    # 按键弹起事件
                        if config['HOOK_SWITCH'] == 1:# 通用模式下，切换配置
                            if key_code == config['HOTKEY_CONFIGURE_1']:
                                config['CONFIGURATION_NAME'] = '配置一'
                                configuration_switch(1)
                            elif key_code == config['HOTKEY_CONFIGURE_2']:
                                config['CONFIGURATION_NAME'] = '配置二'
                                configuration_switch(2)
                            elif key_code == config['HOTKEY_CONFIGURE_3']:
                                config['CONFIGURATION_NAME'] = '配置三'
                                configuration_switch(3)
                            elif key_code == config['HOTKEY_CONFIGURE_4']:
                                config['CONFIGURATION_NAME'] = '配置四'
                                configuration_switch(4)
                            elif key_code == config['HOTKEY_CONFIGURE_5']:
                                config['CONFIGURATION_NAME'] = '配置五'
                                configuration_switch(5)
                            elif key_code == config['HOTKEY_CONFIGURE_6']:
                                config['CONFIGURATION_NAME'] = '配置六'
                                configuration_switch(6)
                            elif key_code == config['HOTKEY_CONFIGURE_7']:
                                config['CONFIGURATION_NAME'] = '配置七'
                                configuration_switch(7)
                            elif key_code == config['HOTKEY_CONFIGURE_8']:
                                config['CONFIGURATION_NAME'] = '配置八'
                                configuration_switch(8)
                            elif key_code == config['HOTKEY_CONFIGURE_9']:
                                config['CONFIGURATION_NAME'] = '配置九'
                                configuration_switch(9)
                            elif key_code == config['HOTKEY_CONFIGURE_10']:
                                config['CONFIGURATION_NAME'] = '配置十'
                                configuration_switch(10)
                            elif key_code == config['HOTKEY_CONFIGURE_11']:
                                config['CONFIGURATION_NAME'] = '配置十一'
                                configuration_switch(11)
                            elif key_code == config['HOTKEY_CONFIGURE_12']:
                                config['CONFIGURATION_NAME'] = '配置十二'
                                configuration_switch(12)
                        if key_code == config['HOTKEY_MACRO_SWITCH']:# 彩手高级设置 热键:宏开/关
                            call_func('macro_switch')
                            if config['SOUND_EFFECT_SWITCH'] == '开':
                                if config['MARCO_SWITCH'] == 'ON' :
                                    play_sound = 1
                                else:
                                    play_sound = 2
                        elif key_code == config['HOTKEY_UI_DISPLAY']:# 彩手高级设置 热键:主界面显/隐
                            call_func('ui_display')
                        elif key_code == config['HOTKEY_STATUS_DISPLAY']:# 彩手高级设置 热键:状态栏显/隐
                            call_func('status_display')
                        if key_code == config['HOTKEY_CLICKER']: # V键 彩手高级设置 热键:连点器 关闭
                            call_func('continuous_clicker', 'up')
            return g_keylogger.user32_.CallNextHookEx(g_keylogger.hook_, nCode, wParam, lParam)
        except Exception as e:
            if '0x0326：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0326：' + str(e) + '\n'
            print('0x0326:ERROR!',e)


    def thread_play_sound():#播放提示声音 线程
        import winsound
        nonlocal play_sound, sign_configuration_switch
        while True:
            try:
                time.sleep(0.01)
                if config['SOUND_EFFECT_SWITCH'] == '开':
                    if play_sound == 1:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/on.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT) # 启动宏，播放提示声音1
                    elif play_sound == 2:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/off.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT) # 启动宏，播放提示声音2
                    elif play_sound == 3:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/配置1.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT) # 切换配置1，播放配置1.wav
                    elif play_sound == 4:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/配置2.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
                    elif play_sound == 5:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/配置3.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
                    elif play_sound == 6:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/配置4.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
                    elif play_sound == 7:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/配置5.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
                    elif play_sound == 8:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/配置6.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
                    elif play_sound == 9:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/配置7.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
                    elif play_sound == 10:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/配置8.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
                    elif play_sound == 11:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/配置9.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
                    elif play_sound == 12:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/配置10.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
                    elif play_sound == 13:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/配置11.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
                    elif play_sound == 14:
                        play_sound = 0
                        winsound.PlaySound(f'./配置文件/sound/配置12.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
                if sign_configuration_switch == 1:
                    sign_configuration_switch = 0
                    while config['SIGN_2'] != 0:
                        time.sleep(0.001)
                    config['SIGN_7'] = 1 # 修改状态栏 模式 123
                    config['SIGN_8'] = 1 # 修改状态栏 配置名字
            except Exception as e:
                if '0x0327：' not in config['ERROR_LOG']:
                    config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x0327：' + str(e) + '\n'
                print('0x0327:ERROR!',e)


    try:
        threading.Thread(target=thread_play_sound).start()
        cfunctype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
        pointer = cfunctype(hookproc)
        g_keylogger = JHKeyLogger(ctypes.windll.user32, ctypes.windll.kernel32)
        g_keylogger.install_hookproc(pointer)       # 注册键盘钩子
        g_keylogger.start()                         # 开始消息循环
    except Exception as e:
        if '0x03：' not in config['ERROR_LOG']:
            config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x03：' + str(e) + '\n'
        print('0x03:ERROR!',e)


def CaiShouM4():#连点器
    sleep_time = 0.1
    mouseDown = SendInput.mouseDown
    mouseUp = SendInput.mouseUp
    while True:
        try:
            if config['CLICKER_BREAK_LIMIT'] == '开':
                if config['CLICKER_SWITCH'] == '开' == config['CLICKER_SIGN']:
                    mouseDown()
                    mouseUp()
                    if sleep_time != 0:
                        sleep_time = 0
                else:
                    if sleep_time != 0.1:
                        sleep_time = 0.1
            else:
                if config['CLICKER_SWITCH'] == '开' == config['CLICKER_SIGN']:
                    mouseDown()
                    mouseUp()
                    sleep_time = config['CLICKER_INTERVAL']
                else:
                    if sleep_time != 0.1:
                        sleep_time = 0.1
            time.sleep(sleep_time)
        except Exception as e:
            if '0x04：' not in config['ERROR_LOG']:
                config['ERROR_LOG'] += str(time.ctime(time.time())) + '\t' + '0x04：' + str(e) + '\n'
            print('0x04:ERROR!',e)


def CaiShouM5():#随机弹道
    counter = 0                                                 # 计数器
    randomTime = 0                                              # 随机弹道间隔时间
    randomXoffset = 0                                           # X轴随机偏移值
    randomYoffset = 0                                           # Y轴随机偏移值
    moveRel = SendInput.moveRel
    while True:
        if config['MARCO_SWITCH'] == 'ON' and (config["RANDOM_BALLISTIC_1"] + config["RANDOM_BALLISTIC_2"]) != 0:
            if config['WM_LBUTTON_STATE'] == 1:      # 左键按下，触发宏
                if config['L_R_P_T'] == '开':# 左右键触发宏
                    if config['WM_RBUTTON_STATE'] == 1: # 右键也同时按下时触发
                        if counter == 0:
                            if config["RANDOM_BALLISTIC_1"] <= config["RANDOM_BALLISTIC_2"]:
                                randomTime = randint(config["RANDOM_BALLISTIC_1"], config["RANDOM_BALLISTIC_2"])
                            else:
                                randomTime = randint(config["RANDOM_BALLISTIC_2"], config["RANDOM_BALLISTIC_1"])
                            if randomTime == 0:
                                randomTime = 1
                            if config["RANDOM_BALLISTIC_3"] <= config["RANDOM_BALLISTIC_4"]:
                                randomXoffset = randint(config["RANDOM_BALLISTIC_3"], config["RANDOM_BALLISTIC_4"])
                            else:
                                randomXoffset = randint(config["RANDOM_BALLISTIC_4"], config["RANDOM_BALLISTIC_3"])
                            if config["RANDOM_BALLISTIC_5"] <= config["RANDOM_BALLISTIC_6"]:
                                randomYoffset = randint(config["RANDOM_BALLISTIC_5"], config["RANDOM_BALLISTIC_6"])
                            else:
                                randomYoffset = randint(config["RANDOM_BALLISTIC_6"], config["RANDOM_BALLISTIC_5"])
                            counter += 1
                        elif counter == randomTime:
                            if config["SELECT_DRIVE"] == 0:
                                moveRel(randomXoffset, randomYoffset)
                            elif config["SELECT_DRIVE"] == 1:
                                LGS_GHUB.moveR(randomXoffset, randomYoffset)
                            counter = 0
                        else:
                            counter += 1
                else:
                    if counter == 0:
                        if config["RANDOM_BALLISTIC_1"] <= config["RANDOM_BALLISTIC_2"]:
                            randomTime = randint(config["RANDOM_BALLISTIC_1"], config["RANDOM_BALLISTIC_2"])
                        else:
                            randomTime = randint(config["RANDOM_BALLISTIC_2"], config["RANDOM_BALLISTIC_1"])
                        if randomTime == 0:
                            randomTime = 1
                        if config["RANDOM_BALLISTIC_3"] <= config["RANDOM_BALLISTIC_4"]:
                            randomXoffset = randint(config["RANDOM_BALLISTIC_3"], config["RANDOM_BALLISTIC_4"])
                        else:
                            randomXoffset = randint(config["RANDOM_BALLISTIC_4"], config["RANDOM_BALLISTIC_3"])
                        if config["RANDOM_BALLISTIC_5"] <= config["RANDOM_BALLISTIC_6"]:
                            randomYoffset = randint(config["RANDOM_BALLISTIC_5"], config["RANDOM_BALLISTIC_6"])
                        else:
                            randomYoffset = randint(config["RANDOM_BALLISTIC_6"], config["RANDOM_BALLISTIC_5"])
                        counter += 1
                    elif counter == randomTime:
                        if config["SELECT_DRIVE"] == 0:
                            moveRel(randomXoffset, randomYoffset)
                        elif config["SELECT_DRIVE"] == 1:
                            LGS_GHUB.moveR(randomXoffset, randomYoffset)
                        counter = 0
                    else:
                        counter += 1
            else: # 左键松开，计数器归零
                if counter != 0:
                    counter = 0
        else: # 关闭宏，计数器归零
            if counter != 0:
                counter = 0
        time.sleep(0.001)


def CaiShouM6():#宏执行
    counter = 0                                                 # 计数器
    sta_timer = 0                                               # 宏的开始运行时间记录
    sleep_time = 0.01                                           # 将宏设置为10毫秒的延迟
    offset_time = 0                                             # 时间偏差
    moveRel = SendInput.moveRel


    def setpriority():#设置进程优先级为实时
        handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, os.getpid())# 打开当前进程
        ctypes.windll.kernel32.SetPriorityClass(handle, 0x100)# 设置进程优先级
        ctypes.windll.kernel32.CloseHandle(handle)# 关闭进程句柄


    def HighPrecisionSleep(time_value):# 高精度休眠计时 替代time.sleep() 以提高延迟精度
        delay_mark = time.perf_counter()
        if time_value > 0.001:# 当需要休眠的时间大于0.001，便先用time.sleep()，再使用高精度延时
            while True:
                past_time = time.perf_counter() - delay_mark
                if past_time >= time_value - 0.001:
                    break
                time.sleep(0.001)
            while True:
                if time.perf_counter() - delay_mark >= time_value:
                    break
                sleep_100us.main()
        else:
            while True:
                if time.perf_counter() - delay_mark >= 0.001:
                    break
                sleep_100us.main()


    def macro_apportion():# 执行宏
        nonlocal counter, sta_timer, sleep_time, offset_time, moveRel
        while True:
            if config['MARCO_SWITCH'] == 'ON':
                if config['WM_LBUTTON_STATE'] == 1:      # 左键按下，触发宏
                
                    # 左键按下时，使用高精度休眠计时
                    if config['MARCO_MODE'] == 2:# 模式二
                        HighPrecisionSleep(0.01)
                    elif config['MARCO_MODE'] == 3:# 模式三
                        time.sleep(config['MACRO_SECTION_ONE_TIME_FLAOT'])
                    elif config['MARCO_MODE'] == 1:# 模式一
                        HighPrecisionSleep(0.005)


                    try:
                        if config['L_R_P_T'] == '开':# 通用模式下，左右键触发宏
                            if config['WM_RBUTTON_STATE'] == 1: # 右键也同时按下时触发
                                if config['MARCO_MODE'] == 1:# 模式一
                                    if counter < config['MACRO_COUNT']:
                                        if counter == 0:
                                            sta_timer = time.time()
                                        if config["SELECT_DRIVE"] == 0:
                                            moveRel(\
                                            config['MACRO_CONVERT'][0][counter], \
                                            config['MACRO_CONVERT'][1][counter])
                                        elif config["SELECT_DRIVE"] == 1:
                                            LGS_GHUB.moveR(\
                                            config['MACRO_CONVERT'][0][counter], \
                                            config['MACRO_CONVERT'][1][counter])
                                        counter += 1
                                elif config['MARCO_MODE'] == 2:# 模式二
                                    if counter < config['MACRO_DURATION']:
                                        if counter == 0:
                                            sta_timer = time.time()
                                        sectin_now = int(counter/config['MACRO_SECTION_ONE_TIME'])
                                        if config["SELECT_DRIVE"] == 0:
                                            moveRel(\
                                            config['MACRO_STEP_LIST'][0][sectin_now], \
                                            config['MACRO_STEP_LIST'][1][sectin_now])
                                        elif config["SELECT_DRIVE"] == 1:
                                            LGS_GHUB.moveR(\
                                            config['MACRO_STEP_LIST'][0][sectin_now], \
                                            config['MACRO_STEP_LIST'][1][sectin_now])
                                        counter += 10
                                        best_time = counter * sleep_time / 10
                                        now_time = time.time() - sta_timer
                                        offset_time = round(now_time - best_time, 3)
                                elif config['MARCO_MODE'] == 3:# 模式三
                                    if counter < config['MACRO_SECTION']:
                                        if config["SELECT_DRIVE"] == 0:
                                            moveRel(\
                                            config['MACRO_STEP_LIST'][0][counter], \
                                            config['MACRO_STEP_LIST'][1][counter])
                                        elif config["SELECT_DRIVE"] == 1:
                                            LGS_GHUB.moveR(\
                                            config['MACRO_STEP_LIST'][0][counter], \
                                            config['MACRO_STEP_LIST'][1][counter])
                                        counter += 1

                            else: # 右键松开，计数器归零
                                counter = 0
                                offset_time = 0


                        else:
                            if config['MARCO_MODE'] == 1:# 模式一
                                if counter < config['MACRO_COUNT']:
                                    if counter == 0:
                                        sta_timer = time.time()
                                    if config["SELECT_DRIVE"] == 0:
                                        moveRel(\
                                        config['MACRO_CONVERT'][0][counter], \
                                        config['MACRO_CONVERT'][1][counter])
                                    elif config["SELECT_DRIVE"] == 1:
                                        LGS_GHUB.moveR(\
                                        config['MACRO_CONVERT'][0][counter], \
                                        config['MACRO_CONVERT'][1][counter])
                                    counter += 1
                            elif config['MARCO_MODE'] == 2:# 模式二
                                if counter < config['MACRO_DURATION']:
                                    if counter == 0:
                                        sta_timer = time.time()
                                    sectin_now = int(counter/config['MACRO_SECTION_ONE_TIME'])
                                    if config["SELECT_DRIVE"] == 0:
                                        moveRel(\
                                        config['MACRO_STEP_LIST'][0][sectin_now], \
                                        config['MACRO_STEP_LIST'][1][sectin_now])
                                    elif config["SELECT_DRIVE"] == 1:
                                        LGS_GHUB.moveR(\
                                        config['MACRO_STEP_LIST'][0][sectin_now], \
                                        config['MACRO_STEP_LIST'][1][sectin_now])
                                    counter += 10
                            elif config['MARCO_MODE'] == 3:# 模式三
                                if counter < config['MACRO_SECTION']:
                                    if config["SELECT_DRIVE"] == 0:
                                        moveRel(\
                                        config['MACRO_STEP_LIST'][0][counter], \
                                        config['MACRO_STEP_LIST'][1][counter])
                                    elif config["SELECT_DRIVE"] == 1:
                                        LGS_GHUB.moveR(\
                                        config['MACRO_STEP_LIST'][0][counter], \
                                        config['MACRO_STEP_LIST'][1][counter])
                                    counter += 1

                    except:
                        pass

                else: # 左键松开，计数器归零
                    if counter != 0:
                        counter = 0
                    if offset_time != 0:
                        offset_time = 0
                    time.sleep(0.01)
            else: # 宏关闭时
                time.sleep(0.01)


    setpriority()
    macro_apportion()


SendInput = SendInputApi()
threading.Thread(target=CaiShouM1).start()# 线程一，主界面、屏幕顶部状态栏
threading.Thread(target=CaiShouM2).start()# 线程二，鼠标钩子
threading.Thread(target=CaiShouM3).start()# 线程三，键盘钩子
threading.Thread(target=CaiShouM4).start()# 线程四，启动连点器
threading.Thread(target=CaiShouM5).start()# 线程五，启动随机弹道
CaiShouM6()# 线程六，启动宏
