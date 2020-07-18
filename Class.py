
import pygame
import random

pygame.init()
clock=pygame.time.Clock()
icon = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\icon.png")
pygame.display.set_caption("Chess")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((700,525)) 
SelectedCopy = 0 ##this variable copies the information of selected(The chosen piece to move next) piece
MousePosition = [0,0] ##Temporary value given for mousePosition
FaceList = ["Up","Down"]
k=0
IsCutLeft = False
IsCutRight = False
IsFront = False
IsSelected = False
Xcordinate=0
Ycordinate=0
PawnCutLeft=True
PawnCutRight=True
PawnCutRightConst = 0
PawnCutLeftConst = 0
PawnFrontMotion1=True
############################BackGround########################################################################################
Background = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\BG.png")
LeftBorder=132
SquareSide=56.34
#
###############################################Functions#######################################################################
##########################Information on selected class##################
class SelectedInfoClass(object):
    def __init__(self,Item,Grid):
        self.Grid = Grid
        self.item=Item

############### 1 Grid ###############
def Grid(x,y):
    if (x<132 or x>570) or (y<40 or y>472):
        GridNum = 100
    elif x<181:
        if y>40 and y<94:
            GridNum=11
        elif y<156:
            GridNum=21
        elif y<213:
            GridNum=31
        elif y<269:
            GridNum=41
        elif y<325:
            GridNum=51
        elif y<381:
            GridNum=61
        elif y<438:
            GridNum=71
        elif y<472:
            GridNum=81
    elif x<231:
        if y>40 and y<94:
            GridNum=12
        elif y<156:
            GridNum=22
        elif y<213:
            GridNum=32
        elif y<269:
            GridNum=42
        elif y<325:
            GridNum=52
        elif y<381:
            GridNum=62
        elif y<438:
            GridNum=72
        elif y<472:
            GridNum=82
    elif x<291:
        if y>40 and y<94:
            GridNum=13
        elif y<156:
            GridNum=23
        elif y<213:
            GridNum=33
        elif y<269:
            GridNum=43
        elif y<325:
            GridNum=53
        elif y<381:
            GridNum=63
        elif y<438:
            GridNum=73
        elif y<472:
            GridNum=83
    elif x<345:
        if y>40 and y<94:
            GridNum=14
        elif y<156:
            GridNum=24
        elif y<213:
            GridNum=34
        elif y<269:
            GridNum=44
        elif y<325:
            GridNum=54
        elif y<381:
            GridNum=64
        elif y<438:
            GridNum=74
        elif y<472:
            GridNum=84
    elif x<404:
        if y>40 and y<94:
            GridNum=15
        elif y<156:
            GridNum=25
        elif y<213:
            GridNum=35
        elif y<269:
            GridNum=45
        elif y<325:
            GridNum=55
        elif y<381:
            GridNum=65
        elif y<438:
            GridNum=75
        elif y<472:
            GridNum=85
    elif x<459:
        if y>40 and y<94:
            GridNum=16
        elif y<156:
            GridNum=26
        elif y<213:
            GridNum=36
        elif y<269:
            GridNum=46
        elif y<325:
            GridNum=56
        elif y<381:
            GridNum=66
        elif y<438:
            GridNum=76
        elif y<472:
            GridNum=86
    elif x<516:
        if y>40 and y<94:
            GridNum=17
        elif y<156:
            GridNum=27
        elif y<213:
            GridNum=37
        elif y<269:
            GridNum=47
        elif y<325:
            GridNum=57
        elif y<381:
            GridNum=67
        elif y<438:
            GridNum=77
        elif y<472:
            GridNum=87
    elif x<573:
        if y>40 and y<94:
            GridNum=18
        elif y<156:
            GridNum=28
        elif y<213:
            GridNum=38
        elif y<269:
            GridNum=48
        elif y<325:
            GridNum=58
        elif y<381:
            GridNum=68
        elif y<438:
            GridNum=78
        elif y<472:
            GridNum=88
    return GridNum

###################To convert the given grid to GridX and GridY
def GridToGridcoordinates(GridValue):
    GridX=GridValue%10
    GridY=(GridValue-GridX)/10
    return(int(GridX),int(GridY))
