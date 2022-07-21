""" Utility functions for use in the AriHou Houdini Package. """

from typing import Union

from numpy import append
import hou

def menu_from_geo(geo: hou.Geometry, geo_types: tuple) -> list:
    """Generates a group menu style list from input geometry types.

    Args:
        geo (hou.Geometry): The geometry to look for the groups in.
        geo_types (tuple, optional): The geometry types to generate the group list from. Defaults to (hou.geometryType.Primitives).

    Returns:
        list: A Menu style list.
    """
    def _add_grp_names(groups: list, menu: list):
        grps = [grp.name() for grp in groups]
        for grp in grps:
            menu.append(grp)
            menu.append(grp)
        if grps:
            menu.append("_separator_")
            menu.append("_separator_")

    menu = []
    if hou.geometryType.Points in geo_types:
        _add_grp_names(geo.pointGroups(), menu)
    
    if hou.geometryType.Primitives in geo_types:
        _add_grp_names(geo.primGroups(), menu)

    if hou.geometryType.Edges in geo_types:
        _add_grp_names(geo.edgeGroups(), menu)
        
    if hou.geometryType.Vertices in geo_types:
        _add_grp_names(geo.vertexGroups(), menu)

    return menu

def menu_from_attrib(geo: hou.Geometry, geo_type: hou.geometryType, attrib_name: str) -> list:
    """Generates a Houdini menu style list from all unique Attribute values of an Attribute.

    Args:
        geo (hou.Geometry): The geometry to look for the attribute in.
        geo_type (hou.geometryType): Geometry type to look for the Attribute in.
        attrib_name (str): Name of the Attribute.

    Returns:
        list: Menu style list with double entries for token and label.
    """
    menu = []
    if geo_type == hou.geometryType.Points:
        for val in geo.pointStringAttribValues(attrib_name):
            menu.append(val)
            menu.append(val)
    if geo_type == hou.geometryType.Primitives:
        for val in geo.primStringAttribValues(attrib_name):
            menu.append(val)
            menu.append(val)
    if geo_type == hou.geometryType.Vertices:
        for val in geo.vertexStringAttribValues(attrib_name):
            menu.append(val)
            menu.append(val)
         
    return menu


def menu_from_attrib_type(geo: hou.Geometry, geo_types: Union[hou.attribType, list, tuple]):
    """Generates a Houdini menu style list from all attributes in all geometry types provided.

    Args:
        geo (hou.Geometry): The geometry to look for the Attributes on.
        geo_types (Union[hou.geometryType, list, tuple]): Either a single geometry type or a list or tuple of multiple.
    """
    menu = []
    if isinstance(geo_types, hou.EnumValue):
        geo_types = [geo_types]
        
    def _append_attrib_type(attribs : list, add_sep: bool = True):
        for attrib in attribs:
            menu.append(attrib.name())
            menu.append(attrib.name())
        if add_sep:
            menu.append("_separator_")
            menu.append("_separator_")
    
    if hou.attribType.Point in geo_types:
        _append_attrib_type(geo.pointAttribs(), geo_types[-1]!=hou.attribType.Point)
        
    if hou.attribType.Prim in geo_types:
        _append_attrib_type(geo.primAttribs(), geo_types[-1]!=hou.attribType.Prim)
        
    if hou.attribType.Vertex in geo_types:
        _append_attrib_type(geo.vertexAttribs(), geo_types[-1]!=hou.attribType.Vertex)
        
    if hou.attribType.Global in geo_types:
        _append_attrib_type(geo.globalAttribs(), geo_types[-1]!=hou.attribType.Global)
        
    return menu
        
        
    
    