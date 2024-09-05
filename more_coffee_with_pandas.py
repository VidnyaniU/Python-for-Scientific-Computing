import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("coffee_survey.csv")
# df = df.dropna().replace("",pd.NA).dropna()
# print(df.head(20))

#--------------------------------------------------------------------------------------
#Where do you brew?

col_name = "where_drink"
df[col_name] = df[col_name].str.strip().str.lower()

labels = ["At home", "At the office", "At a cafe", "On the go", "None of these"]
labels = [label.lower() for label in labels]

filtered_df = df[df[col_name].isin(labels)]

response_counts = filtered_df[col_name].value_counts()

response_counts = response_counts.reindex(labels, fill_value=0)

# print(response_counts)

total = sum(response_counts)

percentages = [(count / total) * 100 for count in response_counts]

# print(percentages)

plt.figure()
bars = plt.barh(labels, percentages, color="blue")

plt.title("Where do you Brew Coffee?", fontsize=16)
plt.xlabel("Percent of Respondents")
plt.xlim(0, 100)
plt.gca().invert_yaxis()  
plt.show()

#-------------------------------------------------------------------------------
#How do you brew coffee?

col_name = "brew"  
labels = ["Pour over", "Espresso", "French press", "Other", "Mr. Coffee", 
          "Cold brew", "Pod Machine", "Cometeer", "Instant coffee", "Bean-to-Cup"]


df[col_name] = df[col_name].str.strip().str.lower()
labels = [label.lower() for label in labels]

filtered_df = df[df[col_name].isin(labels)]
response_counts = filtered_df[col_name].value_counts()
response_counts = response_counts.reindex(labels, fill_value=0)

total = sum(response_counts)
percentages = [(count / total) * 100 for count in response_counts]

plt.figure()
bars = plt.barh(labels, percentages, color="blue")

plt.title("How do you Brew Coffee?", fontsize=16)
plt.xlabel("Percent of Respondents")
plt.xlim(0, 100)
plt.gca().invert_yaxis()  
plt.show()


#---------------------------------------------------------------------------------------------------
#Where do you buy coffee?

col_name = "purchase"  
labels = ["Speciality Coffee Shop","Local Cafe" , "National Chain","Drive-thru","Deli or Supermarket" , "Other"]


df[col_name] = df[col_name].str.strip().str.lower()
labels = [label.lower() for label in labels]

filtered_df = df[df[col_name].isin(labels)]
response_counts = filtered_df[col_name].value_counts()
response_counts = response_counts.reindex(labels, fill_value=0)

total = sum(response_counts)
percentages = [(count / total) * 100 for count in response_counts]

plt.figure()
bars = plt.barh(labels, percentages, color="blue")

plt.title("Where do you buy coffee?", fontsize=16)
plt.xlabel("Percent of Respondents")
plt.xlim(0, 100)
plt.gca().invert_yaxis()  
plt.show()

#-------------------------------------------------------------------------------------------
#What do you add to coffee?

col_name = "additions"  
labels = ["No-just black","Milk,Dairy, or Creamer" , "Sugar or sweetener","Flavor syrup", "Other"]


df[col_name] = df[col_name].str.strip().str.lower()
labels = [label.lower() for label in labels]

filtered_df = df[df[col_name].isin(labels)]
response_counts = filtered_df[col_name].value_counts()
response_counts = response_counts.reindex(labels, fill_value=0)

total = sum(response_counts)
percentages = [(count / total) * 100 for count in response_counts]

plt.figure()
bars = plt.barh(labels, percentages, color="blue")

plt.title("What do you add to coffee?", fontsize=16)
plt.xlabel("Percent of Respondents")
plt.xlim(0, 100)
plt.gca().invert_yaxis()  
plt.show()

#-------------------------------------------------------------------------------------------
#What milk do you add to your coffee?

col_name = "dairy"  
labels = ["Whole milk","Oat milk" , "Half and half","Flavored coffee creamer","Coffee creamer","Almond milk","Skim milk","Soy milk", "Other"]


df[col_name] = df[col_name].str.strip().str.lower()
labels = [label.lower() for label in labels]

filtered_df = df[df[col_name].isin(labels)]
response_counts = filtered_df[col_name].value_counts()
response_counts = response_counts.reindex(labels, fill_value=0)

total = sum(response_counts)
percentages = [(count / total) * 100 for count in response_counts]

plt.figure()
bars = plt.barh(labels, percentages, color="blue")

plt.title("What milk do you add to your coffee?", fontsize=16)
plt.xlabel("Percent of Respondents")
plt.xlim(0, 100)
plt.gca().invert_yaxis()  
plt.show()

#-------------------------------------------------------------------------------------------
#What sugar do you add to your coffee?

col_name = "sweetener"  
labels = ["Granulated Sugar","Raw Sugar Turbinado" , "Artificial Sweetners","Brown Sugar","Honey","Stevia","Maple Syrup","Agave Nectar"]


df[col_name] = df[col_name].str.strip().str.lower()
labels = [label.lower() for label in labels]

filtered_df = df[df[col_name].isin(labels)]
response_counts = filtered_df[col_name].value_counts()
response_counts = response_counts.reindex(labels, fill_value=0)

total = sum(response_counts)
percentages = [(count / total) * 100 for count in response_counts]

plt.figure()
bars = plt.barh(labels, percentages, color="blue")

plt.title("What sugar do you add to your coffee?", fontsize=16)
plt.xlabel("Percent of Respondents")
plt.xlim(0, 100)
plt.gca().invert_yaxis()  
plt.show()

#-------------------------------------------------------------------------------------------
