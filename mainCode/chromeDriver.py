from selenium import webdriver

from proxy.randomProxy import main


def chrome_driver(url):
    """
    初始化Chrome浏览器并设置代理
    :param proxy_ip: 代理IP地址
    :param proxy_port: 代理端口
    :return: 配置好代理的Chrome浏览器实例
    """
    # # 配置Chrome选项
    # proxy_ip, proxy_port = main()
    #
    # chrome_options = webdriver.ChromeOptions()
    #
    # # 设置代理
    # chrome_options.add_argument(f'--proxy-server=http://{proxy_ip}:{proxy_port}')

    # 初始化Chrome浏览器
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()

    # 打开问卷页面

    driver.get(url)
    return driver
