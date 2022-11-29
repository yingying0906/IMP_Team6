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

## Combined use

### add.sh

add the specific data in the database (encrypt and split)

```
sh add.sh [Patient ID] [Number of shares] [Threshold]
```

### get.sh

get the combined file of specific data

```
sh get.sh [Patient ID] [Header] [Number of shares]
```

### cal.sh

calculate the combined data

```
sh cal.sh [Patient ID]
```

## Individual use

### Encrypt file

Put the file you want to encrypt in the directory `data`

```
python3 encrypt.py [filename]
```

### Split encrypted file

Split file into `N` shares with threshold `T`
The shares will be stored in `share`

```
python3 split.py [ID] [N] [T]
```

### Combine splitted encrypted file

Combine `x` shares, where x must be >= T

```
python3 combine.py [ID] [Header] [x]
```

### Decrypt combined splitted encrypted file

Decrypt file

```
python3 decrypt.py [ID] [Header]
```

## Shell script

### remove.sh

Delete all files except original data in `data` and keys in `key`

```
sh remove.sh
```

### test.sh

A demostration of complete process (encrypt, split, combine, decrypt)

### test2.sh

A demostration of computation process (encrypt, split, combine, calculate)

> Recommend run `remove.sh` before using test.sh or test2.sh
