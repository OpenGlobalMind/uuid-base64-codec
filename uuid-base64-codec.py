#!/usr/bin/env python3

import base64
import uuid
import argparse
import sys

def encode(uuid_string):
    try:
        # Convert UUID string to UUID object
        uuid_obj = uuid.UUID(uuid_string)
        # Get bytes in little-endian order
        uuid_bytes = uuid_obj.bytes_le
        # Encode to base64 and remove padding
        encoded = base64.urlsafe_b64encode(uuid_bytes).rstrip(b'=').decode('ascii')
        return encoded
    except ValueError as e:
        raise ValueError(f"Invalid UUID: {e}")

def decode(s):
    try:
        # Add padding if necessary
        s += '=' * (4 - len(s) % 4)
        # Decode from base64
        b = base64.urlsafe_b64decode(s)
        # Convert to UUID
        uuid_obj = uuid.UUID(bytes_le=b)
        return str(uuid_obj)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid base64 string: {e}")

def main():
    parser = argparse.ArgumentParser(description="Encode UUID to base64 or decode base64 to UUID.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encode", help="Encode UUID to base64")
    group.add_argument("-d", "--decode", help="Decode base64 to UUID")
    
    args = parser.parse_args()

    try:
        if args.encode:
            result = encode(args.encode)
            print(result)
        elif args.decode:
            result = decode(args.decode)
            print(result)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
