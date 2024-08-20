from mainCode.openChrome import open_chrome

if __name__ == '__main__':
    # url='https://www.wjx.cn/vm/wu9f2rZ.aspx'
    # url="https://www.wjx.cn/vm/rg3dg49.aspx#"
    url = "https://www.wjx.cn/vm/eo3mdYX.aspx#"
    for i in range(1, 100):
        try:
            open_chrome(url)
        except Exception as e:
            print(f"Skipping due to an error: {e}")
            continue
