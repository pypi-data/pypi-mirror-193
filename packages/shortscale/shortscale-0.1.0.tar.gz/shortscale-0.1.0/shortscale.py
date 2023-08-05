"""English conversion from number to string"""
import sys

__version__ = "0.1.0"

def shortscale(num: int) -> str:
  return '{} ({} bits)'.format(num, num.bit_length())


def main():
  if len(sys.argv) < 2:
    print ('Usage: shortscale num')
    sys.exit(1)

  print(shortscale(int(sys.argv[1],0)))
  sys.exit(0)


if __name__ == '__main__':
  main()