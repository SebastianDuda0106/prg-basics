###
# A program to calculate the volume and surface area of ​​a cube.
# 
cuboid_side_a = int(input('Enter cube side a: '))
cuboid_side_b = int(input('Enter cube side b: '))
cuboid_side_c = int(input('Enter cube side c: '))
cuboid_volume = cuboid_side_a*cuboid_side_b*cuboid_side_c
cuboid_surface_area = (cuboid_side_a*cuboid_side_b*2)+(cuboid_side_b*cuboid_side_c*2)+(cuboid_side_a*cuboid_side_c*2)
print(f'The volume of a cuboid with sides: \n a:{cuboid_side_a}\n b:{cuboid_side_b}\n c:{cuboid_side_c}\n is {cuboid_volume}')
print(f'The surface area of this cuboid is {cuboid_surface_area}')
