import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# la libreria pandas serve per la parte di manipolazione dei dati, matplotlib e seaborn servono per la creazione di grafici. 
# pathlib mi importa la clase Path dal moduilo integrato pathlib, consente la gestione di percorsi di file e cartelle in modo moderno.


BASE_DIR = Path(__file__).resolve().parent.parent
file = BASE_DIR / "data" / "covid_sample.csv"

output_dir = BASE_DIR / "outputs"
output_dir.mkdir(exist_ok=True)

# __file__ individua il file python in esecuzione, il primo parent risale alla cartella src, il secondo alla cartella principale

f1 = pd.read_csv(file)
print(f1.head())

# Legge i file con Pandas
# mostra le prime 5 righe del file

cols = ["location", "date", "total_cases", "new_cases", "population"] 
data = f1[cols]

# prende come riferimento alcune colonne utili

data["date"] = pd.to_datetime(data["date"])

# converte la colonna date in formato data

italy = data[data["location"] == "Italy"] 

# fitra solo il paese italia

print("\nStatistiche Italia:")
print(italy.describe()) 

# descrive i dati per la colonna filtrata

# Grafico: nuovi casi nel tempo
plt.figure(figsize=(10,5))
 # crea una nuova finestra per il grafico, specifica le dimensioni con una tupla (10, 5)
sns.lineplot(data=italy, x="date", y="new_cases") 
# crea il tipo di grafico
plt.title("titolo grafico") 
# crea titolo grafico
plt.xlabel("Dati")
plt.ylabel("casi giornalieri")


plt.savefig(
    output_dir / "Covid_trend_italy.png",
    dpi = 300,
    bbox_inches = "tight"
)

plt.show()
