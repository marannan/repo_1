import sys
import csv
import re


def main():

    f = open("reviews.csv", 'wt')
    try:
        writer = csv.writer(f)
        writer.writerow( ('reviews',) )
        with open("reviews_only.txt") as reviews_text_file:
            #for line in reviews_text_file:
            lines = reviews_text_file.readlines()
            a="'hel,lo'"
            for line in lines:
                #re.sub("\\s+",'', line)
                print line
                writer.writerow( (line[1:-1],) )
                #sys.exit(0)


    finally:
        f.close()


    # f = open("sample.csv", 'wt')
    # try:
    #     writer = csv.writer(f)
    #     writer.writerow( ('Title 1', 'Title 2', 'Title 3') )
    #     for i in range(10):
    #         writer.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)) )
    # finally:
    #     f.close()

if __name__ == "__main__":
    main()