# Import essential python libraries
import csv
import sys
import os
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(message)s')

def normalize_csv(input_file_path):
    """
    Reads a CSV file, normalizes its headers and data rows, and writes the output to a new CSV file.

    Expected final headers: 'symbol', 'price', 'price_change', 'price_percent_change'
    """
    # Verify the input file exists
    assert os.path.isfile(input_file_path), f"File not found: {input_file_path}"

    # Define mapping from raw headers to standard headers
    header_mapping = {
        "Symbol": "symbol",
        "Last Price": "price",
        "Change": "price_change",
        "Percent Change": "price_percent_change"
    }
    normalized_headers = ['symbol', 'price', 'price_change', 'price_percent_change']
    normalize_header = lambda header: header_mapping[header] if header in header_mapping else (header.lower() if header.lower() in normalized_headers else header.lower())
    normalized_rows = []

    with open(input_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        raw_headers = reader.fieldnames
        
        # Ensure the CSV file has headers
        assert raw_headers is not None and len(raw_headers) > 0, "CSV file has no headers"
        logging.info(f"Raw headers: {raw_headers}")

        # Generate conversion dictionary
        conversion = {header: normalize_header(header) for header in raw_headers}
        logging.info(f"Header conversion: {conversion}")

        # String string values
        strip_value = lambda x: x.strip() if isinstance(x, str) else x

        # Process each row, applying the conversion and stripping extra spaces
        for row in reader:
            normalized_row = {new_header: strip_value(row.get(raw_header, '')) 
                              for raw_header, new_header in conversion.items()}
            normalized_rows.append(normalized_row)

    # Ensure that the CSV file contained data rows
    assert len(normalized_rows) > 0, "No data rows found in CSV file"

    # Create output file name by appending '_norm' before the extension
    file_root, file_ext = os.path.splitext(input_file_path)
    output_file_path = f"{file_root}_norm.csv"

    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=normalized_headers)
        writer.writeheader()
        for row in normalized_rows:
            writer.writerow(row)

    logging.info(f"Normalized CSV written to: {output_file_path}")
    return output_file_path

if __name__ == '__main__':
    # Check that a CSV file path is provided as an argument
    assert len(sys.argv) == 2, "Usage: python bin/normalize_csv.py <path to raw CSV file>"

    input_csv_path = sys.argv[1]
    output_csv_path = normalize_csv(input_csv_path)
    print(f"Created normalized CSV: {output_csv_path}")
