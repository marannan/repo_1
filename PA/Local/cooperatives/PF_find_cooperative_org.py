__author__ = 'manojn'
import csv
import re
import os
data_file1 = "Guidestar/guidestar_990PF/PF990_Part_IX_Investments.txt"
data_file2 = "Guidestar/guidestar_990PF/PF990_Part_IX_Activities.txt"
data_file4 = "org_purpose.csv"
data_file5 = "Guidestar/guidestar_990PF/BMF.txt"
data_file6 = "devdict.csv"
bmffolder = "./BMF/"
row_no = 1
include_code = 0 #1 for yes, 0 for no. NTEECC and activity codes
science_dict = ["member", ["association","assn","assoc","associa","associate"], "coopertive", "league", ["fraternal","frater"],"chamber", "legion", "society", "ymca", "club", "post", "consortium"]
#science_dict = ["science"]
maindict = {}
with open(data_file1, 'rb') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter='|', quotechar='"')
    for row in csv_reader:
        #print row
        #print "printing item::::::::::::::::::::::::::::"
        #for item in row:
        #    print item
        if row_no == 1:
            row_no = row_no + 1
        else:
            if str(row[1].lower()) not in maindict:
                maindict[str(row[1]).lower()] = {}
                maindict[str(row[1]).lower()]['ORG_NAME']= str(row[0])
                # maindict[str(row[0])]['PURPOSE']= []
                # maindict[str(row[0])]['SERVICE A']= []
                # maindict[str(row[0])]['SERVICE B']= []
                # maindict[str(row[0])]['SERVICE C']= []
                maindict[str(row[1]).lower()]['NTEECC'] = ""
                maindict[str(row[1]).lower()]['ACT_CODE'] = []
                maindict[str(row[1]).lower()]['PURPOSE'] = ""
                maindict[str(row[1]).lower()]['SERVICE A'] = ""

            # if not str(row[7]) == None and not any(val.lower()  == str(row[3]).lower()  for val in maindict[str(row[0])]['PURPOSE']):
            #     maindict[str(row[0])]['PURPOSE'].append(str(row[3]))

            #if not 'PURPOSE' in maindict[str(row[1]).lower()]:
            maindict[str(row[1]).lower()]['PURPOSE'] = str(row[4])

row_no = 1
with open(data_file2, 'rb') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter='|', quotechar='"')
    for row in csv_reader:
        if row_no == 1:
            row_no = row_no + 1
        else:
            if str(row[1].lower()) not in maindict:
                maindict[str(row[1]).lower()] = {}
                maindict[str(row[1]).lower()]['ORG_NAME']= str(row[0])
                # maindict[str(row[0])]['PURPOSE']= []
                # maindict[str(row[0])]['SERVICE A']= []
                # maindict[str(row[0])]['SERVICE B']= []
                # maindict[str(row[0])]['SERVICE C']= []
                maindict[str(row[1]).lower()]['NTEECC'] = ""
                maindict[str(row[1]).lower()]['ACT_CODE'] = []
                maindict[str(row[1]).lower()]['PURPOSE'] = ""
                maindict[str(row[1]).lower()]['SERVICE A'] = ""


            # if not str(row[7]) == None and not any(val.lower()  == str(row[7]).lower()  for val in maindict[str(row[0])]['SERVICE A']):
            #     maindict[str(row[0])]['SERVICE A'].append(str(row[7]))
            # if not str(row[7]) == None and not any(val.lower()  == str(row[12]).lower()  for val in maindict[str(row[0])]['SERVICE B']):
            #     maindict[str(row[0])]['SERVICE B'].append(str(row[12]))
            # if not str(row[7]) == None and not any(val.lower()  == str(row[17]).lower()  for val in maindict[str(row[0])]['SERVICE C']):
            #     maindict[str(row[0])]['SERVICE C'].append(str(row[17]))
            #if not 'SERVICE A' in maindict[str(row[1]).lower()]:
            maindict[str(row[1]).lower()]['SERVICE A'] = str(row[4])
            # if not 'SERVICE B' in maindict[str(row[1]).lower()]:
            #     maindict[str(row[1]).lower()]['SERVICE B'] = None
            # if not 'SERVICE C' in maindict[str(row[1]).lower()]:
            #     maindict[str(row[1]).lower()]['SERVICE C'] = None

