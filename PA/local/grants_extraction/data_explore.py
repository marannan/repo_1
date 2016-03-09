
# coding: utf-8

# In[2]:

import pandas as pd
pd.set_option('display.max_columns', None)

import os


# In[3]:

s = pd.read_csv('sample_science_data.txt', sep='\t')

for idx, r in s.iterrows():
    print("{0:20s} & {1:30s} & {2:6s} & {3:6s} & {4:90s}\\\\\\midrule".format(str(r.ORG_NAME).title(), 
                                                         str(r.WEBSITE), 
                                                         str(r.NTEECC).capitalize().replace('Nan','-'), 
                                                         str(r.IRS).capitalize().split('.')[0].replace('Nan','-'), 
                                                         str(r.PURPOSE)))


# In[13]:

form = '990' # or just 990

data_path = {'990': 'guidestar_990', '990PF': 'guidestar_990PF'}
prefix = {'990': 'f990_', '990PF': 'PF990_'}

def get_data(form):
    data_files = os.listdir(data_path[form])

    file_dict = dict(zip(data_files, range(len(data_files))))

    d = {}
    for file_name, idx in file_dict.items():
        data_file =  data_path[form] + '/' + file_name
        try:
            d[idx] = pd.read_csv(data_file, sep='|', low_memory=False)
        except:
            pass 
    return d, file_dict

g, f = get_data('990')



# In[18]:

len(g[0].C_EIN.unique())


# ### Funds by 990PF NPOs to other organziations by text in name, from Part XV Grants Paid

# In[9]:

npo_pf, files = get_data('990PF')
pf_grants_paid = npo_pf[21] # PF990_Part_XV_Grants_Paid
d = pf_grantPart_XV_Grants_Paids_paid

uni = d[d.ORGNAME.str.contains('univ|colleg', case=False) == True]
tmp = d[d.ORGNAME.str.contains('univ|colleg', case=False) == False]

hospital = tmp[tmp.ORGNAME.str.contains('hospital|clinic', case=False) == True]
tmp = tmp[tmp.ORGNAME.str.contains('hospital|clinic', case=False) == False]

science = tmp[tmp.ORGNAME.str.contains('science|research|technology|innovation', case=False) == True]
tmp = tmp[tmp.ORGNAME.str.contains('science|research|technology|innovation', case=False) == False]

education = tmp[tmp.ORGNAME.str.contains('institute|education', case=False) == True]

other = tmp[tmp.ORGNAME.str.contains('institute|education', case=False) == False]

org_name = [uni, hospital, science, education, other]
for org in org_name:
    print('{0:12d} & {1:12,} \\\\'.format(round(org.AMOUNT.count()), 
                                            round(org.AMOUNT.sum())))
    


# ### Funds by 990 NPOs to other organziations by legal type, from Schedule I

# In[6]:

npo, files = get_data('990')

npo_grants_paid = npo[51] # f990_Sched_I_Part_II_Gov_Grant
d = npo_grants_paid

#Schedule I

uni = d[d.ORG_NAME.str.contains('univ|colleg', case=False)==True]
tmp = d[d.ORG_NAME.str.contains('univ|colleg', case=False)==False]

npo = tmp[tmp.SECTION.str.contains('501|3') == True]
tmp = d[d.SECTION.str.contains('501|3') == False]

gov = tmp[tmp.SECTION.str.contains('gov|mun|town|county|com|public|state', case=False) == True]
oth = tmp[tmp.SECTION.str.contains('gov|mun|town|county|comm|public|state', case=False) == False]


org_lfo = [uni, npo, gov, oth]
for org in org_lfo:
    org.ndim
    print('{0:12d} & {1:12,} & {2:12d} & {3:12,}\\\\'.format(round(org.ORG_CASH.count()), 
                                            round(org.ORG_CASH.sum()), 
                                            round(org.ORG_NON_CASH.count()),
                                            round(org.ORG_NON_CASH.sum())))
    


# In[8]:

npo_pf.shape(), npo


# In[ ]:



