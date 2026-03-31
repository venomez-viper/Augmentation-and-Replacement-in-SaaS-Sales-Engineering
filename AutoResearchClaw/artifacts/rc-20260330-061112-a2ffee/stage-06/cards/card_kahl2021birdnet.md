# BirdNET: Deep Learning for Avian Species Identification from Audio

## Cite_Key
kahl2021birdnet

## Problem
Extracting accurate species richness data from large passively collected audio datasets is challenging, limiting the scalability of acoustic biodiversity monitoring.

## Method
ResNet-derived DNN (157 layers, 27M+ parameters) trained on 984 North American and European bird species; domain-specific data augmentation, mixup training; evaluated on single-species recordings, annotated soundscape data, and long-term hotspot audio.

## Data
22,960 single-species recordings; 286 h annotated soundscape; 33,670 h long-term soundscape from 4 eBird hotspots over 4 years.

## Metrics
Mean Average Precision 0.791 (single-species); F0.5 score 0.414 (annotated soundscapes); average correlation 0.251 with eBird hotspot observations across 121 species.

## Findings
Domain-specific augmentation is critical for noise robustness; high temporal resolution spectrograms improve classification; task-specific architectures match complex general architectures; BirdNET enables scalable avian diversity monitoring.

## Limitations
Performance degrades with overlapping vocalizations and high ambient noise; correlation with expert eBird observations is moderate; geographic/taxonomic generalization untested.

## Citation
Kahl et al. (2021). BirdNET: A deep learning solution for avian diversity monitoring. Ecological Informatics. https://doi.org/10.1016/j.ecoinf.2021.101236