####################To convert the grid to given coordinates
def GridToCordinates(GridValue):
    for i in range(8):
        for j in range(8):
            if GridValue == ((i+1)*10+(j+1)):
                Xcordinate = 132+(57*j)
                Ycordinate = 43+(57*i)
                return Xcordinate,Ycordinate

#####################class for pawn#############
class PawnUclass(object):
    def __init__(self,x,y,PawnUpImage,IsFirstTouch):
        self.x=x
        self.y=y
        self.image=PawnUpImage
        self.IsFirstTouch = IsFirstTouch


class PawnDclass(object):
    def __init__(self,x,y,PawnDownImage,IsFirstTouch):
        self.x=x
        self.y=y
        self.image=PawnDownImage
        self.IsFirstTouch = IsFirstTouch

################class for king
class KingClass(object):
    def __init__(self,x,y,Image):
        self.x=x
        self.y=y
        self.Image = Image

################Class for queen
class QueenClass(object):
    def __init__(self,x,y,Image):
        self.x=x
        self.y=y
        self.Image=Image

#################Class for bishop
class BishopClass(object):
    def __init__(self,x,y,Image):
        self.x = x
        self.y = y
        self.Image = Image

#################Class for knight
class KnightClass(object):
    def __init__(self,x,y,Image):
        self.x = x
        self.y = y
        self.Image = Image

################Class for rook
class RookClass(object):
    def __init__(self,x,y,Image):
        self.x = x
        self.y = y
        self.Image = Image

DefColor = random.choice([1,0])
print(DefColor)   

if DefColor==0:
    ##White is facing upwards
    PawnUpImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\WhiteUp\PawnWU.png") #White Up

    KnightUImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\WhiteUp\KnightWU.png")

    BishopUImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\WhiteUp\BishopWU.png")

    RookUImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\WhiteUp\RookWU.png")
    
    QueenUImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\WhiteUp\QueenWU.png")

    KingUImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\WhiteUp\KingWU.png")

    PawnChangeImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\WhitePawnChange.png")

    ##Black is facing downwards
    PawnDownImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\BlackDown\PawnBD.png") ##Black down

    KnightDImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\BlackDown\KnightBD.png")

    BishopDImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\BlackDown\BishopBD.png")

    RookDImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\BlackDown\RookBD.png")

    QueenDImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\BlackDown\QueenBD.png")

    KingDImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\BlackDown\KingBD.png")
    ##
elif 1:
        ##Black facing upwards
    PawnUpImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\BlackUp\PawnBU.png") ##Black up

    KnightUImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\BlackUp\KnightBU.png")

    BishopUImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\BlackUp\BishopBU.png")

    RookUImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\BlackUp\RookBU.png")
    
    QueenUImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\BlackUp\QueenBU.png")

    KingUImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\BlackUp\KingBU.png")

    PawnChangeImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\BlackPawnChange.png")

    ##White is facing downwards
    PawnDownImage= pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\WhiteDown\PawnWD.png") ##White down

    KnightDImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\WhiteDown\KnightWD.png")

    BishopDImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\WhiteDown\BishopWD.png")

    RookDImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\WhiteDown\RookWD.png")

    QueenDImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\WhiteDown\QueenWD.png")

    KingDImage = pygame.image.load("E:\Studies\Python\Projects\Games\Chess\Data\WhiteDown\KingWD.png")
    #
#################Defining pieces

##Pawn 
PawnD=[]
PawnU=[]
Xincrement=0
for i in range(8):
    PawnD.append(PawnDclass(132+Xincrement,100,PawnDownImage,True))
    PawnU.append(PawnUclass(132+Xincrement,385,PawnUpImage,True))
    Xincrement+=57

##King
KingU = KingClass(GridToCordinates(85)[0],GridToCordinates(85)[1],KingUImage)
KingD = KingClass(GridToCordinates(15)[0],GridToCordinates(15)[1],KingDImage)

##Queen
QueenU = QueenClass(GridToCordinates(84)[0],GridToCordinates(84)[1],QueenUImage)
QueenUList = [QueenU]
QueenD = QueenClass(GridToCordinates(14)[0],GridToCordinates(14)[1],QueenDImage)
QueenDList = [QueenD]

