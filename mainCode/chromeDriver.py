from selenium import webdriver

from proxy.proxyauth_extension import create_proxyauth_extension
from proxy.randomProxy import main


def chrome_driver(url):
    """
    初始化Chrome浏览器并设置代理
    :param proxy_ip: 代理IP地址
    :param proxy_port: 代理端口
    :return: 配置好代理的Chrome浏览器实例
    """
    # 配置Chrome选项
    proxyauth_plugin_path = create_proxyauth_extension(
        proxy_host="${HOST}",  # 代理IP
        proxy_port="${PORT}",  # 端口号
        # 用户名密码(私密代理/独享代理)
        proxy_username="d2393405771",
        proxy_password="0tcc4090"
    )
    # proxy_ip, proxy_port = main()


    chrome_options = webdriver.ChromeOptions()

    # 设置代理
    chrome_options.add_extension(proxyauth_plugin_path)
    # 第二种方式
    # chrome_options.add_argument(f'--proxy-server=http://{proxy_ip}:{proxy_port}')

    # 初始化Chrome浏览器
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()

    # 打开问卷页面

    driver.get(url)
    return driver
