import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
# __file__ individua il file python in esecuzione, il primo parent risale alla cartella src, il secondo alla cartella principale
file = BASE_DIR / "data" / "covid_sample.csv"

output_dir = BASE_DIR / "outputs"
output_dir.mkdir(exist_ok=True)

f1 = pd.read_csv(file) #Legge i file con Pandas

print(f1.head()) #mostra le prime 5 righe del file

cols = ["location", "date", "total_cases", "new_cases", "population"] #prende come riferimento alcune colonne utili
data = f1[cols]

data["date"] = pd.to_datetime(data["date"]) #converte la colonna date in formato data

italy = data[data["location"] == "Italy"] #fitra solo il paese italia

print("\nStatistiche Italia:")
print(italy.describe()) #descrive i dati per la colonna filtrata

# Grafico: nuovi casi nel tempo
plt.figure(figsize=(10,5)) #crea una nuova finestra per il grafico, specifica le dimensioni con una tupla (10, 5)
sns.lineplot(data=italy, x="date", y="new_cases") #crea il tipo di grafico
plt.title("titolo grafico") #crea titolo grafico
plt.xlabel("Dati")
plt.ylabel("casi giornalieri")


plt.savefig(
    output_dir / "Covid_trend_italy.png",
    dpi = 300,
    bbox_inches = "tight"
)

# plt.show()

