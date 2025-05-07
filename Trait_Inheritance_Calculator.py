'''
Trait Inheritance Calculator 
Created By: Andrew Douangprachanh
'''
import itertools
import tkinter as tk
from tkinter import messagebox, ttk

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
    },
    "Widow's Peak": {
        "dominant": "W", "recessive": "w",
        "dominant_trait": "Widow's Peak", "recessive_trait": "Straight Hairline"
    },
    "Tongue Rolling Ability": {
        "dominant": "R", "recessive": "r",
        "dominant_trait": "Can Roll Tongue", "recessive_trait": "Cannot Roll Tongue"
    },
    "Hitchhiker's Thumb": {
        "dominant": "H", "recessive": "h",
        "dominant_trait": "Straight Thumb", "recessive_trait": "Hitchhiker's Thumb"
    },
    "Handedness": {
        "dominant": "L", "recessive": "l",
        "dominant_trait": "Right-Handed", "recessive_trait": "Left-Handed"
    },
    "Chin Cleft": {
        "dominant": "C", "recessive": "c",
        "dominant_trait": "Cleft Chin", "recessive_trait": "No Cleft"
    },
    "Albinism": {
        "dominant": "A", "recessive": "a",
        "dominant_trait": "Normal Pigmentation", "recessive_trait": "Albinism"
    },
    "Lactose Intolerance": {
        "dominant": "L", "recessive": "l",
        "dominant_trait": "Lactose Tolerant", "recessive_trait": "Lactose Intolerant"
    }
}

#A list of colors used to visually distinguish phenotypes in the Punnett square
COLORS = ["lightblue", "lightpink", "lightgreen", "yellow", "violet"]

#Function to generate possible gametes from a genotype
def GetGametes(genotype):
    #Split genotype into pairs of two alleles for each trait
    alleles = [list(genotype[i:i+2]) for i in range(0, len(genotype), 2)]
    
    #Create all combinations: one allele from each trait, return as strings
    #Use Cartesian product to get all possible combinations of one allele from each pair
    #This simulates gamete formation where each gamete gets one allele per gene
    return [''.join(gamete) for gamete in itertools.product(*alleles)]

# Generate all possible offspring genotypes from parent genotypes
def GenerateGenotypeCombinations(parent1, parent2):
    
    #Get gametes for each parent
    parent1Gametes = GetGametes(parent1)
    parent2Gametes = GetGametes(parent2)
    
    #Use Cartesian product: combine each gamete from parent 1 with each from parent 2
    #This forms all possible offspring genotypes (i.e., the full Punnett square)
    
    #Thsi will store all offspring combinations
    square = []
    #1 trait = 2 letters (e.g., Bb)
    numTraits = len(parent1) // 2  

    #Combine each pair of gametes to form offspring genotypes
    for g1 in parent1Gametes:
        for g2 in parent2Gametes:
            offspring = ''
            for i in range(numTraits):
                genePair = g1[i] + g2[i]
                #Make uppercase (dominant) allele come first if needed
                if genePair[0].islower() and genePair[1].isupper():
                    genePair = genePair[1] + genePair[0]
                offspring += genePair
            square.append(offspring)
    return square, parent1Gametes, parent2Gametes

