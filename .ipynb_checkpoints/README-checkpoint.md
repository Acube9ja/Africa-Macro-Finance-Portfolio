# Africa Macro Finance Portfolio

A collection of independent macroeconomic research projects using public data 
sources. Built to demonstrate applied financial analysis skills across 
data acquisition, cleaning, statistical analysis, and visualisation.

## Projects

### 1. USD Strength & Inflation Transmission — Emerging Africa
Analyses how USD strength transmits to inflation across Nigeria, Ghana, Kenya, 
South Africa, and Egypt using cross-correlation lag analysis (2006–2023).

**Key finding:** Nigeria shows the strongest immediate pass-through (r=0.68), 
while Kenya and South Africa show negative correlations — reflecting structural 
differences between import-dependent and commodity-export economies.

**Tools:** Python, wbgapi, FRED API, statsmodels, matplotlib

---

### 2. Debt Sustainability Analysis — Sub-Saharan Africa
Identifies countries where debt is growing faster than GDP and maps fiscal 
risk against government revenue base (2010–2023).

**Key finding:** Angola is highest risk — debt gap of 10.5pp with only 20% 
revenue/GDP. Zambia shows sustained pre-default stress patterns consistent 
with its 2020 default.

**Tools:** Python, wbgapi, pandas, matplotlib

---

### 3. Nigeria Macro Decomposition
Decomposes Nigeria's GDP into oil and non-oil components and tests whether 
non-oil growth translates to employment gains (2010–2023).

**Key finding:** Nigeria's GDP nearly doubled between 2010–2020 while 
unemployment rose steadily — non-oil growth is not generating jobs, 
pointing to a structural rather than cyclical problem.

**Tools:** Python, wbgapi, FRED API, matplotlib

---

## Setup

```bash
git clone https://github.com/Acube9ja/Africa-Macro-Finance-Portfolio.git
cd Africa-Macro-Finance-Portfolio
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

## Data Sources
- [World Bank Open Data](https://data.worldbank.org/)
- [FRED Economic Data](https://fred.stlouisfed.org/)