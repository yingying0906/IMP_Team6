# IMP_Team6

Special Topics in Innovative Integration of Medicine and EECS 2022 Team 6

# Package installation

Using pip to download the pyphe package and shamirs

```
pip install phe
```

```
python -m pip install shamirs
```

# Usage

## Encrypt file

Put the file you want to encrypt in the directory `data`

```
python3 encrypt.py [filename]
```

## Split encrypted file

Split file into `N` shares with threshold `T`
The shares will be stored in `share`

```
python3 split.py [N] [T]
```

## Combine splitted encrypted file

Combine `x` shares, where x must be >= T

```
python3 combine.py [target] [x]
```

## Decrypt combined splitted encrypted file

Decrypt file

```
python3 decrypt.py [target]
```

## remove.sh

Delete all files except original data in `data`

```
sh remove.sh
```
