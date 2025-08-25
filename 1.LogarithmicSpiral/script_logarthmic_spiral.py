# Developed by Finny Varghese
# Description: This script creates a 2D spiral curve in Fusion 360 using an exponential function.

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
        points = adsk.core.ObjectCollection.create()

        # Spiral parameters
        a = 0.5  # scaling factor
        b = 0.2  # growth rate
        startAngle = 0
        endAngle = 4 * math.pi
        numPoints = 100

        i = 0
        while i <= numPoints:
            theta = startAngle + ((endAngle - startAngle) / numPoints) * i
            r = a * math.exp(b * theta)
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            z = 0  # 2D spiral

            points.add(adsk.core.Point3D.create(x, y, z))
            i += 1

        sketch.sketchCurves.sketchFittedSplines.add(points)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
