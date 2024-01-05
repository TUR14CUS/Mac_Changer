# MAC Changer

MAC Changer is a simple Python script designed to change the MAC address of a network interface on a Linux system. The script provides a user-friendly command-line interface and offers the option to specify a new MAC address or generate a random one.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/TUR14CUS/Mac_Changer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Mac_Changer
   ```

3. Run the script:

   ```bash
   python mac_changer.py
   ```

4. Follow the prompts to enter the interface and, if desired, a new MAC address or use the `--random` option for a randomly generated address.

## Options

- `-i, --interface`: Specify the network interface for which to change the MAC address.

- `-m, --mac`: Specify the new MAC address.

- `-r, --random`: Generate a random MAC address.

## Example

```bash
python mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

or

```bash
python mac_changer.py -i eth0 --random
```

## Dependencies

- Python 3

## Disclaimer

This script is intended for educational purposes only. Changing MAC addresses without proper authorization may violate the terms of service of your network provider.
