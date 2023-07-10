import numpy as np
import json

# Load the configuration
with open('configuration.json') as json_file:
    configuration = json.load(json_file)

# Constants
h = configuration['constants']['h']  # Planck's constant (Joules * seconds)
c = configuration['constants']['c']  # Speed of light (meters/second)
m_e = configuration['constants']['m_e']  # Electron mass (kilograms)

def calculate_initial_photon_energy(wavelength):
    # Energy of a photon is given by E = h * c / wavelength
    return h * c / wavelength

def calculate_final_photon_energy(wavelength, angle):
    # Final energy of a photon after Compton scattering is given by
    # E' = E / (1 + (E / (m_e * c^2)) * (1 - cos(angle)))
    initial_energy = calculate_initial_photon_energy(wavelength)
    return initial_energy / (1 + (initial_energy / (m_e * c**2)) * (1 - np.cos(angle)))

def calculate_wavelength_change(wavelength, angle):
    # Change in wavelength after Compton scattering is given by
    # Δλ = h * (1 - cos(angle)) / (m_e * c)
    return h * (1 - np.cos(angle)) / (m_e * c)

def calculate_final_wavelength(wavelength, angle):
    # Final wavelength after Compton scattering is given by
    # λ' = λ + Δλ
    wavelength_change = calculate_wavelength_change(wavelength, angle)
    return wavelength + wavelength_change
