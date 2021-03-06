import sys
import csv
import unicodecsv
import wooly

infilename = "raw_inp.csv"
outfilename = "sanatized_data.csv"
if (len(sys.argv) == 3):
    infilename = sys.argv[1]
    outfilename = sys.argv[2]

print("In: " + infilename + " Out: " + outfilename)

# open out with Binary as well
with open(outfilename, 'w+b') as outputfile:
    with open(infilename, 'rb') as f:
        # reader = csv.DictReader(f)
        reader = unicodecsv.DictReader(f, encoding='utf-8',doublequote=False, escapechar='\\')
        # writer = csv.writer(outputfile, delimiter=',', quotechar='"')
        # removed for BH pull 'industry','industry':indust,
        writer = unicodecsv.DictWriter(outputfile, fieldnames=['chatorder','eventident','chattype','deltamin','anonchat'], encoding='utf-8', quoting=csv.QUOTE_NONNUMERIC)
        # writer.writerow(['organizationident','industry','eventident','eventtype','anondescription'])
        writer.writeheader()
        rownum = 0
        for row in reader:
            #org = row['organizationid']
            # indust = row['industrytype']
            chatorder = row['chatorder']
            event = row['eventid']
            #etype = row['eventtypesummaryname']
            #edate = row['eventdate']
            ctype = row['chatType']
            deltamin = row['deltamin']
            desc = row['chat']
            woolyDesc = wooly.woolyAnonymizer(desc)
            # print(desc)
            # print("Wooly " + woolyDesc)
            rownum = rownum + 1
            if ((rownum % 50) == 0):
                print("Processed row " + str(rownum) + "...")

            writer.writerow({'chatorder':chatorder, 'eventident':event, 'chattype':ctype, 'deltamin':deltamin, 'anonchat':woolyDesc})


