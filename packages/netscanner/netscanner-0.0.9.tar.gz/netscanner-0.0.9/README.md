
# NETSCANNER

This project was created as part of my final year undergraduate development project for my Bachelor of Science degree.

This program will conduct a comprehensive scan of the local network and surrounding wireless networks using basic OS utilities, Nmap and airodump-ng.

## Screenshots

![Screenshot 1](https://i.ibb.co/PDy14fL/Screenshot-from-2023-02-21-18-07-54-1.png)
![Screenshot 2](https://i.ibb.co/DfKzcfH/Screenshot-from-2023-02-21-18-08-02-1.png)
![Screenshot 3](https://i.ibb.co/Sm2X70F/Screenshot-from-2023-02-21-18-08-09-1.png)

## Requirements

* `python3`: NETSCANNER was designed to work with Python 3.10.
* [`ifconfig`](https://linux.die.net/man/8/ifconfig): For gathering statistical data on local interfaces.
* [`ethtool`](https://linux.die.net/man/8/ethtool): For gathering statistical data on local interfaces
* [`iwconfig`](https://linux.die.net/man/8/iwconfig): For gathering statistical data on local wireless-capable interfaces.
* [`airmon-ng`](https://www.aircrack-ng.org/doku.php?id=airmon-ng): For enabling monitor mode on capable interfaces.
* [`airodump-ng`](https://www.aircrack-ng.org/doku.php?id=airodump-ng): For capturing 802.11 beacon frames.
* [`Nmap`](https://nmap.org/): For conducting local network reconnaissance.

A monitor-mode capable wireless interface is also required if you wish to use the wireless network discovery feature. See [here](http://www.aircrack-ng.org/doku.php?id=compatible_cards) for more information on this.
## Execution

### Using PyPi
The preferred method of running the program is installing the Python package from PyPi directly.

```bash
  pip install netscanner==0.0.9
```

Then running the program:

```bash
  python3 netscanner <mode specification> <options>
```

### Manually
You can also run the module itself by downloading the __main__.py module and running it.

```bash
  python3 __main__.py <mode specification> <options>
```

## Modes and Options

### Modes 
* Mode 1 
    * This mode will execute all functions of the program. If no flags are specified this will be the mode of operation.
* Mode 2 (-nP)
    * This flag will execute Mode 2, NO PORT SCAN, which will execute the Host Discovery and 802.11 WLAN Discovery processes.
* Mode 3 (-w)
    * This flag will execute Mode 3, WIRELESS ONLY, which will execute the 802.11 WLAN Discovery process exclusively.
* Mode 4 (-l)
    * This flag will execute Mode 4, LOCAL SCAN ONLY, which will execute the Host Discovery and Port Scan processes.
* Mode 5 (-hD)
    * This flag will execute Mode 5, HOST DISCOVERY ONLY, which will execute the Host Discovery Process exclusively.

### Options
* Wireless Scan Period (--wP)
    * This option allows you to specify a scan period for the 802.11 WLAN Discovery process. The default is 60. This value is ignored if the mode of operation is not Mode 1, 2 or 3. Large values will result in longer scan times but greater verbosity.
* Port Scan Period (--pP)
    * This option allows you to specify a scan period for the Port Scan process. The default is 60. This value is ignored if the mode of operation is not Mode 1 or 4. Large values will result in longer scan times but greater verbosity. 
* Port Range (--pR)
    * This option allows you to specify a port range for the Port Scan process. The default is the 100 most common ports determined by Nmap (-F). Large values will result in longer scan times but greater verbosity. It is useful to combine this option with the --pP option to avoid scan timeouts when scanning large ranges. 
## Processes

This section provides a brief synopsis of each process used in the program. There are three processes that are used.

### Host Discovery
This process gathers characteristics about the local network and hosts on the local network using ifconfig, iwconfig, ethtool and the ARP Request Ping Flood and rDNS query flood in Nmap, host discovery techniques.

### Port Scan
By default, this process uses Nmap to determine the state of the 100 most used TCP and UDP ports, determined by Nmap, on all active hosts on the local network using the TCP Half-Open Scan and the UDP Scan, port scanning techniques. The ports that are scanned can be changed using the --pR flag, in the command line, to indicate a port range.

This process also has a default timeout period of 60 seconds which can be changed using the --pP flag.

### Remote WLAN Discovery
This process determines the characteristics of remote wireless networks in the vicinity of the host machine if a wireless interface is present and available using the 802.11 packet capture technique with airodump-ng.

This process has a default timeout period of 60 seconds which can be changed using the --wP flag.
