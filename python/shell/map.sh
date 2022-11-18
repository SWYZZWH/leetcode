declare -A map
map["a"]="1"
map["b"]="2"
map["c"]="3"
# shellcheck disable=SC2068
echo ${map[@]}
echo ${map["a"]}
echo ${!map[*]}

for k in ${!map[*]}
do
    echo ${map[$k]}
done

for v in ${map[*]}
do
  echo $v
done

read -a strarr <<< "a b c"
for i in ${strarr[*]}; do
  echo $i
done