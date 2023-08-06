# HAZARD
HAZARD is a repository that contains information about the python package ```pyhazard```, which seeks to facilitate the calculation of seismic hazard by facilitating different GMPEs.

<img src="https://github.com/blyona/HAZARD/blob/main/hazard.png" width="150" height="190" />

- **Autor**: [Benjamín Lyon](https://github.com/blyona)
- **Version**: 1.0.1
- **Fecha**: 22 de febrero del 2023

## Requisitos

- Python 3.8+
- [numpy](https://pypi.org/project/numpy/ "numpy")
- [scipy](https://pypi.org/project/scipy/ "scipy")

## Ejemplos

```
import numpy as np
from pyhazard.gmpes import I2014_REV

To   = 0
M    = [5, 6, 7, 8]
Rrup = 100*np.ones((4 ,1))
Rhyp = 110*np.ones((4 ,1))
Ztor = 15* np.ones((4, 1))
Zhyp = 25* np.ones((4, 1))
Vs30 = 200

lny, sigma, tau, phi = I2014_REV(To, M, Rrup, Rhyp, Ztor, Zhyp, Vs30)
```

## Github

El paquete se puede encontrar con las últimas versiones en el repositorio [HAZARD](https://github.com/blyona/HAZARD).