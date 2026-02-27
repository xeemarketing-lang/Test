# FMCG Field Force & Distributor Analytics Dashboard

A lightweight interactive dashboard template for FMCG operations teams.

## What this includes

- Advanced KPI cards for:
  - Revenue
  - Churn rate
  - Retention rate
  - DAU/MAU stickiness
  - Inventory cover days
- Filter controls:
  - Region
  - Channel
  - Month
- Visual analytics:
  - Sales trend
  - DAU vs MAU
  - Churn vs retention
  - Inventory trend
- Performance tables:
  - Top bookers
  - Distributor health (fill rate, out-of-stock SKUs, coverage)

## Run locally

Preferred (works in preview environments that call non-root paths like `/preview`):

```bash
python3 server.py
```

Fallback static server:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Next enhancements for production

- Connect to your DMS/ERP + SFA APIs.
- Add cohort-based retention analysis.
- Add SKU, beat, and outlet level drilldowns.
- Add forecasting for churn, demand, and stockout risk.
- Add role-based access for management, ASM, SO, and distributor users.
