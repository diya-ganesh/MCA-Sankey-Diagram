# Multilevel Sankey Diagrams for MCA Chicago

**This project, developed as part of the DS3500 course, visualizes data from the Museum of Contemporary Art (MCA) Chicago using multilevel Sankey diagrams. These diagrams explore connections between artist attributes, such as nationality, decade of birth, and gender, providing insights into representation and diversity in the art world.**

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributors](#contributors)

## Introduction

Sankey diagrams are powerful tools for visualizing flows and relationships in complex datasets. This project leverages a dataset of over 10,000 artists represented at the Museum of Contemporary Art Chicago to create compelling visualizations of their attributes. Using the **Plotly** library, this project highlights patterns and insights in artist nationality, decade of birth, and gender.

The project aims to:
- Illustrate the most represented countries, decades, and genders in the MCA collection.
- Highlight patterns in diversity, inclusion, and representation in the art world.
- Extend basic Sankey diagram functionality to handle multilevel flows.

Key tasks include:
1. Aggregating artist data by nationality, gender, and decade of birth.
2. Filtering and visualizing subsets of the data using bi-level and multilevel Sankey diagrams.
3. Providing insights on diversity and bias within the dataset.

## Features

- **Bi-Level Sankey Diagrams:**
  - Nationality vs. Decade of Birth.
  - Nationality vs. Gender.
  - Gender vs. Decade of Birth.
- **Multilevel Sankey Diagram:**
  - Combines nationality, gender, and decade of birth in a single visualization.
- **Custom Visualization Framework:**
  - Modularized Python code to extend and reuse Sankey diagram functionality.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/diya-ganesh/sankey.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd sankey
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare the data:**
   Ensure the `artists.json` dataset is present in the project directory.

2. **Generate the visualizations:**
   ```bash
   python make_visualizations.py
   ```
   - Produces bi-level and multilevel Sankey diagrams in the output directory.

3. **Analyze results:**
   - Review the diagrams and corresponding text analysis for insights.

## Documentation

- **`sankey.py`**: Core functions for creating and customizing Sankey diagrams.
- **`make_visualizations.py`**: Main script to process data and generate diagrams.
- **`artists.json`**: Dataset containing information about artists from MCA Chicago.

## Contributors

- **Diya Ganesh**: Developer and contributor.

---

For more information, see the [project repository](https://github.com/diya-ganesh/sankey). 
