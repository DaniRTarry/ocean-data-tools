# SWOT L3 passes over a region of interest

Tools to find, download and plot SWOT KaRIn L3 sea surface height passes over a given area and time period. The example covers the Balearic Sea in **September 2026**.

The workflow has three steps:

1. **Pass detection** – find which SWOT passes cross the area during the selected period.
2. **Data download** – fetch the matching L3 files from the AVISO THREDDS server and crop them to the overflight window.
3. **Plotting** – Absolute Dynamic Topography (ADT) maps with geostrophic velocity arrows, one panel per pass.

---

## 1. Pass detection

Passes are selected with CNES's [altimetry-search](https://github.com/CNES/altimetry-search) tool, which searches SWOT passes (science and cal/val phases) by date and geographic area. It can be used through its Python API or its map-based GUI.

The result is exported to `selected_passes.csv` (semicolon-separated), with one row per pass and the time window during which the swath is over the area:

```
Cycle number;Pass number;First date;Last date
55;320;2026-09-01 07:53:10;2026-09-01 07:53:55
55;335;2026-09-01 21:08:30;2026-09-01 21:08:42
...
```

Dates must be in UTC.

## 2. Data download

**Product:** SWOT L3 LR SSH, *Expert* version, v3.0 (`forward` processing), distributed by AVISO through THREDDS:

```
https://tds-odatis.aviso.altimetry.fr/thredds/catalog/dataset-l3-swot-karin-nadir-validated/l3_lr_ssh/v3_0/Expert/forward/
```

For each row in the CSV, the script:

- Reads the THREDDS catalog of the cycle with `siphon` (one request per cycle). Cycles not yet published are skipped.
- Finds the file whose name contains `_CCC_PPP_` (cycle/pass). If a pass is missing from the server, it is reported and skipped.
- Downloads the file over HTTP into `swot_data/`, unless it is already there. Downloads that return an HTTP error raise an exception instead of being saved.
- Crops the swath along-track (`num_lines`) to the `First date`–`Last date` window.
- Wraps longitude to −180..180, because some passes cross the Greenwich meridian.

### Credentials

Downloading requires an AVISO account with the SWOT L3 product enabled under *My products*. Credentials are read from `~/.netrc` and are never written in the code:

```
machine tds-odatis.aviso.altimetry.fr
login your_aviso_email
password your_password
```

```bash
chmod 600 ~/.netrc
```

On Windows the file is `%USERPROFILE%\_netrc`.

## 3. Plotting

Each panel shows:

- **Background:** ADT = `ssha_filtered + mdt`, minus a single mean computed over all passes, so colours are comparable between panels.
- **Arrows:** absolute geostrophic velocities `ugos_filtered`, `vgos_filtered`, which are consistent with the ADT field. The arrows are subsampled every few pixels.

All panels share the colour range (98th percentile of |ADT − mean| across all passes), the arrow scale and the spatial domain (lon 0–4°E, lat 39–41.5°N). The subplot grid adapts to the number of passes available: the number of columns is fixed, the rows are computed from the number of files, and unused panels are removed. Tick labels are drawn only on the outer panels.

Output: `swot_all_passes.png`.

## Requirements

```
numpy
pandas
xarray
netCDF4
requests
siphon
matplotlib
cartopy >= 0.22
```

## Notes

- L3 files are published with a delay of a few weeks, so recent passes may not be available yet.
- Some passes are not distributed in L3 (manoeuvres, calibration periods or data rejected during editing).
- `ssha_unfiltered` also contains the nadir altimeter measurements in the gap between the two swaths.

## References

- CNES, *altimetry-search*: https://github.com/CNES/altimetry-search (BSD-3-Clause)
- AVISO, SWOT L3 LR SSH product: https://www.aviso.altimetry.fr
