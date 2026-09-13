# Bootstrap and jackknife Standard Error Analysis

Comparison of plug-in, non-parametric bootstrap, parametric bootstrap with smoothing, jackknife, and theoretical standard error of the sample mean for a known Normal population.

## Problem Statement

- A- Generate a single sample of 100 observations from some Normal distribution. Compute $\bar{X}$, the usual estimate of the mean, and compute the standard error in the usual way. Now use a large number of bootstrap samples to estimate the standard error. Compare your two estimates of the variance of $\bar{X}$, and compare these with the theoretical standard error (that is, the one you would get if you actually knew the value of $\sigma^2$).
- B- Use the parametric bootstrap to estimate the variance for the above data. Try different amounts of smoothing.
- C- Use the jackknife instead of the bootstrap.

## Project Files

| File | Description |
|------|-------------|
| `bootstrapStandardError.py` | generates the sample, computes both standard-error estimates, and prints the comparison |
| `parametricBootstrapStandardError.py` | Parametric bootstrap with smoothing: estimates variance of the sample mean by drawing from a fitted Normal distribution with optional kernel smoothing (bandwidth `h`) |
| `jackKnifeStandardError.py` | Jackknife estimate of the standard error and bias of the sample mean via leave-one-out resampling |
| `question.txt` | Text version of the assignment |
| `requirements.txt` | Python dependencies |

## Method Summary

The script draws one sample of $n = 100$ observations from $N(\mu, \sigma^2)$ with $\mu = 10$ and $\sigma = 2$ (fixed seed for reproducibility) and estimates the uncertainty of $\bar{X}$ in three different ways.

### 1. Usual (plug-in) estimate

The sample mean and sample standard deviation are computed, and the standard error is estimated with the classical formula:

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$$

$$SE_{\text{usual}} = \frac{s}{\sqrt{n}}$$

