# Fct_Useful_Maybe
Set of local fcts that might be useful

# Butterworth filter
* Bandpass Butterworth filter
* Highpass Butterworth filter

# Normal DFT
* The normal discrete Fourier transform  
There are always someone (like me) who would like to use a normal discret Fourier transform instead of the FFT.

# Call Script
If there exists someone (like me) who prefer to work with Python IDLE (really?), or if you want to call a script during execution of another and you also want to avoid some issues caused by ``import``, you can do as this :
```python
import os

filename = 'foobar.py'
path = 'foo/bar/file/path'
with open(os.path.join(path, filename)) as f:
    exec(f.read())
```
or simply:
```python
exec(open('foo/bar/file/path/foobar.py').read())
```
