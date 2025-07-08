# -*- coding: utf-8 -*-
import requests
import argparse
import sys


def get_ip_info(args):
    """
    Main function to fetch and display IP information.
    """
    try:
        # API URL, which automatically detects the user's IP
        url = "https://ipinfo.io/json"

        print("Fetching your IP information...")

        # Send a request to the API with a 10-second timeout
        response = requests.get(url, timeout=10)

        # Check for HTTP errors (e.g., 404, 500, 429 - rate limit)
        response.raise_for_status()

        # Convert the received JSON data into a dictionary
        data = response.json()

        # Extract the necessary information
        # Using .get() with a default value to avoid errors if a field is missing
        ip_address = data.get('ip', 'N/A')
        isp_org = data.get('org', 'N/A')
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')

        # --- Display Information ---
        print("\n" + "=" * 30)
        print("  PUBLIC IP INFORMATION")
        print("=" * 30)

        print(f"[*] Public IP:      {ip_address}")
        print(f"[*] ISP / Org:      {isp_org}")
        print(f"[*] Location:       {city}, {region}")

        # Display optional information if requested by the user
        if args.country:
            print(f"[*] Country:        {country}")

        if args.asn:
            # ASN information is often included in the 'org' field
            # e.g., "AS18403 The Viettel Group"
            print(f"[*] ASN Info:       {isp_org}")

        print("=" * 30)

    except requests.exceptions.RequestException as e:
        print(f"\n[ERROR] Could not connect to the ipinfo.io service. Please check your internet connection.",
              file=sys.stderr)
        print(f"Error details: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Handles command-line arguments and calls the main function.
    """
    # Create a parser to handle command-line arguments
    parser = argparse.ArgumentParser(
        description="A tool to display your public IP and ISP/Organization information.",
        formatter_class=argparse.RawTextHelpFormatter  # Keep the formatting for the help text
    )

    # Add the arguments
    parser.add_argument(
        '--country',
        action='store_true',  # When this flag is present, its value will be True
        help='Display the country code (e.g., US, VN).'
    )
    parser.add_argument(
        '--asn',
        action='store_true',
        help='Display the ASN (Autonomous System Number) information.'
    )

    # Parse the arguments provided by the user
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    get_ip_info(args)


if __name__ == "__main__":
    main()