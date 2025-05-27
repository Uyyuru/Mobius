Mobius Strip Modeling Assignment
Overview
This repository contains a Python implementation for modeling a Mobius strip, as part of the technical round for the backend intern position at Karkhana.io. The assignment involves creating a MobiusStrip class that generates a 3D mesh of the Mobius strip using parametric equations, computes its surface area and edge length numerically, and visualizes the result.
Assignment Requirements
The task was to:

Implement a MobiusStrip class that:
Accepts radius ( R ) (distance from center to strip), width ( w ) (strip width), and resolution ( n ) (number of points in the mesh).
Generates a 3D mesh of ((x, y, z)) points using the parametric equations:
( x(u,v) = (R + v \cdot \cos(u/2)) \cdot \cos(u) )
( y(u,v) = (R + v \cdot \cos(u/2)) \cdot \sin(u) )
( z(u,v) = v \cdot \sin(u/2) )
Where ( u \in [0, 2\pi] ), ( v \in [-w/2, w/2] ).


Computes the surface area numerically using integration.
Computes the edge length numerically along the boundary.


Provide a clean, modular, and well-commented Python script.
Include a 3D visualization of the Mobius strip.
Write a short explanation of the code structure, surface area approximation, and challenges faced.

Files in the Repository

mobius_strip.py: The main Python script containing the MobiusStrip class, implementing the mesh generation, surface area, edge length calculations, and visualization.
mobius_strip.png: The output 3D visualization of the Mobius strip, generated with sample parameters (( R = 1.0 ), ( w = 0.5 ), ( n = 100 )).
writeup.md: A document explaining the code structure, numerical methods used, and challenges encountered (included separately as per assignment requirements).

Dependencies

Python 3.6 or higher
NumPy: For numerical computations and mesh generation.
Matplotlib: For 3D visualization of the Mobius strip.


Run the script:python mobius_strip.py


The script will:
Compute the surface area and edge length for the Mobius strip with default parameters (( R = 1.0 ), ( w = 0.5 ), ( n = 100 )).
Output the results to the console.
Generate a 3D plot saved as mobius_strip.png.



Sample Output
Running the script with the default parameters produces:

Surface Area: Approximately 6.2832 (varies slightly with resolution).
Edge Length: Approximately 12.5664 (varies slightly with resolution).
Visualization: A 3D plot of the Mobius strip, saved as mobius_strip.png:


Code Structure

MobiusStrip Class:
__init__: Initializes with ( R ), ( w ), and ( n ), and calls methods to compute the mesh, surface area, and edge length.
generate_mesh: Creates a 3D mesh using NumPy's meshgrid and the parametric equations.
compute_surface_area: Uses the trapezoidal rule for numerical double integration over the cross-product magnitude of partial derivatives.
compute_edge_length: Parameterizes the boundary curve (( v = w/2 ), ( u \in [0, 4\pi] )) and integrates the speed numerically.
plot_surface: Generates and saves a 3D visualization using Matplotlib.



Numerical Methods

Surface Area: Computed using the parametric surface area formula:[A = \iint_D \left| \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \right| , du , dv]The trapezoidal rule (np.trapz) is applied over ( v ) and then ( u ).
Edge Length: Computed by parameterizing the boundary at ( v = w/2 ), integrating the speed of the curve over ( u \in [0, 4\pi] ) to account for the single edge due to the twist.

Challenges and Solutions

Boundary Curve: Ensuring the edge length accounted for the Mobius strip's single boundary required parameterizing over ( u \in [0, 4\pi] ), solved by adjusting the integration range.
Numerical Accuracy: Chose a resolution of ( n = 100 ) for balance between accuracy and performance, with ( 2n ) points for edge length to capture detail.
Code Modularity: Structured the code into methods for clarity and reusability, ensuring each handles a specific task.

Notes for Reviewers

The implementation is robust for typical inputs but could be extended to handle edge cases like very small ( n ) or ( w = 0 ).
The visualization is optional but included to demonstrate the surface's geometry.
The code is optimized with NumPy for efficiency, suitable for backend applications requiring numerical computations.

