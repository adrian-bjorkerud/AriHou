import hou

def uv_rectangle(min : hou.Vector2 = hou.Vector2(0.0, 0.0), max : hou.Vector2 = hou.Vector2(1.0, 1.0)) -> hou.Geometry:
    """ Creates and returns a rectangle hou.Geometry Object. """
    geo = hou.Geometry()
    grid_verb = hou.sopNodeTypeCategory().nodeVerb("grid")

    size = max - min
    diag_vec = hou.Vector2(min - max)
    orig = diag_vec * 0.5
    grid_verb.setParms({
    "orient": 0,
    "t": hou.Vector3(orig.x(), orig.y(), 0.0),
    "size": size,
    "rows": 2,
    "cols": 2,
    })

    grid_verb.execute(geo, [])

    return geo