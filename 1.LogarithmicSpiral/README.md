
## Logarithmic Spiral Equation in Fusion 360 Script

This Fusion 360 script generates a logarithmic spiral using parametric equations derived from its polar form.

### Mathematical Form

The logarithmic spiral is defined in polar coordinates as:

    r(θ) = a * e^(bθ)

Where:
- `r` is the radial distance from the origin,
- `θ` is the angle in radians,
- `a` is a positive scaling factor,
- `b` is the growth rate constant.

### Cartesian Conversion

To plot the spiral in Fusion 360, which uses Cartesian coordinates, the polar equation is converted as follows:

    x = r * cos(θ) = a * e^(bθ) * cos(θ)
    y = r * sin(θ) = a * e^(bθ) * sin(θ)
    z = 0 (for a 2D spiral on the XY plane)

### Implementation in the Script

The script evaluates the spiral over a range of angles from `startAngle` to `endAngle`, using a specified number of points (`numPoints`). For each angle `θ`, it computes the corresponding `(x, y, z)` coordinates and adds them to a sketch in Fusion 360.

Key parameters used:
- `a = 0.5` (scaling factor)
- `b = 0.2` (growth rate)
- `startAngle = 0`
- `endAngle = 4π`
- `numPoints = 100`

These points are then connected using a fitted spline to visualize the spiral.

