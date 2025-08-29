# Developed by Finny Varghese
# Waveform Surface Generator with Smooth Splines

import adsk.core, adsk.fusion, adsk.cam, traceback, math

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)

        # Parameters for the waveform
        amplitude = 1.0      # Height of the wave
        frequency = 2.0      # Number of waves per unit length
        width = 10.0         # Width of the grid
        height = 10.0        # Height of the grid
        resolution = 1.0     # Distance between grid points

        # Create grid of points with sinusoidal Z values
        points = []
        x_steps = int(width / resolution)
        y_steps = int(height / resolution)

        for i in range(x_steps + 1):
            row = []
            x = i * resolution
            for j in range(y_steps + 1):
                y = j * resolution
                z = amplitude * math.sin(frequency * x)
                row.append(adsk.core.Point3D.create(x, y, z))
            points.append(row)

        # Create smooth fitted splines for each row
        for row in points:
            spline_points = adsk.core.ObjectCollection.create()
            for pt in row:
                spline_points.add(pt)
            sketch.sketchCurves.sketchFittedSplines.add(spline_points)

        # Create smooth fitted splines for each column
        for col in range(len(points[0])):
            spline_points = adsk.core.ObjectCollection.create()
            for row in range(len(points)):
                spline_points.add(points[row][col])
            sketch.sketchCurves.sketchFittedSplines.add(spline_points)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
