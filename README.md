# Recommender Systems in Action: Amazon vs. Ratings Platforms

**Author:** Sheriann McLarty  
**Course:** DATA 612 – Recommender Systems  
**Assignment:** Research Discussion #1  
**Repo Branch:** Research-Discussion-1  
**Date:** `r Sys.Date()`

## Overview

This project explores two major types of recommender systems:

- Personalized (Content-Based): A simulated version of Amazon’s co-purchase recommendation system
- Non-Personalized: Popular review platforms including Metacritic, Rotten Tomatoes, and IMDb

The project also discusses potential manipulation tactics, such as shilling attacks, and methods for prevention.

## Included Files

- `Research-Discussion-Assignment-1.Rmd` – RMarkdown source with embedded Python via reticulate
- `Research-Discussion-Assignment-1.html` – Rendered HTML output for submission and viewing
- Visualizations: Two comparison plots generated with Python (Seaborn/Matplotlib)

## Key Concepts

- Simulated content-based filtering logic using co-purchase scores
- Visualization of non-personalized recommendation scores from rating platforms
- Discussion on attacks against recommender systems and platform-level defense strategies
- Recommendations for hybrid approaches that combine user-specific and general scores

## Tools Used

- R with the reticulate package to run embedded Python
- Python libraries: pandas, seaborn, matplotlib
- RMarkdown for document structure and reproducibility

## Summary

Personalized recommenders like Amazon’s can feel intuitive and tailored but may limit user exposure.  
Non-personalized platforms provide broader visibility but are more prone to manipulation.  
A balanced hybrid approach helps create secure, relevant, and user-friendly recommendations.

## View Online

Link to GitHub HTML Preview:  
[Research Discussion Assignment – HTML Output](https://github.com/sheriannmclarty/data612_recommender_systems/blob/Research-Discussion-1/Research-Discussion-Assignment-1.html)

## References

- Linden, G., Smith, B., & York, J. (2003). *Amazon.com Recommendations*. IEEE Internet Computing.
- Hutto, C. J., & Gilbert, E. (2014). *VADER: A Parsimonious Rule-based Model for Sentiment Analysis.*
- Stanford SNAP. *Amazon Product Co-Purchasing Network.* https://snap.stanford.edu/data/amazon-meta.html
- Metacritic. *About Metascores.* https://www.metacritic.com/about-metascores
- Andrews, T. M. (2017). *IMDb Users Gang Up on The Promise.* The Washington Post
