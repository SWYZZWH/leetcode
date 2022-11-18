arr=(1 2 3 4)

for num in "${arr[@]}"
do
  echo $num
done

for num in 1 2 3 4
do
  echo $num
done

for num in {1..5}
do
  echo $num
done

for num in $(seq 0 2 10)
do
  echo $num
done

new_arr=()
for ((i=0; i < 4; i++)) do
  new_arr[((i + 1))]=$i
done
echo "${new_arr[*]}"

# slice of arr
new_arr_1=${new_arr:0:2}
new_arr_2=${new_arr:2:2}
echo "first 2 elements: ${new_arr_1[*]}"
echo "last 2 elements: ${new_arr_2[*]}"
#new_arr=("${new_arr:0:1}" "${new_arr:1:1}")
echo "total array: ${new_arr[*]}"