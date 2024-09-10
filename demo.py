from pathlib import Path
import re


def main():
    # 读取文件
    file_path = Path(__file__).parent / 'Y文件样例' / 'Y59205-2022.TXT'
    with open(file_path, 'r', encoding='gbk') as f:
        lines = f.readlines()
    # content_R = re.findall(r'R\n(.*?)=', lines[0])
    index_R = lines.index('R\n')
    print(index_R)

if __name__ == '__main__':
    main()




