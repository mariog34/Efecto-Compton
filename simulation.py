import compton
import numpy as np
import json

# Load the configuration
with open('configuration.json') as json_file:
    configuration = json.load(json_file)

def run_simulation(initial_wavelengths, angles):
    # Preallocate an array to hold the final wavelengths
    final_wavelengths = np.zeros((len(initial_wavelengths), len(angles)))

    # Iterate over all combinations of initial wavelengths and angles
    for i, wavelength in enumerate(initial_wavelengths):
        for j, angle in enumerate(angles):
            # Calculate the final wavelength for this combination
            final_wavelength = compton.calculate_final_wavelength(wavelength, angle)
            final_wavelengths[i, j] = final_wavelength

    return final_wavelengths

def main():
    # Define the initial wavelengths and angles
    initial_wavelengths = np.linspace(configuration['simulation_parameters']['initial_wavelengths'][0], configuration['simulation_parameters']['initial_wavelengths'][1], 100)
    angles = np.linspace(configuration['simulation_parameters']['angles'][0], configuration['simulation_parameters']['angles'][1], 100)

    # Run the simulation
    final_wavelengths = run_simulation(initial_wavelengths, angles)

    # Save the results to a file
    with open('simulation_results.txt', 'w') as f:
        f.write('# This file contains the results of the Compton scattering simulation.\n')
        f.write('# Each row corresponds to a different initial wavelength, and each column corresponds to a different scattering angle.\n')
        f.write('# The values are the final wavelengths of the photons after Compton scattering.\n')
        np.savetxt(f, final_wavelengths)

    

if __name__ == '__main__':
    main()
