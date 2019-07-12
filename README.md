# Latexify

package based in function developed by Nipunbatra

https://nipunbatra.github.io/blog/2014/latexify.html

## Requeriments

The following python packages are requiered

- `matplotlib`

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

latexify(columns=2)

plt.plot(x, np.cos(x), label="$\cos x$")
plt.plot(x, np.sin(x), label="$\sin x$")

plt.xlabel("Angle $[^\circ]$")

plt.legend()

plt.savefig("plot.pdf")
```

![Sine and cosine plot](img/plot.png?raw=true "Sine and cosine plot, converted from pdf to png using convert")

[plot.pdf](img/plot.pdf)
