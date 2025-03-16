#!/usr/bin/env python3

import random
import json
import os
from utils.planet_generator import generate_exoplanet, validate_exoplanet

def main():
    # Generate an exoplanet with full metadata
    exoplanet = generate_exoplanet()
    
    # Validate the generated exoplanet
    validation_results = validate_exoplanet(exoplanet)
    if not validation_results["valid"]:
        print("\nWarning: Generated exoplanet has inconsistencies!")
        for issue in validation_results["issues"]:
            print(f" - {issue}")
    
    # Display metadata in a readable format
    print("\nGenerated Exoplanet Metadata:\n")
    print(json.dumps(exoplanet, indent=4))
    
    # Ensure output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Save metadata to a JSON file
    file_path = os.path.join(output_dir, "generated_exoplanet.json")
    with open(file_path, "w") as file:
        json.dump(exoplanet, file, indent=4)
        print(f"\nExoplanet metadata saved to {file_path}")
    
    # Save a README file with project description
    readme_content = """# Exoplanet Generator\n\nThis project generates a random but scientifically plausible exoplanet with various metadata, \nvalidates its atmospheric and planetary properties, and outputs the results in JSON format.\n\n## Usage\nRun the script:\n```bash\npython main.py\n```\n\nThe output is displayed in the terminal and saved in the `output/` directory.\n\n## Project Structure\n- `main.py`: Main script to generate and validate an exoplanet\n- `utils/planet_generator.py`: Handles exoplanet metadata generation and validation\n- `output/`: Directory where generated exoplanet metadata is stored\n- `README.md`: Documentation for the project\n\n## Requirements\nEnsure you have Python 3.9+ installed. No additional dependencies are required."""
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)
        print("\nREADME.md file created with project details.")

if __name__ == "__main__":
    main()
