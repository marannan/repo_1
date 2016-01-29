__author__ = 'manojn'
import csv
import re
data_file1 = "Guidestar/guidestar_990/f990_Part_III.txt"
data_file2 = "Guidestar/guidestar_990/f990_Part_III_Achievements.txt"
data_file3 = "f990_Sched_I_Part_II_Gov_Grant.txt"
data_file4 = "org_purpose.csv"
data_file5 = "Guidestar/guidestar_990/BMF.txt"
data_file6 = "devdict_brent_edited.csv"
row_no = 1
science_dict = ["science", "research", "technology"]
#science_dict = ["science"]

maindict = {}
row_no =1
with open(data_file6, 'rb') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csv_reader:
        #print row
        #print "printing item::::::::::::::::::::::::::::"
        #for item in row:
        #    print item
        if row_no == 1:
            row_no = row_no + 1
        else:
            if str(row[0].lower()) not in maindict:
                maindict[str(row[0]).lower()] = {}
                count = 0
                for val in row:
                    #print count,val
                    count += 1
                maindict[str(row[0]).lower()]['EIN'] = str(row[1])
                maindict[str(row[0]).lower()]['NTEECC'] = str(row[2])
                maindict[str(row[0]).lower()]['ACT_CODE'] = str(row[3])
                maindict[str(row[0]).lower()]['PURPOSE'] = str(row[7])
                maindict[str(row[0]).lower()]['SERVICE A'] = str(row[8])
                maindict[str(row[0]).lower()]['SERVICE B'] = str(row[9])
                maindict[str(row[0]).lower()]['SERVICE C'] = str(row[10])
                maindict[str(row[0]).lower()]['ACTUAL_CLASS'] = str(row[5])


