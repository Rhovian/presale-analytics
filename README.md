## Setup
Supported chains: 
- Ethereum
- Polygon
- Binance Smart Chain

The script excepts a ``.env`` file with the following keys:

```
ETHERSCAN_KEY = <your key here>
POLYGON_KEY = <your key here>
BSC_KEY = <your key here>
```
### Native coin command

```
poetry run python3 presales/main.py -c ethereum -p 0xd82477E8e75f18D210770574F57f31D57FBfC50f -t NATIVE
```

## Examples
These are just some random contracts i found to test the system.

### Binance Smart chain

Target presale: [0x44540f6d9AF649F7c4247817216e95AE82CE06cD](https://bscscan.com/address/0x44540f6d9af649f7c4247817216e95ae82ce06cd#readContract)
<br>
Target token: BUSD | [0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56](https://bscscan.com/address/0xe9e7cea3dedca5984780bafc599bd69add087d56)

*command*
```
poetry run python3 presales/main.py -c bsc -p 0x44540f6d9AF649F7c4247817216e95AE82CE06cD -t 0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56
```


### Ethereum Mainnet

Target presale: [0xd82477E8e75f18D210770574F57f31D57FBfC50f](https://etherscan.io/address/0xd82477e8e75f18d210770574f57f31d57fbfc50f)
<br>
Target token: [0xdAC17F958D2ee523a2206206994597C13D831ec7](https://etherscan.io/address/0xdAC17F958D2ee523a2206206994597C13D831ec7)

*command*
```
poetry run python3 presales/main.py -c ethereum -p 0xd82477E8e75f18D210770574F57f31D57FBfC50f - t 0xdAC17F958D2ee523a2206206994597C13D831ec7
```

### Polygon

Target presale: [0x054925aa212c9CC4610A25df9a18854f461BcdDb](https://polygonscan.com/address/0x054925aa212c9CC4610A25df9a18854f461BcdDb#code)
<br>
Target token: NATIVE

*command*
```
poetry run python3 presales/main.py -c polygon -p 0x054925aa212c9CC4610A25df9a18854f461BcdDb - t NATIVE
```
