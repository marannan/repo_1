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
    columns = ['EIN', 'SUBSECCD', 'NAME', 'CITY', 'STATE', 'ZIP_CODE', 'TOTAL_ASSETS', 'REVENUE', 'NET_INCOME']
    
    data_files = os.listdir(data_path)
    file_dict = dict(zip(data_files, range(len(data_files))))
    
    for file_name, idx in file_dict.items():
        data_file =  data_path + '/' + file_name

        #skipping temp files
        if "~" in str(data_file):
            continue

        try:
            file_name_no_exnt = file_name.split('.')[0]
            year = file_name_no_exnt.split('_')[2]
            year = int(year)
        except:
            year = 'NA'
        
        files.append(data_file)
          
        try:
            data[year] = pd.read_csv(data_file, sep=',', low_memory=False, quotechar='"', nrows = 1000)
            #data[year] = pd.read_csv(data_file, sep=',', low_memory=False, quotechar='"')
            
            #convert column data into numeric type for sorting and processing
            data[year]['SUBSECCD'] = data[year]['SUBSECCD'].convert_objects(convert_numeric = True)
            
            #adding a common column for assets because of different columns in different year files
            if 'ASS_EOY' in data[year]:
                data[year]['TOTAL_ASSETS'] = data[year]['ASS_EOY'].convert_objects(convert_numeric = True)
            
            elif 'p4e_asst' in data[year]:
                data[year]['TOTAL_ASSETS'] = data[year]['p4e_asst'].convert_objects(convert_numeric = True)
            
            else:
                #print "TOTAL_ASSETS not found for file : " + str(file_name)
                data[year]['TOTAL_ASSETS'] = 0
                
            #adding a common column for revenue because of different columns in different year files
            if 'TOTREV2' in data[year]:
                data[year]['REVENUE'] = data[year]['TOTREV2'].convert_objects(convert_numeric = True)
            
            elif 'p1totrev' in data[year]:
                data[year]['REVENUE'] = data[year]['p1totrev'].convert_objects(convert_numeric = True)
                
            elif 'p1psrev' in data[year]:
                data[year]['REVENUE'] = data[year]['p1psrev'].convert_objects(convert_numeric = True)
            
            else:
                #print "REVENUE not found for file : " + str(file_name)
                data[year]['REVENUE'] = 0
                
            #adding a common column for revenue because of different columns in different year files
            if 'grossinc' in data[year]:
                data[year]['NET_INCOME'] = data[year]['grossinc'].convert_objects(convert_numeric = True)
            
            elif 'NETINC' in data[year]:
                data[year]['NET_INCOME'] = data[year]['NETINC'].convert_objects(convert_numeric = True)
            
            else:
                #print "NET_INCOME not found for file : " + str(file_name)
                data[year]['NET_INCOME'] = 0  
                
            #adding a common column for 5 digit zip code because of different columns in different year files for zip
            if 'ZIP5' in data[year]:
                data[year]['ZIP_CODE'] = data[year]['ZIP5'].convert_objects(convert_numeric = True)
            
            elif 'zip5' in data[year]:
                data[year]['ZIP_CODE'] = data[year]['zip5'].convert_objects(convert_numeric = True)
        
            else:
                data[year]['ZIP_CODE'] = ''
                
            data_all = data_all.append(data[year][columns], ignore_index=True)
            print ("loaded file : " + str(file_name))
        
        except:
            traceback.print_exc(file=sys.stdout)
            exit()
    
    return data, data_all


def create_tables(year = None, state = None):
    SUBSECCD_val = [1,12,14,15,16,50,60,80]
    data_year_wise, data_all = get_data('../data/core_other/')
    data_subseccd = data_all.loc[data_all['SUBSECCD'].isin(SUBSECCD_val)]
    
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
    
    
    #table 2 for particular year (same as table 1)
    if year != None:
        data_year = pd.DataFrame()
        for yr in year:
            data_year = data_year.append(data_year_wise[yr], ignore_index=True)
            
        data_year = data_year.loc[data_year['SUBSECCD'].isin(SUBSECCD_val)]
        
        table_2_columns = ['SUBSECCD', 'YEAR', 'TOTAL_ENTRIES', 'TOTAL_ASSETS', 'REVENUE', 'REVENUE_AVERAGE', 'REVENUE_MEDIAN', 'NET_INCOME', 'NET_INCOME_AVERAGE', 'NET_INCOME_MEDIAN' ]
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
        print (data_table_2.to_string(index=False))
        data_table_2.to_csv('../results/core_other_table_2_' + str(year) + '_.csv', mode = 'w', index=False)                
    
    else:
        print ("error : year not specified for year wise data")
        
        
    #table 3 for particular state
    if state != None:
        data_state = data_all.loc[data_all['STATE'].isin(state)]
        data_state = data_state.loc[data_state['SUBSECCD'].isin(SUBSECCD_val)]
    
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
        print (data_table_3.to_string(index=False))
        data_table_3.to_csv('../results/core_other_table_3_' + str(state) + '_.csv', mode = 'w', index=False)        
    
    else:
        print ("error : state not specified for state wise data")
    

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
    create_tables(year= [2013], state=['CA'])
    #create_map(year = [1995], state = ['CA'])