##Bishop
Bishop1U = BishopClass(GridToCordinates(83)[0],GridToCordinates(83)[1],BishopUImage)
Bishop2U = BishopClass(GridToCordinates(86)[0],GridToCordinates(86)[1],BishopUImage)
BishopUList = [Bishop1U,Bishop2U]
Bishop1D = BishopClass(GridToCordinates(13)[0],GridToCordinates(13)[1],BishopDImage)
Bishop2D = BishopClass(GridToCordinates(16)[0],GridToCordinates(16)[1],BishopDImage)
BishopDList = [Bishop1D,Bishop2D]

##Knight
Knight1U = KnightClass(GridToCordinates(82)[0],GridToCordinates(82)[1],KnightUImage)
Knight2U = KnightClass(GridToCordinates(87)[0],GridToCordinates(87)[1],KnightUImage)
KnightUList = [Knight1U,Knight2U]
Knight1D = KnightClass(GridToCordinates(12)[0],GridToCordinates(12)[1],KnightDImage)
Knight2D = KnightClass(GridToCordinates(17)[0],GridToCordinates(17)[1],KnightDImage)
KnightDList = [Knight1D,Knight2D]

##Rook
Rook1U = RookClass(GridToCordinates(81)[0],GridToCordinates(81)[1],RookUImage)
Rook2U = RookClass(GridToCordinates(88)[0],GridToCordinates(88)[1],RookUImage) 
RookUList = [Rook1U,Rook2U]
Rook1D = RookClass(GridToCordinates(11)[0],GridToCordinates(11)[1],RookDImage)
Rook2D = RookClass(GridToCordinates(18)[0],GridToCordinates(18)[1],RookDImage)
RookDList = [Rook1D,Rook2D]

AllPieceList = [PawnU,PawnD,KnightUList,KnightDList,BishopUList,BishopDList,RookUList,RookDList,QueenUList,QueenDList,KingU,KingD]
UpPieceList = [PawnU,KnightUList,BishopUList,RookUList,QueenU,KingU]
DownPieceList = [PawnD,KnightUList,BishopDList,RookDList,QueenD,KingD]

running = True
############################Running loop######################################################################################
while running:
    ##Background
    clock.tick(50)
    screen.blit(Background,(0,0))
    i=0
    ######################################Bliting all peices
    ##bliting all pawns in its respective positions
    for i in range(8):
        screen.blit(PawnD[i].image,(PawnD[i].x,PawnD[i].y))
        screen.blit(PawnU[i].image,(PawnU[i].x,PawnU[i].y))
    #############Rook
    screen.blit(Rook1U.Image,(Rook1U.x,Rook1U.y))
    screen.blit(Rook2U.Image,(Rook2U.x,Rook2U.y))
    screen.blit(Rook1D.Image,(Rook1D.x,Rook1D.y))
    screen.blit(Rook2D.Image,(Rook2D.x,Rook2D.y))
    #############Knight
    screen.blit(Knight1U.Image,(Knight1U.x,Knight1U.y))
    screen.blit(Knight2U.Image,(Knight2U.x,Knight2U.y))
    screen.blit(Knight1D.Image,(Knight1D.x,Knight1D.y))
    screen.blit(Knight2D.Image,(Knight2D.x,Knight2D.y))
    #############Bishop
    screen.blit(Bishop1U.Image,(Bishop1U.x,Bishop1U.y))
    screen.blit(Bishop2U.Image,(Bishop2U.x,Bishop2U.y))
    screen.blit(Bishop1D.Image,(Bishop1D.x,Bishop1D.y))
    screen.blit(Bishop2D.Image,(Bishop2D.x,Bishop2D.y))
    #############Queen
    screen.blit(QueenUImage,(QueenU.x,QueenU.y))
    screen.blit(QueenDImage,(QueenD.x,QueenD.y))
    #############King
    screen.blit(KingU.Image,(KingU.x,KingU.y))
    screen.blit(KingD.Image,(KingD.x,KingD.y)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button== 1:
                print("left Button")
                MousePosition = pygame.mouse.get_pos()
                print(MousePosition)
                print(Grid(MousePosition[0],MousePosition[1]))



    ##checking whether any pawns facing UPWARDS coincides with the position of mousepointer
    for Lists in UpPieceList:
        print("List")
        for pieces in Lists:
            print("Pieces")
            #if Grid(MousePosition[0],MousePosition[1])==Grid(pieces.x,pieces.y):
             #   SelectedInfo = SelectedInfoClass(pieces,Grid(MousePosition[0],MousePosition[1]))
              #  IsSelected = True
               # print("Selected X coordinate on grid",GridToGridcoordinates(Grid(SelectedInfo.item.x,SelectedInfo.item.y)))
    ####Checking for all the possible moves of pawn####################
    if IsSelected:
        print(SelectedInfo.Grid-Grid(PawnD[i].x,PawnD[i].y))
        if SelectedInfo.Grid-Grid(PawnD[k].x,PawnD[k].y)==10:
            PawnFrontMotion1=False
        else:
            PawnFrontMotion1Const =0
            for i in range(8):
                if SelectedInfo.Grid-Grid(DownPieceList[i].x,DownPieceList[i].y)==10:
                    PawnFrontMotion1Const +=1
                if PawnFrontMotion1Const==0:
                    PawnFrontMotion1=True
                else:
                    PawnFrontMotion1=False
                
        if k!=0:
            PawnCutLeftConst=0
            if SelectedInfo.Grid-Grid(PawnD[k-1].x,PawnD[k-1].y)==11:
                PawnCutLeftConst+=1
                PawnCutLeftPiece=PawnD[k-1]
            else:
                for i in range(8):
                    if SelectedInfo.Grid-Grid(DownPieceList[i].x,DownPieceList[i].y) == 11:
                        PawnCutLeft=True
                        PawnCutLeftPiece = DownPieceList[i]
                        PawnCutLeftConst+=1
        if PawnCutLeftConst>0:
            PawnCutLeft=True
        else:
            PawnCutLeft=False

        if k!=7:
            PawnCutRightConst = 0
            if SelectedInfo.Grid-Grid(PawnD[k+1].x,PawnD[k+1].y)==9 :
                PawnCutRightPiece=PawnD[k+1]
                PawnCutRightConst+=1
            else:
                for i in range(8):
                    if SelectedInfo.Grid-Grid(DownPieceList[i].x,DownPieceList[i].y)==9:
                        PawnCutRightConst+=1
                        PawnCutRightPiece = DownPieceList[i]
        if PawnCutRightConst>0:
            PawnCutRight=True
        else:
            PawnCutRight=False

    ##Motion of pawn
    if IsSelected:
        print("hey")
        if PawnFrontMotion1:##Moving front
            print(Grid(MousePosition[0],MousePosition[1])-Grid(PawnU[k].x,PawnU[k].y))
            if PawnU[k].IsFirstTouch:
                if (Grid(PawnU[k].x,PawnU[k].y)-Grid(MousePosition[0],MousePosition[1]) == 10) or (Grid(PawnU[k].x,PawnU[k].y)-Grid(MousePosition[0],MousePosition[1]) == 20):
                    PawnU[k].y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                    PawnU[k].IsFirstTouch=False
            elif (Grid(PawnU[k].x,PawnU[k].y)-Grid(MousePosition[0],MousePosition[1])) == 10:
                PawnU[k].y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                PawnU[k].IsFirstTouch=False
                print("Graaa")
        if SelectedInfo.Grid>10 and SelectedInfo.Grid<20:
            PawnU[k].x=700
            PawnU[k].y=525
            screen.blit(PawnChangeImage,(GridToCordinates(43)[0]-11,GridToCordinates(43)[1]+10))
            
            
        if PawnCutLeft and k!=0:##Cutting left
            if Grid(PawnU[k].x,PawnU[k].y)-Grid(MousePosition[0],MousePosition[1])==11:
                PawnU[k].x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                PawnU[k].y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                PawnCutLeftPiece.x=700
                PawnCutLeftPiece.y=525
        if PawnCutRight and k!=7:##Cutting right
            if Grid(PawnU[k].x,PawnU[k].y)-Grid(MousePosition[0],MousePosition[1])==9:
                PawnU[k].x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                PawnU[k].y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                PawnCutRightPiece.x=700
                PawnCutRightPiece.y=525


    
    pygame.display.update()