import pandas as pd
from matplotlib import pyplot as plt

csv_data = pd.read_csv("csv_tables/finance_economics_dataset.csv", parse_dates=["Date"])

csv_data.set_index("Date", inplace=True)

csv_data["Year"] = csv_data.index.year

grouped = csv_data.groupby(["Year","Stock Index"])["Close Price"].mean()

result_list = [(year,stock,round(avg,2)) for (year,stock), avg in grouped.items()]

stock_groups = {}
for year,stock_index, avg in result_list :
    if stock_index not in stock_groups :
        stock_groups[stock_index] = {"years" : [], "avg_prices" : []}
    stock_groups[stock_index]["years"].append(year)
    stock_groups[stock_index]["avg_prices"].append(avg)

for stock_index,data in stock_groups.items():
    plt.plot(data["years"],data["avg_prices"],marker = "o", label = stock_index)

plt.xlabel("Year")
plt.ylabel("Average Close Price")
plt.title("Average Stock Index Close Price per Year")
plt.grid(True)
plt.legend(title="Stock Index")
plt.savefig("stock_prices_plot.png")
plt.close()