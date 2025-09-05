import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Helper functions

def initial_lattice(N):
    #Generate NxN lattice with random spins (+1 or -1).
    return np.random.choice([-1, 1], size=(N, N))


def energy(lattice, J=1.0):
    #Calculate total energy of the lattice.
    N = lattice.shape[0]
    E = 0
    for i in range(N):
        for j in range(N):
            S = lattice[i, j]
            # periodic boundary conditions
            neighbors = lattice[(i+1)%N, j] + lattice[i, (j+1)%N] + \
                        lattice[(i-1)%N, j] + lattice[i, (j-1)%N]
            E += -J * S * neighbors
    return E / 2  # each pair counted twice


def magnetization(lattice):
    #Calculate total magnetization.
    return np.sum(lattice)


def metropolis_step(lattice, beta, J=1.0):
    #Perform one Metropolis Monte Carlo step.
    N = lattice.shape[0]
    for _ in range(N*N):
        i = np.random.randint(0, N)
        j = np.random.randint(0, N)
        S = lattice[i, j]
        neighbors = lattice[(i+1)%N, j] + lattice[i, (j+1)%N] + \
                    lattice[(i-1)%N, j] + lattice[i, (j-1)%N]
        dE = 2 * J * S * neighbors
        if dE < 0 or np.random.rand() < np.exp(-beta * dE):
            lattice[i, j] *= -1
    return lattice


# Run simulation at a single temperature

def run_simulation(N=50, T=2.5, steps=1000, equil=200):
    #Run simulation and measure magnetization/energy.
    beta = 1.0 / T
    lattice = initial_lattice(N)
    E_list, M_list = [], []

    for step in range(steps):
        lattice = metropolis_step(lattice, beta)
        if step >= equil:  # after equilibration
            E_list.append(energy(lattice))
            M_list.append(magnetization(lattice))

    return np.mean(E_list), np.mean(M_list)/N**2, lattice


# Phase transition curve

def phase_transition(N=30, T_vals=np.linspace(1.5, 3.5, 10), steps=2000, equil=500):
    #Sweep temperatures and plot magnetization vs T.
    M_avg, E_avg = [], []

    for T in T_vals:
        E, M, _ = run_simulation(N, T, steps=steps, equil=equil)
        M_avg.append(abs(M))
        E_avg.append(E / N**2)

    plt.figure(figsize=(6,4))
    plt.plot(T_vals, M_avg, 'o-', label="|M| per site")
    plt.xlabel("Temperature (T)")
    plt.ylabel("Magnetization per site")
    plt.title("2D Ising Model Phase Transition")
    plt.legend()
    plt.grid(True)
    plt.savefig("2D Ising Model Phase Tranition")
    plt.show()

    return T_vals, M_avg, E_avg



# Snapshots

def plot_snapshot(lattice, title="Spin configuration"):
    plt.figure(figsize=(5,5))
    plt.imshow(lattice, cmap="coolwarm", interpolation="nearest")
    plt.title(title)
    plt.colorbar(label="Spin")
    plt.savefig("Snapshots")
    plt.show()


# Animation of spin dynamics

def animate_dynamics(N=50, T=2.5, steps=200, savefile="ising_dynamics.mp4"):
    beta = 1.0 / T
    lattice = initial_lattice(N)

    fig, ax = plt.subplots(figsize=(5,5))
    im = ax.imshow(lattice, cmap="coolwarm", animated=True)

    def update(frame):
        nonlocal lattice
        lattice = metropolis_step(lattice, beta)
        im.set_array(lattice)
        return [im]

    ani = animation.FuncAnimation(fig, update, frames=steps, interval=100, blit=True)
    ani.save(savefile, writer="ffmpeg", fps=10)
    plt.close(fig)
    print(f"Animation saved to {savefile}")


# Demo
if __name__ == "__main__":
    # Single run example
    E, M, lattice = run_simulation(N=40, T=2.5, steps=1000, equil=200)
    print(f"Average energy per site: {E/(40*40):.3f}")
    print(f"Average magnetization per site: {M:.3f}")
    plot_snapshot(lattice, "Final spin configuration at T=2.5")

    # Phase transition curve
    T_vals = np.linspace(1.5, 3.5, 10)
    phase_transition(N=30, T_vals=T_vals, steps=1500, equil=300)

    # Animation
    animate_dynamics(N=40, T=2.0, steps=200, savefile="ising.mp4")
