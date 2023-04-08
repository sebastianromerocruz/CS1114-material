from sys import argv

DATA_IDX, CLEAN_IDX = 1, 2


if __name__ =="__main__":
    try:
        file = open(argv[DATA_IDX], 'r')
    except FileNotFoundError:
        print(f"ERROR: Could not file file '{argv[DATA_IDX]}.'")
    else:
        clean_file = open(argv[CLEAN_IDX], 'w')

        for line in file:
            line = line.strip().replace('"', '')
            print(line, file=clean_file)
        
        file.close()
        clean_file.close()
