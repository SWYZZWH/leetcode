read number
if [[ $number -lt 2 ]]; then
    echo "too small"
elif [ $number -lt 4 ]; then
    echo medium
else
    echo large
fi

if ((number < 2)); then
    echo "too small"
elif ((number < 4)); then
    echo medium
else
    echo large
fi

if [ -z "$number" ]; then
    echo empty string
fi

if [ ! -z "$number" ]; then
    echo not empty string
fi


for (( i = 0; i < 10; i++ )); do
    echo $i
done

