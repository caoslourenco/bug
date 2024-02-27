# Logotipo 3D inspirado em Ada Lovelace e computação
import bpy

# Limpar cena atual
bpy.ops.wm.read_factory_settings(use_empty=True)

# Criar um cubo
bpy.ops.mesh.primitive_cube_add(size=2)

# Redimensionar o cubo
bpy.ops.transform.resize(value=(1.5, 1.5, 1.5))

# Adicionar texto
bpy.ops.object.text_add(enter_editmode=True, align='WORLD', location=(0, 0, 2))
bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
bpy.ops.font.text_insert(text="Ada")
bpy.ops.object.editmode_toggle()

# Extrudar o texto
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.extrude_context_move(TRANSFORM_OT_translate={"value":(0, 0, 1)})
bpy.ops.object.mode_set(mode='OBJECT')

# Criar um cilindro
bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.5, depth=2, location=(0, 0, 1))

# Rotacionar o cilindro
bpy.ops.transform.rotate(value=0.3, orient_axis='Z')

# Adicionar material
material = bpy.data.materials.new(name="Computador")
material.diffuse_color = (0.2, 0.4, 0.8, 1)
bpy.context.object.data.materials.append(material)

# Renderizar
bpy.ops.render.render(write_still=True)
