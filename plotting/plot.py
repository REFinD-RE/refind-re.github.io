import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {'no/other_relation' : 13046, 
    'pers:title:title' : 4468, 
    'org:gpe:operations_in' : 4043, 
    'pers:org:employee_of' : 2479, 
    'org:org:agreement_with' : 935, 
    'org:date:formed_on' : 640, 
    'pers:org:member_of' : 630, 
    'org:org:subsidiary_of' : 551, 
    'org:org:shares_of' : 408, 
    'org:money:revenue_of' : 311, 
    'org:money:loss_of' : 202, 
    'org:gpe:headquartered_in' : 193, 
    'org:date:acquired_on' : 186,
    'pers:org:founder_of' : 131,
    'org:gpe:formed_in' : 115, 
    'org:org:acquired_by' : 78, 
    'pers:univ:employee_of' : 76, 
    'pers:gov_agy:member_of' : 56,
    'pers:univ:attended' : 43, 
    'pers:univ:member_of' : 33,
    'org:money:profit_of' : 29, 
    'org:money:cost_of' : 23}

relations = []
n_instances = []
for relation, value in sorted(data.items(), key=lambda item: item[1], reverse=True):
    relations.append(relation)
    n_instances.append(value)

sns.barplot(x= relations, y = n_instances)
plt.xlabel('Relations')
plt.ylabel('Number of Instances')
plt.xticks(rotation=65, ha='right', fontsize=8)
plt.tight_layout()
#plt.show()
plt.savefig("barplot.png", dpi=300)