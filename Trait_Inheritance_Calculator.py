'''
Trait Inheritance Calculator 
Created By: Andrew Douangprachanh
'''

import itertools
import tkinter as tk
from tkinter import messagebox

#Dictionary used to store traits
#Contains the trait name, what letters represent what alleles, and the actual trait they represent
TRAITS = {
    "Eye Color": {
        "dominant": "B", "recessive": "b",
        "dominant_trait": "Brown Eyes", "recessive_trait": "Blue Eyes"
    },
    "Hair Type": {
        "dominant": "D", "recessive": "d",
        "dominant_trait": "Curly Hair", "recessive_trait": "Straight Hair"
    },
    "Dimples": {
        "dominant": "M", "recessive": "m",
        "dominant_trait": "Has Dimples", "recessive_trait": "No Dimples"
    },
    "Freckles": {
        "dominant": "F", "recessive": "f",
        "dominant_trait": "Has Freckles", "recessive_trait": "No Freckles"
    },
    "Earlobe Attachment": {
        "dominant": "E", "recessive": "e",
        "dominant_trait": "Free Earlobes", "recessive_trait": "Attached Earlobes"
    }
}

#Function to generate the Punnet square combinations
def GenerateGenotypeCombinations(parent1, parent2, trait):
    
    #Get dominant and recessive allele characters for the selected trait
    dominant = TRAITS[trait]["dominant"]
    recessive = TRAITS[trait]["recessive"]
    
    #Generate all possible combinations of one allele from each parent
    combinations = list(itertools.product(parent1, parent2))
    
    #Sort the alleles so dominant appears first
    sortedCombinations = [''.join(sorted(comb, key=lambda x: x != dominant)) for comb in combinations]
    return sortedCombinations, dominant, recessive, trait


#Function that determines the phenotype from a genotype
def DeterminePhenotype(genotype, dominant, recessive, trait):
    if dominant in genotype:
        return TRAITS[trait]["dominant_trait"]
    else:
        return TRAITS[trait]["recessive_trait"]

#Function to visualize the Punnett square and phenotype percentages
def CreateVisualization(root, canvas, grid, parent1, parent2, phenotype_counts):
    
    #Clear the previous visualization
    canvas.delete("all")

    #Define the size of each cell and calculate grid dimensions
    cellSize = 50
    gridWidth = len(parent2) * cellSize
    gridHeight = len(parent1) * cellSize
    #Calculate x and y offsets to center the grid and leave space for text
    offsetX = (canvas.winfo_width() - gridWidth - 200) // 2  
    offsetY = (canvas.winfo_height() - gridHeight) // 2 - 50 

    #Loop through each row and column of the grid to draw the cells
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            
            #Calculate the coordinates for the cell
            x1 = offsetX + c * cellSize
            y1 = offsetY + r * cellSize
            x2 = x1 + cellSize
            y2 = y1 + cellSize
            
            #Determine phenotype and assign color based on dominant/recessive
            phenotype = DeterminePhenotype(col, TRAITS[traitVar.get()]["dominant"], TRAITS[traitVar.get()]["recessive"], traitVar.get())
            color = "lightblue" if phenotype == TRAITS[traitVar.get()]["dominant_trait"] else "lightpink"
            
            #Draw the cell with appropriate color and label
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black", width=2, tags="grid")
            canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=col, font=('Arial', 10, 'bold'))

    #Label alleles of Parent 1 along the left side of the grid
    for i, allele in enumerate(parent1):
        canvas.create_text(offsetX - 20, offsetY + i * cellSize + cellSize / 2, text=allele, font=('Arial', 10))

    #Label alleles of Parent 2 across the top of the grid
    for i, allele in enumerate(parent2):
        canvas.create_text(offsetX + i * cellSize + cellSize / 2, offsetY - 20, text=allele, font=('Arial', 10))

    #Display phenotype result percentages to the right of the grid
    total = sum(phenotype_counts.values())
    textOffsetX = offsetX + gridWidth + 20
    textOffsetY = offsetY

    canvas.create_text(textOffsetX, textOffsetY, text="Phenotype Percentages:", anchor="w", font=('Arial', 12, 'bold'))
    textOffsetY += 20
    
    #Print each phenotype with its calculated percentage
    for phenotype, count in phenotype_counts.items():
        percentage = (count / total) * 100
        canvas.create_text(textOffsetX, textOffsetY, text=f"{phenotype}: {percentage:.1f}%", anchor="w", font=('Arial', 10))
        textOffsetY += 20


