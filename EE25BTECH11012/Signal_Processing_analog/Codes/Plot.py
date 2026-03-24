import sys
import pandas as pd
import matplotlib.pyplot as plt
import io

def plot_from_stdin():
    # Read the C output from standard input
    data = sys.stdin.read()
    df = pd.read_csv(io.StringIO(data))

    plt.figure(figsize=(8, 6))
    
    # Separate poles and zeros
    zeros = df[df['TYPE'] == 'ZERO']
    poles = df[df['TYPE'] == 'POLE']

    # Plot Zeros (circles) and Poles (crosses)
    plt.scatter(zeros['REAL'], zeros['IMAG'], marker='o', s=100, facecolors='none', edgecolors='blue', label='Zeros')
    plt.scatter(poles['REAL'], poles['IMAG'], marker='x', s=100, color='red', label='Poles')

    # Formatting the S-Plane
    plt.axhline(0, color='black', lw=1) # Real axis
    plt.axvline(0, color='black', lw=1) # Imaginary axis
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.title('Pole-Zero Map (S-Plane)')
    plt.xlabel('Real (σ)')
    plt.ylabel('Imaginary (jω)')
    plt.legend()
    
    # Ensure axes are equal so the unit circle (if added) looks like a circle
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    plot_from_stdin()