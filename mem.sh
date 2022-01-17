#
# Get mem usage
#
free -h | grep 'Mem' | awk '{usage=($7)} END {print usage}'
