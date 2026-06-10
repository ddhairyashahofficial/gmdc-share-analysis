import yfinance as yf
import pandas as pd

# ── Configuration ──────────────────────────────────────────────────────────────
ticker = "GMDCLTD.NS"
start  = "2015-01-01"
end    = "2025-10-14"

# ── 1. Download GMDC daily OHLCV data ─────────────────────────────────────────
df = yf.download(ticker, start=start, end=end, progress=True)

print(df.head())
print(df.info())

df.to_csv("gmdc_daily.csv", index=True)
print("Saved to gmdc_daily.csv")

# ── 2. Monthly resampled data ──────────────────────────────────────────────────
monthly = df['Close'].resample('M').agg(['first', 'max', 'min', 'last', 'sum'])
monthly.columns = ['Open', 'High', 'Low', 'Close', 'VolumeSum']
monthly.to_csv("gmdc_monthly.csv", index=True)
print("Saved to gmdc_monthly.csv")

# ── 3. Peer comparison (GMDC vs Coal India vs NMDC) ───────────────────────────
tickers = ["GMDCLTD.NS", "COALINDIA.NS", "NMDC.NS"]
data = {}
for t in tickers:
    data[t] = yf.download(t, start=start, end=end)['Close']

df_peers = pd.concat(data, axis=1)

# Fix: use index=False so the Date column gets a proper header
# (avoids the "Unnamed: 0" artefact when re-reading the CSV)
df_peers.index.name = "Date"
df_peers.to_csv("gmdc_and_peers_close.csv", index=True)
print("Saved to gmdc_and_peers_close.csv")
