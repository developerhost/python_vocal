from spleeter.separator import Separator

def main():
    # 2つのステムに分ける設定('vocals'と'accompaniment')
    separator = Separator('spleeter:2stems')

    # 音声ファイルのパスを指定して分離
    audio_descriptor = 'test.mp3'
    output_directory = 'output_directory'

    # 分離の実行
    separator.separate_to_file(audio_descriptor, output_directory)

if __name__ == '__main__':
    main()
