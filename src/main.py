"""
PROJECT_NAME - demo main
"""
from src.utils import read_data, simple_plot

def main():
    df = read_data("data/sample.csv")
    print("Preview:")
    print(df.head())
    simple_plot(df, "value", "results/figures/trend_plot.png")
    print("Plot saved to results/figures/trend_plot.png")

if __name__ == "__main__":
    main()
