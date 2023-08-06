# comforter

`comforter` is a small python package for performing statistical coverage tests
to make you feel comfortable with the quality of your posterior estimators. `comforter`
is framework-agnostic: it works with posterior estimators and samplers written in
numpy, pytorch, jax.

`comforter` currently implements the distance to random point (DRP) test introduced
in [Lemos, Coogan et al 2023](https://arxiv.org/abs/2302.03026), which relies on
posterior samples.

<!-- An upcoming release will implement the highest posterior density region test (HPDR; see [Hermans, Delaunoy et al 2022](https://arxiv.org/abs/2110.06581) or [Cole et al 2022](https://arxiv.org/abs/2111.08030)), which requires a posterior density estimator. -->

## Installation

Soon you'll be able to install from PyPI with `pip install comforter`. For now,
```
git clone git@github.com:Ciela-Institute/comforter.git
cd comforter
pip install .
```
will install the `comforter` package.

## Contributing

Please reach out to us if you're interested in contributing!

To start, follow the installation instructions, replacing the last line with
```bash
pip install -e ".[dev]"
```
This creates an editable install and installs the dev dependencies for generating
docs, running tests and packaging for PyPI.

Please use `isort` and `black` to format your code. Open up [issues](https://github.com/Ciela-Institute/comforter/issues)
for bugs/missing features. Use pull requests for additions to the code. Write tests
that can be run by [`pytest`](https://docs.pytest.org/).
