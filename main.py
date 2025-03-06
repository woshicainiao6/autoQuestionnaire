from mainCode.openChrome import open_chrome
from static.configuration import questionAire_url, questionAire_num
import concurrent.futures


def open_chrome_thread(url, index):
    try:
        open_chrome(url)
    except Exception as e:
        print(f"Thread {index} skipping due to an error: {e}")


if __name__ == '__main__':
    url = questionAire_url

    # 每次最多使用10个线程
    max_threads = 5

    # 创建线程池并发执行，每次最多10个线程
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = []
        for i in range(1, questionAire_num):
            # 提交任务并存储Future对象
            future = executor.submit(open_chrome_thread, url, i)
            futures.append(future)

            # 如果达到最大线程数，则等待当前线程完成
            if len(futures) >= max_threads:
                # 等待至少一个线程完成
                done, _ = concurrent.futures.wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)
                # 从`futures`列表中移除已经完成的线程
                futures = [f for f in futures if f not in done]

        # 确保所有线程完成
        concurrent.futures.wait(futures)

        # 处理剩余线程的结果
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error in thread: {e}")
