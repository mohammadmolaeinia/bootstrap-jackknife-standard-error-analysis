import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

#creat sample of 100 Observ from normal Dist 

sampleN = 100
rng = np.random.default_rng(seed=42)
normalMean = 10
normalSTD = 2
mainSample = rng.normal(normalMean, normalSTD, sampleN)

#for making Standard Deviation we need number of data and avrage of data
sampleMean = np.mean(mainSample)
stdD = np.std(mainSample, ddof=1)
n = len(mainSample)
sampleStandardError = stdD / math.sqrt(sampleN)
theoricalStandardError = normalSTD / math.sqrt(sampleN)

#now Jackknife

jKMeans = np.empty(n)

for i in range(n):
    jKSample = np.delete(mainSample, i)
    jKMeans[i] = np.mean(jKSample)

jKMeanBar = np.mean(jKMeans)
jKVar = (n - 1) / n * np.sum((jKMeans - jKMeanBar)**2)
jKStandardError = np.sqrt(jKVar)

sampleVar = sampleStandardError**2
theoriVar = theoricalStandardError**2

bias = (n - 1) * (jKMeanBar - sampleMean)

print(f"The Mean of Sample : {sampleMean:.4f}")
print(f"The STD of Sample : {stdD:.4f}")

print(f"The Real Mean : {normalMean:.4f}")
print(f"The Real STD : {normalSTD:.4f}")

print(f"The Standard Error of Sample : {sampleStandardError:.4f}")
print(f"The Standard Error of JackKnife : {jKStandardError:.4f}")
print(f"The Real Standard Error : {theoricalStandardError:.4f}")

print(f"The Variance of Sample : {sampleVar:.4f}")
print(f"The Variance of JackKnife : {jKVar:.4f}")
print(f"The Real Variance : {theoriVar:.4f}")
print(f"The bias : {bias:.4f}")
