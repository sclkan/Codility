import argparse

parser = argparse.ArgumentParser(description= 'Binary Gap')
parser.add_argument('--integer', help='input an integer', default=0, type=int)

args = parser.parse_args()

integer= args.integer

def gap(integer):
    gap = [0]
    count=0
    for i in format(integer,'b'):
        if i == '0':
            count += 1
        else:
            gap.append(count)
            count = 0

    return max(gap)

if __name__ == '__main__':
	print('The binary gap for your entry is: ', gap(integer))