#
# maindict = {}
# with open(data_file1, 'rb') as csvfile:
#     csv_reader = csv.reader(csvfile, delimiter='|', quotechar='"')
#     for row in csv_reader:
#         #print row
#         #print "printing item::::::::::::::::::::::::::::"
#         #for item in row:
#         #    print item
#         if row_no == 1:
#             row_no = row_no + 1
#         else:
#             if str(row[1].lower()) in devdict:
#                 if str(row[1].lower()) not in maindict:
#                     maindict[str(row[1]).lower()] = {}
#                     maindict[str(row[1]).lower()]['ORG_NAME']= str(row[0])
#                     # maindict[str(row[0])]['PURPOSE']= []
#                     # maindict[str(row[0])]['SERVICE A']= []
#                     # maindict[str(row[0])]['SERVICE B']= []
#                     # maindict[str(row[0])]['SERVICE C']= []
#                     maindict[str(row[1]).lower()]['NTEECC'] = ""
#                     maindict[str(row[1]).lower()]['ACT_CODE'] = ""
#
#
#                 # if not str(row[7]) == None and not any(val.lower()  == str(row[3]).lower()  for val in maindict[str(row[0])]['PURPOSE']):
#                 #     maindict[str(row[0])]['PURPOSE'].append(str(row[3]))
#
#                 if not 'PURPOSE' in maindict[str(row[1]).lower()]:
#                     maindict[str(row[1]).lower()]['PURPOSE'] = str(row[3])
#
# row_no = 1
# with open(data_file2, 'rb') as csvfile:
#     csv_reader = csv.reader(csvfile, delimiter='|', quotechar='"')
#     for row in csv_reader:
#         if row_no == 1:
#             row_no = row_no + 1
#         else:
#             if str(row[1].lower()) in devdict:
#
#                 if str(row[1].lower()) not in maindict:
#                     maindict[str(row[1]).lower()] = {}
#                     maindict[str(row[1]).lower()]['ORG_NAME']= str(row[0])
#                     # maindict[str(row[0])]['PURPOSE']= []
#                     # maindict[str(row[0])]['SERVICE A']= []
#                     # maindict[str(row[0])]['SERVICE B']= []
#                     # maindict[str(row[0])]['SERVICE C']= []
#                     maindict[str(row[1]).lower()]['NTEECC'] = ""
#                     maindict[str(row[1]).lower()]['ACT_CODE'] = ""
#
#
#                 # if not str(row[7]) == None and not any(val.lower()  == str(row[7]).lower()  for val in maindict[str(row[0])]['SERVICE A']):
#                 #     maindict[str(row[0])]['SERVICE A'].append(str(row[7]))
#                 # if not str(row[7]) == None and not any(val.lower()  == str(row[12]).lower()  for val in maindict[str(row[0])]['SERVICE B']):
#                 #     maindict[str(row[0])]['SERVICE B'].append(str(row[12]))
#                 # if not str(row[7]) == None and not any(val.lower()  == str(row[17]).lower()  for val in maindict[str(row[0])]['SERVICE C']):
#                 #     maindict[str(row[0])]['SERVICE C'].append(str(row[17]))
#                 if not 'SERVICE A' in maindict[str(row[1]).lower()]:
#                     maindict[str(row[1]).lower()]['SERVICE A'] = str(row[7])
#                 if not 'SERVICE B' in maindict[str(row[1]).lower()]:
#                     maindict[str(row[1]).lower()]['SERVICE B'] = str(row[12])
#                 if not 'SERVICE C' in maindict[str(row[1]).lower()]:
#                     maindict[str(row[1]).lower()]['SERVICE C'] = str(row[17])
#
# nteeccdict = {}
# row_no = 1
# with open(data_file4, 'rb') as csvfile:
#     csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#     for row in csv_reader:
#         if row_no == 1:
#             row_no = row_no + 1
#         else: #7 and 10
#             #print val, str(row[7]).lower()
#             #if val == str(row[7]).lower():
#             #    print "match"
#             nteeccdict[str(row[7]).lower()] = str(row[10])
# print "done creating nteecc dict"
# #print nteeccdict
#
# act_code_dict = {}
# row_no = 1
# with open(data_file5, 'rb') as csvfile:
#     csv_reader = csv.reader(csvfile, delimiter='|', quotechar='"')
#     for row in csv_reader:
#         if row_no == 1:
#             row_no = row_no + 1
#         else: #7 and 10
#             #print val, str(row[7]).lower()
#             #if val == str(row[7]).lower():
#             #    print "match"
#             act_code_dict[str(row[1]).lower()] = str(row[13])
# print "done creating act_code dict"
#
# row_no = 1
# count = 0
# for val in maindict:
#     #print len(maindict),count
#     if val in nteeccdict:
#         #print "match"
#         count+=1
#         maindict[val]['NTEECC'] = nteeccdict[val]
# print "done finding the NTEECC values for the list with count:{} matched from {}".format(count,len(maindict))
#
# row_no = 1
# count = 0
# for val in maindict:
#     #print len(maindict),count
#     if val in act_code_dict and not act_code_dict[val] == "":
#         #print "match"
#         count+=1
#         maindict[val]['ACT_CODE'] = act_code_dict[val]
# print "done finding the activity code values for the list with count:{} matched from {}".format(count,len(maindict))
tp = 0
fp = 0
tn = 0
fn = 0
act_code_science_list = ["161","162","180","181","182","209","230","236","351","529"];
with open('devdict_classified.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
        quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["ORG_NAME","EIN","NTEECC","ACT_CODE", "WEIGHT","ACTUAL_CLASS","PREDICTED_CLASS","PURPOSE", "SERVICE A", "SERVICE B", "SERVICE C"])
        # for val in maindict:
        #     count = 0
        #     for val1 in science_dict:
        #         for val2 in maindict[val]["PURPOSE"]:
        #             if val1 in val2:
        #                 count+=1
        #         for val2 in maindict[val]["SERVICE A"]:
        #             if val1 in val2:
        #                 count+=1
        #         for val2 in maindict[val]["SERVICE B"]:
        #             if val1 in val2:
        #                 count+=1
        #         for val2 in maindict[val]["SERVICE C"]:
        #             if val1 in val2:
        #                 count+=1
        #for val in maindict:
            #print maindict[val]['ACT_CODE']
        for val in maindict:
            count = 0
            #regex = 'Weight[^:;,.]*?:[^:,.]*?\s*-*([0-9]+\.*[0-9]*)\s*((?:g|tons|ton|lbs|lb|pounds|pound|ounce|oz|gram|grams)*(?:/cm2|/m2|/m|/cm|/mm|/mm2)*(?:\&sup2)*)\s*[\.|<>]*'
            if re.match(r'(?:H[0-9A-Z]{2}|U[0-9A-Z]{2})',maindict[val]['NTEECC']):
                count = 2000
            #any(val.lower()  == str(row[3]).lower()  for val in maindict[str(row[0])]['PURPOSE'])
            elif any(tempval == maindict[val]['ACT_CODE'][0] for tempval in act_code_science_list):
                count = 1000

            # elif any(tempval == tempval1 for tempval in act_code_science_list for tempval1 in maindict[val]['ACT_CODE']):
            #     count = 1000


            for val1 in maindict[val]:
                if not val1 == 'ORG_NAME' and not val1 == 'ACT_CODE' and not val1== 'NTEECC':
                    c1 = 0
                    c2 = 0
                    c3 = 0
                    c4 = 0
                    c5 = 0
                    c6 = 0

                    for val2 in science_dict:
                        #print val,val1,val2,
                        if val2 in maindict[val][val1]:
                            if val2 == 'science': c1+=1
                            elif val2 == 'research': c2+=1
                            elif val2 == 'education': c3+=1
                            elif val2 == 'training': c4+=1
                            elif val2 == 'technology': c5+=1
                            else: c6+=1
                    #C60, E70, E91, H*, K*, U*, V*,
                    if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
                        count+=20
                    elif (c1>0 and c2>0 and c3>0) or (c1>0 and c2>0 and c4>0) or (c1>0 and c2>0 and c5>0) or (c1>0 and c4>0 and c5>0) or (c1>0 and c3>0 and c5>0) or (c1>0 and c2>0 and c5>0) or (c2>0 and c3>0 and c4>0) or (c2>0 and c3>0 and c5>0) or (c2>0 and c4>0 and c5>0) or (c3>0 and c4>0 and c5>0):
                        count+=10
                    elif (c1>0 and c2>0) or (c1>0 and c3>0) or (c1>0 and c4>0) or (c1>0 and c5>0) or (c2>0 and c3>0) or (c2>0 and c4>0) and (c2>0 and c5>0) or (c3>0 and c4>0) or (c3>0 and c5>0) or (c4>0 and c5>0):
                        count+=5
                    elif c1>0 or c2>0 or c5>0:
                        count+=3
                    elif c3>0 or c4>0:
                        count+=2
                    elif c6>0:
                        count+=1
                    # if val2 == 'science' and val2 == 'research' and val2 == 'education':
                    #     count+=10
                    # elif (val2 == 'science' and val2 == 'research') or (val2 == 'science' and val2 == 'education') or (val2 == 'education' and val2 == 'research'):
                    #     count+=5
                    # elif val2 == 'education' and val2 == 'training':
                    #     count+=4
                    # elif val2 == 'science' or val2 == 'research':
                    #     count+=3
                    # elif val2 == 'education' or val2 == 'training':
                    #     count+=2
                    # else:
                    #     count+=1
