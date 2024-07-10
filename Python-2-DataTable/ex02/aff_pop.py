from load_csv import load
import matplotlib.pyplot as plt


def convertMillions(value):
    if isinstance(value, str) and value.endswith("M"):
        return float(value.replace(",", "").replace("M", ""))


def main():
    rawData = load("population_total.csv")
    if rawData is None:
        print("File not found")
        return
    try:
        countryName1 = "France"
        countryName2 = "Belgium"

        data1 = (rawData[rawData["country"] == countryName1]).iloc[0]
        data2 = (rawData[rawData["country"] == countryName2]).iloc[0]

        maxData = 2050 - 1800
        years = data1.index.drop("country").to_numpy().astype(int)
        years = years[1:maxData]
        values1 = [convertMillions(value) for value in data1.values[1:maxData]]
        values2 = [convertMillions(value) for value in data2.values[1:maxData]]

        plt.plot(years, values1, label=countryName1)
        plt.plot(years, values2, label=countryName2)

        yearTick = 40
        plt.xticks(range(0, years.max(), yearTick))
        plt.xlabel("Year")
        plt.xlim(years.min() - yearTick/2, 2050 + yearTick/2)

        popTick = 20
        plt.yticks(range(0, int(max(values1 + values2)), popTick))
        plt.ylabel("Population")
        plt.ylim(int(min(values1 + values2)) - popTick/2, int(max(values1 + values2)) + popTick/2)

        plt.title("Population Projection")
        plt.legend()
        plt.show()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
