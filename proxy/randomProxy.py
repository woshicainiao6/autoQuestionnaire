import requests
from static.configuration import proxypool_url,proxy_target_url
# 代理池API URL
proxypool_url = proxypool_url
target_url = proxy_target_url

# 全局变量用于存储已经使用过的 IP 地址
used_ips = set()


def get_random_proxy():
    """
    从代理池获取随机代理
    :return: proxy
    """
    return requests.get(proxypool_url).text.strip()


def main():
    proxy = get_random_proxy()
    # 从API获取代理IP和端口
    proxy_ip, proxy_port = proxy.split(":")[0], proxy.split(":")[1]

    # 检查是否已经使用过该 IP
    if (proxy_ip, proxy_port) not in used_ips:
        used_ips.add((proxy_ip, proxy_port))
        return proxy_ip, proxy_port


# 运行主函数
if __name__ == '__main__':
    main()
