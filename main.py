from mainCode.openChrome import open_chrome
from static.configuration import questionAire_url, questionAire_num, max_threads
import concurrent.futures


def open_chrome_thread(url, index):
    try:
        open_chrome(url)
    except Exception as e:
        print(f"Thread {index} skipping due to an error: {e}")


if __name__ == '__main__':
    url = questionAire_url

    # 创建线程池并发执行，每次最多10个线程
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        print(f"开始执行，总共执行{questionAire_num}份问卷")
        futures = []
        completed_count = 0  # 新增：用于记录已完成的问卷总数

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
                completed_count += len(done)  # 更新已完成问卷总数
                print(f"总共已完成: {completed_count}份问卷")

        # 确保所有线程完成
        concurrent.futures.wait(futures)

        # 处理剩余线程的结果
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
                completed_count += 1  # 更新已完成问卷总数
            except Exception as e:
                print(f"Error in thread: {e}")

        # 最终输出总完成数
        print(f"所有任务已完成，总共完成: {completed_count}份问卷")
