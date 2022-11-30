# change cwd
cd code

# check usage
no_args="true"
usage(){
    echo "Usage: sh cal.sh..."
    echo "Options:"
    echo "  -i        Patient ID"
}

# option
while getopts ':i:' OPT; do
    case ${OPT} in
        i)
            ID=${OPTARG};;
        *)
            usage
            exit;;
    esac
    no_args="false"
done

# no argument
[[ "$no_args" == "true" ]] && { usage; exit 1; }

# computate 
python3 computation.py $ID