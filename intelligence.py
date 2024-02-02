# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
import matplotlib.pyplot as plt
import numpy as np


def find_red_pixels(map_filename, upper_threshold=100, lower_threshold=50):
    """function that read a city map image , specified by the filename,
    map filename (e.g., ='map.png'), find all the red pixels from the image, and output a binary
    image file as map-red-pixels.jpg"""
    rgb_img = plt.imread('data\\'+ map_filename)
    rgb_img = rgb_img * 255
    #double for loop
    for i in rgb_img:
        for j in i:
            r,g,b = j[0], j[1], j[2]
            if r > upper_threshold and g < lower_threshold and b < lower_threshold:
                j[0]= 255
                j[1] = 255
                j[2] = 255
            else:
                j[0] = 0
                j[1] = 0
                j[2] = 0
    
    #read and save image           
    plt.imshow(rgb_img/255)
    plt.show()
    plt.imsave('map-red-pixels.jpg', rgb_img/255)

#find_red_pixels('map.png')

def find_cyan_pixels(map_filename, upper_threshold=100, lower_threshold=50):
    """ funcion that read a city map image, specified by the filename, map filename (e.g., ='map.png'), 
    find all the cyan pixels from the image, and output a binary image file as map-cyan-pixels.jpg. 
    """
    rgb_img = plt.imread('data\\'+ map_filename)
    rgb_img = rgb_img * 255
    #double for loop
    for i in rgb_img:
        for j in i:
            r,g,b = j[0], j[1], j[2]
            if r < lower_threshold and g > upper_threshold and b > upper_threshold:
                j[0]= 255
                j[1] = 255
                j[2] = 255
            else:
                j[0] = 0
                j[1] = 0
                j[2] = 0
    
    #read and save image          
    plt.imshow(rgb_img/255)
    plt.show()
    plt.imsave('map-cyan-pixels.jpg', rgb_img/255)

#find_cyan_pixels('map.png')


binary_image = 'map-red-pixels.jpg'

def detect_connected_components(img):
    """
    reads a binary IMG returned from the first task, returns a 2D
    array in numpy MARK and writes the number of pixels inside each connected component region into a text file cc-output-2a.txt
    """
    #reads the binary image
    image = plt.imread(img)
    image = image/255
    
    Q = np.array([[0,0]])
    components = []
    height = len(image)
    width = len(image[0])
    #create mark the size of the image filled with zeros
    mark = [[0 for _ in range(width)] for _ in range(height)]
    #delete first line of created array 
    Q = np.delete(Q,0,axis=0)
    #double for loop
    for y in range(height):
        for x in range(width):
            #define r,g,b as image pixel color 
            r,g,b, = image[y][x][0], image[y][x][1], image[y][x][2]
            #if pixel is unvisited and pavement pixel 
            if mark[y][x] == 0 and r +g+ b >= 1:
                component = []
                mark[y][x] = 1
                arr = np.array([[y,x]])
                #add pavement pixel to Q array
                Q = np.concatenate([Q,arr])
                #while there are still neighboour pixels to check 
                while Q.size != 0 :
                    m = Q[0][0]
                    n = Q[0][1]
                    Q = np.delete(Q,0,axis=0)
                    component.append((m,n))
                    neighbour = [(m-1,n-1),(m-1,n),(m-1,n+1),(m,n-1),(m,n+1),(m+1,n-1),(m+1,n),(m+1,n+1)]
                    for s,t in neighbour:
                        #checks if pixel is not at the border
                        if 0 <= s < height and 0 <= t < width:
                            #checks if neighbour pixel is pavement as well
                            if (image[int(s)][int(t)][0] + image[int(s)][int(t)][1] + image[int(s)][int(t)][2]) >= 1 and mark[s][t] == 0:
                                mark[s][t] = 1
                                arr2 = np.array([[s,t]])
                                Q = np.concatenate([Q,arr2])
                #make a 2d list of components
                components.append(component)
    
    mark_array = np.array(mark,np.uint8)
    #writes the data in a txt file 
    result_ls = []
    file = open('cc-output-2a.txt','w')
    for i in range(len(components)):
        result_ls.append(len(components[i]))
        file.write(str(i+1)+','+str(result_ls[i])+'\n')
    
    #gets the two bigest conected component
    base = len(components[0])
    for compn1 in range(1,len(components)):
        if len(components[compn1]) >= base:
            base = len(components[compn1])
            val1 = components[compn1]
    components.remove(val1)

    base = len(components[0])
    for compn2 in range(1,len(components)):
        if len(components[compn2]) >= base:
            base = len(components[compn2])
            val2 = components[compn2]
    
    return mark_array,val1,val2
    
    
#print(detect_connected_components(binary_image))

def detect_connected_components_sorted(mark):
    """
    fonction a changer pour faire en foncton de mark !!!!
    """
    #get data from detect_connected_components
    marker,c1,c2 = mark

    stocking = {}
    intermidiate = {}
    sorted_dict = {}
    height = len(marker)
    width = len(marker[0])
    stocking_array = np.zeros((height, width, 3), dtype=np.uint8)
    
    #checks the two bigest components 
    for x in c1:
        if marker[x[0]][x[1]] == 1:
            stocking_array[x[0]][x[1]] = [255,255,255]
    for y in c2:
        if marker[y[0]][y[1]] == 1:
            stocking_array[y[0]][y[1]] = [255,255,255]
    
    #reads the txt file with required info 
    with open('cc-output-2a.txt') as file:
        value_ls = file.read()
        value_ls = value_ls[:-1]
        embeded_ls = value_ls.split('\n')
        for index in range(len(embeded_ls)):
            component, pixel = embeded_ls[index].split(",")
            component = int(component)
            stocking[component] = int(pixel)
        #double sort to make sure the last component 
        #is the lowest in values of pixel and in conected componet id 
        while len(stocking) > 0:
            maxi = max(stocking.keys())
            intermidiate[maxi] = stocking[maxi]
            stocking.pop(maxi)
        while len(intermidiate) > 0:
            maximum = max(intermidiate,key=intermidiate.get)
            sorted_dict[maximum] = intermidiate[maximum]
            intermidiate.pop(maximum)

    #writes a txt file with asked format and sorted conected components
    file = open('cc-output-2b.txt','w')
    for i in sorted_dict:
        file.write('Conected Component ' + str(i) + ', number of pixels = ' + str(sorted_dict[i]) + '\n')
    file.write('Total number of connected components = ' + str(len(sorted_dict)))

    #save newly generated image 
    plt.imshow(stocking_array/255)
    plt.imsave('cc-top-2.jpg', stocking_array/255)


#detect_connected_components_sorted(detect_connected_components(binary_image))