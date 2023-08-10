# Galaxy Clusters, Cosmic Chronometers and the Einstein Equivalence Principle   
[![DOI](https://zenodo.org/badge/DOI/10.1088/1475-7516/2021/10/084.svg)](https://doi.org/10.1088/1475-7516/2021/10/084)
[![Inspire HEP](https://img.shields.io/badge/Inspire-HEP-blue)](https://inspirehep.net/literature/1933934)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0001--7182--7273-green)](https://orcid.org/0000-0001-7182-7273)



The Einstein equivalence principle within the electromagnetic sector may may be violated in modified theories of gravity scenarios. Such violations arise from a multiplicative coupling between a scalar field and the electromagnetic Lagrangian. In these theories, deviations from the standard relation of the cosmic distance duality relation and variations in the fine structure constant become intertwined. This study aimed to identify potential cosmological indicators of these effects using measurements of galaxy cluster gas mass fractions and cosmic chronometers.

We achieve this by employing Gaussian Processes Regression (GPR) to reconstruct the angular diameter distance for each galaxy cluster situated at a redshift z, using the H(z) measurements obtained from cosmic chronometers. We maximize the likelihoods for three distinct models: (i) a model with a CDDR violation parameterized by $\eta(z) = 1 + \eta_{0}z$ with a constant depletion factor, (ii) a model with a CDDR violation parameterized by $\eta (z) = (1 + \eta_{0}z)$ with a depletion factor $\gamma (z) = (1+\gamma_{1}z)$, and (iii) a model with a CDDR violation parameterized by $\eta (z) = (1+\eta_{0}z)$ with a constant depletion factor and a non-flat universe.

And our results are summarized in the table:

| Dataset Used                                       | $\eta_{0}$                    | Reference                                                 |
| -------------------------------------------------- | ----------------------------- | --------------------------------------------------------- |
| ADD + SNeIa                                        | $0.069 \pm 0.106$             | [R. F. L. Holanda et. al. 2016](https://arxiv.org/abs/1606.07923) |
| ADD + SNeIa + $T_{CMB}$                            | $−0.005 \pm 0.025$            | [R. F. L. Holanda et. al. 2016](https://arxiv.org/abs/1610.01512) |
| Gas Mass Fraction + SNeIa + $T_{CMB}$             | $−0.020 \pm 0.027$            | [R. F. L. Holanda et. al. 2017](https://arxiv.org/abs/1612.09365) |
| Gas Mass Fraction + Cosmic Chronometers (i)   | $−0.017^{ +0.077 }_{ −0.075 }$    | This Work                                                 |
| Gas Mass Fraction + Cosmic Chronometers (ii)  | $−0.115^{ +0.362 }_{ −0.211 }$    | This Work                                                 |
| Gas Mass Fraction + Cosmic Chronometers (iii) | $0.081^{ +0.389 }_{ −0.359 }$     | This Work                                                 |

For more details on my publication, see: [arXiv](https://arxiv.org/abs/2107.14169v2).
Export citation:
<div style="background-color: Snow; padding: 10px; margin-top: 10px;">
    <a href="https://htmlpreview.github.io/?https://github.com/aCosmicDebugger/Galaxy-Clusters-Cosmic-Chronometers-EEP/blob/main/bibtex.html" style="color: MidnightBlue;">bibtex.txtn</a>
</div>



## Tools Used:


- ![Python](https://img.shields.io/badge/Python-3.11-blue)(https://docs.python.org/3/)
- ![Jupyter Notebook](https://img.shields.io/badge/Jupyter%20Notebook-5.3.0-orange)(https://docs.jupyter.org/en/latest/)
- ![Sci-Kit Learn](https://img.shields.io/badge/Sci--Kit%20Learn-1.2.2-yellow)(https://scikit-learn.org/stable/user_guide.html)
- ![emcee](https://img.shields.io/badge/emcee-3.1.4-green)(https://emcee.readthedocs.io/en/stable/)
- ![corner.py](https://img.shields.io/badge/corner.py-2.2.2-cerulean)(https://corner.readthedocs.io/en/latest/)




Feel free to explore the code and analysis in the associated files.
