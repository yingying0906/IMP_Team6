# IMP_Team6

Special Topics in Innovative Integration of Medicine and EECS 2022 Team 6

# Package installation

Using pip to download the pyphe package and shamirs

```
pip install phe
```

```
python3 -m pip install shamirs
```

```
python3 -m pip install cherrypy
```

# Usage

## Combined use

### add.sh

Add specified data in the database (encrypt and split)

```
sh add.sh...
Options:
    -i        Patient ID
    -n        Number of shares need to split
    -t        Minimum number of shares need to combine
    -p        Path of the data
```

### get.sh

Fetch and combine the splitted data to retrieve the original encrypted data

```
sh get.sh...
Options:
    -i        Patient ID
    -h        Header of data needed to combine
    -t        Number of shares needed to combine
```

### cal.sh

Use the combined encrypted data to carry out calculation

```
sh cal.sh...
Options:
    -i        Patient ID
```

## Individual use

### Encrypt file

Put the file you want to encrypt in the directory `data`

```
python3 encrypt.py [path] [filename]
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

### Transfer a csv into data files

```
python3 read_csv.py [filename]
```

## Shell script

### remove.sh

Delete all files except original data in `data` and keys in `key`

```
sh remove.sh
```

## Script for testing
### test.sh

A demostration of complete process (encrypt, split, combine, decrypt)

### test2.sh

A demostration of computation process (encrypt, split, combine, calculate)

> Recommend run `remove.sh` before using test.sh or test2.sh

### test3.sh

A demostration of patient_dataset (encrypt, split, combine, calculate)

```
python3 read_csv.py patient_dataset.csv [number_of_patient]
sh test3.sh patient_dataset [number_of_patient]
```
