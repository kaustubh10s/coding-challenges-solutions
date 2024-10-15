import os, sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="wc command line tool clone")

    parser.add_argument("-c", action="store_true", help="output the number of bytes in a file")
    parser.add_argument("-l", action="store_true", help="outputs the number of lines in a file")
    parser.add_argument("-w", action="store_true", help="outputs the number of words in a file")
    parser.add_argument("-m", action="store_true", help="outputs the number of characters in a file")

    # [TODO] add some functionality to give all outputs when no flag is added
    parser.add_argument("file", nargs="?", help="filepath to be processed")

    return parser

def count_bytes(text):
    print(f"No. of bytes in the file: {os.path.getsize(text)}")

def count_lines(text):
    with open(text, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"No. of lines in the file: {len(lines)}")

def count_words(text):
    with open(text, 'r', encoding='utf-8') as f:
        content = f.read()
    words = content.split()
    print(f"No. of words in the file: {len(words)}")

def count_characters(text):
    with open(text, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"No of characters in the file: {len(content)}")

def count_all(text):
    count_bytes(text)
    print("\n")
    count_lines(text)
    print("\n")
    count_words(text)
    print("\n")
    count_characters(text)

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.file:
        file = args.file
    else: 
        file = sys.stdin.read()

    if args.c:
        count_bytes(file)
    if args.l:
        count_lines(file)
    if args.w:
        count_words(file)
    if args.m:
        count_characters(file)
    
    # handle the case when no flag is given
    if not (args.c or args.l or args.w or args.m):
        count_all(file)


if __name__ == "__main__":
    main()    