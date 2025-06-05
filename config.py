"""
Configuration file for the Utrecht Mobility Project.
This module defines the directory structure and paths used throughout the project.
"""

from pathlib import Path

# Get the project root directory (where this config.py file is located)
PROJECT_ROOT = Path(__file__).parent.absolute()

# Define data directories relative to project root
DATA_DIR = PROJECT_ROOT / "1.0_data"
RAW_DIR = DATA_DIR / "1.1 - raw"
PROCESSED_DIR = DATA_DIR / "1.2 - processed"
QGIS_DIR = DATA_DIR / "1.3 - QGIS"

# Define output directory relative to project root
OUTPUT_DIR = PROJECT_ROOT / "2.0_notebooks" / "0.0_outputs"

# Create all directories if they don't exist
for directory in [DATA_DIR, RAW_DIR, PROCESSED_DIR, QGIS_DIR, OUTPUT_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Print output to confirm
print(f"Project root directory: {PROJECT_ROOT}")
print(f"Output directory is set to: {OUTPUT_DIR}")


