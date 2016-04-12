import sys
import os   
import traceback
import pandas as pd
import time
        
def get_data(data_path):
    import sys
    import os   
    import traceback
    import pandas as pd
    import time
    
    data = {}
    data_all = pd.DataFrame()
    years = []
    files = []
    columns = ['EIN', 'SUBSECCD', 'FisYr', 'NAME', 'CITY', 'STATE', 'ZIP_CODE', 'TOTAL_ASSETS', 'REVENUE', 'NET_INCOME']
    
    data_files = os.listdir(data_path)
    file_dict = dict(zip(data_files, range(len(data_files))))
    
    for file_name, idx in file_dict.items():
        data_file =  data_path + '/' + file_name

        #skipping temp files
        if "~" in str(data_file):
            continue

        year = None
        #for year in range(1990, 2100):
            #if str(year) in file_name:
                #years.append(year)
                #break

        file_name_no_exnt = file_name.split('.')[0]
        year = file_name_no_exnt.split('_')[2]
        year = int(year)
        #print year
        
        files.append(data_file)
        
        #if year != 2010:
            #continue
        
        
        try:
            data[year] = pd.read_csv(data_file, sep=',', low_memory=False, quotechar='"', nrows = 1000)
            #data[year] = pd.read_csv(data_file, sep=',', low_memory=False, quotechar='"')
            
            #print the column names
            #print ("file : " + str(file_name))
            #print list(data[year].columns.values)
            
            #convert column data into numeric type for sorting and processing
            data[year]['SUBSECCD'] = pd.to_numeric(data[year]['SUBSECCD'], errors='coerce')
            data[year]['FisYr'] = pd.to_numeric(data[year]['FisYr'], errors='coerce')
            columns_ori = list(data[year].columns.values)
        
            
            #adding a common column for assets because of different columns in different year files
            if 'ASS_EOY' in data[year]:
                data[year]['TOTAL_ASSETS'] = pd.to_numeric(data[year]['ASS_EOY'], errors='coerce')
            
            elif 'p4e_asst' in data[year]:
                data[year]['TOTAL_ASSETS'] = pd.to_numeric(data[year]['p4e_asst'], errors='coerce')
            
            else:
                #print "TOTAL_ASSETS not found for file : " + str(file_name)
                data[year]['TOTAL_ASSETS'] = 0
                

            #adding a common column for revenue because of different columns in different year files
            if 'TOTREV2' in data[year]:
                data[year]['REVENUE'] = pd.to_numeric(data[year]['TOTREV2'], errors='coerce')
            
            elif 'p1totrev' in data[year]:
                data[year]['REVENUE'] = pd.to_numeric(data[year]['p1totrev'], errors='coerce')  
                
            elif 'p1psrev' in data[year]:
                data[year]['REVENUE'] = pd.to_numeric(data[year]['p1psrev'], errors='coerce')              
            
            else:
                #print "REVENUE not found for file : " + str(file_name)
                data[year]['REVENUE'] = 0
                
                
            #adding a common column for revenue because of different columns in different year files
            if 'grossinc' in data[year]:
                data[year]['NET_INCOME'] = pd.to_numeric(data[year]['grossinc'], errors='coerce')
            
            elif 'NETINC' in data[year]:
                data[year]['NET_INCOME'] = pd.to_numeric(data[year]['NETINC'], errors='coerce')  
            
            else:
                #print "NET_INCOME not found for file : " + str(file_name)
                data[year]['NET_INCOME'] = 0  
                
            
            #adding a common column for 5 digit zip code because of different columns in different year files for zip
            if 'ZIP5' in data[year]:
                data[year]['ZIP_CODE'] = pd.to_numeric(data[year]['ZIP5'], errors='coerce')
            
            elif 'zip5' in data[year]:
                data[year]['ZIP_CODE'] = pd.to_numeric(data[year]['zip5'], errors='coerce')
        
            else:
                data[year]['ZIP_CODE'] = ''
                
               
            data_all = data_all.append(data[year][columns], ignore_index=True)
            print ("loaded file : " + str(file_name))
        
        except:
            traceback.print_exc(file=sys.stdout)
    

    return data, data_all


