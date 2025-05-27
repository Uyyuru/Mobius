import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MobiusStrip:
    def __init__(self, R, w, n):
        """Initialize the Mobius strip with radius R, width w, and resolution n."""
        self.R = R  # Radius from center to strip
        self.w = w  # Width of the strip
        self.n = n  # Resolution (number of points along u and v)
        self.generate_mesh()
        self.compute_surface_area()
        self.compute_edge_length()

    def generate_mesh(self):
        """Generate a 3D mesh of points on the Mobius strip surface."""
        # Parameter ranges
        u = np.linspace(0, 2 * np.pi, self.n)
        v = np.linspace(-self.w / 2, self.w / 2, self.n)
        # Create 2D grid of u and v values
        U, V = np.meshgrid(u, v, indexing='ij')
        self.U = U
        self.V = V
        # Parametric equations
        self.X = (self.R + V * np.cos(U / 2)) * np.cos(U)
        self.Y = (self.R + V * np.cos(U / 2)) * np.sin(U)
        self.Z = V * np.sin(U / 2)

    def compute_surface_area(self):
        """Compute the surface area numerically using the parametric surface area formula."""
        # Partial derivatives with respect to u
        dx_du = (-0.5 * self.V * np.sin(self.U / 2)) * np.cos(self.U) - (self.R + self.V * np.cos(self.U / 2)) * np.sin(self.U)
        dy_du = (-0.5 * self.V * np.sin(self.U / 2)) * np.sin(self.U) + (self.R + self.V * np.cos(self.U / 2)) * np.cos(self.U)
        dz_du = 0.5 * self.V * np.cos(self.U / 2)
        # Partial derivatives with respect to v
        dx_dv = np.cos(self.U / 2) * np.cos(self.U)
        dy_dv = np.cos(self.U / 2) * np.sin(self.U)
        dz_dv = np.sin(self.U / 2)
        # Cross product components
        cross_x = dy_du * dz_dv - dz_du * dy_dv
        cross_y = dz_du * dx_dv - dx_du * dz_dv
        cross_z = dx_du * dy_dv - dy_du * dx_dv
        # Magnitude of the cross product (area element)
        mag = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
        # Numerical double integration over v then u
        v = np.linspace(-self.w / 2, self.w / 2, self.n)
        u = np.linspace(0, 2 * np.pi, self.n)
        integral_v = np.trapz(mag, v, axis=1)
        self.surface_area = np.trapz(integral_v, u)

    def compute_edge_length(self):
        """Compute the edge length numerically along the boundary curve."""
        # Boundary curve parameterization: u from 0 to 4π at v = w/2
        s = np.linspace(0, 4 * np.pi, 2 * self.n)
        u_s = s
        V_s = np.full_like(u_s, self.w / 2)
        # Partial derivatives with respect to u at v = w/2 (speed components)
        dx_du_s = (-0.5 * V_s * np.sin(u_s / 2)) * np.cos(u_s) - (self.R + V_s * np.cos(u_s / 2)) * np.sin(u_s)
        dy_du_s = (-0.5 * V_s * np.sin(u_s / 2)) * np.sin(u_s) + (self.R + V_s * np.cos(u_s / 2)) * np.cos(u_s)
        dz_du_s = 0.5 * V_s * np.cos(u_s / 2)
        # Speed along the boundary
        speed = np.sqrt(dx_du_s**2 + dy_du_s**2 + dz_du_s**2)
        # Numerical integration
        self.edge_length = np.trapz(speed, s)

    def plot_surface(self):
        """Generate a 3D plot of the Mobius strip and save it to a file."""
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Mobius Strip')
        plt.savefig('mobius_strip.png')
        plt.close()

# Example usage
if __name__ == "__main__":
    # Test parameters
    R = 1.0  # Radius
    w = 0.5  # Width
    n = 100  # Resolution
    mobius = MobiusStrip(R, w, n)
    print(f"Surface Area: {mobius.surface_area:.4f}")
    print(f"Edge Length: {mobius.edge_length:.4f}")
    # Generate visualization
    mobius.plot_surface()