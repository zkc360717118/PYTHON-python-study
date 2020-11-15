import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--inputPath', type=str, default = None)
parser.add_argument('--valiPath', type=int, default=32)
args = parser.parse_args()
print(args.inputPath, type(args.inputPath))
print(args.valiPath, type(args.valiPath))