#Generates a Punnett square based on user input for traits and parent genotypes.
#Handles both monohybrid and dihybrid crosses, validates the input,
#calculates genotype/phenotype combinations, and visualizes the results.
def GeneratePunnetSquare():
    
    #Get user-selected traits and parent genotypes
    trait1 = trait1Var.get()
    trait2 = trait2Var.get() if dihybridMode.get() else None
    parent1 = parent1Entry.get().strip()
    parent2 = parent2Entry.get().strip()

    #Get allele definitions from the trait dictionary
    dominant1 = TRAITS[trait1]["dominant"]
    recessive1 = TRAITS[trait1]["recessive"]

    #Assign if there is a trait 2
    if trait2:
        dominant2 = TRAITS[trait2]["dominant"]
        recessive2 = TRAITS[trait2]["recessive"]
    else:
        dominant2 = recessive2 = None

    #Expect 2 alleles (monohybrid) or 4 alleles (dihybrid)
    expectedLength = 4 if dihybridMode.get() else 2

    #Basic input length validation
    if len(parent1) != expectedLength or len(parent2) != expectedLength:
        messagebox.showerror("Invalid Input", "Genotype must consist of the correct number of alleles.")
        return
    
    #Validate allele ordering (e.g., dominant first)
    if not IsValidOrder(parent1, dominant1, recessive1, dominant2, recessive2) or not IsValidOrder(parent2, dominant1, recessive1, dominant2, recessive2):
        # Set the message based on whether trait2 is defined
        message = f"Genotypes must be in correct order (e.g., {dominant1}{recessive1}{dominant2 if trait2 else ''}{recessive2 if trait2 else ''})"
        
        # Show the error message
        messagebox.showerror("Invalid Input", message)
        return


    #Allele validation for monohybrid crosses
    if not dihybridMode.get():
        validAlleles = {dominant1, recessive1}
        if not all(c in validAlleles for c in parent1 + parent2):
            messagebox.showerror("Invalid Input", "Genotype must only contain the correct alleles for the selected trait.")
            return
    else:
        #Allele validation for each trait in dihybrid crosses
        parent1Trait1 = parent1[:2]
        parent1Trait2 = parent1[2:]
        parent2Trait1 = parent2[:2]
        parent2Trait2 = parent2[2:]

        validTrait1Alleles = {dominant1, recessive1}
        validTrait2Alleles = {dominant2, recessive2}

        if not all(c in validTrait1Alleles for c in parent1Trait1 + parent2Trait1):
            messagebox.showerror("Invalid Input", f"The first two alleles must match {trait1}.")
            return
        if not all(c in validTrait2Alleles for c in parent1Trait2 + parent2Trait2):
            messagebox.showerror("Invalid Input", f"The last two alleles must match {trait2}.")
            return

    #Generate the Punnett square and get gametes
    square, parent1Gametes, parent2Gametes = GenerateGenotypeCombinations(parent1, parent2)

    #Create a 2D grid to represent the Punnett square visually
    rows = len(parent1Gametes)
    cols = len(parent2Gametes)
    grid = []
    index = 0
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(square[index])
            index += 1
        grid.append(row)

    #Count occurrences of each genotype and phenotype
    phenotypeCounts = {}
    genotypeCounts = {}
    for genotype in square:
        phenotype = DeterminePhenotype(genotype, dominant1, recessive1,
                                        dominant2 if trait2 else None,
                                        recessive2 if trait2 else None,
                                        trait1, trait2)
        phenotypeCounts[phenotype] = phenotypeCounts.get(phenotype, 0) + 1
        genotypeCounts[genotype] = genotypeCounts.get(genotype, 0) + 1

    #Visualize the grid and results on the canvas
    CreateVisualization(canvas, grid, parent1Gametes, parent2Gametes, phenotypeCounts, genotypeCounts, trait1, trait2)

#Function to check if the genotype is valid and properly ordered
def IsValidOrder(genotype, dominant1, recessive1, dominant2=None, recessive2=None):
    #Loop through each allele pair
    for i in range(0, len(genotype), 2):
        pair = genotype[i:i+2]
        
        #Trait 1 validation
        if i == 0:
            validSet = {dominant1, recessive1}
        #Trait 2 validation
        else:
            if dominant2 is None or recessive2 is None:
                return False  #Invalid for dihybrid case if trait2 alleles missing
            validSet = {dominant2, recessive2}

        #Ensure only allowed allele characters are used
        if not set(pair).issubset(validSet):
            return False

        #Ensure dominant allele (uppercase) comes first
        if sorted(pair, key=lambda x: (x.islower(), x)) != list(pair):
            return False

    return True

