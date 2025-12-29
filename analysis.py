#!/usr/bin/env python3
"""
Data analysis script for copper electrolysis experiment.

This script calculates the moles of copper deposited, the theoretical yield
according to Faraday's law, and the percent efficiency of the electrolysis.

Usage:
    python analysis.py --current 0.5 --time 1800 --mass_gain 0.082
    or
    python analysis.py --interactive
"""

import argparse
import sys

# Constants
FARADAY = 96485.33212  # Faraday constant, C mol⁻¹
M_Cu = 63.546           # molar mass of copper, g mol⁻¹
VALENCE = 2             # Cu²⁺ → Cu, 2 electrons per atom

def faraday_law_mass(current_A, time_s):
    """
    Calculate the theoretical mass of copper deposited (or dissolved)
    using Faraday's first law:
    
        m_theoretical = (I * t * M) / (n * F)
    
    where:
        I = current (A)
        t = time (s)
        M = molar mass of copper (g mol⁻¹)
        n = number of electrons transferred per atom (2 for Cu²⁺ → Cu)
        F = Faraday constant (C mol⁻¹)
    
    Returns theoretical mass in grams.
    """
    return (current_A * time_s * M_Cu) / (VALENCE * FARADAY)

def experimental_moles(mass_g):
    """Convert mass of copper (g) to amount of substance (mol)."""
    return mass_g / M_Cu

def efficiency(mass_experimental_g, mass_theoretical_g):
    """
    Calculate the percent efficiency of the electrolysis:
    
        efficiency (%) = (m_experimental / m_theoretical) * 100
    """
    if mass_theoretical_g == 0:
        raise ValueError("Theoretical mass cannot be zero.")
    return (mass_experimental_g / mass_theoretical_g) * 100.0

def run_analysis(current_A, time_s, mass_gain_g):
    """
    Perform the complete analysis and print results.
    """
    print("=" * 50)
    print("Copper Electrolysis Data Analysis")
    print("=" * 50)
    print(f"Current: {current_A:.3f} A")
    print(f"Time: {time_s:.0f} s ({time_s/60:.1f} min)")
    print(f"Experimental mass gain at cathode: {mass_gain_g:.4f} g")
    
    # Theoretical mass
    m_theor = faraday_law_mass(current_A, time_s)
    print(f"Theoretical mass (Faraday's law): {m_theor:.4f} g")
    
    # Moles
    n_exp = experimental_moles(mass_gain_g)
    n_theor = experimental_moles(m_theor)
    print(f"Moles of Cu deposited (experimental): {n_exp:.6f} mol")
    print(f"Moles of Cu deposited (theoretical): {n_theor:.6f} mol")
    
    # Efficiency
    eff = efficiency(mass_gain_g, m_theor)
    print(f"Efficiency: {eff:.2f} %")
    
    # Check for anomalies
    if eff > 105.0:
        print("\n⚠️  Warning: Efficiency > 105% suggests measurement error.")
    elif eff < 95.0:
        print("\n⚠️  Warning: Efficiency < 95% may indicate side reactions or incomplete deposition.")
    else:
        print("\n✓ Efficiency within expected range (95–105%).")
    
    return {
        'current_A': current_A,
        'time_s': time_s,
        'mass_gain_g': mass_gain_g,
        'theoretical_mass_g': m_theor,
        'experimental_moles': n_exp,
        'theoretical_moles': n_theor,
        'efficiency_percent': eff
    }

def interactive_mode():
    """Prompt the user for input values."""
    print("Interactive data entry for copper electrolysis analysis.")
    try:
        current = float(input("Enter current (A): "))
        time = float(input("Enter time (s): "))
        mass = float(input("Enter mass gain at cathode (g): "))
    except ValueError:
        print("Error: please enter numeric values.")
        sys.exit(1)
    
    run_analysis(current, time, mass)

def main():
    parser = argparse.ArgumentParser(
        description="Analyze copper electrolysis data."
    )
    parser.add_argument(
        '--current', type=float,
        help='Constant current in amperes (A)'
    )
    parser.add_argument(
        '--time', type=float,
        help='Electrolysis time in seconds (s)'
    )
    parser.add_argument(
        '--mass_gain', type=float,
        help='Experimental mass gain at cathode (g)'
    )
    parser.add_argument(
        '--interactive', action='store_true',
        help='Run in interactive mode (ignores other arguments)'
    )
    
    args = parser.parse_args()
    
    if args.interactive:
        interactive_mode()
    elif args.current is not None and args.time is not None and args.mass_gain is not None:
        run_analysis(args.current, args.time, args.mass_gain)
    else:
        print("Error: either provide --current, --time, and --mass_gain, or use --interactive.")
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()