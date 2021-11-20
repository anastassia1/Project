print("Гипотезы:")
print("Cреди клиентов магазина больше женщин, чем мужчин")
print("Средний доход мужчин больше среднего дохода женщин")
print("Оценка расходов больше у женщин, чем у мужчин")
print("У наибольшего количества клиентов возраст составляет от 50 до 60 лет")
print("Наибольшая оценка расходов в 2 раза меньше наибольшего дохода")





import pandas as pd


df = pd.read_csv('Mall_Customers.csv')

import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
sc = StandardScaler() 

def fill_genre(Genre):
    if Genre == 'Female': 
        return 1
    return 0 
df['Genre'] = df['Genre'].apply(fill_genre)     
df['Genre'] = df['Genre'].apply(int) 

###########1
print(df['Genre'].value_counts())

#p1 = pd.Series(data = [88, 112], index = ['мужчины', 'женщины'])
#p1.plot(kind = 'barh')
#plt.title('посещаемость магазина')
#plt.show()

#p1 = pd.Series(data = [88, 112], index = ['мужчины', 'женщины'])
#p1.plot(kind = 'pie')
#plt.title('посещаемость магазина')
#plt.show()

print("Вывод: среди клиентов магазина 112 женщин и 88 мужчин")
print("Вывод: гипотеза оказалась верной")
###########1

############2
print(df.groupby(by = 'Genre')['Annual Income (k$)'].mean())

#p2 = pd.Series(data = [62.2, 59.2], index = ['мужчины', 'женщины'])
#p2.plot(kind = 'pie')
#plt.title('средний доход')
#plt.show()

#p2 = pd.Series(data = [62.2, 59.2], index = ['м', 'ж'])
#p2.plot(kind = 'bar')
#plt.title('средний доход')
#plt.show()

print("Вывод: средний доход мужчин - 62.2, средний доход женщин - 59.2")
print("Вывод: гипотеза оказалась верной")

###########3

print(df.groupby( by = 'Genre')['Spending Score (1-100)'].mean())

#p3 = pd.Series(data = [48.5, 51.2], index = ['мужчины', 'женщины'])
#p3.plot(kind = 'barh')
#plt.title('средняя оценка расходов')
#plt.show()

#p3 = pd.Series(data = [48.5, 51.2], index = ['мужчины', 'женщины'])
#p3.plot(kind = 'pie')
#plt.title('средняя оценка расходов')
#plt.show()

print("Вывод: средняя оценка расходов женщин - 51.5, средняя оценка расходов мужчин - 48.5")
print("Вывод: гипотеза оказалась верной")

##########4
print(df['Age'].value_counts())


#df['Age'].value_counts().plot(kind = 'barh', figsize = (8, 8))
#plt.show()

print("Вывод: у наибольшего количества клиентов возраст составляет от 30 до 35 лет")
print("Вывод: гипотеза окаазалась неверной")


#########5
print(df['Annual Income (k$)'].max)
print(df.nlargest(1, 'Annual Income (k$)'))
print(df.nlargest(1, 'Spending Score (1-100)'))

print("Вывод: наибольшая оценка доходов - 137, наибольшая оценка расходов - 99")
print("Вывод: гипотеза оказалась неверной")

#p5 = pd.Series(data = [137, 99], index = ['доходы', 'расходы'])
#p5.plot(kind = 'barh')
#plt.title('наибольшая оценка доходов и расходов')
#plt.show()


#df.plot(kind = 'barh', figsize = (20, 20))                


#plt.show()



print(df)
print(df.info())

print(df.head())

print(df.describe())
