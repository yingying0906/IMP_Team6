# change cwd
cd code

# check usage
no_args="true"
usage(){
    echo "Usage: sh get.sh..."
    echo "Options:"
    echo "  -i        Patient ID"
    echo "  -h        Header of data needed to combine"
    echo "  -t        Number of shares needed to combine"
}

# option
while getopts ':i:h:t:' OPT; do
    case ${OPT} in
    i)
        ID=${OPTARG};;
    h)
        HEADER=${OPTARG};;
    t)
        T_SHARES=${OPTARG};;
    (*)
        usage
        exit;;
    esac
    no_args="false"
done

# no argument
[ "$no_args" == "true" ] && { usage; exit 1; }

# combine and decrypt GOT in 7 share
python3 combine.py $ID $HEADER $T_SHARES