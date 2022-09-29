# ddr_davis_data

Pakcage uses lvreader(1.2.0) to read and write .set file of Davis. lvreader is not installed with the package and hence it has to be installed saparately. lvreader is not available on pypi (as of Sept 2022).

## Download and install lvreader

[Download *.zip* file of lvreader(1.2.0) from here](https://www.lavision.de/en/downloads/software/python_add_ons.php).

Extract the *.zip* file and inside there are multiple *.whl* files. According to the python version, the resective file needs to be installed. for Python 3.9.0 install *lvreader-1.2.0-cp39-cp39-win_amd64.whl*. For Python 3.10 install *lvreader-1.2.0-cp310-cp310-win_amd64.whl*.

<sub>Above instructions assumes Windows as OS. For Linux the *.whl* file name changes which is easily distinguishible in the list of files.</sub>

Then open Anaconda powershell or cmd.exe. navigate to the extracted folder and perform the installation using pip.

```py
pip install lvreader-1.2.0-cp310-cp310-win_amd64.whl
```
<sub>Select the file name according to the Python version or-else the error will come.</sub>


```python
import time

t1 = time.time()
for i in range(10):
    time.sleep(0.01)
t2 = time.time()
print('time elapsed =',t2-t1)
```

    time elapsed = 0.15801000595092773
    
