# VmDas file types

Brief description of the file types produced by VmDas during ship ADCP data acquisition, listed roughly in the order of the processing chain.

## ADCP data

| Extension | Format | Description |
|-----------|--------|-------------|
| `.ENR` | Binary | Raw single-ping ADCP ensemble data in beam coordinates, exactly as received from the instrument, before any VmDas screening. |
| `.ENJ` | Binary | Modified ADCP ensemble data written by an external user-supplied program (user exit) that reads the `.ENR` file. Only produced when *External Raw ADCP Data Screening* is enabled. VmDas screening can still be applied to it afterwards. |
| `.ENS` | Binary | Single-ping ADCP data after VmDas screening, still in beam coordinates, with the screened navigation and attitude data merged into each ensemble. |
| `.ENX` | Binary | Single-ping ADCP data transformed to Earth coordinates, using heading and attitude corrections. This is the input to the averaging step. |
| `.STA` | Binary | Short-term averaged ADCP data in Earth coordinates, averaged over the user-defined short-term interval. |
| `.LTA` | Binary | Long-term averaged ADCP data in Earth coordinates, averaged over the user-defined long-term interval. Usually the starting point for most post-processing. |

## Navigation data

| Extension | Format | Description |
|-----------|--------|-------------|
| `.N1R` / `.N2R` | ASCII text | Raw NMEA navigation data, as received from the first (`.N1R`) and second (`.N2R`) navigation inputs. |
| `.N1J` / `.N2J` | ASCII text | Modified NMEA data, in the same NMEA format as the raw files, written by an external user-supplied program that reads the `.N1R` / `.N2R` files. Only produced when *External Raw Nav Data Screening* is enabled, in which case VmDas reads them instead of the raw files. |
| `.NMS` | Binary | Navigation data after VmDas screening and averaging of the NMEA data between ADCP time stamps. |

## Configuration and logs

| Extension | Format | Description |
|-----------|--------|-------------|
| `.VMO` | ASCII text | VmDas options file: the full set of acquisition settings used for the run (ADCP commands, navigation inputs, screening thresholds, averaging intervals, transducer alignment, etc.). Useful to know how the data were collected. |
| `.LOG` | ASCII text | Log of the acquisition session: events, warnings and errors reported by VmDas during data collection. |

## Notes

- The `.ENJ` and `.N1J` / `.N2J` files only exist if the corresponding user exit options are enabled.
- The `.ENS`, `.ENX`, `.STA` and `.LTA` files all use the same RDI binary ensemble format, so the same reader can be used for all of them.

- For a complete processing of the dataset CODAS (Common Ocean Data Access System) should be used. More info can be found at:
    - https://currents.soest.hawaii.edu/docs/adcp_doc/index.html
    - https://github.com/ocesaulo/pysadcp