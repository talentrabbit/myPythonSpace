
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline  # 为了在jupyter notebook里作图，需要用到这个命令
#tips=pd.read_csv("D:\\ML\\tips2.csv")
tips=sns.load_dataset("tips")
sns.set(style="darkgrid",palette="deep",color_codes=True)
sns.lmplot("total_bill","tip",tips,col="sex")
plt.show()
# sns.distplot(tips['total_bill'],axlabel="bill No.", label="bill price",)
# plt.show()
# plt.plot(tips['total_bill'])
# plt.show()
# sns.jointplot("total_bill","tip", tips, kind="reg")
# plt.show()
# sns.jointplot("total_bill","tip", tips, kind="scatter")
# plt.show()