echo "please input a series of numbers and end with Ctrl+D"
sum=0
while read n
do
  ((sum += n))
done
echo "sum of the input is: $sum"