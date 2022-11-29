import hou
import viewerstate.utils as vu

class Selector(object):
    
    def __init__(self, parent, scene_viewer : hou.SceneViewer, geometry : hou.Geometry, geometry_type : hou.geometryType):
        self._parent = parent
        self._scene_viewer = scene_viewer
        self._geo = geometry
        self._geo_type = geometry_type

        self.selection = []
        self._hover = -1
        self._intersector = vu.GeometryIntersector(geometry, scene_viewer)
        self._drawable = hou.GeometryDrawable(scene_viewer, hou.drawableGeometryType.Face, "selection", params = {'color1' : (1,1,0,0.8), 'use_cd' : False})
        self._drawable.show(True)
        
        self._hover_drawable = hou.GeometryDrawable(scene_viewer, hou.drawableGeometryType.Face, "hover", params = {'color1' : (0.8,0.8,0,0.2), 'use_cd' : False})
        self._hover_drawable.show(True)

    
    def setGeometry(self, geometry: hou.Geometry):
        self._geo = geometry
        self._drawable.setGeometry(geometry)
        self._hover_drawable.setGeometry(geometry)
        
    def clear(self):
        self.selection = []
        
    def onMouseEvent(self, kwargs):
        ui_event = kwargs["ui_event"]
        device = ui_event.device()
        reason = ui_event.reason()
        origin, direction = ui_event.ray()
        
        hit, pos, norm, uvw = vu.sopGeometryIntersection(
                self._geo, origin, direction
            )
        self._hover = hit

        if hit != -1:
            if device.isLeftButton():
                if device.isShiftKey():
                    if reason in [hou.uiEventReason.Picked]:
                        
                        if hit not in self.selection:
                            self.selection.append(hit)
                        elif hit in self.selection:
                            self.selection.remove(hit)
                else:
                    if reason in [hou.uiEventReason.Picked]:
                        if hit not in self.selection:
                            self.selection = [hit]
                        elif hit in self.selection:
                            self.selection = []
        else:
            if device.isLeftButton():
                if not device.isShiftKey():
                    if reason in [hou.uiEventReason.Picked]:
                        self.selection = []
                    
                        
    def onDraw(self, kwargs):
        handle = kwargs['draw_handle']
        params = {
            "highlight_mode":hou.drawableHighlightMode.GlowMinusMatte,
            "glow_width":5,
            "color2":(1,1,0,1)
        }
        
        hover_params = {
            "indices" : [self._hover],
            "highlight_mode":hou.drawableHighlightMode.Matte,
            "glow_width":5,
            "color2":(1,1,0,1)
        }
        
        verbs = hou.sopNodeTypeCategory().nodeVerbs()
        blast_verb = verbs["blast"]
        blast_verb.setParms({
            "group":" ".join([str(sel) for sel in self.selection]),
            "negate":1
        })
        
        draw_geo = hou.Geometry()
        blast_verb.execute(draw_geo, [self._geo])
        
        self._drawable.setGeometry(draw_geo)
        self._drawable.show(bool(self.selection))
        
        if self._hover != -1:
            self._hover_drawable.draw(handle, hover_params)
            
        self._drawable.draw(handle, params)