#Function to handle the button click that generates the Punnett square
def GeneratePunnetSquare():
    trait = traitVar.get()
    parent1 = parent1Entry.get().strip()
    parent2 = parent2Entry.get().strip()

    #Validate input: must be 2 characters and valid alleles
    validAlleles = TRAITS[trait]["dominant"] + TRAITS[trait]["recessive"]
    if len(parent1) != 2 or len(parent2) != 2 or not all(c in validAlleles for c in parent1 + parent2):
        messagebox.showerror("Invalid Input", "Genotype must consist of the correct alleles.")
        return

    #Get all genotype combinations and trait details
    square, dominant, recessive, trait = GenerateGenotypeCombinations(parent1, parent2, trait)

    #Convert the flat list into a 2D grid for display
    rows = len(parent1)
    cols = len(parent2)
    grid = []
    index = 0
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(square[index])
            index += 1
        grid.append(row)

    #Count how many times each phenotype appears
    phenotypeCounts = {}
    for genotype in square:
        phenotype = DeterminePhenotype(genotype, dominant, recessive, trait)
        phenotypeCounts[phenotype] = phenotypeCounts.get(phenotype, 0) + 1

    #Draw the Punnett square and phenotype summary
    CreateVisualization(root, canvas, grid, parent1, parent2, phenotypeCounts)

#Function to reset the text fields and clear the canvas
def ResetInputs():
    # Reset the parent genotype entries (without changing the trait selection)
    parent1Entry.delete(0, tk.END)
    parent2Entry.delete(0, tk.END)

    #Clear the canvas
    canvas.delete("all")

#Function to update the trait description when a new trait is selected
def UpdateTraitInfo(*args):
    
    """Update the trait information label based on the selected trait."""
    selectedTrait = traitVar.get()
    dominant = TRAITS[selectedTrait]["dominant"]
    recessive = TRAITS[selectedTrait]["recessive"]
    dominantTrait = TRAITS[selectedTrait]["dominant_trait"]
    recessiveTrait = TRAITS[selectedTrait]["recessive_trait"]

    #Update the info label with trait details
    traitInfoLabel.config(
        text=f"Dominant: {dominant} = {dominantTrait}\nRecessive: {recessive} = {recessiveTrait}"
    )

# --- GUI Setup Below ---

#Create the main window
root = tk.Tk()
root.resizable(False, False)
root.title("Punnett Square Visualization")
root.geometry("700x600")  

#Trait selection dropdown
traitVar = tk.StringVar()
traitVar.set("Eye Color")
traitVar.trace("w", UpdateTraitInfo)  

traitLabel = tk.Label(root, text="Select Trait:")
traitLabel.pack()

traitDropdown = tk.OptionMenu(root, traitVar, *TRAITS.keys())
traitDropdown.pack()

#Trait description label (e.g., A = Brown Eyes)
traitInfoLabel = tk.Label(root, text="", font=('Arial', 10, 'italic'))
traitInfoLabel.pack()

# Update the trait information when the app starts
UpdateTraitInfo()

#Entry fields for each parent's genotype
parent1Label = tk.Label(root, text="Enter Parent 1 Genotype (e.g., Bb):")
parent1Label.pack()
parent1Entry = tk.Entry(root)
parent1Entry.pack()

parent2Label = tk.Label(root, text="Enter Parent 2 Genotype (e.g., Bb):")
parent2Label.pack()
parent2Entry = tk.Entry(root)
parent2Entry.pack()

#Buttons to generate and reset Punnett square
generateButton = tk.Button(root, text="Generate Punnett Square", command=GeneratePunnetSquare)
generateButton.pack()

resetButton = tk.Button(root, text="Reset", command=ResetInputs)
resetButton.pack()

#Canvas to draw the Punnett square visualization
canvas = tk.Canvas(root, width=500, height=500)  
canvas.pack()

#Start the GUI application
root.mainloop()