#science_dict = ["science", "research", "education", "training", "certification", "accreditation", "exploration"]

            if count >= 1000:
                csv_writer.writerow([val,maindict[val]["EIN"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],count,maindict[val]["ACTUAL_CLASS"],1,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"],maindict[val]["SERVICE B"],maindict[val]["SERVICE C"]])
                if maindict[val]["ACTUAL_CLASS"] == '1':
                    tp+=1
                else:
                    fp+=1

            elif count >= 5:
                csv_writer.writerow([val,maindict[val]["EIN"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],count,maindict[val]["ACTUAL_CLASS"],1,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"],maindict[val]["SERVICE B"],maindict[val]["SERVICE C"]])
                if maindict[val]["ACTUAL_CLASS"] == '1':
                    tp+=1
                else:
                    fp+=1
            else:
                csv_writer.writerow([val,maindict[val]["EIN"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],count,maindict[val]["ACTUAL_CLASS"],0,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"],maindict[val]["SERVICE B"],maindict[val]["SERVICE C"]])
                if maindict[val]["ACTUAL_CLASS"] == '0':
                    tn+=1
                else:
                    fn+=1
print tp,fp,tn,fn
accuracy = 100*float(tp+tn)/float(tp+tn+fp+fn)
recall = 100*float(tp)/float(tp+fn)
precision = 100*float(tp)/float(tp+fp)
print " accuracy:{}, recall:{}, precision: {}".format(accuracy,recall,precision)


