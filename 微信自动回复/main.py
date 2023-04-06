def print_hi():
    """
    requests，号称为人类准备的HTTP库，可以与服务器进行交互
    安装方法(在终端或CMD行中输入)：pip install requests
    uiautomation，一个非常强大的windowsUI自动化控制工具
    安装方法(在终端或CMD命令行中输入): pip install uiautomation
    pypercLip，剪切板相关库，可以将字符串复制到剪切板或读取剪切板内容
    安装方法(在终端或CMD命令行中输入): pip install pyperclip
    """
    import pyperclip  # 导入剪切板相关库
    import requests  # 导入HTTP库，用于接口对接
    import uiautomation as ui  # 导入控件控制库

    wx = ui.WindowControl(Name="微信")  # 绑定名为微信的主窗口控件
    wx.SwitchToThisWindow()  # 切换窗口
    hw = wx.ListControl(Name="会话")  # 寻找会话控件绑定
    while True:  # 循环等待消息
        we = hw.TextControl(searchDepth=4)  # 查找未读消息
        try:  # 主要用于去报错处理，不捕获错误
            if we.Name:  # 假如存在未读消息
                print("检测到未读消息")
                we.Click(simulateMove=False)  # 点击未读消息
                last_msg = wx.ListControl(Name='消息').GetChildren()[-1].Name  # 读取最后一条消息.
                response = requests.get(f'https://api.qingyunke.com/api.php?key=free&appid=0&msg={last_msg}')
                msg = response.json()['content']  # 结果提取 #智能接口
                pyperclip.copy(msg.replace('{br}', '\n'))  # 替换接口中的换行符
                wx.SendKeys("{Ctrl}v", waitTime=0)  # 将结果输入文字框
                print("发送消息")
                wx.SendKeys("{Enter}", waitTime=0)  # 回车发送消息
                print(f"发送[成功]\n")
                wx.TextControl(SubName=msg[:5]).RightClick()
                m_ent = ui.MenuControl(ClassName="CMenuWnd")
                m_ent.TextControl(Name="不显示聊天").Click()
        except:
            pass


if __name__ == '__main__':
    print_hi()


