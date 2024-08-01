# MISP Tools and Scripts

A collection of tools and scripts for interacting with and exporting data from a MISP instance.

## Contents

- `get_iocs_tag.py`: Fetches events from a MISP instance based on specified tags and exports them to a CSV file.

## Requirements

- Python 3.x
- Required libraries: `pymisp`, `requests`, `urllib3`

Install the dependencies using pip:

```bash
pip install pymisp requests urllib3
```

## Notes

- Scripts may disable SSL warnings for requests, which is not recommended for production environments. Ensure proper SSL handling in production.
- Contributions and improvements are welcome. Please fork the repository and submit a pull request.