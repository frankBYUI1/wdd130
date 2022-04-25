import math
CAN_NAME_INDEX = 0
CAN_RADIUS_INDEX = 1 
CAN_HEIGHT_INDEX = 2 

def main():

    can1 = ["#1 Picnic", 6.83, 10.16, 0.28]
    can2 = ["#2 Tall", 7.78, 11.91, 0.43]

    cans_list = [can1, can2]
    for can in cans_list:
        volume = compute_volume(can[CAN_RADIUS_INDEX], can[CAN_HEIGHT_INDEX])
        surf_area = compute_surface_area(can1[CAN_RADIUS_INDEX], can[CAN_HEIGHT_INDEX])
        storage_effiency = volume / surf_area
        print(f"{can1[CAN_NAME_INDEX]} {storage_effiency:.1f}")
    
def compute_volume(radius, height):
    """Compute and return the volume of a cylinder.
 
    Parameters
    radius: the radius of the cylinder
    height: the height of the cylinder
    Return: the volume of the cylinder
    """
    volume = math.pi * radius**2 * height
    return volume
 
def compute_surface_area(radius, height):
    """Compute and return the surface area of a cylinder.
 
    Parameters
    radius: the radius of the cylinder
    height: the height of the cylinder
    Return: the surface area of the cylinder
    """
    surf_area = 2 * math.pi * radius * (radius + height)
    return surf_area
 
    # Start this program by
    # calling the main function.

main()
    
    
    #name = can1(0)
    #radius = 6.83


