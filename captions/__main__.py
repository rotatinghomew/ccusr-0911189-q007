import argparse
import json
from pathlib import Path

from .workflow import report


def main():
    parser = argparse.ArgumentParser(description='图书馆片头字幕抽看与发行版对照')
    parser.add_argument('operation', choices=['intake'])
    parser.add_argument('records', type=Path, help='业务记录 JSON 文件')
    args = parser.parse_args()
    try:
        output = report(json.loads(args.records.read_text(encoding='utf-8')))
    except (ValueError, OSError, KeyError) as error:
        parser.exit(2, f'无法生成报告：{error}\n')
    print(json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