#Determine the phenotype (physical trait) from a genotype
def DeterminePhenotype(genotype, dominant1, recessive1, dominant2=None, recessive2=None, trait1=None, trait2=None):
    #For trait1, check if dominant allele is present in the genotype
    phenotype1 = TRAITS[trait1]["dominant_trait"] if dominant1 in genotype else TRAITS[trait1]["recessive_trait"]
    
    #If there's a second trait, check it too
    if trait2:
        phenotype2 = TRAITS[trait2]["dominant_trait"] if dominant2 in genotype else TRAITS[trait2]["recessive_trait"]
        return f"{phenotype1}, {phenotype2}"
    
    #Only one trait is present
    return phenotype1

#Draws the Punnett square and trait statistics on a canvas
def CreateVisualization(canvas, grid, parent1Gametes, parent2Gametes, phenotypeCounts, genotypeCounts, trait1, trait2):
    
    #Clear the canvas before drawing new content
    canvas.delete("all")
    
    #Map each unique phenotype to a color (cycling through COLORS list)
    phenotypeToColor = {p: COLORS[i % len(COLORS)] for i, p in enumerate(phenotypeCounts)}
    
    #Size of each square in the grid
    cellSize = 70
    #Total width based on columns
    gridWidth = len(parent2Gametes) * cellSize
    #Total height based on rows
    gridHeight = len(parent1Gametes) * cellSize
    #Offset the grid so it's centered with space for the text
    offsetX = (canvas.winfo_width() - gridWidth - 600) // 2  
    offsetY = (canvas.winfo_height() - gridHeight) // 2

    #Loop through each row and cell to draw the square
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            x1 = offsetX + c * cellSize
            y1 = offsetY + r * cellSize
            x2 = x1 + cellSize
            y2 = y1 + cellSize
            
            #Get the phenotype for the current genotype
            phenotype = DeterminePhenotype(col, TRAITS[trait1]["dominant"], TRAITS[trait1]["recessive"],
                                             TRAITS[trait2]["dominant"] if trait2 else None,
                                             TRAITS[trait2]["recessive"] if trait2 else None, trait1, trait2)
            #Fill with assigned color for this phenotype
            color = phenotypeToColor.get(phenotype, "white")
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black", width=2)
            canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=col, font=('Arial', 10, 'bold'))

    #Draw gametes labels along the top and left of the grid
    for i, gamete in enumerate(parent1Gametes):
        canvas.create_text(offsetX - 20, offsetY + i * cellSize + cellSize / 2, text=gamete, font=('Arial', 10, 'bold'))
    for i, gamete in enumerate(parent2Gametes):
        canvas.create_text(offsetX + i * cellSize + cellSize / 2, offsetY - 20, text=gamete, font=('Arial', 10, 'bold'))
    
    #Total number of genotypes/phenotypes
    totalGenotypes = sum(genotypeCounts.values())
    totalPhenotypes = sum(phenotypeCounts.values())
    
    #Where to start drawing phenotype/genotype info
    textOffsetX = offsetX + gridWidth + 30
    textOffsetY = offsetY

    #Title for phenotype data
    canvas.create_text(textOffsetX, textOffsetY, text="Phenotype Percentages & Ratios:", anchor="w", font=('Arial', 12, 'bold'))
    textOffsetY += 30
    
    #Width for phenotype text block
    phenotypeColumnWidth = 250  
    genotypeColumnOffset_X = textOffsetX + phenotypeColumnWidth + 50  # Space between columns for genotype

    #Show each phenotype with color, percentage, and ratio
    for phenotype, count in phenotypeCounts.items():
        percentage = (count / totalPhenotypes) * 100
        ratio = f"{count}/{totalPhenotypes}"
        color = phenotypeToColor.get(phenotype, "white")
        
        #Small colored box next to phenotype
        canvas.create_rectangle(textOffsetX - 5, textOffsetY - 5, textOffsetX + 15, textOffsetY + 15, fill=color)
        #Text next to colored box
        canvas.create_text(textOffsetX + 25, textOffsetY, text=f"{phenotype}: {percentage:.1f}% ({ratio})", anchor="w", font=('Arial', 10))
        textOffsetY += 25

    #Now display genotypes side by side with phenotypes
    canvas.create_text(genotypeColumnOffset_X, offsetY, text="Genotype Percentages & Ratios:", anchor="w", font=('Arial', 12, 'bold'))
    textOffsetY = offsetY + 30 

    #Sort genotypes by their percentage in descending order
    sortedGenotypes = sorted(genotypeCounts.items(), key=lambda x: (x[1] / totalGenotypes) * 100, reverse=True)

    #Display sorted genotypes
    for genotype, count in sortedGenotypes:
        percentage = (count / totalGenotypes) * 100
        ratio = f"{count}/{totalGenotypes}"
        canvas.create_text(genotypeColumnOffset_X + 25, textOffsetY, text=f"{genotype}: {percentage:.1f}% ({ratio})", anchor="w", font=('Arial', 10))
        textOffsetY += 25

