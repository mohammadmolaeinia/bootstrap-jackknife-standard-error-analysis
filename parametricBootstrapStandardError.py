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

#now Bootstrap

bootSampleN = 10000
bootMeans = np.empty(bootSampleN)
h = 0.1

for i in range(bootSampleN):
    bootSample = rng.normal(sampleMean, stdD, size=n)
    smoothBootSample = bootSample + rng.normal(0, h, size=n)
    bootMeans[i] = np.mean(smoothBootSample)

bootStandardError = np.std(bootMeans, ddof=1)

sampleVar = sampleStandardError**2
bootVar = bootStandardError**2
theoriVar = theoricalStandardError**2

print(f"The Mean of Sample : {sampleMean:.4f}")
print(f"The STD of Sample : {stdD:.4f}")

print(f"The Real Mean : {normalMean:.4f}")
print(f"The Real STD : {normalSTD:.4f}")

print(f"The Standard Error of Sample : {sampleStandardError:.4f}")
print(f"The Standard Error of Bootstrap : {bootStandardError:.4f}")
print(f"The Real Standard Error : {theoricalStandardError:.4f}")

print(f"The Variance of Sample : {sampleVar:.4f}")
print(f"The Variance of Bootstrap : {bootVar:.4f}")
print(f"The Real Variance : {theoriVar:.4f}")
