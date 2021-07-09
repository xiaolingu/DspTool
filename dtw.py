from pywt import wavedec
coeffs = wavedec([1,2,3,4,5,6,7,8], 'db1', level=2)
cA2, cD2, cD1 = coeffs
print (cA2, cD2, cD1)