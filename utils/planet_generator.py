#!/usr/bin/env python3

import random

def generate_exoplanet():
    """Generates a random exoplanet with scientifically plausible metadata."""
    exoplanet = {
        "name": f"X-{random.randint(1000, 9999)}b",
        "radius_earth": round(random.uniform(1.0, 2.5), 2),
        "mass_earth": round(random.uniform(1.0, 10.0), 2),
        "orbital_distance_au": round(random.uniform(0.1, 1.0), 3),
        "insolation_earth": round(random.uniform(0.5, 2.0), 2),
        "atmosphere_pressure_atm": round(random.uniform(0.5, 2.0), 2),
        "composition": {
            "Nitrogen": round(random.uniform(60, 80), 1),
            "Oxygen": round(random.uniform(15, 30), 1),
            "Carbon Dioxide": round(random.uniform(0.01, 5.0), 2),
            "Methane": round(random.uniform(0.01, 2.0), 2)
        },
        "temperature_kelvin": round(random.uniform(250, 350), 1),
        "gravity_g": round(random.uniform(0.8, 2.5), 2)
    }
    return exoplanet

def validate_gravity(exoplanet):
    """Validates that gravity is consistent with mass and radius."""
    expected_gravity = exoplanet["mass_earth"] / (exoplanet["radius_earth"] ** 2)
    if abs(expected_gravity - exoplanet["gravity_g"]) > 0.2:
        return "Gravity does not match expected value based on mass and radius."
    return None

def validate_atmospheric_composition(exoplanet):
    """Validates that atmospheric composition sums to approximately 100%."""
    total_composition = sum(exoplanet["composition"].values())
    if total_composition < 95 or total_composition > 105:
        return "Atmospheric composition percentages do not sum to approximately 100%."
    return None

def validate_temperature(exoplanet):
    """Validates that surface temperature is within a plausible range."""
    if exoplanet["temperature_kelvin"] < 200 or exoplanet["temperature_kelvin"] > 400:
        return "Surface temperature is outside expected habitable range."
    return None

def validate_exoplanet(exoplanet):
    """Runs all validation checks and returns a report."""
    issues = []
    
    for validation_func in [validate_gravity, validate_atmospheric_composition, validate_temperature]:
        issue = validation_func(exoplanet)
        if issue:
            issues.append(issue)
    
    return {"valid": len(issues) == 0, "issues": issues}
