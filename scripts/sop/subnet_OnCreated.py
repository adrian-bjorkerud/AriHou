import hou
node = kwargs["node"]

size = hou.Vector2(2.5, 1.5)
color = hou.Color(1.0, 1.0, 1.0)

input_note = node.createStickyNote("input_note")
input_note.setText("Expected Input : ")
input_note.setSize(size)
input_note.setPosition(hou.Vector2(-0.75, 6.5))
input_note.setColor(color)

output_note = node.createStickyNote("output_note")
output_note.setText("Expected Output : ")
output_note.setSize(size)
output_note.setPosition(hou.Vector2(-0.75, 1.75))
output_note.setColor(color)