nteeccdict = {}
row_no = 1
with open(data_file4, 'rb') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csv_reader:
        if row_no == 1:
            row_no = row_no + 1
        else: #7 and 10
            #print val, str(row[7]).lower()
            #if val == str(row[7]).lower():
            #    print "match"
            nteeccdict[str(row[7]).lower()] = str(row[10])
print "done creating nteecc dict from org_purpose.csv"

bmffiles = os.listdir(bmffolder)
for val in bmffiles:
    if re.match(r'BMF-.*\.csv',val):
        row_no = 1
        print "opening file: {}".format(str(val))
        with open(bmffolder+val, 'rb') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csv_reader:
                if row_no == 1:
                    row_no = row_no + 1
                else: #7 and 10
                    #print val, str(row[7]).lower()
                    #if val == str(row[7]).lower():
                    #print str(row[0])
        #            print str(row[1]).lower(), str(row[4])
                    nteeccdict[str(row[1]).lower()] = str(row[4])
print "done creating nteecc dict from bmf files"


#print nteeccdict

act_code_dict = {}
row_no = 1
with open(data_file5, 'rb') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter='|', quotechar='"')
    for row in csv_reader:
        if row_no == 1:
            row_no = row_no + 1
        else: #7 and 10
            #print val, str(row[7]).lower()
            #if val == str(row[7]).lower():
            #    print "match"
            act_code_dict[str(row[1]).lower()]=[]
            act_code_dict[str(row[1]).lower()].append(str(row[13]))
            act_code_dict[str(row[1]).lower()].append(str(row[14]))
            act_code_dict[str(row[1]).lower()].append(str(row[15]))
print "done creating act_code dict"

row_no = 1
count = 0
for val in maindict:
    #print len(maindict),count
    if val in nteeccdict:
        #print "match"
        count+=1
        maindict[val]['NTEECC'] = nteeccdict[val]
print "done finding the NTEECC values for the list with count:{} matched from {}".format(count,len(maindict))

row_no = 1
count = 0
for val in maindict:
    #print len(maindict),count
    if val in act_code_dict and not act_code_dict[val] == ["","",""]:
        #print "match"
        count+=1
        maindict[val]['ACT_CODE'] = act_code_dict[val]
    else:
        maindict[val]['ACT_CODE'] = [""]
print "done finding the activity code values for the list with count:{} matched from {}".format(count,len(maindict))

print maindict

#act_code_science_list = ["161","162","180","181","182","209","230","236","351","529"];
act_code_science_list = ['002', '033', '034', '035', '036', '037', '038', '088', '157', '167', '168', '201', '202', '203', '205', '210', '229', '230', '231', '232', '233', '234', '235', '236', '237', '249', '250', '251', '252', '253', '254', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '296', '297', '298', '299', '300', '301', '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327', '328', '349', ' 350', '351', '352', '353', '354', '355', '356', '379', ' 380', '381', '382', '398', '399', '400', '401', '402', '403', '404', '405', '406', '407', '408', '429']

