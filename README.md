# MIR Cleanup Mac package — version 1.2.1

Version 1.2 fixes Excel worksheet export compatibility and adds calibration metrics, plot expansion, a magnifier with selectable rectangle zoom-in/zoom-out directions, cumulative toggle selection, complete legends, spectrum/sample units in A/B, and a combined full-dataset tab.

**Double-click `MIR Cleanup 1.2.1.app` to start.** No terminal or separate Python installation is needed for normal use.

- `MIR Cleanup 1.2.1.app` — ready-to-use application for Apple Silicon Macs.
- `MAC_APP_GUIDE.md` — English instructions for inputs, review, exclusions, saved sessions and export.
- `MIR_CLEANUP_WORKFLOW.md` — workflow diagram and explanation.
- `Source/` — application source, build settings, tests and release copies of shared dependencies; optional for normal use.
- `Verification/` — test results, screenshots and fingerprints of the delivered app files.

You can move this entire folder elsewhere. Keep the `.app` bundle intact. Your reference workbook, spectra and saved sessions are separate data; select them through the app. Windows packaging is not included.

The standalone `soil_mir_data_cleanup.py`, its viewer template, CLI guide and the two `_with_cleanup.py` modelling scripts remain in the parent `Data clean up code` folder. The original modelling scripts remain at the project root. Editing those standalone files does not modify this bundled app; app changes require rebuilding from `Source/`.

The previous `MIR Cleanup.app` (version 1.1) was left intact because it was running during delivery. Finish and close it, then launch `MIR Cleanup 1.2.1.app` for the updated workflow.
