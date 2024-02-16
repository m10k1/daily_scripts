import os

def delete_empty_folders(directory):
    # ディレクトリ内のすべてのアイテムに対してループ
    for foldername, subfolders, filenames in os.walk(directory, topdown=False):
        # 現在のフォルダが空かどうかをチェック
        if not os.listdir(foldername):
            # フォルダが空の場合、削除
            os.rmdir(foldername)
            print(f"空のフォルダ {foldername} を削除しました。")



if __name__ == '__main__':
    directory_path = 'path/to/target'
    delete_empty_folders(directory_path)