#Updates the label with descriptions of the selected traits, showing
#which alleles are dominant and recessive, and their associated traits.
def UpdateTraitInfo(*args):
    # et the currently selected trait from the first dropdown (always used)
    selectedTrait1 = trait1Var.get()
    #If in dihybrid mode, get the second selected trait; otherwise, use an empty string
    selectedTrait2 = trait2Var.get() if dihybridMode.get() else ""
    
    #Initialize the info string that will hold the description of the selected traits
    info = ""

    #If trait is selected in the first dropdown
    if selectedTrait1:
        
        #Look up details of the selected trait from the TRAITS dictionary
        trait1 = TRAITS.get(selectedTrait1, {})
        
        #Extract dominant and recessive allele symbols and their associated traits
        dominant1 = trait1.get("dominant", "")
        recessive1 = trait1.get("recessive", "")
        dominantTrait1 = trait1.get("dominant_trait", "")
        recessiveTrait1 = trait1.get("recessive_trait", "")

        #Add the formatted trait information to the info string
        info += (f"Trait 1: Dominant: {dominant1} = {dominantTrait1}, "
                 f"Recessive: {recessive1} = {recessiveTrait1}")

    #If a second trait is selected and dihybrid mode is enabled
    if selectedTrait2:
        
        #Look up the second trait from the TRAITS dictionary
        trait2 = TRAITS.get(selectedTrait2, {})
        
        #Extract dominant and recessive allele symbols and their associated traits
        dominant2 = trait2.get("dominant", "")
        recessive2 = trait2.get("recessive", "")
        dominantTrait2 = trait2.get("dominant_trait", "")
        recessiveTrait2 = trait2.get("recessive_trait", "")

        #Add the formatted second trait information to the info string, on a new line
        info += (f"\nTrait 2: Dominant: {dominant2} = {dominantTrait2}, "
                 f"Recessive: {recessive2} = {recessiveTrait2}")
    
    #Update the label in the GUI to display the trait information
    traitInfoLabel.config(text=info)

#Function that clears user inputs and resets the canvas
def ResetInputs():
    parent1Entry.delete(0, tk.END)
    parent2Entry.delete(0, tk.END)
    canvas.delete("all")
    
#Enables or disables the Trait 2 dropdown and updates the trait info display based on whether dihybrid mode is active.
def ToggleMode():
    if dihybridMode.get():
        trait2Dropdown.config(state='normal')
    else:
        trait2Dropdown.config(state='disabled')
    UpdateTraitInfo()
    

# --- GUI Setup Below ---

#Create the main window
root = tk.Tk()
root.title("Trait Inheritance Calculator")
root.geometry("1100x750")
root.configure(bg="lightblue")
root.resizable(False, False)

# Style configuration for ttk widgets
style = ttk.Style(root)
style.configure('TLabel', font=('Arial', 11))
style.configure('TButton', font=('Arial', 11), padding=5)
style.configure('TCombobox', font=('Arial', 11))

#Create a frame to hold all the input widgets
frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=10)

