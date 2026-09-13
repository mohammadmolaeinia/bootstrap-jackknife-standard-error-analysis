# Bootstrap Standard Error Analysis

Monte Carlo comparison of the usual (plug-in) estimate of the standard error of the sample mean with a bootstrap estimate, evaluated against the exact theoretical standard error for a known Normal population.

## Problem Statement

Generate a single sample of 100 observations from some Normal distribution. Compute $\bar{X}$, the usual estimate of the mean, and compute the standard error in the usual way. Now use a large number of bootstrap samples to estimate the standard error. Compare your two estimates of the variance of $\bar{X}$, and compare these with the theoretical standard error (that is, the one you would get if you actually knew the value of $\sigma^2$).

## Project Files

| File | Description |
|------|-------------|
| `bootstrapStandardError.py` | Main script: generates the sample, computes both standard-error estimates, and prints the comparison |
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

### 3. Theoretical (exact) value

Since the true $\sigma$ is known in this exercise, the exact standard error is available for reference:

$$SE_{\text{theory}} = \frac{\sigma}{\sqrt{n}}$$

The script prints the standard error and the variance of $\bar{X}$ for all three approaches so they can be compared directly. All three values are expected to be close: the usual estimate and the bootstrap estimate both approximate $\sigma/\sqrt{n} = 0.2$, differing only by sampling noise (from the single original sample) and Monte Carlo noise (from finitely many bootstrap replications).

## Requirements
```
pip install -r requirements.txt
```

## How to Run
```
python bootstrap_se.py
```

## Output

Terminal output includes:

- Sample mean ($\bar{X}$) and sample standard deviation ($s$)
- True population mean ($\mu$) and true standard deviation ($\sigma$)
- Standard error: usual estimate, bootstrap estimate, theoretical value $\sigma/\sqrt{n}$
- Variance of $\bar{X}$: usual estimate, bootstrap estimate, theoretical value $\sigma^2/n$

## Notes

- This project was developed as part of an academic exercise related to uncertainty modeling, fuzzy variables, and probabilistic simulation in engineering applications.
- The comparison illustrates why the bootstrap is valuable: it agrees closely with the classical formula for statistics that have a closed-form standard error (like the mean), but it also works for statistics such as the median where no simple formula exists.
- A fixed random seed (`seed=42`) is used so results are reproducible; exact printed values will match every run but depend on the seed.
- With $B = 10{,}000$ bootstrap replications, the Monte Carlo noise in $SE_{\text{boot}}$ is small relative to the sampling variability of the original sample of size $n = 100$.
