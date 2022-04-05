
import pandas as pd
import re 

df = pd.read_csv('Linkedin Job Checked Code\Input\config_linkedin_jobpostchecked_mapping.csv')
a = df.dropna()
print(a)
print('================================')
b = a['Recruiter links']
print(b)
print('================================')
# pattern= ('https://www.')
# for word in pattern:
#     mod_string = re.sub(pattern, '', str(b))
#     print(mod_string)
gh=[]
s = 0
for i in range(len(b)):
    r = re.compile(r"[ https://www.][ http://www.]")
    l = r.sub('',b[s])
    gh.append(l)
    gf=b[s].split()
    s = s+1
print(gh)