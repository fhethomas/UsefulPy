# UsefulPy
Useful python snippets

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
