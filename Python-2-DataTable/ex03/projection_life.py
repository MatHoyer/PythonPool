from load_csv import load
import matplotlib.pyplot as plt


def main():
  rawIncomeData = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
  rawLifeData = load("life_expectancy_years.csv")
  if rawIncomeData is None or rawLifeData is None:
    print("File not found")
    return
  
  try:
    year = "1900"
    lifeData = rawLifeData[year]
    incomeData = rawIncomeData[year]

    plt.scatter(incomeData, lifeData, alpha=1)

    plt.xlabel("Gross domestic product")

    plt.ylabel("Life expectancy")

    plt.title(year)
    plt.show()

  except Exception as e:
    print(e)


if __name__ == "__main__":
  main()