# --- TRAIT 1 ---
#Label for Trait 1
tk.Label(frame, text="Trait 1:", bg="lightblue", font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=5, sticky='e')
#Dropdown for Trait 1 selection
trait1Var = tk.StringVar(value=list(TRAITS.keys())[0])
trait1Dropdown = ttk.Combobox(frame, textvariable=trait1Var, values=list(TRAITS.keys()), state="readonly")
trait1Dropdown.grid(row=0, column=1, padx=5)
trait1Dropdown.bind("<<ComboboxSelected>>", UpdateTraitInfo)

# --- TRAIT 2 ---
#Label for Trait 2
tk.Label(frame, text="Trait 2:", bg="lightblue", font=('Arial', 12, 'bold')).grid(row=0, column=2, padx=5, sticky='e')
#Dropdown for Trait 2 selection (initially disabled unless dihybrid mode is enabled)
trait2Var = tk.StringVar(value=list(TRAITS.keys())[1])
trait2Dropdown = ttk.Combobox(frame, textvariable=trait2Var, values=list(TRAITS.keys()), state="disabled")
trait2Dropdown.grid(row=0, column=3, padx=5)
trait2Dropdown.bind("<<ComboboxSelected>>", UpdateTraitInfo)

# --- PARENT 1 GENOTYPE ---
#Label for Parent 1 genotype input
tk.Label(frame, text="Parent 1 Genotype:", bg="lightblue", font=('Arial', 12, 'bold')).grid(row=1, column=0, padx=5, sticky='e')
#Entry for Parent 1 genotype (default is "Bb")
parent1Entry = tk.Entry(frame, width=10, font=('Arial', 11))
parent1Entry.grid(row=1, column=1, padx=5)
parent1Entry.insert(0, "Bb")

# --- PARENT 2 GENOTYPE ---
#Label for Parent 2 genotype input
tk.Label(frame, text="Parent 2 Genotype:", bg="lightblue", font=('Arial', 12, 'bold')).grid(row=1, column=2, padx=5, sticky='e')
#Entry for Parent 2 genotype (default is "Bb")
parent2Entry = tk.Entry(frame, width=10, font=('Arial', 11))
parent2Entry.grid(row=1, column=3, padx=5)
parent2Entry.insert(0, "Bb")

# --- DIHYBRID MODE CHECKBOX ---
#Checkbox to enable/disable dihybrid cross (two traits at once)
dihybridMode= tk.BooleanVar(value=False)
tk.Checkbutton(frame, text="Enable Dihybrid Cross", variable=dihybridMode, bg="lightblue", font=('Arial', 11), command=ToggleMode).grid(row=2, column=0, columnspan=4, pady=5)

# --- TRAIT INFO DISPLAY ---
#Label to show dominant/recessive info for selected traits
traitInfoLabel = tk.Label(root, text="", bg="lightblue", font=('Arial', 11))
traitInfoLabel.pack(pady=5)
UpdateTraitInfo() #Show info based on default selections

# --- BUTTONS ---
#Frame to group action buttons
buttonFrame = tk.Frame(root, bg="lightblue")
buttonFrame.pack(pady=10)

#Button to generate Punnett square
generateButton = tk.Button(frame, text="Generate Punnet Square", command=GeneratePunnetSquare,
                            bg="green", fg="white", activebackground="green", activeforeground="white",
                            font=('Arial', 11, 'bold'), padx=10)
generateButton.grid(row=3, column=1)
#Button to reset all input fields and canvas
resetButton = tk.Button(frame, text="Reset", command=ResetInputs,
                         bg="red", fg="white", activebackground="red", activeforeground="white",
                         font=('Arial', 11, 'bold'), padx=10)
resetButton.grid(row=3, column=2)

# --- OUTPUT CANVAS ---
#Canvas where the Punnett square will be drawn
canvas = tk.Canvas(root, width=1000, height=500, bg="white")
canvas.pack(pady=20)

#Start the Tkinter main event loop (keeps window open and responsive)
root.mainloop()