where $s$ uses the $n-1$ divisor (Bessel's correction), and the variance of $\bar{X}$ is $SE_{\text{usual}}^2$.

### 2. Bootstrap estimate

The observed sample is treated as an estimate of the population, and $B = 10{,}000$ bootstrap samples of size $n$ are drawn from it with replacement. Each bootstrap sample yields a recomputed mean. The bootstrap standard error is the standard deviation of the $B$ bootstrap means (Hesterberg, 2015; Larget, course notes):

$$SE_{\text{boot}} = \sqrt{\frac{1}{B-1}\sum_{b=1}^{B}\left(\bar{x}^{(b)} - \bar{\bar{x}}\right)^2}$$

where $\bar{x}^{(b)}$ is the mean of bootstrap sample $b$ and $\bar{\bar{x}}$ is the average of the $B$ bootstrap means.

The bootstrap is a general resampling technique in which computer simulation replaces mathematical analysis; resampling with replacement from the original sample mimics drawing new samples from the population.

### 3. Parametric bootstrap with smoothing

Instead of resampling from the empirical distribution, the parametric bootstrap draws $B = 10{,}000$ new samples of size $n$ directly from a fitted Normal distribution $N(\bar{x}, s^2)$. To explore the effect of smoothing, each draw is additionally perturbed by independent noise:

$$x_i^* = z_i + \varepsilon_i, \quad z_i \sim N(\bar{x},\, s^2), \quad \varepsilon_i \sim N(0,\, h^2)$$

so the effective sampling variance per observation becomes $s^2 + h^2$. The bandwidth $h$ controls the amount of smoothing; $h = 0$ recovers the unsmoothed parametric bootstrap. The parametric bootstrap variance of $\bar{X}$ is estimated as the variance of the $B$ bootstrap means.

### 4. Jackknife estimate

The jackknife estimates the variance of $\bar{X}$ by leave-one-out resampling. For a sample of size $n$, define $\bar{x}_{(i)}$ as the mean of the sample with observation $i$ removed. The jackknife variance estimator is:

$$\widehat{\text{Var}}_{\text{JK}}(\bar{X}) = \frac{n-1}{n} \sum_{i=1}^{n} \left(\bar{x}_{(i)} - \bar{\bar{x}}_{\text{JK}}\right)^2$$

where

$$
\bar{\bar{x}}_{\text{JK}} = \frac{1}{n}\sum_{i=1}^{n} \bar{x}_{(i)}
$$

The jackknife standard error is:

$$
{SE_{\text{JK}} = \sqrt{\widehat{\text{Var}}_{\text{JK}}}}
$$

The jackknife also estimates bias. For a statistic $T$ estimated from the full sample as $\hat{\theta}$:

$$\widehat{\text{bias}}_{\text{JK}} = (n-1)\left(\bar{\bar{x}}_{\text{JK}} - \bar{x}\right)$$

For the sample mean, this bias is exactly zero by linearity, which the script confirms.

### 5. Theoretical (exact) value

Since the true $\sigma$ is known in this exercise, the exact standard error is available for reference:

$$SE_{\text{theory}} = \frac{\sigma}{\sqrt{n}}$$

The script prints the standard error and the variance of $\bar{X}$ for all three approaches so they can be compared directly. All three values are expected to be close: the usual estimate and the bootstrap estimate both approximate $\sigma/\sqrt{n} = 0.2$, differing only by sampling noise (from the single original sample) and Monte Carlo noise (from finitely many bootstrap replications).

## Requirements
```
pip install -r requirements.txt
```

## How to Run
```
python bootstrapStandardError.py   # non-parametric bootstrap SE
python parametric_bootstrap.py     # Parametric bootstrap with smoothing
python jackknife_se.py             # Jackknife SE and bias estimation
```

## Output

**Terminal output:**

**A- Bootstrap:**

- Sample mean ($\bar{X}$) and sample standard deviation ($s$)
- True population mean ($\mu$) and true standard deviation ($\sigma$)
- Standard error: usual estimate, bootstrap estimate, theoretical value $\sigma/\sqrt{n}$
- Variance of $\bar{X}$: usual estimate, bootstrap estimate, theoretical value $\sigma^2/n$

**B- Parametric Bootstrap:**

- Sample mean ($\\bar{X}$) and sample standard deviation ($s$)
- True population mean ($\\mu$) and true standard deviation ($\\sigma$)
- Standard error: usual estimate, parametric bootstrap estimate, theoretical value $\\sigma/\\sqrt{n}$
- Variance of $\\bar{X}$: usual estimate, parametric bootstrap estimate, theoretical value $\\sigma^2/n$

**C- Jackknife:**

- Sample mean ($\\bar{X}$) and sample standard deviation ($s$)
- True population mean ($\\mu$) and true standard deviation ($\\sigma$)
- Standard error: usual estimate, jackknife estimate, theoretical value $\\sigma/\\sqrt{n}$
- Variance of $\\bar{X}$: usual estimate, jackknife estimate, theoretical value $\\sigma^2/n$
- Bias of the jackknife estimate

## Notes

- This project was developed as part of an academic exercise related to uncertainty modeling, fuzzy variables, and probabilistic simulation in engineering applications.
- The comparison illustrates why the bootstrap is valuable: it agrees closely with the classical formula for statistics that have a closed-form standard error (like the mean), but it also works for statistics such as the median where no simple formula exists.
- The parametric bootstrap differs from the non-parametric (resampling) bootstrap: it assumes a distributional family and draws from the fitted model. Smoothing (bandwidth `h > 0`) inflates the effective variance by $h^2/n$, which is visible in the printed results.
- The jackknife is deterministic — no random draws are involved — and for the mean it agrees closely with the plug-in estimate. It is less accurate than the bootstrap for non-smooth statistics.
- A fixed random seed (`seed=42`) is used so results are reproducible; exact printed values will match every run but depend on the seed.
- With $B = 10{,}000$ bootstrap replications, the Monte Carlo noise in $SE_{\text{boot}}$ is small relative to the sampling variability of the original sample of size $n = 100$.
