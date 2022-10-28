import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  
    race_count = (df["race"].value_counts())
  
    # What is the average age of men?
    # Con esto saco los hombres que hay
    hombres = df["sex"] == "Male"
    # Hago la media de las edades de esos hombres y redondeo a 1 decimal
    average_age_men = round(df[hombres]['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    # Cantidad de hombres con licenciatura
  
    bachelors = df["education"].value_counts()
    bachelors = bachelors["Bachelors"]
    tamano = df.shape[0]
    
    percentage_bachelors =  round((bachelors/tamano)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    # Los 35 clasificados con true o false si tienen alguno de estos estudios o no
    superiores = df['education'].isin(['Bachelors','Masters','Doctorate'])
    inferiores = ~superiores

    higher_education = superiores
    lower_education = inferiores

    # El numero de los que cobran + 50 k
    mayores50 = df["salary"] == '>50K'
  
    # percentage with salary >50K

    # Estudios superiores y mas de 50k / estudios superiores 
    higher_education_rich = round(((higher_education & mayores50).sum()/higher_education.sum())*100,1)
    lower_education_rich = round(((lower_education & mayores50).sum()/lower_education.sum())*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
 
    min_work_hours =  df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    pocas_horas = df["hours-per-week"].isin(["1"])

    rich_percentage = round(((pocas_horas & mayores50).sum()/pocas_horas.sum())*100,1)

    # What country has the highest percentage of people that earn >50K?
    # Nos da la lista de paises con mas que cobran 50k ordenada
    paises = df[mayores50]["native-country"].value_counts()
    # Numero de persona por pais
    todo = df["native-country"].value_counts()
  
    # Divido los que cumplen entre todos y lo ordeno 
    ranking = (paises/todo).sort_values(ascending=False)

    # Me quedo con el indice del primero
    highest_earning_country = ranking.index[0]

    # Me quedo con el valor redondeado
    highest_earning_country_percentage = round(ranking.iloc[0]*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    # Primero los que cobran +50k en la india
    filtro = df[mayores50]["native-country"] == "India"
    ocupaciones = df["occupation"].value_counts().index[0]
  
    top_IN_occupation = ocupaciones

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }