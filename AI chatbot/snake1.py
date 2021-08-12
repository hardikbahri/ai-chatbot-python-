import mysql.connector
def snake():
    print('''

                                                  ______
                                             .M
                                     .:AMMO:
                            .:AMMMMMHIIIHMMM.
                 ....   .AMMMMMMMMMMMHHHMHHMMMML:AMF"
                 .:MMMMMLAMMMMMMMHMMMMMMHHIHHIIIHMMMML.
                     "WMMMMMMMMMMMMMMMMMMH:::::HMMMMMMHII:.
                .AMMMMMMMHHHMMMMMMMMMMHHHHHMMMMMMMMMAMMMHHHHL.
              .MMMMMMMMMMHHMMMMMMMMHHHHMMMMMMMMMMMMMHTWMHHHHHML
             .MMMMMMMMMMMMMMMMMMMHHHHHHHHHMHMMHHHHIII:::HMHHHHMM.
             .MMMMMMMMMMMMMMMMMMMMMMHHHHHHMHHHHHHIIIIIIIIHMHHHHHM.
             MMMMMMMMMMMMMMMMMHHMMHHHHHIIIHHH::IIHHII:::::IHHHHHHHL
             "MMMMMMMMMMMMMMMMHIIIHMMMMHHIIHHLI::IIHHHHIIIHHHHHHHHML
             .MMMMMMMMMMMMMM"WMMMHHHMMMMMMMMMMMLHHHMMMMMMHHHHHHHHHHH
            .MMMMMMMMMMMWWMW""YYHMMMMMMMMMMMMF""HMMMMMMMMMHHHHHHHH.
            .MMMMMMMMMM W" V                         W"WMMMMMHHHHHHHHHH
           "MMMMMMMMMM".                                 "WHHHMH"HHHHHHL
           MMMMMMMMMMF  .                                         IHHHHH.
           MMMMMMMMMM .                                  .        HHHHHHH
           MMMMMMMMMF. .                               .  .       HHHHHHH.
           MMMMMMMMM .     ,AWMMMMML.              ..    .  .     HHHHHHH.
         :MMMMMMMMM".  .  F"'    'WM:.         ,::HMMA, .  .      HHHHMMM
         :MMMMMMMMF.  . ."         WH..      AMM"'     "  .  .    HHHMMMM
          MMMMMMMM . .     ,;AAAHHWL"..     .:'                   HHHHHHH
          MMMMMMM:. . .   -MK"OTO L :I..    ...:HMA-.             "HHHHHH
     ,:IIIILTMMMMI::.      L,,,,.  ::I..    .. K"OTO"ML           'HHHHHH
     LHT::LIIIIMMI::. .      '""'.IHH:..    .. :.,,,,           '  HMMMH: HLI'
     ILTT::"IIITMII::.  .         .IIII.     . '""""             ' MMMFT:::.
     'HML:::WMIINMHI:::.. .          .:I.     .   . .  .        '  ."'.....I.
     "HWHINWI:.'.HHII::..          .HHI     .II.    .  .      . . :M.',, ..I:
      '"MLI"ML': 'HHII::...        MMHHL     :::::  . :..      .'.'LMLML,
       "MMLIHHWL:IHHII::....:I:"'MHHWHI'...:'w',,"  '':::.      ..'  ":.
         "MMMHITIIHHH:::::IWF"    """T99"'  '""    '.':II:..'.'..'  I'.HHIHI'
           YMMHII:IHHHH:::IT..     . .   ...  . .    ''THHI::.'.' .;H.""."H"
             HHII:MHHI"::IWWL     . .     .    .  .     HH"HHHIIHHH":HWWM"
              """ MMHI::HY""ML,          ...     . ..  :"  :HIIIIIILTMH"
                   MMHI'.'    'HL,,,,,,,,..,,,......,:" . ''::HH 
                   'MMH:..   . 'MML': """MM""""MMM"      .'.IH'"MH"
                    "MMHL..   .. ''MMMMMML,MM,HMMMF''    .   .IHM"
                      "MMHHL    .. MMMMMMMMMMMM"  . .  '.IHF'
                        'MMMML    .. "MMMMMMMM"  .     .'HMF
                         'HHHMML''.                    .'MMF"
                        IHHHHHMML.               .'HMF"
                        HHHHHHITMML.           .'IF..
                        "HHHHHHIITML,.       ..:F...
                         'HHHHHHHHHMMWWWWWW::"......
                           
                                




                             ''')
    yname=str(input('Enter your name'))
    from gtts import gTTS
    import os
    from subprocess import Popen
    language='en'
    import pygame
    from pygame import mixer

    import sys

    import time

    import random
             
                                 

    red = pygame.Color(255, 0, 0)

    black = pygame.Color(0, 0, 0)

    white = pygame.Color(255, 255, 255)


    brown = pygame.Color(165, 42, 42)

    a=0
    c=('Hi I  am varvis your gaming buddy.I can help you choose colour of your snake.Press 1 for red, 2 for white, 3 for black. Then minimise this window and click on the window that appears')
    print(c)
    source=gTTS(text=c,lang=language,slow=False)
    source.save('k1.mp3')
    mixer.init()
    mixer.music.load("k1.mp3")
    mixer.music.play()
    a=input(":")
    if a=='1':
        red=red
    if a=='2':
        red=white
    elif a=='3':
        red=black

    pygame.time.delay(5000)
    mixer.init()
    mixer.music.load("JAVA game theme song - Snake III JAVA game theme song.mp3")
    mixer.music.play()
    # Pygame Init

    init_status = pygame.init()

    if init_status[1] > 0:

        print("(!) Had {0} initialising errors, exiting... ".format(init_status[1]))

        sys.exit()

    else:

        print("(+) Pygame initialised successfully ")



    # Play Surface

    size = width, height = 640, 320

    playSurface = pygame.display.set_mode(size)

    pygame.display.set_caption("Snake Game")



    # Colors

    green = pygame.Color(0, 255, 0)

    # FPS controller

    fpsController = pygame.time.Clock()



    # Game settings

    delta = 10

    snakePos = [100, 50]

    snakeBody = [[100, 50], [90, 50], [80, 50]]

    foodPos = [400, 50]

    foodSpawn = True

    direction = 'RIGHT'

    changeto = ''

    score = 0





    # Game Over

    def gameOver():

        myFont = pygame.font.SysFont('monaco', 72)

        GOsurf = myFont.render("Game Over", True, red)

        GOrect = GOsurf.get_rect()

        GOrect.midtop = (320, 25)

        playSurface.blit(GOsurf, GOrect)

        showScore(0)
    

        pygame.display.flip()

        time.sleep(4)

        pygame.quit()
        print(scory)
        pygame.mixer.quit()
        pass2=str(input("Enter your mysql password"))
        mydb1= mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=pass2,
        database='snake')
        cursor1=mydb1.cursor()
        sql="INSERT INTO snakegamescores(name,score) VALUES (%s,%s)"
        val=(yname,scory)
        cursor1.execute(sql,val)
        mydb1.commit()

        sys.exit()





    # Show Score

    def showScore(choice=1):

        SFont = pygame.font.SysFont('monaco', 32)

        Ssurf = SFont.render("Score  :  {0}".format(score-1), True, black)

        Srect = Ssurf.get_rect()

        if choice == 1:

            Srect.midtop = (80, 10)

        else:

            Srect.midtop = (320, 100)

        playSurface.blit(Ssurf, Srect)





    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()


                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:

                    changeto = 'RIGHT'

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:

                    changeto = 'LEFT'

                if event.key == pygame.K_UP or event.key == pygame.K_w:

                    changeto = 'UP'


                if event.key == pygame.K_DOWN or event.key == pygame.K_s:

                    changeto = 'DOWN'

                if event.key == pygame.K_ESCAPE:

                    pygame.event.post(pygame.event.Event(pygame.QUIT))



        # Validate direction

        if changeto == 'RIGHT' and direction != 'LEFT':

            direction = changeto

        if changeto == 'LEFT' and direction != 'RIGHT':

            direction = changeto

        if changeto == 'UP' and direction != 'DOWN':

            direction = changeto

        if changeto == 'DOWN' and direction != 'UP':

            direction = changeto



        # Update snake position

        if direction == 'RIGHT':

            snakePos[0] += delta

        if direction == 'LEFT':

            snakePos[0] -= delta

        if direction == 'DOWN':

            snakePos[1] += delta

        if direction == 'UP':

            snakePos[1] -= delta



        # Snake body mechanism

        snakeBody.insert(0, list(snakePos))

        if snakePos == foodPos:

            foodSpawn = False

            score += 1
            global scory
            scory=score-1
        else:

            snakeBody.pop()

        if foodSpawn == False:

            foodPos = [random.randrange(1, width // 10) * delta, random.randrange(1, height // 10) * delta]

            foodSpawn = True



        playSurface.fill(green)

        for pos in snakeBody:

            pygame.draw.rect(playSurface, red, pygame.Rect(pos[0], pos[1], delta, delta))

        pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], delta, delta))



        # Bounds

        if snakePos[0] >= width or snakePos[0] < 0:


            gameOver()
            

        if snakePos[1] >= height or snakePos[1] < 0:

            gameOver()
            
         


        # Self hit

        for block in snakeBody[1:]:

            if snakePos == block:

                gameOver()
                pygame.mixer.stop()
                

        showScore()

        pygame.display.flip()

        fpsController.tick(20)
  



 

    

                                                



                                                    

