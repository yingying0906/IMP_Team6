# change cwd
cd code

# check usage
no_args="true"
usage(){
    echo "Usage: sh add.sh..."
    echo "Options:"
    echo "  -i        Patient ID"
    echo "  -n        Number of shares needed to split"
    echo "  -t        Minimum number of shares needed to combine"
    echo "  -p        Path of the data"
}

# option
while getopts ':i:n:t:p:' OPT; do
    case ${OPT} in
        i)
            ID=${OPTARG};;
        n)
            NUM_SHARES=${OPTARG};;
        t)
            T_SHARES=${OPTARG};;
        p)
            PATH_d=${OPTARG};;
        (*)
            usage
            exit;;
    esac
    no_args="false"
done

# no argument
[ "$no_args" == "true" ] && { usage; exit 1; }

# encrypt
python3 encrypt.py $PATH_d $ID 

# split
python3 split.py $ID $NUM_SHARES $T_SHARES