#!/usr/bin/env python3

#			(tips)  If this was useful to you.

#                 BTC:	bc1qnqtqyqfu9rntykn299sp3pydr2vn3khwcvd58t
#                ETH:	0x471c21cD1a37994636cc3e588E57ccfF252c9f57
#    (TRC-20)  USDT:	TH4NgnVWR4mqNH5bgC5aq4qQqmnXdh87v3

#			Convert all BTC addr from file "Legacy" to rmd160
#                                  (Compressed btc addr only)

import base58
import time

def decode_bitcoin_address(address):
    decoded = base58.b58decode(address)
    return decoded[:-4]

def extract_ripemd160_hash(decoded):
    return decoded[1:]

def process_legacy_addresses(input_file, output_file):
    with open(input_file, 'r') as f:
        addresses = f.readlines()
    
    with open(output_file, 'w') as f:
        for address in addresses:
            address = address.strip()
            decoded = decode_bitcoin_address(address)
            ripemd160_hash = extract_ripemd160_hash(decoded)
            f.write(ripemd160_hash.hex() + '\n')

def main():
    input_file = "Legacy"
    output_file = "rmd160"
    process_legacy_addresses(input_file, output_file)
    print("Success", output_file)

if __name__ == "__main__":
    main()

input()
