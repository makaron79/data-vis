from sys import exit
try:
    import pandas as pd
    print("Moduł pandas wczytany.")
except:
    print("Zainstaluj: 'pip install pandas' ")
    exit(0)

source_data = "http://otwartedane.gdynia.pl/portal/data/city/6/3/data.csv"
print(f"Dane źródłowe: {source_data}")
# Tworzymy tzw. "DataFrame"
try:
    df = pd.read_csv(source_data)
    print("Pobrano dane źródłowe.")
except:
    print("UWAGA! Wystąpił błąd.")
    exit(0)
print("----[ informacje o danych źródłowych ]---")
print(df)
print("----------------")
# Wycinamy pewne dane
new_df = df[["obce", "polskie", "month"]]

plot = new_df.plot(
    kind="line",
    x="month",
    xlabel="Rok - miesiąc",
    ylabel="Liczba obsłużonych statków",
    title="Przeładunki w porcie w Gdyni",
)
plot.get_figure().savefig("wykres.png")