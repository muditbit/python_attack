
def Hanoi(disks, source, destination,middle):
    
    if disks>0:
        Hanoi(disks-1, source, middle, destination)
        print('Move disk',disks,'from',source,'->',destination)
        Hanoi(disks-1, middle, destination, source)
n = int(input('Enter the no of disks :  '))

print('A is Source Pole')
print('C being the Destination Pole')
print('B is Auxillairy Pole')

print('Assume the top most disk be 1')

print('For',n,'disks the solution would be\n')

Hanoi(n,'A','C','B')
