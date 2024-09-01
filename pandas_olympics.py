import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#to load the dataset
df = pd.read_csv("./olympics.csv")

# df.head()


#How many total countries are listed in the table?
total_countries = df["noc"].nunique()
print("Total countries :: " + str(total_countries))

#How many golds, silver and bronze have India won?
india_medals = df[df["team"]=="India"]["medal"].value_counts()
print("Medals won by India :: " + str(india_medals))

#Plot a boxplot of ages of all athletes.
plt.figure(figsize=(12,6))
sns.boxplot(x = df["age"].dropna())
plt.title("Boxplot of ages of all the athletes")
plt.xlabel("age")
# plt.show()

#boxplot for Indian athletes
plt.figure(figsize=(12,6))
sns.boxplot(x = df[df["team"] == "India"]["age"].dropna())
plt.title("Boxplot of ages of Indian athletes")
plt.xlabel("age")
# plt.show()

# What is the median and mean ages of the male and female athletes
median_age = df.groupby("sex")["age"].median()
mean_age = df.groupby("sex")["age"].mean()
print("Median age :: ")
print(median_age)
print("Mean age :: ")
print(mean_age)

# Plot the ratio of male:female athletes for each Olympic
gender_counts = df.groupby(["year" , "sex"]).size().unstack()
gender_ratio = gender_counts["M"] / gender_counts["F"]

plt.figure(figsize=(14,7))
gender_ratio.plot(kind="bar" , color = "red")
plt.title("Male to Female athletes ratio per olympic year")
plt.xlabel("year")
plt.ylabel("Male:Female Ratio")
plt.show()
