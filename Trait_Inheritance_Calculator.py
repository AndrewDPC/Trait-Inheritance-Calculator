'''
Trait Inheritance Calculator 
Created By: Andrew Douangprachanh
'''
import itertools

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
def punnett_square(parent1, parent2, trait):
    #Get dominant and recessive allele characters for the selected trait
    dominant = TRAITS[trait]["dominant"]
    recessive = TRAITS[trait]["recessive"]
    
    #Generate all possible combinations of one allele from each parent
    combinations = list(itertools.product(parent1, parent2))

    #Sort the alleles so dominant appears first
    sorted_combinations = [ ''.join(sorted(comb, key=lambda x: x != dominant)) for comb in combinations]

    return sorted_combinations, dominant, recessive, trait

#FUnction that determines the phenotype from a genotype
def determine_phenotype(genotype, dominant, recessive, trait):
    #If the dominant allele is present, the dominant trait is expressed
    if dominant in genotype:
        return TRAITS[trait]["dominant_trait"]
    #If both alleles are recessive, the recessive trait is expressed
    else:
        return TRAITS[trait]["recessive_trait"]

def main():
    print("Trait Inheritance Calculator\n")

    #Display available traits for user to choose from
    print("Available Traits:")
    for trait in TRAITS.keys():
        print(f"- {trait}")
    
    #Prompt the user to select a trait by typing it
    trait = input("Choose a trait from the list: ").strip()

    #Check if the selected trait exists in the TRAITS dictionary
    if trait not in TRAITS:
        print("Invalid trait selected.")
        return
    
    #Ask to enter the geneotypes for both parents
    parent1 = input(f"Enter genotype for Parent 1 (e.g., Bb for {trait}): ").strip()
    parent2 = input(f"Enter genotype for Parent 2 (e.g., Bb for {trait}): ").strip()

     #Validate that input is two characters long and uses valid alleles
    if len(parent1) != 2 or len(parent2) != 2 or not all(allele in TRAITS[trait]["dominant"] + TRAITS[trait]["recessive"] for allele in parent1 + parent2):
        print("Invalid input. Genotype must consist of the correct alleles.")
        return

    #Generate the Punnet square combinations
    square, dominant, recessive, trait = punnett_square(parent1, parent2, trait)

    #Display the Punnett square
    print(f"\nPunnett Square for {trait}:")
    print(f"Parent 1: {parent1} x Parent 2: {parent2}")
    print("Possible offspring genotypes:")
    for genotype in square:
        print(f"   {genotype}")

    #Display the phenotyope for each genotype
    print("\nPhenotype Results:")
    phenotypes = [determine_phenotype(genotype, dominant, recessive, trait) for genotype in square]
    for phenotype in phenotypes:
        print(f"   {phenotype}")

if __name__ == "__main__":
    main()
