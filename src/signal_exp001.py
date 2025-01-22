import signal
import logging
import time

# シグナル処理のサンプル
# 基本的な使い方

# ロガー作成
logging.basicConfig(level=logging.DEBUG, encoding='utf-8')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# コンソールハンドラ
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)


logger.addHandler(ch)

def signal_handler(signum, frame):
    logging.debug(f"シグナル {signum} を受信しました")
    exit(0)

    
def main():
    # キーボードからの割り込み（通常はCtrl+C）を処理
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        logger.debug("処理中・・・")
        time.sleep(1)

if __name__ == "__main__":
    main()