with open('coop_pf_dict.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
        quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["ORG_NAME","EIN","NTEECC","ACT_CODE", "TITLE WEIGHT","WEIGHT","WEIGHT1","WEIGHT2","PREDICTION","PURPOSE", "ACTIVITY"])
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
            count1 = 0
            count2 = 0
            count = 0
            titlecount = 0
            #regex = 'Weight[^:;,.]*?:[^:,.]*?\s*-*([0-9]+\.*[0-9]*)\s*((?:g|tons|ton|lbs|lb|pounds|pound|ounce|oz|gram|grams)*(?:/cm2|/m2|/m|/cm|/mm|/mm2)*(?:\&sup2)*)\s*[\.|<>]*'
            #if re.match(r'(?:H[0-9A-Z]{2}|U[0-9A-Z]{2})',maindict[val]['NTEECC']):
            if re.match(r'(?:L[0-9A-Z]{2}|Y[0-9A-Z]{2}|O[0-9A-Z]{2}|C[0-9A-Z]{2}|S[0-9A-Z]{2}|N[0-9A-Z]{2}|K12|B99|D30|D31|D32|D33|D34|B94|J40|X03|W20|I72|I73|P75|Q99|W60|P27|B83|K28|B80|K20|I71|I72|I73|K26|B84|K25|D60|P70|A65|Y99|K99)',maindict[val]['NTEECC']):
                count += 1
                count1 += 1
            #any(val.lower()  == str(row[3]).lower()  for val in maindict[str(row[0])]['PURPOSE'])
            if any(tempval == maindict[val]['ACT_CODE'][0] for tempval in act_code_science_list):
                count += 1
                count1 += 1

            # elif any(tempval == tempval1 for tempval in act_code_science_list for tempval1 in maindict[val]['ACT_CODE']):
            #     count = 1000
            for tval in science_dict:
                if type(tval) == str:
                    if tval.lower() in str(val).lower():
                        titlecount+=1
                else:
                    for tval1 in tval:
                        if str(tval1).lower() in str(val).lower():
                            titlecount+=1
                            break

            for val1 in maindict[val]:
                if not val1 == 'ORG_NAME' and not val1 == 'ACT_CODE' and not val1== 'NTEECC':
                    for val2 in science_dict:
                        if type(val2) == str:
                            if val2.lower() in str(maindict[val][val1]).lower():
                                count1+=1
                                count2+=1
                        else:
                            for val3 in val2:
                                if str(val3).lower() in str(maindict[val][val1]).lower():
                                    count1+=1
                                    count2+=1
                    # c1 = 0
                    # c2 = 0
                    # c3 = 0
                    # c4 = 0
                    # c5 = 0
                    # c6 = 0
                    #
                    # for val2 in science_dict:
                    #     #print val,val1,val2,
                    #     if type(val2) == str:
                    #         if val2 in maindict[val][val1]:
                    #             #science_dict = ["member", ["association","assn","assoc","associa","associate"], "coopertive", "league", ["fraternal","frater"],"chamber", "legion", "society", "ymca", "club", "post", "consortium"]
                    #             if val2 == 'cooperative': c1+=1
                    #             elif val2 == 'association': c2+=1
                    #             elif val2 == 'member': c3+=1
                    #             elif val2 == 'fraternal': c4+=1
                    #             elif val2 == 'league': c5+=1
                    #             else: c6+=1
                    #     else:
                    #         for val3 in val2:
                    #             if val3 in maindict[val][val1]:
                    #                 #science_dict = ["member", "association", "coopertive", "league", "fraternal"]
                    #                 if "coop" in val3: c1+=1
                    #                 elif 'ass' in val3: c2+=1
                    #                 elif 'memb' in val3: c3+=1
                    #                 elif 'frat' in val3: c4+=1
                    #                 elif 'leag' in val3: c5+=1
                    #                 else: c6+=1
                    #
                    # #C60, E70, E91, H*, K*, U*, V*,
                    # if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
                    #     count1+=20
                    #     count2+=20
                    # elif (c1>0 and c2>0 and c3>0) or (c1>0 and c2>0 and c4>0) or (c1>0 and c2>0 and c5>0) or (c1>0 and c4>0 and c5>0) or (c1>0 and c3>0 and c5>0) or (c1>0 and c2>0 and c5>0) or (c2>0 and c3>0 and c4>0) or (c2>0 and c3>0 and c5>0) or (c2>0 and c4>0 and c5>0) or (c3>0 and c4>0 and c5>0):
                    #     count1+=10
                    #     count2+=10
                    # elif (c1>0 and c2>0) or (c1>0 and c3>0) or (c1>0 and c4>0) or (c1>0 and c5>0) or (c2>0 and c3>0) or (c2>0 and c4>0) and (c2>0 and c5>0) or (c3>0 and c4>0) or (c3>0 and c5>0) or (c4>0 and c5>0):
                    #     count1+=5
                    #     count2+=5
                    # elif c1>0 or c2>0 or c5>0:
                    #     count1+=3
                    #     count2+=3
                    # elif c3>0 or c4>0:
                    #     count1+=2
                    #     count2+=2
                    # elif c6>0:
                    #     count1+=1
                    #     count2+=1

            #includes activity code and nteecc code
            if include_code == 1:
                if (count1 > 2000 or (count1 > 1000 and count1 < 2000)) and titlecount > 0:
                    csv_writer.writerow([val,maindict[val]["ORG_NAME"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],titlecount, count,count1,count2,4,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"]])
                elif count2>0 and titlecount > 0:
                    csv_writer.writerow([val,maindict[val]["ORG_NAME"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],titlecount, count,count1,count2,3,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"]])
                elif ((count >= 2000 or (count >= 1000 and count < 2000)) or count2>0) and titlecount > 0:
                    csv_writer.writerow([val,maindict[val]["ORG_NAME"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],titlecount, count,count1,count2,2,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"]])
                elif (count >= 2000 or (count >= 1000 and count < 2000)) or count2>0 or titlecount > 0:
                    csv_writer.writerow([val,maindict[val]["ORG_NAME"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],titlecount, count,count1,count2,1,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"]])
                else:
                    csv_writer.writerow([val,maindict[val]["ORG_NAME"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],titlecount, count,count1,count2,0,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"]])

            #dont include:
            else:
                if count2 > 0 and titlecount > 0:
                    csv_writer.writerow([val,maindict[val]["ORG_NAME"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],titlecount, count,count1,count2,2,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"]])
                elif count2>0 or titlecount > 0:
                    csv_writer.writerow([val,maindict[val]["ORG_NAME"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],titlecount, count,count1,count2,1,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"]])
                else:
                    csv_writer.writerow([val,maindict[val]["ORG_NAME"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],titlecount, count,count1,count2,0,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"]])

            # if count >= 1000:
            #     if count >= 1000:
            #         csv_writer.writerow([val,maindict[val]["ORG_NAME"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],titlecount, count,count1,count2,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"],maindict[val]["SERVICE B"],maindict[val]["SERVICE C"]])
            # elif count >= 0:
            #     csv_writer.writerow([val,maindict[val]["ORG_NAME"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],titlecount, count,count1,count2,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"],maindict[val]["SERVICE B"],maindict[val]["SERVICE C"]])
            # #csv_writer.writerow([val,maindict[val]["ORG_NAME"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],titlecount, count,count1,count2,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"],maindict[val]["SERVICE B"],maindict[val]["SERVICE C"]])

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# __author__ = 'manojn'
# import csv
# import re
# import os
# data_file1 = "Guidestar/guidestar_990/f990_Part_III.txt"
# data_file2 = "Guidestar/guidestar_990/f990_Part_III_Achievements.txt"
# data_file3 = "f990_Sched_I_Part_II_Gov_Grant.txt"
# data_file4 = "org_purpose.csv"
# data_file5 = "Guidestar/guidestar_990/BMF.txt"
# data_file6 = "devdict.csv"
# bmffolder = "./BMF/"
# row_no = 1
# science_dict = ["member", "association", "coopertive", "league", "fraternal"]
# #science_dict = ["science"]
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
#             if str(row[1].lower()) not in maindict:
#                 maindict[str(row[1]).lower()] = {}
#                 maindict[str(row[1]).lower()]['ORG_NAME']= str(row[0])
#                 # maindict[str(row[0])]['PURPOSE']= []
#                 # maindict[str(row[0])]['SERVICE A']= []
#                 # maindict[str(row[0])]['SERVICE B']= []
#                 # maindict[str(row[0])]['SERVICE C']= []
#                 maindict[str(row[1]).lower()]['NTEECC'] = ""
#                 maindict[str(row[1]).lower()]['ACT_CODE'] = []
#
#
#             # if not str(row[7]) == None and not any(val.lower()  == str(row[3]).lower()  for val in maindict[str(row[0])]['PURPOSE']):
#             #     maindict[str(row[0])]['PURPOSE'].append(str(row[3]))
#
#             if not 'PURPOSE' in maindict[str(row[1]).lower()]:
#                 maindict[str(row[1]).lower()]['PURPOSE'] = str(row[3])
#
# row_no = 1
# with open(data_file2, 'rb') as csvfile:
#     csv_reader = csv.reader(csvfile, delimiter='|', quotechar='"')
#     for row in csv_reader:
#         if row_no == 1:
#             row_no = row_no + 1
#         else:
#             if str(row[1].lower()) not in maindict:
#                 maindict[str(row[1]).lower()] = {}
#                 maindict[str(row[1]).lower()]['ORG_NAME']= str(row[0])
#                 # maindict[str(row[0])]['PURPOSE']= []
#                 # maindict[str(row[0])]['SERVICE A']= []
#                 # maindict[str(row[0])]['SERVICE B']= []
#                 # maindict[str(row[0])]['SERVICE C']= []
#                 maindict[str(row[1]).lower()]['NTEECC'] = ""
#                 maindict[str(row[1]).lower()]['ACT_CODE'] = []
#
#
#             # if not str(row[7]) == None and not any(val.lower()  == str(row[7]).lower()  for val in maindict[str(row[0])]['SERVICE A']):
#             #     maindict[str(row[0])]['SERVICE A'].append(str(row[7]))
#             # if not str(row[7]) == None and not any(val.lower()  == str(row[12]).lower()  for val in maindict[str(row[0])]['SERVICE B']):
#             #     maindict[str(row[0])]['SERVICE B'].append(str(row[12]))
#             # if not str(row[7]) == None and not any(val.lower()  == str(row[17]).lower()  for val in maindict[str(row[0])]['SERVICE C']):
#             #     maindict[str(row[0])]['SERVICE C'].append(str(row[17]))
#             if not 'SERVICE A' in maindict[str(row[1]).lower()]:
#                 maindict[str(row[1]).lower()]['SERVICE A'] = str(row[7])
#             if not 'SERVICE B' in maindict[str(row[1]).lower()]:
#                 maindict[str(row[1]).lower()]['SERVICE B'] = str(row[12])
#             if not 'SERVICE C' in maindict[str(row[1]).lower()]:
#                 maindict[str(row[1]).lower()]['SERVICE C'] = str(row[17])
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
# print "done creating nteecc dict from org_purpose.csv"
#
# bmffiles = os.listdir(bmffolder)
# for val in bmffiles:
#     if re.match(r'BMF-.*\.csv',val):
#         row_no = 1
#         print "opening file: {}".format(str(val))
#         with open(bmffolder+val, 'rb') as csvfile:
#             csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#             for row in csv_reader:
#                 if row_no == 1:
#                     row_no = row_no + 1
#                 else: #7 and 10
#                     #print val, str(row[7]).lower()
#                     #if val == str(row[7]).lower():
#                     #print str(row[0])
#         #            print str(row[1]).lower(), str(row[4])
#                     nteeccdict[str(row[1]).lower()] = str(row[4])
# print "done creating nteecc dict from bmf files"
#
#
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
#             act_code_dict[str(row[1]).lower()]=[]
#             act_code_dict[str(row[1]).lower()].append(str(row[13]))
#             act_code_dict[str(row[1]).lower()].append(str(row[14]))
#             act_code_dict[str(row[1]).lower()].append(str(row[15]))
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
#     if val in act_code_dict and not act_code_dict[val] == ["","",""]:
#         #print "match"
#         count+=1
#         maindict[val]['ACT_CODE'] = act_code_dict[val]
#     else:
#         maindict[val]['ACT_CODE'] = [""]
# print "done finding the activity code values for the list with count:{} matched from {}".format(count,len(maindict))
#
# #act_code_science_list = ["161","162","180","181","182","209","230","236","351","529"];
# act_code_science_list = ['002', '033', '034', '035', '036', '037', '038', '088', '157', '167', '168', '201', '202', '203', '205', '210', '229', '230', '231', '232', '233', '234', '235', '236', '237', '249', '250', '251', '252', '253', '254', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '296', '297', '298', '299', '300', '301', '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327', '328', '349', ' 350', '351', '352', '353', '354', '355', '356', '379', ' 380', '381', '382', '398', '399', '400', '401', '402', '403', '404', '405', '406', '407', '408', '429']
#
# with open('coopdict.csv', 'wb') as csvfile:
#         csv_writer = csv.writer(csvfile, delimiter=',',
#         quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow(["ORG_NAME","EIN","NTEECC","ACT_CODE", "WEIGHT","WEIGHT1","WEIGHT2","PURPOSE", "SERVICE A", "SERVICE B", "SERVICE C"])
#         # for val in maindict:
#         #     count = 0
#         #     for val1 in science_dict:
#         #         for val2 in maindict[val]["PURPOSE"]:
#         #             if val1 in val2:
#         #                 count+=1
#         #         for val2 in maindict[val]["SERVICE A"]:
#         #             if val1 in val2:
#         #                 count+=1
#         #         for val2 in maindict[val]["SERVICE B"]:
#         #             if val1 in val2:
#         #                 count+=1
#         #         for val2 in maindict[val]["SERVICE C"]:
#         #             if val1 in val2:
#         #                 count+=1
#         #for val in maindict:
#             #print maindict[val]['ACT_CODE']
#         for val in maindict:
#             count1 = 0
#             count2 = 0
#             count = 0
#             #regex = 'Weight[^:;,.]*?:[^:,.]*?\s*-*([0-9]+\.*[0-9]*)\s*((?:g|tons|ton|lbs|lb|pounds|pound|ounce|oz|gram|grams)*(?:/cm2|/m2|/m|/cm|/mm|/mm2)*(?:\&sup2)*)\s*[\.|<>]*'
#             #if re.match(r'(?:H[0-9A-Z]{2}|U[0-9A-Z]{2})',maindict[val]['NTEECC']):
#             if re.match(r'(?:L[0-9A-Z]{2}|Y[0-9A-Z]{2}|O[0-9A-Z]{2}|C[0-9A-Z]{2}|S[0-9A-Z]{2}|N[0-9A-Z]{2}|K12|B99|D30|D31|D32|D33|D34|B94|J40|X03|W20|I72|I73|P75|Q99|W60|P27|B83|K28|B80|K20|I71|I72|I73|K26|B84|K25|D60|P70|A65|Y99|K99)',maindict[val]['NTEECC']):
#                 count = 2000
#                 count1 = 2000
#             #any(val.lower()  == str(row[3]).lower()  for val in maindict[str(row[0])]['PURPOSE'])
#             elif any(tempval == maindict[val]['ACT_CODE'][0] for tempval in act_code_science_list):
#                 count = 1000
#                 count1 = 1000
#
#             # elif any(tempval == tempval1 for tempval in act_code_science_list for tempval1 in maindict[val]['ACT_CODE']):
#             #     count = 1000
#
#
#             for val1 in maindict[val]:
#                 if not val1 == 'ORG_NAME' and not val1 == 'ACT_CODE' and not val1== 'NTEECC':
#                     c1 = 0
#                     c2 = 0
#                     c3 = 0
#                     c4 = 0
#                     c5 = 0
#                     c6 = 0
#
#                     for val2 in science_dict:
#                         #print val,val1,val2,
#                         if val2 in maindict[val][val1]:
#                             #science_dict = ["member", "association", "coopertive", "league", "fraternal"]
#                             if val2 == 'cooperative': c1+=1
#                             elif val2 == 'association': c2+=1
#                             elif val2 == 'member': c3+=1
#                             elif val2 == 'fraternal': c4+=1
#                             elif val2 == 'league': c5+=1
#                             else: c6+=1
#                     #C60, E70, E91, H*, K*, U*, V*,
#                     if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
#                         count1+=20
#                         count2+=20
#                     elif (c1>0 and c2>0 and c3>0) or (c1>0 and c2>0 and c4>0) or (c1>0 and c2>0 and c5>0) or (c1>0 and c4>0 and c5>0) or (c1>0 and c3>0 and c5>0) or (c1>0 and c2>0 and c5>0) or (c2>0 and c3>0 and c4>0) or (c2>0 and c3>0 and c5>0) or (c2>0 and c4>0 and c5>0) or (c3>0 and c4>0 and c5>0):
#                         count1+=10
#                         count2+=10
#                     elif (c1>0 and c2>0) or (c1>0 and c3>0) or (c1>0 and c4>0) or (c1>0 and c5>0) or (c2>0 and c3>0) or (c2>0 and c4>0) and (c2>0 and c5>0) or (c3>0 and c4>0) or (c3>0 and c5>0) or (c4>0 and c5>0):
#                         count1+=5
#                         count2+=5
#                     elif c1>0 or c2>0 or c5>0:
#                         count1+=3
#                         count2+=3
#                     elif c3>0 or c4>0:
#                         count1+=2
#                         count2+=2
#                     elif c6>0:
#                         count1+=1
#                         count2+=1
#                     # if val2 == 'science' and val2 == 'research' and val2 == 'education':
#                     #     count+=10
#                     # elif (val2 == 'science' and val2 == 'research') or (val2 == 'science' and val2 == 'education') or (val2 == 'education' and val2 == 'research'):
#                     #     count+=5
#                     # elif val2 == 'education' and val2 == 'training':
#                     #     count+=4
#                     # elif val2 == 'science' or val2 == 'research':
#                     #     count+=3
#                     # elif val2 == 'education' or val2 == 'training':
#                     #     count+=2
#                     # else:
#                     #     count+=1
# #science_dict = ["science", "research", "education", "training", "certification", "accreditation", "exploration"]
#             # if count >= 1000:
#             #     if count >= 1000:
#             #         csv_writer.writerow([val,maindict[val]["ORG_NAME"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],count,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"],maindict[val]["SERVICE B"],maindict[val]["SERVICE C"]])
#             # elif count >= 0:
#             #     csv_writer.writerow([val,maindict[val]["ORG_NAME"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],count,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"],maindict[val]["SERVICE B"],maindict[val]["SERVICE C"]])
#             csv_writer.writerow([val,maindict[val]["ORG_NAME"],maindict[val]["NTEECC"],maindict[val]["ACT_CODE"],count,count1,count2,maindict[val]["PURPOSE"],maindict[val]["SERVICE A"],maindict[val]["SERVICE B"],maindict[val]["SERVICE C"]])
#
