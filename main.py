import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, chi2_contingency


###################################### Func1 ######################################
def loadData(filepath):
    try:
        alzhData=pd.read_csv(filepath)
        filterData=alzhData[['PatientID', 'Age', 'Gender', 'Diagnosis']]
        filterData.to_csv('filtered_alzheimers_data.csv', index=False)
        return pd.read_csv('filtered_alzheimers_data.csv')
    except FileNotFoundError:
        print(f"Error: The file not found :(.")
        exit()
    except Exception as e:
        print(f"Error! I cant load your file :( {e}")
        exit()


###################################### Func2 ######################################
def solveOfmissingvalues(alzhData):
    try:
        missingVals= alzhData.isnull().sum()
        if missingVals.sum()>0:
            print("\nThere are missing values :( Processing missing values...")
            alzhData = alzhData.dropna()
            alzhData.to_csv('processed_alzheimers_data.csv', index=False)
            print("\nRows with missing values have been removed :).")
        else:
            print("\nNo missing values detected ^_^. The data is ready!.")
        return alzhData
    except Exception as e:
        print(f"Sorry! There is an error :( {e}")
        exit()


###################################### Func3 ######################################
def age_distrib(alzhData):
    try:
        plt.figure(figsize=(10, 5))
        sns.histplot(alzhData['Age'], bins=20, color='darkviolet')
        plt.title('Age Distribution')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.show()
    except Exception as e:
        print(f"Sorry! I cant plot your plot :( {e}")



###################################### Func4 ######################################
def gender_distrib(alzhData):
    try:
        plt.figure(figsize=(6, 4))
        sns.countplot(x='Gender', data=alzhData, hue='Gender', dodge=False, palette='pastel', legend=False)
        plt.title('|Gender Distribution|')
        plt.xticks([0, 1], ['Male', 'Female'])
        plt.ylabel('Count')
        plt.show()
    except Exception as e:
        print(f"Sorry! I cant plot your plot :( {e}")



###################################### Func5 ######################################
def diagnosis_distrib(alzhData):
    try:
        diagnosis_counts=alzhData['Diagnosis'].value_counts()
        plt.figure(figsize=(6, 6))
        diagnosis_counts.plot(kind='pie', autopct='%1.1f%%', labels=['No Alzheimer\'s', 'Alzheimer\'s'], colors=['skyblue', 'salmon'])
        plt.title('||Diagnosis Distribution||')
        plt.ylabel('')
        plt.show()
    except Exception as e:
        print(f"Sorry! I cant plot your plot :( {e}")



###################################### Func6 ######################################
def ageGroups(alzhData):
    try:
        alzhData['AgeGroup']= pd.cut(alzhData['Age'], bins=[60, 70, 80, 90], labels=['60-70', '70-80', '80-90'])
        alzhData=alzhData.dropna(subset=['AgeGroup'])
        return alzhData
    except Exception as e:
        print(f" Sorry! I Couldnt add the gropus :( {e}")
        exit()



###################################### Func7 ######################################
def groups_distribution(alzhData):
    try:
        groups=alzhData.groupby(['AgeGroup', 'Diagnosis'], observed=True).size().unstack()
        fffig, axs=plt.subplots(figsize=(10, 7))
        groups.plot(kind='bar', stacked=True, color=['gray', 'brown'], ax=axs)
        axs.set_title("Alzheimer's Diagnosis by Age Group", fontsize=16, fontweight='bold')
        axs.set_xlabel('Age Group', fontsize=14)
        axs.set_ylabel('Count', fontsize=14)
        axs.legend(['No Alzheimer\'s', 'Alzheimer\'s'], fontsize=12, title_fontsize=14)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Sorry! I cant plot your plot :( {e}")



###################################### Func8 ######################################
def gender_diagnosis(alzhData):
    gender_diagnosis=alzhData.groupby(['Gender', 'Diagnosis']).size().unstack()
    gender_diagnosis.plot(kind='bar', stacked=True, figsize=(8, 6), color=['skyblue', 'pink'])
    plt.title("|||Alzheimer's Diagnosis by Gender|||")
    plt.xlabel('|Gender|')
    plt.ylabel('|Count|')
    plt.xticks([0, 1], ['Male', 'Female'])
    plt.legend(['No Alzheimer\'s', 'Alzheimer\'s'], title='Diagnosis')
    plt.show()



###################################### Func9 ######################################
def plot_detailed_age_group_analysis(alzhData):
    alzhData['Diagnosis']=alzhData['Diagnosis'].astype(str)
    ages = alzhData['AgeGroup'].unique()
    for num in ages:
        
        subset = alzhData[alzhData['AgeGroup']==num]
        plt.figure(figsize=(6, 4))
        sns.countplot(x='Gender', hue='Diagnosis', data=subset, palette={'0': 'gold', '1': 'purple'})
        plt.title(f"Age Group: {num}", fontsize=14)
        plt.xlabel('*Gender*')
        plt.ylabel('*Count*')
        plt.xticks([0, 1], ['Male', 'Female'], fontsize=10)
        plt.legend(title='Diagnosis', labels=['No Alzheimer\'s', 'Alzheimer\'s'])
        plt.tight_layout()
        plt.show()
        counts=subset['Diagnosis'].value_counts()
        plt.figure(figsize=(6, 6))
        counts.plot(kind='pie', autopct='%1.1f%%', colors=['green', 'yellow'], labels=['No Alzheimer\'s', 'Alzheimer\'s'])
        plt.title(f"**Diagnosis Distribution in Age: {num}**")
        plt.show()



###################################### Func10 #####################################
def tests(alzhData):
    try:
        alzheimer_no = alzhData[alzhData['Diagnosis'] == '0']
        alzheimer_yes = alzhData[alzhData['Diagnosis'] == '1']
        t, p = ttest_ind(alzheimer_yes['Age'], alzheimer_no['Age'])
        print(f"\nAge T-Test:\nT-statistic = {t:.4f}")
        print(f"P-value = {p:.4f}")
        gender_contingency = pd.crosstab(alzhData['Gender'], alzhData['Diagnosis'])
        chi2, p2, _, _ = chi2_contingency(gender_contingency)
        print(f"\nGender Chi-Square Test:\nChi2 = {chi2:.4f}")
        print(f"P-value = {p2:.4f}")
    except Exception as e:
        print(f"Sorry! I cant implemnt your tests :( {e}")



###################################### Func11 ######################################
def age_diagnosis(alzhData):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=alzhData, x= 'Age', hue='Diagnosis', kde=True, palette={'0': 'yellow', '1': 'green'}, bins=20)
    plt.title('Age Distribution by Diagnosis')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.legend(['No Alzheimer\'s', 'Alzheimer\'s'])
    plt.show()



################################### Finally: main ##################################
def main():
    filepath = 'alzheimers_disease_data.csv'
    alzhData = loadData(filepath)
    alzhData = solveOfmissingvalues(alzhData)

    age_distrib(alzhData)
    gender_distrib(alzhData)
    diagnosis_distrib(alzhData)

    alzhData = ageGroups(alzhData)
    groups_distribution(alzhData)
    gender_diagnosis(alzhData)
    plot_detailed_age_group_analysis(alzhData)

    tests(alzhData)
    age_diagnosis(alzhData)



################################### Call main :D ##################################
if __name__ == "__main__":
    main()

