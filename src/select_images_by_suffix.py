import os
import fnmatch
import shutil
from tqdm import tqdm

def copy_images_with_suffix_and_length(source_directory, target_directory, suffixes):
    """
    指定されたディレクトリおよびサブディレクトリ内で、
    ファイル名の末尾が特定の桁数と数値で終わるJPEG画像を検索し、
    それらを指定された別のディレクトリにコピーします。
    サブフォルダの構造は維持されます。

    Parameters:
    - source_directory: 検索するディレクトリのパス
    - target_directory: コピー先のディレクトリのパス
    - suffix: ファイル名の末尾の数値（文字列）
    - length: 抽出したい末尾の桁数
    """
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    suffix_length = len(suffixes[0])
    matches = []
    for root, _, filenames in os.walk(source_directory):
        for filename in filenames:
            if filename.endswith('.jpg'):
                for suffix in suffixes:
                    suffix_length = len(suffix)

                    if filename[-suffix_length-4:-4] == suffix:
                        matches.append(os.path.join(root, filename))
                        break
    
    for file_path in tqdm(matches, desc="Copying files"):
        relative_path = os.path.relpath(file_path, source_directory)
        target_path = os.path.join(target_directory, relative_path)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        shutil.copy(file_path, target_path)


def main():
    src_dir = r"/path/to/src"
    target_dir = r"path/to/output"
    suffixes = ["01", "05"]

    copy_images_with_suffix_and_length(src_dir, target_dir, suffixes)

if __name__ == "__main__":
    main()