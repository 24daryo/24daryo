from io import BytesIO
import zipfile
import os
from typing import Any, List
from google.cloud import storage  # pip install google-cloud-storage
import shutil
import datetime
import pandas as pd

today: str = f"{datetime.date.today()}"

# メモ
# - IAMでのアクセス権限があるか確認する
# - 「読み取りはできるが、書き込みできないみたい」なケースが起こり得る

# 事前準備
# 1. Google Cloud StorageのIAMを有効にする
# 2. 有効にしたIAMからサービスアカウントキー(json)を発行
# 3. コード側でバケットとキーを指定


class GoogleCloudStorage:

    def __init__(self):
        bucket_name = 'phj_auto_scraping'
        api_json = "<<<service account json>>>"

        # Initialize
        _dirpath = os.path.dirname(__file__)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"{_dirpath}/{api_json}"
        client: Any = storage.Client()
        bucket = client.get_bucket(bucket_name)

        self._client = client
        self._bucket = bucket
        self.bucket_name = bucket_name

    # def show_bucket_names(self):
    #     """バケット名の一覧を表示
    #     """
    #     [print(bucket.name) for bucket in self._client.list_buckets()]

    def show_bucket_names(self):
        """バケット名の一覧を表示
        """
        [print(bucket.name) for bucket in self._client.list_buckets()]

    def show_file_names(self):
        """バケット内のファイル一覧を表示
        """
        [print(file.name) for file in self._client.list_blobs(self._bucket)]

    def file_names(self):
        """バケット内のファイル一覧を表示
        """
        return [file.name for file in self._client.list_blobs(self._bucket)]

    def upload_file(self, local_path, gcs_path):
        """GCSにローカルファイルをアップロード

        Arguments:
            local_path {str} -- local file path
            gcs_path {str} -- gcs file path
        """
        blob = self._bucket.blob(gcs_path)
        blob.upload_from_filename(local_path)

    def upload_file_as_dataframe(self, df, gcs_path, flg_index=False, flg_header=True):
        """GCSにpd.DataFrameをCSVとしてアップロード

        Arguments:
            df {pd.DataFrame} -- DataFrame for upload
            gcs_path {str} -- gcs file path

        Keyword Arguments:
            flg_index {bool} -- DataFrame index flg (default: {False})
            flg_header {bool} -- DataFrame header flg (default: {True})
        """
        blob = self._bucket.blob(gcs_path)
        blob.upload_from_string(df.to_csv(
            index=flg_index, header=flg_header, sep=","))

    def download_file(self, local_path, gcs_path):
        """GCSのファイルをファイルとしてダウンロード

        Arguments:
            local_path {str} -- local file path
            gcs_path {str} -- gcs file path
        """
        blob = self._bucket.blob(gcs_path)
        blob.download_to_filename(local_path)

    def download_file_as_dataframe(self, gcs_csv_path):
        """GCSのファイルをpd.DataFrameとしてダウンロード

        Arguments:
            gcs_csv_path {str} -- gcs file path (only csv file)

        Returns:
            [pd.DataFrame] -- csv data as pd.DataFrame
        """
        blob = self._bucket.blob(gcs_csv_path)
        content = blob.download_as_string()
        df = pd.read_csv(BytesIO(content))
        return df

    # def upload_file(self, target_path: str, to: str):
    #     # データ送信前にかぶっているかチェック
    #     blob = self._bucket.blob(to)
    #     if blob.exists():
    #         print(f"Google Cloud Strage：{to}は既に存在するため、アップロードを中止しました")
    #         return False
    #     else:
    #         # データを送信
    #         blob.upload_from_filename(target_path)
    #         print(f'Google Cloud Strage：{to}のアップロードが成功しました')
    #         return True

    # def upload_dir_and_compress(self, input_local_dir: str, output_remote_path: str) -> bool:
    #     print("⭐️UPLOAD⭐️")
    #     target_name = os.path.splitext(os.path.basename(input_local_dir))[0]
    #     local_zip_path = f'{input_local_dir}.zip'

    #     if not os.path.exists(input_local_dir):
    #         print(f'{local_zip_path}が見つかりませんでした')
    #         return False

    #     # 送りたいディレクトリを圧縮する
    #     shutil.make_archive(input_local_dir, 'zip', root_dir=input_local_dir)

    #     # アップロード先を作成
    #     remote_zip_path = f"{output_remote_path}/{target_name}.zip"
    #     blob = self.bucket.blob(remote_zip_path)  # to

    #     # データ送信前にかぶっているかチェック
    #     if blob.exists():
    #         print(f"リモートディレクトリ：{remote_zip_path}は既に存在するため、アップロードを中止しました")
    #         return False
    #     else:
    #         # データを送信
    #         blob.upload_from_filename(local_zip_path)
    #         print(f'ローカルディレクトリ：{local_zip_path}のアップロードが成功しました')
    #         return True

    # def download_zip_and_unzip(self, input_remote_zip: str, output_local_dir: str) -> bool:
    #     """GCPのzipファイルをダウンロードし、tmpに解凍して展開する"""

    #     print("⭐️DOWNLOAD⭐️")
    #     # オブジェクトインスタンス作成
    #     blob = self.bucket.blob(input_remote_zip)
    #     if not blob.exists():
    #         print(f'リモートファイル{input_remote_zip}が見つかりませんでした')
    #         return False

    #     # リモートにあるデータをダウンロード
    #     if not os.path.exists(output_local_dir):
    #         os.makedirs(output_local_dir, exist_ok=True)
    #     blob.download_to_filename(f"{output_local_dir}.zip")

    #     # 解凍する
    #     with zipfile.ZipFile(f"{output_local_dir}.zip") as existing_zip:
    #         existing_zip.extractall(f'{output_local_dir}')

    #     print(f'ローカルディレクトリ：{output_local_dir}へダウンロードが成功しました')
    #     return True


# g_storage = GoogleStorage()
# # print(g_storage.filepath())
# # print(g_storage.filepath(prefix="suumo"))
# reins_path = "reins/ver1"
# g_storage.upload_dir_and_compress(
#     input_local_dir=f"./tmp/{today}/fukuoka",
#     output_remote_path=reins_path
# )

# g_storage.download_zip_and_unzip(
#     input_remote_zip=f"{reins_path}/fukuoka.zip",
#     output_local_dir=f"./tmp/{today}/hokkaido"
# )
