from PIL import Image

from PIL import Image
from  imagehash import phash 
import os

def compare_images(image_path1, image_path2, hash_size=8, cutoff=5):
    """
    二つの画像のパーセプチュアルハッシュ値を比較して、類似度を判断します。

    Parameters:
    - image_path1: 比較する最初の画像のパス
    - image_path2: 比較する二つ目の画像のパス
    - hash_size: ハッシュを生成する際のサイズ（大きいほど詳細な比較が可能）
    - cutoff: この値以下のハミング距離を持つ画像は「似ている」と判断

    Returns:
    - True: 画像は似ている
    - False: 画像は似ていない
    """
    # 画像を開いてハッシュ値を計算
    hash1 = phash(Image.open(image_path1), hash_size=hash_size)
    hash2 = phash(Image.open(image_path2), hash_size=hash_size)

    # ハッシュ値のハミング距離を計算
    if hash1 - hash2 < cutoff:
        return True
    else:
        return False

def dump_hash(image_dir, output_file, hash_size=8, cutoff=10):
    """
    画像フォルダ内の画像をハッシュ値として出力します。

    Parameters:
    - image_dir: 画像フォルダのパス
    - output_file: 出力ファイルのパス
    """

    prev_hash_value = None

    with open(output_file, 'w') as f:
        # 画像フォルダ内の画像を取得
        image_files = os.listdir(image_dir)
        for root, _, filenames in os.walk(image_dir):
            for filename in filenames:
                if filename.endswith('.jpg'):
                    image_path = os.path.join(root, filename)
                    hash_value = phash(Image.open(image_path), hash_size=hash_size)

                    if prev_hash_value is not None:
                        diff = hash_value - prev_hash_value
                        if diff < cutoff:
                            os.remove(image_path)

                        f.write(f'{image_path},{hash_value},{diff}\n')

                    prev_hash_value = hash_value


def main():
    image_dir = r"G:\JR西日本\小浜線\test"
    dump_hash(image_dir, "images_hash_list2.txt", 8, 10)

if __name__ == '__main__':
    main()

