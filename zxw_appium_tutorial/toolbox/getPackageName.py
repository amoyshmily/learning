import logging
import os


def get_by_adb_shell():
    # 前提：（1）设备已成功以debug模式连接PC，打开目标应用，并保持app界面置顶。

    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

    command_adb_shell = 'adb shell dumpsys activity'
    result = os.popen(command_adb_shell).read()

    # 缩小查找的结果范围
    start = result.find('ACTIVITY MANAGER ACTIVITIES')
    end = result.find('ACTIVITY MANAGER RUNNING PROCESSES')
    target = result[start:end].split('\n')

    # 过滤结果
    activity_list = []
    for i in target:
        if i.find('android.intent.category.LAUNCHER') != -1:
            cmp = i.split(' ')
            for j in cmp:
                if j.find('cmp=') != -1:
                    activity_list.append(j)

    # （如果后台启动多个app，结果列表的个数会大于1，排列顺序是activities from top to bottom）
    # 获取的初始结果的大致样式：
    '''
    Intent { act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER]
    flg=0x10200000 cmp=com.***.***/.ui.activity.***.WelcomeActivity (has extras) }
    '''

    # 格式化结果
    app_package = activity_list[0].replace('cmp=', '').split('/')[0]
    app_activity = activity_list[0].replace('cmp=', '').split('/')[1]
    logging.info('appPackage: '+app_package)
    logging.info('appActivity: '+app_activity)

    app_info_dict = {'appPackage': app_package, 'appActivity': app_activity}
    return app_info_dict


if __name__ == '__main__':
    dic = get_by_adb_shell()
    print(dic['appPackage'])
