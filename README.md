# MIR Cleanup for Mac — version 1.3.0

MIR Cleanup supports review and cleanup of mid-infrared spectra and reference data before modelling.

Version 1.3.0 adds automatic A/B candidate cleanup for eligible properties in a separate session copy, with sample-level exclusions, progress, recovery, and an export readiness summary. Existing manual workflows remain available. Version 1.2.3 avoids a macOS crash associated with the wait cursor during plot redraws, such as when changing properties. Version 1.2.2 removes the application-wide wait cursor, which was implicated in a macOS crash when starting a background task. The Working status remains visible during processing. Version 1.2.1 fixed Excel worksheet export compatibility.

This repository contains the source code and build instructions. A prebuilt application is not included in the repository. The build targets Apple Silicon Macs and requires Python 3.12 and the dependencies listed in `Source/requirements-build.txt`.

To build from the repository root:

```sh
python -m PyInstaller --noconfirm --distpath Build/dist --workpath Build/work "Source/MIR Cleanup.spec"
```

The resulting application is `Build/dist/MIR Cleanup.app`. See [MAC_APP_GUIDE.md](MAC_APP_GUIDE.md) for the review workflow and [MIR_CLEANUP_WORKFLOW.md](MIR_CLEANUP_WORKFLOW.md) for a workflow diagram. Your input data and saved sessions are separate from the application.
