# MISP Event Exporter

This script fetches events from a MISP instance based on specified tags and exports the details to a CSV file.

## Requirements

- Python 3.x
- `pymisp` library
- `requests` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Bushyon/MISP-tools.git
    ```
2. Navigate to the project directory:
    ```sh
    cd MISP-tools/scripts/event_exporter_tag
    ```
3. Install the required libraries:
    ```sh
    pip install pymisp requests urllib3
    ```

## Usage

1. Open the script `get_iocs_tag.py` and replace the placeholder values with your MISP instance details:
    ```python
    misp_url = 'https://misp-url.com'
    misp_key = 'misp-token'
    misp_verifycert = False
    tags = ['companytag1', 'companytag2']
    start_date = datetime.datetime(2023, 7, 1)
    end_date = datetime.datetime.now()
    ```

2. Run the script:
    ```sh
    python3 get_iocs_tag.py
    ```

3. The script will generate an `output.csv` file with the event details.

## Note

- This script disables SSL warnings for requests. Do not use this in production environments.
- Ensure your MISP instance and API key are correctly configured.
