# 2D-Ising-Model-Simulation-Mentropolis-Monte-Carlo

![](Snapshots.png)


## **Abstract**

We present a Python implementation of the two‑dimensional Ising model using the **Metropolis Monte Carlo algorithm** to investigate ferromagnetic phase transitions. The simulation models an $$\( N \times N \)$$ lattice of spins $$(\( S = \pm 1 \))$$ with periodic boundary conditions and nearest‑neighbor interactions. Energy and magnetization are computed from first principles, and the system is evolved via stochastic spin flips governed by the Boltzmann acceptance criterion.  

The framework supports single‑temperature runs for equilibrium property estimation, as well as temperature sweeps to generate magnetization–temperature curves that reveal the critical temperature $$\( T_c \)$$ characteristic of the 2D Ising universality class. Visualization tools include static snapshots of spin configurations and animations of spin dynamics, enabling direct observation of domain formation and critical fluctuations.  

## Overview
This project simulates the **two‑dimensional Ising model** using the **Metropolis Monte Carlo algorithm** to study ferromagnetic phase transitions.  
It computes energy, magnetization, and visualizes spin configurations and dynamics.

The code can:
- Run single‑temperature simulations to measure equilibrium properties
- Sweep over temperatures to produce phase transition curves
- Visualize spin configurations as static plots
- Animate spin dynamics over time


## Features
- **Physics Model**:
  - $$\( N \times N \)$$ lattice of spins $$(\( S = \pm 1 \))$$
  - Nearest‑neighbor interactions with coupling constant $$\( J \)$$
  - Periodic boundary conditions
- **Monte Carlo Updates**:
  - Metropolis acceptance criterion
  - Full‑lattice sweeps per Monte Carlo step
- **Measurements**:
  - Average energy per site
  - Average magnetization per site
- **Visualization**:
  - Static snapshots of spin configurations
  - Magnetization vs. temperature phase transition plots
  - Animated spin dynamics saved as `.mp4`



## Requirements
- Python 3.x
- NumPy
- Matplotlib
- FFmpeg (for saving animations)

Install dependencies:

pip install numpy matplotlib

## Usage

### Run the script: 2D Ising.py

The demo will:
1. Run a single‑temperature simulation at \( T = 2.5 \)
2. Plot the final spin configuration
3. Sweep $$\( T \)$$ from 1.5 to 3.5 to generate a phase transition curve
4. Animate spin dynamics at $$\( T = 2.0 \)$$

## Key Functions

| Function | Purpose |
|----------|---------|
| `initial_lattice(N)` | Generate random spin configuration |
| `energy(lattice, J)` | Compute total lattice energy |
| `magnetization(lattice)` | Compute total magnetization |
| `metropolis_step(lattice, $$beta$$, J)` | Perform one Monte Carlo sweep |
| `run_simulation()` | Run simulation at a fixed temperature |
| `phase_transition()` | Sweep temperatures and plot magnetization curve |
| `plot_snapshot()` | Visualize spin configuration |
| `animate_dynamics()` | Animate spin evolution |



## Output Examples
- **Snapshots**: Color‑coded spin configurations
- **Phase Transition Plot**: Magnetization per site vs. temperature
- **Animation**: `.mp4` file showing domain evolution



## Customization
- `N`: Lattice size
- `T`: Simulation temperature
- `steps`: Total Monte Carlo steps
- `equil`: Number of equilibration steps before measurement
- `T_vals`: Temperature range for phase transition sweep


## References
- K. Binder & D. W. Heermann, *Monte Carlo Simulation in Statistical Physics*, Springer (2010)
- R. H. Swendsen & J.-S. Wang, "Nonuniversal critical dynamics in Monte Carlo simulations," *Phys. Rev. Lett.*, 58, 86–88 (1987)


## License
MIT License: free to use, modify, and distribute with attribution.
