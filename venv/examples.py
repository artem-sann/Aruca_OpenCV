import cv2
import cv2 as cv
import cv2.aruco as aruco
import math

cap = cv.VideoCapture(0)

def get_lenth(ppt1, ppt2):
    x = int((ppt1[0] + ppt2[0]) / 2)
    y =int((ppt1[1] + ppt2[1]) / 2)

    return math.sqrt(x**2 + y**2)



flag = 1
while (True):
    ids = []
    ids1 = []
    corners1 = [[]]
    ret, frame = cap.read()

    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    corners, ids, rejection = aruco.detectMarkers(gray_frame,
                                                  dictionary=aruco.getPredefinedDictionary(aruco.DICT_7X7_1000))

    print(ids)
    if flag == 0:
        if ids != None:
            flag = 1
            if ids.size > 0:
                flag = 1

    aruco.drawDetectedMarkers(frame, corners, ids, (255, 255, 0))

    '''
    fnd = [243]


    print(flag)
    if flag == 1:
        ids1[0] = ids[0]
        corners1[0] = corners[0]
        aruco.drawDetectedMarkers(frame, corners1, ids1, (255, 0, 255))

    
    if flag == 1:
        for i in range(len(ids)):
            print(len(ids))
            if ids[i-1] == fnd:
                ids1[1] = ids[1]
                corners1[1] = corners[1]
                aruco.drawDetectedMarkers(frame, corners1, ids1, (255, 0, 255))

    #ids = None
    '''



    # cv.line(frame, (0, 0), (50, 50), (255, 255, 0), 5)
    indexes = []
    if ids is not None:

        for num, i in enumerate(ids):
            if i == 243:
                indexes.append(num)
            if i == 25:
                indexes.append(num)



    if len(indexes) == 1:
        ppt1_x = int((corners[indexes[0]][0][0][0] + corners[indexes[0]][0][2][0])/2)
        ppt1_y = int((corners[indexes[0]][0][0][1] + corners[indexes[0]][0][2][1])/2)

        kat1 = int(abs((corners[indexes[0]][0][0][0] - corners[indexes[0]][0][2][0])))
        kat2 = int(abs((corners[indexes[0]][0][0][1] - corners[indexes[0]][0][2][1])))

        diametr = (kat1**2 + kat2**2)**0.5


        #ppt2_x = int((corners[indexes[1]][0][0][0] + corners[indexes[1]][0][2][0]) / 2)
        #ppt2_y = int((corners[indexes[1]][0][0][1] + corners[indexes[1]][0][2][1]) / 2)

        #a = get_lenth((corners[indexes[0]][0][0][0], corners[indexes[0]][0][0][1]), (corners[indexes[0]][0][1][0], corners[indexes[0]][0][1][1]))
        #cv.line(frame, (int(corners[indexes[0]][0][0][0]), int(corners[indexes[0]][0][0][1])),
                #(int(corners[indexes[0]][0][1][0]), int(corners[indexes[0]][0][1][1])), (255, 0, 255), 5)
        #per_pixel = 30/a
        #b = get_lenth((ppt1_x, ppt1_y), (ppt2_x, ppt2_y))
        #print(b*per_pixel)

        #cv.line(frame, (ppt1_x, ppt1_y), (ppt1_x+5, ppt1_y+5), (255, 255, 0), 5)
        center_coordinates = (ppt1_x, ppt1_y)
        print(int(diametr))
        cv2.circle(frame, center_coordinates, int(diametr/2), (255, 0, 255), 4)




    '''
    for i in corners:
        cv2.line(frame, (int(i[0][0][0]), int(i[0][0][1])), (int(i[0][2][0]), int(i[0][2][1])), (155, 255, 0), 2)
        cv2.line(frame, (int(i[0][1][0]), int(i[0][1][1])), (int(i[0][3][0]), int(i[0][3][1])), (155, 255, 0), 2)
     '''


    cv.imshow('frame', frame)


    if cv.waitKey(1) & 0xFF == ord('q'):
        break

