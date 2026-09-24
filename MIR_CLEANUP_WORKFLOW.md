# MIR Cleanup desktop workflow

This chart describes the staged desktop app. The command-line `analyse` command remains a legacy workflow that calculates both halves before manual review.

```mermaid
flowchart TD
 A[Choose workbook, spectra, output and properties] --> B[Validate records and metadata; prepare raw spectra]
 B --> C[Fit PCA: mean-centred, unscaled, up to 15 PCs]
 C --> D[YOU inspect PCA and nearest neighbours]
 D --> E{Confirm exclusions?}
 E -->|Yes| F[Mark exclusions; keep existing coordinates until refit]
 F --> G[Refit PCA on retained spectra; up to three fits]
 G --> D
 E -->|Review finished| H[Finish PCA review; split retained samples into A and B]
 H --> I[Optimize A using B; refit calibration A at rank 15 if feasible]
 I --> J[YOU inspect A plot/table; confirm exclusions; finish A]
 J --> K[Reuse A preprocessing and selected rank for B; evaluate on retained A; diagnose B at rank 15 if feasible]
 K --> L[YOU inspect B plot/table; confirm exclusions; finish B]
 L --> M[Validate decisions and optional percentage limit]
 M --> N[Preview counts; export and verify cleaned workbook; save audit and reports]
 N --> O[Run LOGO or Monte Carlo copy separately]
```

- A/B splitting uses sample-average PCA scores and deterministic Kennard–Stone selection. Replicates remain together.
- Metadata supplies response transformation, units and CO₂ exclusion. Sheet values stay untransformed.
- No point selection or numerical candidate removes data without confirmation.
- Calibration decisions remove either individual spectra or whole samples within a property, as chosen by the user. The percentage limit defaults to disabled; its enabled percentage is editable.
- Calibration plots and tables use the same diagnostic rank; marking exclusions does not refit that half.
- Changed PCA decisions invalidate downstream results. Changed A decisions invalidate B's model and confirmations.
- Saved sessions support resume and source relocation with fingerprint validation. Existing legacy reviews are preserved.
- Exports do not overwrite existing workbooks. The offline PCA viewer uses a labelled basis; hiding points is not refitting PCA.

See `MAC_APP_GUIDE.md` for controls, interpretation and first-release boundaries.
