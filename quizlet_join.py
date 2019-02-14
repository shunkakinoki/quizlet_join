filenames = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']
with open('output.txt', 'w') as writer:
    readers = [open(filename) for filename in filenames]
    for lines in zip(*readers):
        print(', '.join([line.strip() for line in lines]), file=writer)