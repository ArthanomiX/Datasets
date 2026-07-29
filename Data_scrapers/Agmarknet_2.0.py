#Installation
pip install agmarknet

#1. Initialization
from agmarknet import Agmarknet
# Create an instance of the AGMARKNET client
api = Agmarknet()

#2. Fetching Daily Price and Arrival Reports: By default, the SDK requests both price and arrival data (data_type="both"). This ensures you get prices (min, max, modal) as well as arrival volumes and unit names.
df = api.report(
    from_date="2026-06-01",
    to_date="2026-06-05",
    commodity="Tomato",
    state="Karnataka",
    district="Kolar",        # Optional
    market="Bangarpet APMC"  # Optional
)

print(df.head())



### NOTE 
#Hint Number 01
#If need to fetch Long Historical Datasets:  backend API restricts very large queries. To fetch years of historical data, use the start and end parameters. The SDK automatically partitions the request by calendar year, manages page-by-page downloads, and compiles the result:
historical_df = api.report(
    start="2015-01-01",
    end="2026-07-01",
    commodity="Tomato",
    state="Karnataka",
    district="Kolar",
    market="Bangarpet APMC",
    progress=True  # Displays download progress in stdout/stderr
)



#Hint Number 02: if you need to access meta data and filters, use the code
filters = api.filters()

# Access commodity metadata
print(filters.commodities.head())

# Access states metadata
print(filters.states.head())

# Access markets metadata
print(filters.markets.head())
