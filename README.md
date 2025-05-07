# Genetic Trait Punnett Square Visualizer

This project is a Punnett square generator with a graphical user interface that simulates genetic inheritance based on user inputs. It allows users to explore the probabilities of inherited traits by generating a Punnett square based on the genetic input of two parents. The program can visualize the results with a color-coded grid and show phenotype and genotype percentages and ratios.

---

## ✅ Features (What It Can Do)

- **Single and Dihybrid Crosses**  
  Supports monohybrid (1 trait) and dihybrid (2 traits) Punnett squares.

- **Trait Selection**  
  Choose from more than 10 different Mendelian traits such as:
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

## How to Use (Monohybrid)

1. **Download and Run the Program**  
   Download the "Trait_Inheritance_Calculator.exe" file and run it by double clicking it.

2. **Select Trait**  
   Choose your desired trait from the 'Trait 1' dropdown list.

3. **Enter Genotype for Parent 1 and Parent 2**  
   Depending on what trait you selected, the guide on screen will tell you what to enter inside the boxes:

4. **Click the 'Generate Punnet Square' Button**  
   Once steps 2-3 are done, clicking the button will generate a Punnet square along with data.

5. **Click the 'Reset' Button**  
   If you want to clear the canvas, click the 'Reset' button to clear all values and the canvas space.

---

## How to Use (Dihybrid)

1. **Download and Run the Program**  
   Download the "Trait_Inheritance_Calculator.exe" file and run it by double clicking it.

2. **Click the 'Enable Dihybrid Cross' Checkbox**  
   This will enable the ability for you to enter dihybrid mode and choose a second trait.

3. **Select Traits**  
   Choose your desired trait from the 'Trait 1' and 'Trait 2' dropdown list.

4. **Enter Genotype for Parent 1 and Parent 2**  
   Depending on what traits you selected, the guide on screen will tell you what to enter inside the boxes. For dihybrid crosses, you’ll need to input the genotype for both traits. This means entering four letters—two alleles for each of the two traits (e.g., AaBb)."

5. **Click the 'Generate Punnet Square' Button**  
   Once steps 2-4 are done, clicking the button will generate a Punnet square along with data.

6. **Click the 'Reset' Button**  
   If you want to clear the canvas, click the 'Reset' button to clear all values and the canvas space.

---
