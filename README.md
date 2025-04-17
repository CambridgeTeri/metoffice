# Met Office BDD UI Test Assignment

This repo contains BDD-style UI automation tests for the Met Office website (https://www.metoffice.gov.uk/) using Python with Playwright and Behave for BDD-style testing.

## Setup
1. Clone the repo
2. Create a virtual environment:
   `python -m venv venv && source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
3. Install requirements:
   `pip install -r requirements.txt`

This project contains automated tests for the Met Office website (https://www.metoffice.gov.uk/) using Python with Playwright and Behave for BDD-style testing.

## Project Structure

```
project_structure/
├── features/
│   ├── environment.py                # Test setup and teardown
│   ├── metoffice_forecast.feature    # BDD scenarios
│   └── steps/
│       └── metoffice_steps.py        # Step definitions
├── pages/
│   ├── base_page.py                  # Base page object with common methods
│   ├── home_page.py                  # Home page specific methods
│   ├── forecast_page.py              # Weather forecast page methods
│   ├── pollen_page.py                # Pollen forecast page methods
│   └── precipitation_map_page.py     # Precipitation map page methods
└── requirements.txt                  # Project dependencies
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Unzip or Clone this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows


## Running Tests

To run all tests:

```bash
behave
```

To run with more detailed output:

```bash
behave -v
```

