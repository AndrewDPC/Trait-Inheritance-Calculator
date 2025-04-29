# Genetic Trait Punnett Square Visualizer

This project is a Punnett square generator with a graphical user interface (GUI) that simulates genetic inheritance based on user inputs. It allows users to explore the probabilities of inherited traits by generating a Punnett square based on the genetic input of two parents. The program can visualize the results with a color-coded grid and show phenotype and genotype percentages and ratios.

---

## ✅ Features (What It Can Do)

- **Single and Dihybrid Crosses**  
  Supports monohybrid (1 trait) and dihybrid (2 traits) Punnett squares.

- **Trait Selection**  
  Choose from 14 different Mendelian traits such as:
  - Eye Color
  - Hair Type
  - Dimples
  - Earlobe Attachment
  - Widow's Peak
  - Tongue Rolling
  - Hitchhiker’s Thumb
  - Handedness
  - Chin Cleft
  - Freckles
  - PTC Tasting
  - Albinism
  - Lactose Intolerance

- **User Input Validation**  
  Validates genotype length based on mono/dihybrid mode.

- **Phenotype and Genotype Calculation**  
  Computes possible offspring genotypes and maps them to traits using a Mendelian dominance model.

- **Color-Coded Visualization**  
  Displays the Punnett square using a Tkinter canvas with unique colors for each phenotype.

- **Statistics Output**  
  Shows percentage and ratio for each phenotype and genotype.

---

## ❌ Limitations (What It Can't Do)

- **Non-Mendelian Genetics**  
  Does not account for incomplete dominance, codominance, polygenic inheritance, or environmental influence.

- **Sex-Linked Traits Modeling**  
  Does not handle X/Y chromosome inheritance patterns (e.g., hemophilia, red-green color blindness correctly).

- **No Dynamic Trait Addition**  
  Traits must be hardcoded in the script and cannot be added through the GUI.

---
