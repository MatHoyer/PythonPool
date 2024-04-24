from load_csv import load
import matplotlib.pyplot as plt


def main():
    rawData = load("life_expectancy_years.csv")
    if rawData is None:
        print("File not found")
        return
    try:
        countryName = "France"
        data = (rawData[rawData["country"] == countryName]).iloc[0]

        years = data.index.drop("country").to_numpy().astype(int)
        values = [float(value) for value in data.values[1:]]

        plt.plot(years, values, label=f"Life expectancy Projection in {countryName}")

        yearTick = 40
        plt.xticks(range(0, years.max(), yearTick))
        plt.xlabel("Year")
        plt.xlim(years.min() - yearTick/2, years.max() + yearTick/2)

        lifeTick = 10
        plt.yticks(range(0, int(max(values)), lifeTick))
        plt.ylabel("Life expectancy")
        plt.ylim(int(min(values)) - lifeTick/2, int(max(values)) + lifeTick/2)

        plt.title(f"{countryName} Life expectancy Projection")
        plt.legend()
        plt.show()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()