def create_tables(year = None, state = None):
    SUBSECCD_val = [1,12,14,15,16,50,60,80]
    data_year_wise, data_all = get_data('../data/core_other/')
    
    ##temp exit
    #exit()

    #table 1 to get data of orgs for all years whose SUBSECCD_val = [1,12,14,15,16,50,60,80]
    data_subseccd = data_all.loc[data_all['SUBSECCD'].isin(SUBSECCD_val)]
    data_subseccd = data_subseccd.sort_values(by=['SUBSECCD'], ascending=[True])
    #data_subseccd.to_csv('core_other_subseccd.csv', mode = 'w', index=False)    
    
    #same as table_1 with yearwise data
    if year != None:
        data_year = data_subseccd.loc[data_subseccd['FisYr'].isin(year)]
        data_year = data_year.sort_values(by=['FisYr'], ascending=[True])
        #data_year.to_csv('core_other_year.csv', mode = 'w', index=False)
        
        
    #same as table_1 with statewise data
    if state != None:
        data_state = data_subseccd.loc[data_subseccd['STATE'].isin(state)]
        data_state = data_state.sort_values(by=['STATE'], ascending=[True])
        #data_state.to_csv('core_other_state.csv', mode = 'w', index=False)
        
    
    table_1_columns = ['SUBSECCD', 'TOTAL_ENTRIES', 'TOTAL_ASSETS', 'REVENUE', 'REVENUE_AVERAGE', 'REVENUE_MEDIAN', 'NET_INCOME', 'NET_INCOME_AVERAGE', 'NET_INCOME_MEDIAN' ]
    data_table_1 = pd.DataFrame(columns=table_1_columns)
    for val in SUBSECCD_val:
        data_temp = data_subseccd.loc[data_subseccd['SUBSECCD'] == val]
        total_entries = len(data_temp)
        #Total Assets
        total_asst = data_temp['TOTAL_ASSETS'].sum()
        #Revenue
        total_rev = data_temp['REVENUE'].sum()
        try:
            total_rev_mean = int(data_temp['REVENUE'].mean())
        except:
            total_rev_mean = 0
        total_rev_median = data_temp['REVENUE'].median()
        #Net Income
        total_inc = data_temp['NET_INCOME'].sum()
        try:
            total_inc_mean = int(data_temp['NET_INCOME'].mean())
        except:
            total_inc_mean = 0
        total_inc_median = data_temp['NET_INCOME'].median()        
          
        data_table_1.loc[SUBSECCD_val.index(val)] = [val, total_entries, total_asst, total_rev, total_rev_mean, total_rev_median, total_inc, total_inc_mean, total_inc_median]
        
    print ("table_1")   
    print data_table_1.to_string(index=False)
    data_table_1.to_csv('../results/core_other_table_1_all_years.csv', mode = 'w', index=False)


    table_2_columns = ['SUBSECCD', 'FISYEAR', 'TOTAL_ENTRIES', 'TOTAL_ASSETS', 'REVENUE', 'REVENUE_AVERAGE', 'REVENUE_MEDIAN', 'NET_INCOME', 'NET_INCOME_AVERAGE', 'NET_INCOME_MEDIAN' ]
    data_table_2 = pd.DataFrame(columns=table_2_columns)
    for val in SUBSECCD_val:
        data_temp = data_year.loc[data_year['SUBSECCD'] == val]
        total_entries = len(data_temp)
        #Total Assets
        total_asst = data_temp['TOTAL_ASSETS'].sum()
        #Revenue
        total_rev = data_temp['REVENUE'].sum()
        try:
            total_rev_mean = int(data_temp['REVENUE'].mean())
        except:
            total_rev_mean = 0
        total_rev_median = data_temp['REVENUE'].median()
        #Net Income
        total_inc = data_temp['NET_INCOME'].sum()
        try:
            total_inc_mean = int(data_temp['NET_INCOME'].mean())
        except:
            total_inc_mean = 0
        total_inc_median = data_temp['NET_INCOME'].median()        
        
        data_table_2.loc[SUBSECCD_val.index(val)] = [val, year, total_entries, total_asst, total_rev, total_rev_mean, total_rev_median, total_inc, total_inc_mean, total_inc_median]
    
    print ("table_2")   
    print data_table_2.to_string(index=False)
    data_table_2.to_csv('../results/core_other_table_2_' + str(year) + '_.csv', mode = 'w', index=False)        
    
    
    table_3_columns = ['SUBSECCD', 'STATE', 'TOTAL_ENTRIES', 'ASSETS', 'REVENUE', 'REVENUE_AVERAGE', 'REVENUE_MEDIAN', 'NET_INCOME', 'NET_INCOME_AVERAGE', 'NET_INCOME_MEDIAN' ]
    data_table_3 = pd.DataFrame(columns=table_3_columns)
    for val in SUBSECCD_val:
        data_temp = data_state.loc[data_state['SUBSECCD'] == val]
        total_entries = len(data_temp)
        #Total Assets
        total_asst = data_temp['TOTAL_ASSETS'].sum()
        #Revenue
        total_rev = data_temp['REVENUE'].sum()
        try:
            total_rev_mean = int(data_temp['REVENUE'].mean())
        except:
            total_rev_mean = 0
        total_rev_median = data_temp['REVENUE'].median()
        #Net Income
        total_inc = data_temp['NET_INCOME'].sum()
        try:
            total_inc_mean = int(data_temp['NET_INCOME'].mean())
        except:
            total_inc_mean = 0
        total_inc_median = data_temp['NET_INCOME'].median()        
        
        data_table_3.loc[SUBSECCD_val.index(val)] = [val, state, total_entries, total_asst, total_rev, total_rev_mean, total_rev_median, total_inc, total_inc_mean, total_inc_median]
    
    print ("table_3")      
    print data_table_3.to_string(index=False)
    data_table_3.to_csv('../results/core_other_table_3_' + str(state) + '_.csv', mode = 'w', index=False)        
    

def create_map(year = None, state = None):
    SUBSECCD_val = [1,12,14,15,16,50,60,80]
    data_year_wise, data_all = get_data('../data/core_other/')
    
    subseccd = {}
    for val in SUBSECCD_val:
        subseccd[val] = data_all.loc[data_all['SUBSECCD'].isin([val])]
    

    for val in SUBSECCD_val:
        print list(subseccd[val]['EIN'].values)
        print list(subseccd[val]['ZIP_CODE'].values)
        
    
    
    
    
    


if __name__ == '__main__':
    create_map(year = [1995], state = ['CA'])
