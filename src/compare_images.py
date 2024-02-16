from PIL import Image

from PIL import Image
from  imagehash import phash 
import os


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
    image_dir = r"/path/to/image/dir"
    dump_hash(image_dir, "images_hash_list2.txt", 8, 10)

if __name__ == '__main__':
    main()

