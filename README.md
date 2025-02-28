# GPRMax Simulation Data Processor

## Overview
This project automates the process of **reading, extracting, and saving Ez field data** from **gprMax simulations**. It converts **.out simulation files** into structured **CSV datasets** for further analysis.

## Features
- Reads Ez field data from `.out` simulation files.
- Extracts and processes labels from `labels.txt`.
- Saves structured GPR data into CSV format.
- Handles missing files gracefully.

## Installation
Clone this repository and install the dependencies:
```bash
git clone https://github.com/YOUR_USERNAME/GPRMax-Simulation-Data-Processor.git
cd GPRMax-Simulation-Data-Processor
pip install -r requirements.txt
```

## Usage
Run the script to process GPR simulation data:
```bash
python gprmax_data_processor.py
```

## Expected Output
- A CSV file containing **labels and Ez field data** extracted from the simulation.
- Example output files:
  - `labels.csv` (Processed labels from `labels.txt`)
  - `traces_Ez.csv` (Extracted Ez field values)

## Disclaimer
This script is optimized for a specific **gprMax simulation setup**. If using a different file naming convention or data structure, modifications may be required.

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Make your improvements.
4. Submit a pull request.

## License
This project is licensed under the MIT License.
