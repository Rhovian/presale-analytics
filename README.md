### Setup
The script excepts a ``.env`` file with the following keys:

```
ETHERSCAN_KEY = <your key here>
```

This script will work with the free tier for Etherscan, Polygonscan (soon), and bscscan (soon)

### Native coin command

```
poetry run python3 presales/main.py -c ethereum -p 0xd82477E8e75f18D210770574F57f31D57FBfC50f -t NATIVE
```

### ERC20 token command


```
poetry run python3 presales/main.py -c ethereum -p 0xd82477E8e75f18D210770574F57f31D57FBfC50f -t 0xdAC17F958D2ee523a2206206994597C13D831ec7
```
