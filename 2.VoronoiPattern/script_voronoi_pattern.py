# Author: Finny Varghese
# Voronoi Pattern Generator with Closed Loops for Extrusion

import adsk.core, adsk.fusion, adsk.cam, traceback, random, math

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

        # Parameters
        num_points = 10
        width = 10
        height = 10
        grid_resolution = 0.5

        # Generate random seed points
        seed_points = []
        for _ in range(num_points):
            x = random.uniform(0, width)
            y = random.uniform(0, height)
            seed_points.append((x, y))

        # Create a grid of points
        x_steps = int(width / grid_resolution)
        y_steps = int(height / grid_resolution)
        grid_points = []
        for i in range(x_steps + 1):
            for j in range(y_steps + 1):
                x = i * grid_resolution
                y = j * grid_resolution
                grid_points.append((x, y))

        # Assign each grid point to the nearest seed point
        region_map = {}
        for gp in grid_points:
            min_dist = float('inf')
            closest_index = -1
            for idx, sp in enumerate(seed_points):
                dist = math.hypot(gp[0] - sp[0], gp[1] - sp[1])
                if dist < min_dist:
                    min_dist = dist
                    closest_index = idx
            region_map[gp] = closest_index

        # Group grid points by region
        region_points = {}
        for pt, region in region_map.items():
            if region not in region_points:
                region_points[region] = []
            region_points[region].append(pt)

        # Draw closed loops for each region
        for region, pts in region_points.items():
            center = seed_points[region]
            pts.sort(key=lambda p: math.atan2(p[1] - center[1], p[0] - center[0]))
            for i in range(len(pts)):
                p1 = pts[i]
                p2 = pts[(i + 1) % len(pts)]
                sketch.sketchCurves.sketchLines.addByTwoPoints(
                    adsk.core.Point3D.create(p1[0], p1[1], 0),
                    adsk.core.Point3D.create(p2[0], p2[1], 0)
                )

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
