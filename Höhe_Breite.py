y=int(0)#höhe
x=int(0)#breite
bytes=int(0)#> 3byte pro pixel (rgb)
Anzhal =int (0) #bilder Anzhal
Speicherbedarf = int(0)
#1Gib = 1.073.741.824 Bytes
#1Mib = 1 048 576 bytes

#Begrussunmg des Programmes
print("hallo this program is  to calculate  the size of the foto" )
#speicherbedarf pro pixel  in byte
print("For RGB we use 3 bytes per pixel or 24 bits per pixel ")
bytes=int(input("Enter how many bytes are gonna be used for one pixel: "))
y=int(input("Enter  pixel:"))
x=int(input("Enter  pixel:"))
Anzhal=int(input("the number of fotos:"))
#umrechnen
# total bytes
size_bytes = x * y * bytes * Anzhal

# convert to MiB
size_mib = size_bytes / 1048576

if size_mib < 1024:
    print(f"The required storage space is: {size_mib:.2f} MiB")
else:
    size_gib = size_mib / 1024
    print(f"The required storage space is: {size_gib:.2f} GiB")
