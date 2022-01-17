#
# Get the google auth backup code randomly
#
auth_code_file="~/.authcodebak"
rd=$(($RANDOM%10%5+1))
tail -n5 $auth_code_file| awk 'NR=='"$rd"'{print}'
