# VmDas file types

Brief description of the file types produced by VmDas during ship ADCP data acquisition.

| Extension | Format | Description |
|-----------|--------|-------------|
| `.ENR` | Binary | Raw ADCP ensemble data, exactly as received from the instrument, before any VmDas screening. |
| `.ENJ` | Binary | Modified ADCP ensemble data written by an external user-supplied program (user exit) that reads the `.ENR` file. Only produced when *External Raw ADCP Data Screening* is enabled. VmDas screening can still be applied to it afterwards. |
| `.N1R` / `.N2R` | ASCII text | Raw NMEA navigation data, as received from the first (`.N1R`) and second (`.N2R`) navigation inputs. |
| `.N1J` / `.N2J` | ASCII text | Modified NMEA data, in the same NMEA format as the raw files, written by an external user-supplied program that reads the `.N1R` / `.N2R` files. Only produced when *External Raw Nav Data Screening* is enabled, in which case VmDas reads them instead of the raw files. |
| `.NMS` | Binary | Navigation data after VmDas screening and averaging of the NMEA data between ADCP time stamps. |

## Notes

- The `.ENJ` and `.N1J` / `.N2J` files only exist if the corresponding user exit options are enabled.
