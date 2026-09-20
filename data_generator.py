import numpy as np
import json

# Declare expected particle masses in MeV/c^2
mass_vals = [0.511, 105.66, 139.57, 493.68]

# Create array for measured data
num_particles = 1000
data = np.zeros(num_particles)

# Generate random indices
rng = np.random.default_rng()
indcs = rng.integers(low=0, high=len(mass_vals), size=num_particles)

# Get particle mass data
for i in range(num_particles):
    data[i] = mass_vals[indcs[i]]

# Write measured particle masses to a json file
with open('data/particle_masses.json', 'w') as f:
    json.dump(data.tolist(), f)