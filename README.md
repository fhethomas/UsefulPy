# UsefulPy
Useful python snippets

# Pandas Pivot & revert this to a regular table
```
# create pivot table
piv=pd.pivot_table(data=df,index=['Year','Type'],values='Amount',aggfunc='median')

# reset the index - reverts the index of the pivot table to be regular columns - adds an index from 0 up
piv.reset_index()
```

# Test for Normality (where n>50)
```
from scipy.stats import kstest
kstest(data,"norm")
```
# T-test
```
from scipy.stats import ttest_ind
ttest_ind(df1,df2)
```

# T-Test for non-normal 
```
from scipy.stats import mannwhitneyu
mannwhitneyu(df1,df2)
```

# Seaborn Boxplots
```
import seaborn as sns
sns.boxplot(data=df,x="Pay",y="Year",showfliers=False)
```

# Add data labels onto subplit
```
fig,ax = plt.subplots()
plt.bar(df.index,df["data"],edgecolor="r")
plt.xticks(rotation=45)
plt.title(y)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)    
i=1
for rect in ax.patches:
    #print(height)
    # Find where everything is located
    height = rect.get_height()
    width = rect.get_width()
    x = rect.get_x()
    y = rect.get_y()
    #print(rect.get_facecolor())
    # The height of the bar is the data value and can be used as the label
    label_text = f'{height:.2f}'  # f'{height:.2f}' to format decimal values

    # ax.text(x, y, text)
    

    label_x = x + width
    label_y = y + height

    # plot only when height is greater than specified value
    if i==0:
        xminus=-0
        i=1
    else:
        xminus=0
        i=0
    if height > 0:
        ax.text(label_x-0.3, (label_y)+xminus, label_text, ha='center', va='center', fontsize=14,rotation=70)
plt.show()
```

# Zip File
```
import zipfile36 as zf
import os
directory_str = "C:\\Users\\Test"
os.chdir(directory_str)
zipped_file = zf.ZipFile("TestFile.zip",mode="w")
zipped_file.setpassword(b"TestPassword")
zipped_file.close()
# Write all files in current directory to zip file
[zipped_file.write("{1}".format(directory_str,x)) for x in os.listdir() if x[-3:]=="txt"]
```
# All Iterations
Below creates a list of all permutations of 0-9 
```
import itertools
l=[str(x) for x in range(0,10)]
l_permutations=itertools.permutations(l)
l_permutations=list(l_permutations)
l_permutations = [int("".join(x)) for x in l_permutations]
```

