from gui_files.svg import *

DICE_CAPTION = "based on our true story :("


def draw_dice(num):
    width, height = 100, 100
    graphic = create_graphic(width, height)
    draw_rect(graphic, 0, 0, 100, 100, fill="white", stroke="black")
    "above is provided code"
    if num == 1:
        #background
        draw_rect(graphic, 0, 0, 100, 100, stroke="DarkOrange", fill="DarkOrange")
        #number 1
        draw_rect(graphic, 18,8,12,46,stroke = "Navy",fill = "Navy")
        draw_rect(graphic, 10,50,27,6,stroke = "Navy",fill = "Navy")
        draw_triangle(graphic, 18,8,8,20,18,20,stroke = "Navy",fill = "Navy")
        draw_rect(graphic, 18,8,12,46,stroke = "Navy",fill = "Navy")
        draw_rect(graphic, 10,54,27,6,stroke = "Navy",fill = "Navy")
        draw_triangle(graphic, 18,8,8,20,18,20,stroke = "Navy",fill = "Navy")
        #oski_body
        draw_triangle(graphic, 80,65,100,75,70,75, stroke = "goldenrod", fill = "goldenrod")
        draw_triangle(graphic, 80,65,70,70,70,75, stroke = "goldenrod", fill = "goldenrod")
        draw_triangle(graphic,60,65,50,70,70,70, stroke = "goldenrod", fill = "goldenrod")
        draw_triangle(graphic, 50,60,70,70,90,60, stroke = "goldenrod", fill = "goldenrod")
        draw_rect(graphic, 50,30,40,30,stroke = "goldenrod", fill = "goldenrod")
        draw_triangle(graphic, 50,30,45,50,50,60, stroke = "goldenrod", fill = "goldenrod")
        draw_triangle(graphic, 90,30,95,50,90,60, stroke = "goldenrod", fill = "goldenrod")
        #oski_ear
        draw_circle(graphic, 50, 32, 8.5, stroke = "goldenrod", fill ="goldenrod")
        draw_circle(graphic, 90, 32, 8.5, stroke="goldenrod", fill = "goldenrod")
        draw_circle(graphic, 50, 32, 4, stroke = "lightpink", fill = "lightpink")
        draw_circle(graphic, 90, 32, 4, stroke= "lightpink", fill = "lightpink")
        #oski_eyes,nose
        draw_circle(graphic, 60,45,2,stroke ="black", fill = "black")
        draw_circle(graphic, 80,45,2, stroke="black", fill = "black")
        draw_triangle(graphic,65,50,73,50,69,54, stroke = "SaddleBrown", fill = "SaddleBrown")
        #desk
        draw_rect(graphic, 0, 70, 100, 30, stroke="Moccasin", fill="Moccasin")
        #laptop
        draw_rect(graphic, 15,65,60,30,stroke = "Gainsboro",fill = "Gainsboro")        
        #text
        write_text(graphic,24,85,str("CS 61A"),stroke = "DimGray",fill = "DimGray", font_size="small")
        write_text(graphic,38,12,str("st Day"), stroke = "white",fill = "white", font_size="Small")
    if num ==2:
        draw_rect(graphic, 0, 0, 100, 100, fill="Gold", stroke="Gold")
        #left oski
        draw_rect(graphic,0,55,15,45,stroke="goldenrod",fill = "goldenrod")
        draw_rect(graphic,15,60,15,30,stroke="goldenrod",fill = "goldenrod")
        draw_rect(graphic,15,55,11,5,stroke="goldenrod",fill = "goldenrod")
        draw_triangle(graphic,26,55,26,60,30,60,stroke="goldenrod",fill = "goldenrod")#코
        ### mouth 
        draw_circle(graphic, 30, 80, 10, stroke="goldenrod", fill = "goldenrod")
        # glasses(parasite)
        draw_rect(graphic, 10, 62, 25, 5)
        #nose and eyes
        draw_circle(graphic, 37, 73, 2)

        #right oski
        draw_rect(graphic,85,55,15,45,stroke = "goldenrod",fill = "goldenrod")
        draw_rect(graphic,80,55,5,5,stroke = "goldenrod",fill = "goldenrod")
        draw_rect(graphic,75,60,10,30,stroke = "goldenrod",fill = "goldenrod")
        draw_rect(graphic,70,70,5,20,stroke = "goldenrod",fill = "goldenrod")
        draw_triangle(graphic,80,55,75,60,80,60,stroke = "goldenrod",fill = "goldenrod")
        draw_circle(graphic,100,55,10,stroke = "darkgoldenrod",fill = "darkgoldenrod")#ear
        # mouth and nose and glass(parasite)
        draw_circle(graphic, 70, 80, 10, stroke="goldenrod", fill="goldenrod")
        draw_circle(graphic, 63, 73, 2)
        draw_rect(graphic, 70, 62, 25, 5)
        #lambda
        draw_rect(graphic,45,30,30,20,stroke = "Indigo",fill = "Indigo")
        draw_triangle(graphic,40,40,45,55,62,55,stroke = "Gold",fill ="Gold")
        draw_triangle(graphic,30,20,76,20,76,50,stroke = "Gold", fill = "Gold")
        draw_circle(graphic,30,27,25,stroke = "Indigo", fill = "Indigo")
        draw_circle(graphic,30,27,13,stroke = "Gold", fill = "Gold")
        draw_rect(graphic,0,0,30,53,stroke = "Gold",fill = "Gold") 
        # left oski's ear
        draw_circle(graphic, 0, 55, 10, stroke="darkgoldenrod", fill="darkgoldenrod")
        #text
        write_text(graphic,28, 97,str("Learning"),stroke = "forestgreen",fill = "forestgreen",font_size="small")
        write_text(graphic, 58, 25, str("lambda"), stroke="green", fill="green", font_size="small")
    if num ==3 :
        #background
        draw_rect(graphic, 0, 0, 100, 100, stroke="DarkBlue", fill="DarkBlue")
        #oskibody
        draw_triangle(graphic,40,80,30,100,40,100, stroke = "Goldenrod",fill = "Goldenrod")
        draw_triangle(graphic,60,73,40,80,70,80,stroke = "Goldenrod",fill = "Goldenrod")
        draw_triangle(graphic,80,73,70,80,100,80, stroke = "Goldenrod",fill = "Goldenrod")
        draw_rect(graphic,40,80,60,20,stroke = "Goldenrod",fill = "Goldenrod")
        draw_triangle(graphic,50,70,90,70,70,80,stroke = "Goldenrod",fill = "Goldenrod")
        draw_triangle(graphic,50,40,45,60,50,70,stroke = "Goldenrod",fill = "Goldenrod")
        draw_triangle(graphic,90,40,95,60,90,70,stroke = "Goldenrod",fill = "Goldenrod")
        draw_rect(graphic,50,40,40,30,stroke = "Goldenrod",fill = "Goldenrod")
        # ear
        draw_circle(graphic, 50, 40, 10, stroke="DarkGoldenrod", fill="DarkGoldenrod")
        draw_circle(graphic, 90, 40, 10, stroke="DarkGoldenrod", fill="DarkGoldenrod")
        draw_circle(graphic,50,40,5,stroke = "lightpink",fill = "lightpink") 
        draw_circle(graphic,90,40,5,stroke = "lightpink",fill = "lightpink")        

        #face and eyes
        draw_circle(graphic, 82, 55, 2)
        draw_circle(graphic, 58, 55, 2)
        draw_triangle(graphic,67,60,75,60,71,64,stroke="SaddleBrown",fill = "SaddleBrown")#nose
        draw_circle(graphic, 84, 74, 1, stroke="CornflowerBlue", fill="CornflowerBlue")
        draw_circle(graphic, 57, 74, 1, stroke="CornflowerBlue", fill="CornflowerBlue")
        n = 0
        while n <= 2:
            draw_circle(graphic, 79+3*n, 58, 1, stroke="CornflowerBlue", fill="CornflowerBlue")
            draw_circle(graphic, 55 + 3*n ,58, 1, stroke="CornflowerBlue", fill="CornflowerBlue")
            draw_circle(graphic, 84, 62 + 4 * n, 1, stroke="CornflowerBlue", fill="CornflowerBlue")
            draw_circle(graphic, 57, 62 + 4 * n, 1, stroke="CornflowerBlue", fill="CornflowerBlue")
            n += 1

        #hand
        draw_rect(graphic, 40, 60, 10, 40, stroke="darkgoldenrod", fill = "darkgoldenrod")
        draw_circle(graphic, 45, 60, 5, stroke="darkgoldenrod", fill = "darkgoldenrod")
        draw_circle(graphic, 45, 60, 2.5, stroke="lightpink", fill="lightpink")

        draw_circle(graphic,12,23,18,stroke = "DarkOrange",fill = "DarkOrange") #upper three
        draw_circle(graphic,12,23,8,stroke="DarkBlue",fill="DarkBlue")
        draw_circle(graphic,12,49,18,stroke="DarkOrangeed",fill = "DarkOrange")#down three
        draw_circle(graphic,12,49,8,stroke="DarkBlue",fill="DarkBlue")
        #draw_rect(graphic,17,27,5,10,stroke="red",fill = "red")
        draw_rect(graphic,0,0,7,75,stroke="DarkBlue",fill = "DarkBlue")

        #texts
        write_text(graphic,65,13,str("Exam"), stroke = "white",fill = "white", font_size="small")
        write_text(graphic,33,17,str("0%"),stroke = "white",fill = "white", font_size="small")

        ####### wave of tears #########
        draw_rect(graphic,0,80,100,20,stroke = "DodgerBlue",fill = "DodgerBlue")
        n = 0
        while n<=97:
            draw_circle(graphic,6*n+3,80,4,stroke= "SteelBlue", fill = "SteelBlue")
            draw_circle(graphic,6*n+3,85,5,stroke= "RoyalBlue", fill = "RoyalBlue")
            draw_circle(graphic, 6*n+3, 90, 5, stroke= "CornflowerBlue", fill = "CornflowerBlue")
            draw_circle(graphic, 6*n+3, 95, 5, stroke ="LightSkyBlue", fill = "LightSkyBlue") 
            draw_circle(graphic, 6*n+3, 100, 5, stroke = "LightBlue", fill = "LightBlue")
            n+=1
    if num == 4:
        draw_rect(graphic, 0, 0, 100, 100, fill = "ForestGreen", stroke = "ForestGreen")
        # four
        draw_triangle(graphic, 40, 10, 25, 35, 40, 35, stroke = "darkred", fill = "darkred")
        draw_triangle(graphic, 40, 30, 40, 20, 45, 20, stroke = "darkred", fill = "darkred")
        draw_rect(graphic, 25, 35, 45, 10, stroke = "darkred", fill = "darkred")
        draw_rect(graphic, 40, 10, 25, 10, stroke = "darkred", fill = "darkred")
        draw_rect(graphic, 55, 20, 10, 35, stroke = "darkred", fill = "darkred")
        #bear
        draw_rect(graphic, 75, 65, 25, 35, stroke="goldenrod", fill="goldenrod")
        draw_rect(graphic, 70, 70, 5, 30, stroke="goldenrod", fill = "goldenrod")
        draw_triangle(graphic, 70, 70, 75, 70, 75, 65, stroke="goldenrod", fill = "goldenrod")
        #bear hand
        draw_rect(graphic, 60, 60, 10, 40, stroke="darkgoldenrod", fill = "darkgoldenrod")
        draw_circle(graphic, 65, 60, 5, stroke="darkgoldenrod", fill = "darkgoldenrod")
        draw_circle(graphic, 65, 60, 2.4, stroke = "lightpink", fill = "lightpink")
        #bear nose and eyes
        draw_circle(graphic, 70, 90, 10, stroke = "goldenrod", fill = "goldenrod")
        draw_circle(graphic, 62, 82, 2.5)
        draw_circle(graphic, 75, 75, 1)
        draw_circle(graphic, 97, 63, 10, stroke="darkgoldenrod", fill = "darkgoldenrod")
        #text
        draw_line(graphic, 50, 80, 30, 70, stroke="ghostwhite")
        draw_line(graphic, 50, 90, 30, 100, stroke = "ghostwhite")
        write_text(graphic, 15, 85, str(". . ."), stroke = "ghostwhite", fill = "ghostwhite")
        write_text(graphic, 5, 60, str("asking"), stroke = "ghostwhite", fill = "ghostwhite", font_size="small")
        write_text(graphic, 70, 30, str("help"), stroke="ghostwhite", fill="ghostwhite", font_size="small")
    if num == 5:
        #background
        draw_rect(graphic, 0, 0, 100, 100, stroke = "midnightblue", fill = "midnightblue")
        draw_rect(graphic, 10, 40, 90, 50, stroke = "DimGray", fill = "DimGray")
        #book
        draw_rect(graphic, 60, 55, 20, 25, fill = "lightgray")
        draw_rect(graphic, 40, 55, 20, 25, fill = "lightgray")
        #bear face
        draw_circle(graphic, 55, 100, 25, stroke = "goldenrod", fill = "goldenrod")
        draw_circle(graphic, 65, 83, 1.5)
        draw_circle(graphic, 45, 83, 1.5)
        draw_circle(graphic, 55, 72.5, 2.5)
        #bear hands
        draw_rect(graphic, 80, 70, 10, 30, stroke = "darkgoldenrod", fill = "darkgoldenrod")
        draw_rect(graphic, 20, 70, 10, 100, stroke = "darkgoldenrod", fill = "darkgoldenrod")
        draw_circle(graphic, 85, 70, 5, stroke = "darkgoldenrod", fill = "darkgoldenrod")
        draw_circle(graphic, 25, 70, 5, stroke = "darkgoldenrod", fill = "darkgoldenrod")
        #number
        draw_rect(graphic, 10, 10, 35, 10, stroke = "Gold", fill="Gold")
        draw_rect(graphic, 10, 20, 10, 20, stroke="Gold", fill = "Gold")
        draw_circle(graphic, 20, 60, 25, stroke = "Gold", fill = "Gold")
        draw_circle(graphic, 20, 60, 15, stroke = "DimGray", fill = "DimGray")
        draw_rect(graphic, 0, 40, 9, 50, stroke="DimGray", fill = "DimGray")
        draw_rect(graphic, 0, 30, 9, 9, stroke = "midnightblue", fill = "midnightblue")
        # text
        write_text(graphic, 50, 15, str("hrs of"), stroke = "ghostwhite", fill = "ghostwhite")
        write_text(graphic, 55, 35, str("sleep"), stroke = "ghostwhite", fill = "ghostwhite")

    if num == 6:
        #background
        draw_rect(graphic, 0, 0, 100, 100, stroke= "Indigo", fill = "Indigo",)
        #lambda (A+)
        draw_triangle(graphic, 80, 20, 70, 60, 90, 60, stroke = "LightYellow", fill = "LightYellow")
        draw_triangle(graphic, 80, 40, 75, 62, 85, 62, stroke = "Indigo", fill = "Indigo")
        draw_triangle(graphic, 80, 20, 75, 20, 77.5, 30, stroke = "LightYellow", fill = "LightYellow") 
        draw_line(graphic, 85, 10, 85, 20, stroke="LightYellow")
        draw_line(graphic, 85.5, 10, 85.5, 20, stroke="lightyellow")
        draw_line(graphic, 80, 15, 90, 15, stroke="LightYellow") 
        draw_line(graphic, 80, 15.5, 90, 15.5, stroke="lightyellow")    
        # Final
        draw_rect(graphic, 10, 10, 45, 15, stroke = "gold", fill="gold")
        write_text(graphic, 38, 95, str("Final"), stroke="lightyellow", fill="lightyellow", font_size="small")
        # bear's face
        draw_rect(graphic, 20, 40, 25, 40, stroke = "gold", fill = "gold")
        draw_triangle(graphic, 45, 40, 40, 45, 55, 45, stroke="gold", fill = "gold")
        draw_rect(graphic, 45, 45, 10, 35, stroke="gold", fill = "gold")
        draw_rect(graphic, 50, 55, 5, 25, stroke="gold", fill = "gold")
        draw_circle(graphic, 49, 67.5, 12.5, stroke="gold", fill="gold")
        ## bear's nose and eyes
        draw_circle(graphic, 61, 61, 2.5)
        draw_line(graphic, 45, 50, 50, 55)
        draw_line(graphic, 45.5, 50, 50.3, 55)
        draw_line(graphic, 45, 50, 40, 55)
        draw_line(graphic, 45.5, 50, 40.3, 55)
        #bear's hand and ear
        draw_circle(graphic, 15, 20, 5, stroke = "goldenrod", fill="goldenrod")
        draw_circle(graphic, 20, 40, 10, stroke="darkgoldenrod", fill = "darkgoldenrod")
        draw_rect(graphic, 10, 20, 10, 60, stroke = "goldenrod", fill = "goldenrod")
        draw_circle(graphic, 15, 23, 3, stroke = "mistyrose", fill = "mistyrose")
        draw_rect(graphic, 9, 79.5, 50, 0.7, stroke="indigo", fill="indigo")




        
    return graphic
