echo "patient:" $1

echo "file convert"
time sh 1conv.sh $1
echo "================"

echo "encrypt"
time sh 2encrypt.sh $1
echo "================"

echo "split"
time sh 3split.sh $1
echo "================"

echo "reconstruct"
time sh 4recon.sh $1 GPT & time sh 4recon.sh $1 GOT
echo "================"

echo "computed"
time sh 5compute.sh $1
echo "================"

echo "decrypt"
time sh 6decrypt.sh $1 GOT & time sh 6decrypt.sh $1 GPT
echo "================"

