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
        countryName = "Afghanistan"
        data = (rawData[rawData["country"] == countryName]).iloc[0]

        years = data.index.drop("country").to_numpy().astype(int)
        values = [convertMillions(value) for value in data.values[1:]]

        plt.plot(years, values, label=f"Millions of people in {countryName}")

        plt.xticks(range(0, years.max(), 50))
        plt.xlabel("Year")
        plt.xlim(years.min(), years.max())

        plt.yticks(range(0, int(max(values)), 5))
        plt.ylabel("Population (millions)")
        plt.ylim(0, int(max(values)) + 1)

        plt.title(f"Population in {countryName} over the years")
        plt.legend()
        plt.show()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()