# Latexify

package based in function developed by Nipunbatra

https://nipunbatra.github.io/blog/2014/latexify.html

## Requeriments

The following python packages are requiered

- `matplotlib`
- `math`

## Instalation

```bash
python setup.py install
```

## Usage

```python
import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify

x = np.linspace(0,2*np.pi)
y = np.cos(x)

latexify()

plt.plot(x,y, label="Cosine")

plt.xlabel("Angle")
plt.ylabel("Cosine")

plt.legend()

plt.savefig("test.pdf")
```