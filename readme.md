
# pi bench
Pi Benchmark

## Description
Calculates accurate value of pi using 1 millon iterations of Leibniz’s formula
see: https://www.geeksforgeeks.org/calculate-pi-with-python


## Dependencies
python3


## Example usage

### hp 14 laptop
Integer based calcuations
```
$ time python3 pi-int.py
3.1415925535897915

real    0m1.433s
user    0m1.420s
sys     0m0.013s

```

Decimal based calculations
```
$ time python3 pi-dec.py
3.141591653589793238712643378

real    0m0.550s
user    0m0.534s
sys     0m0.012s
```

### qemu ubuntu vm
Integer based calcuations
```
$ time python3 pi-int.py
3.1415916535897743

real    0m2.809s
user    0m2.678s
sys     0m0.021s

```

Decimal based calculations
```
$ time python3 pi-dec.py
3.141591653589793238712643378

real    0m18.291s
user    0m8.539s
sys     0m0.112s
```


