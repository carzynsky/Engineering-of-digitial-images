import bpy

def main(context):
    bpy.ops.mesh.primitive_monkey_add(location=(0, 0, 0))
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subdivision"].render_levels = 3
    bpy.context.object.modifiers["Subdivision"].levels = 3
    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, location=(0, 0, 0))
    bpy.ops.transform.resize(value=(19.7042, 19.7042, 19.7042), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.transform.translate(value=(0, 0, 1.85701), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)

        
class CustomMonkey(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "myops.add_costummonkey"
    bl_label = "Custom Monkey"
    
    def execute(self, context):
        main(context)
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(CustomMonkey)
    
def unregister():
    bpy.utils.unregister_class(CustomMonkey)
    
if __name__ == "__main__":
    register()
    # test call
    bpy.ops.myops.add_costummonkey()
   