# Pymol script to render Proflex output files
# Sebastian Raschka
# 03/10/2013

remove ////XXX
create SEL, all
hide lines, all
disable
select LIG, hetatm
show cartoon, SEL
show sticks, LIG
enable SEL
deselect

cmd.color('s170', 'SEL and b< 40.0')
cmd.color('s170', 'SEL and b= 40.0')
cmd.color('s185', 'SEL and b> 40.0 and b< 41.0')
cmd.color('s185', 'SEL and b= 41.0')
cmd.color('s200', 'SEL and b> 41.0 and b< 42.0')
cmd.color('s200', 'SEL and b= 42.0')
cmd.color('s217', 'SEL and b> 42.0 and b < 43.0') 
cmd.color('s217', 'SEL and b= 43.0')
cmd.color('s225', 'SEL and b> 43.0 and b < 44.0') 
cmd.color('s225', 'SEL and b= 44.0')
cmd.color('s237', 'SEL and b> 44.0 and b < 45.0') 
cmd.color('s237', 'SEL and b= 45.0')
cmd.color('s250', 'SEL and b> 45.0 and b < 46.0') 
cmd.color('s250', 'SEL and b= 46.0')
cmd.color('s265', 'SEL and b> 46.0 and b < 47.0') 
cmd.color('s265', 'SEL and b= 47.0')
cmd.color('s280', 'SEL and b> 47.0 and b < 48.0') 
cmd.color('s280', 'SEL and b= 48.0')
cmd.color('s310', 'SEL and b> 48.0 and b < 49.0') 
cmd.color('s310', 'SEL and b= 49.0')
cmd.color('grey', 'SEL and b> 49.0 and b < 50.0') 
cmd.color('grey', 'SEL and b= 50.0')
cmd.color('s670', 'SEL and b> 50.0 and b < 51.0') 
cmd.color('s670', 'SEL and b= 51.0')
cmd.color('s690', 'SEL and b> 51.0 and b < 52.0') 
cmd.color('s690', 'SEL and b= 52.0')
cmd.color('s710', 'SEL and b> 52.0 and b < 53.0') 
cmd.color('s710', 'SEL and b= 53.0')
cmd.color('s730', 'SEL and b> 53.0 and b < 54.0') 
cmd.color('s730', 'SEL and b= 54.0')
cmd.color('s745', 'SEL and b> 54.0 and b < 55.0') 
cmd.color('s745', 'SEL and b= 55.0')
cmd.color('s760', 'SEL and b> 55.0 and b < 56.0') 
cmd.color('s760', 'SEL and b= 56.0')
cmd.color('s775', 'SEL and b> 56.0 and b < 57.0') 
cmd.color('s757', 'SEL and b= 57.0')
cmd.color('s790', 'SEL and b> 57.0 and b < 58.0') 
cmd.color('s790', 'SEL and b= 58.0')
cmd.color('s805', 'SEL and b> 58.0 and b < 59.0') 
cmd.color('s805', 'SEL and b= 59.0')
cmd.color('s820', 'SEL and b> 59.0 and b < 60.0')
cmd.color('s820', 'SEL and b= 60.0')
cmd.color('s850', 'SEL and b > 60.0')
