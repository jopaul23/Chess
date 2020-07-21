
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
IsPawnChange = False
IsPawnChanging = False
KnightMotion = False
TopLeftTempConst = 0
KingMotionNum=0
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
    def __init__(self,x,y,Image,IsFirstTouch):
        self.x=x
        self.y=y
        self.Image=PawnUpImage
        self.IsFirstTouch = IsFirstTouch


class PawnDclass(object):
    def __init__(self,x,y,Image,IsFirstTouch):
        self.x=x
        self.y=y
        self.Image=PawnDownImage
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
        self.x = x
        self.y = y
        self.Image = Image

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
KingUList = [KingU]
KingD = KingClass(GridToCordinates(15)[0],GridToCordinates(15)[1],KingDImage)
KingDList = [KingD]
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

AllPieceList = [PawnU,PawnD,KnightUList,KnightDList,BishopUList,BishopDList,RookUList,RookDList,QueenUList,QueenDList,KingUList,KingDList]
UpPieceList = [PawnU,KnightUList,BishopUList,RookUList,QueenUList,KingUList]
DownPieceList = [PawnD,KnightDList,BishopDList,RookDList,QueenDList,KingDList]

running = True
############################Running loop######################################################################################
while running:
    ##Background
    clock.tick(50)
    screen.blit(Background,(0,0))
    i=0
    ######################################Bliting all peices
    ##bliting all pawns in its respective positions
    for lists in AllPieceList:
        for piece in lists:
            screen.blit(piece.Image,(piece.x,piece.y))
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
        for pieces in Lists:
            if Grid(MousePosition[0],MousePosition[1])==Grid(pieces.x,pieces.y):
                SelectedInfo = SelectedInfoClass(pieces,Grid(MousePosition[0],MousePosition[1]))
                IsSelected = True
    #########################################pawn#################################################3
    ####Checking for all the possible moves of pawn####################
    if IsSelected:
        for pawn in PawnU:
            if SelectedInfo.item==pawn:
                PawnFrontMotion1Const =0
                for lists in DownPieceList:
                    for pieces in lists:
                
                        if SelectedInfo.Grid-Grid(pieces.x,pieces.y)==10:
                            PawnFrontMotion1Const +=1
                        if PawnFrontMotion1Const==0:
                            PawnFrontMotion1=True
                        else:
                            PawnFrontMotion1=False
                
                if GridToGridcoordinates(SelectedInfo.Grid)[0]!=0:
                    PawnCutLeftConst=0
                    for lists in DownPieceList:
                        for pieces  in  lists:
                            if SelectedInfo.Grid-Grid(pieces.x,pieces.y)==11:
                                PawnCutLeftConst+=1
                                PawnCutLeftPiece=pieces
                            PawnCutLeft=True
                if PawnCutLeftConst>0:
                    PawnCutLeft=True
                else:
                    PawnCutLeft=False

                if GridToGridcoordinates(SelectedInfo.Grid)[0]!=8 :
                    PawnCutRightConst = 0
                    for lists in DownPieceList:
                        for piece in lists:
                            if SelectedInfo.Grid-Grid(piece.x,piece.y)==9 :
                                PawnCutRightPiece=piece
                                PawnCutRightConst+=1
                if PawnCutRightConst>0:
                    PawnCutRight=True
                else:
                    PawnCutRight=False

    ##Motion of pawnhh
    if IsSelected:
        for pawn in PawnU:
            if SelectedInfo.item==pawn:
                if PawnFrontMotion1:##Moving front
                    if SelectedInfo.item.IsFirstTouch:##This is the case of pawn
                        if (SelectedInfo.Grid-Grid(MousePosition[0],MousePosition[1]) == 10) or (SelectedInfo.Grid-Grid(MousePosition[0],MousePosition[1]) == 20):
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                            SelectedInfo.item.IsFirstTouch=False
                    elif SelectedInfo.Grid-Grid(MousePosition[0],MousePosition[1]) == 10:
                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                        SelectedInfo.item.IsFirstTouch=False

        ###What happens when pawn reach the other end
        for pawn in PawnU:
            if Grid(SelectedInfo.item.x,SelectedInfo.item.y)>10 and(Grid(SelectedInfo.item.x,SelectedInfo.item.y)<20 and SelectedInfo.item==pawn) :##Checking whtether it reached last row
                IsPawnChange=True
        if IsPawnChange:
            screen.blit(PawnChangeImage,(GridToCordinates(43)[0]-11,GridToCordinates(43)[1]+10))
            if Grid(MousePosition[0],MousePosition[1])==43 or Grid(MousePosition[0],MousePosition[1])==53:
                RookUList.append(RookClass(SelectedInfo.item.x,SelectedInfo.item.y,RookUImage))  
                SelectedInfo.item.x=700
                SelectedInfo.item.y=525
                IsPawnChange=False 
            elif Grid(MousePosition[0],MousePosition[1])==44 or Grid(MousePosition[0],MousePosition[1])==54:
                BishopUList.append(BishopClass(SelectedInfo.item.x,SelectedInfo.item.y,BishopUImage))
                SelectedInfo.item.x=700
                SelectedInfo.item.y=525
                IsPawnChange=False 
            elif Grid(MousePosition[0],MousePosition[1])==45 or Grid(MousePosition[0],MousePosition[1])==55:
                KnightUList.append(KnightClass(SelectedInfo.item.x,SelectedInfo.item.y,KnightUImage))
                SelectedInfo.item.x=700
                SelectedInfo.item.y=525
                IsPawnChange=False 
            elif Grid(MousePosition[0],MousePosition[1])==46 or Grid(MousePosition[0],MousePosition[1])==56:
                QueenUList.append(QueenClass(SelectedInfo.item.x,SelectedInfo.item.y,QueenUImage))
                SelectedInfo.item.x=700
                SelectedInfo.item.y=525
                IsPawnChange=False 
        for pawn in PawnU:
            if SelectedInfo.item==pawn:
                if PawnCutLeft and GridToGridcoordinates(SelectedInfo.Grid)[0]!=1:##Cutting left
                    if SelectedInfo.Grid-Grid(MousePosition[0],MousePosition[1])==11:
                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                        PawnCutLeftPiece.x=700
                        PawnCutLeftPiece.y=525
                if PawnCutRight and GridToGridcoordinates(SelectedInfo.Grid)[0]!=8:##Cutting right
                    if SelectedInfo.Grid-Grid(MousePosition[0],MousePosition[1])==9:
                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                        PawnCutRightPiece.x=700
                        PawnCutRightPiece.y=525
                        print(Grid(MousePosition[0],MousePosition[1]))
    ####################################################
    ######################################knight
    if IsSelected:
        for Knight in KnightUList:
            GridDifference = Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid
            if SelectedInfo.item == Knight:
                if ((GridDifference==-12 or GridDifference==-8)or(GridDifference==12 or GridDifference==8))or((GridDifference==-21 or GridDifference==-19)or(GridDifference==19 or GridDifference==21)):
                    KnightMotion=True
                    SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                    SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                    for lists in DownPieceList:
                        for piece in lists:
                            if Grid(MousePosition[0],MousePosition[1])==Grid(piece.x,piece.y):
                                piece.x=700
                                piece.y=525
            
    #########Bishop
    ###topleft
    TopLeftTempConst=0
    if IsSelected:
        for Bishop in BishopUList:
            if SelectedInfo.item==Bishop:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==-11*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==-11*(i+1):
                                        if TopLeftTempConst==0:
                                            TopLeftBlockPiece=piece
                                        else:
                                            if Grid(TopLeftBlockPiece.x,TopLeftBlockPiece.y)<Grid(piece.x,piece.y):
                                                TopLeftBlockPiece=piece
                                        TopLeftTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])>Grid(TopLeftBlockPiece.x,TopLeftBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(TopLeftBlockPiece.x,TopLeftBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if TopLeftBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        TopLeftBlockPiece.x=700
                                                        TopLeftBlockPiece.y=525
                        if TopLeftTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]

    ###topRight
    TopRightTempConst=0
    if IsSelected:
        for Bishop in BishopUList:
            if SelectedInfo.item==Bishop:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==-9*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==-9*(i+1):
                                        if TopRightTempConst==0:
                                            TopRightBlockPiece=piece
                                        else:
                                            if Grid(TopRightBlockPiece.x,TopRightBlockPiece.y)<Grid(piece.x,piece.y):
                                                TopRightBlockPiece=piece
                                        TopRightTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])>Grid(TopRightBlockPiece.x,TopRightBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(TopRightBlockPiece.x,TopRightBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if TopRightBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        TopRightBlockPiece.x=700
                                                        TopRightBlockPiece.y=525
                        if TopRightTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
    ###Bottomleft
    BottomLeftTempConst=0
    if IsSelected:
        for Bishop in BishopUList:
            if SelectedInfo.item==Bishop:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==9*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==9*(i+1):
                                        if BottomLeftTempConst==0:
                                            BottomLeftBlockPiece=piece
                                        else:
                                            if Grid(BottomLeftBlockPiece.x,BottomLeftBlockPiece.y)>Grid(piece.x,piece.y):
                                                BottomLeftBlockPiece=piece
                                        BottomLeftTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])<Grid(BottomLeftBlockPiece.x,BottomLeftBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(BottomLeftBlockPiece.x,BottomLeftBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if BottomLeftBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        BottomLeftBlockPiece.x=700
                                                        BottomLeftBlockPiece.y=525
                        if BottomLeftTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]

    ####BottomRight
    BottomRightTempConst=0
    if IsSelected:
        for Bishop in BishopUList:
            if SelectedInfo.item==Bishop:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==11*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==11*(i+1):
                                        if BottomRightTempConst==0:
                                            BottomRightBlockPiece=piece
                                        else:
                                            if Grid(BottomRightBlockPiece.x,BottomRightBlockPiece.y)>Grid(piece.x,piece.y):
                                                BottomRightBlockPiece=piece
                                        BottomRightTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])<Grid(BottomRightBlockPiece.x,BottomRightBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(BottomRightBlockPiece.x,BottomRightBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if BottomRightBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        BottomRightBlockPiece.x=700
                                                        BottomRightBlockPiece.y=525
                        if BottomRightTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
    ##############Roook
    ##bottom
    BottomTempConst=0
    if IsSelected:
        for Rook in RookUList:
            if SelectedInfo.item==Rook:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==10*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==10*(i+1):
                                        if BottomTempConst==0:
                                            BottomBlockPiece=piece
                                        else:
                                            if Grid(BottomBlockPiece.x,BottomBlockPiece.y)>Grid(piece.x,piece.y):
                                                BottomBlockPiece=piece
                                        BottomTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])<Grid(BottomBlockPiece.x,BottomBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(BottomBlockPiece.x,BottomBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if BottomBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        BottomBlockPiece.x=700
                                                        BottomBlockPiece.y=525
                        if BottomTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
    ##Top
    TopTempConst=0
    if IsSelected:
        for Rook in RookUList:
            if SelectedInfo.item==Rook:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==-10*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==-10*(i+1):
                                        if TopTempConst==0:
                                            TopBlockPiece=piece
                                        else:
                                            if Grid(TopBlockPiece.x,TopBlockPiece.y)<Grid(piece.x,piece.y):
                                                TopBlockPiece=piece
                                        TopTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])>Grid(TopBlockPiece.x,TopBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(TopBlockPiece.x,TopBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if TopBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        TopBlockPiece.x=700
                                                        TopBlockPiece.y=525
                        if TopTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                             
    ###Left
    LeftTempConst=0
    if IsSelected:
        for Rook in RookUList:
            if SelectedInfo.item==Rook:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==-1*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==-1*(i+1):
                                        if LeftTempConst==0:
                                            LeftBlockPiece=piece
                                        else:
                                            if Grid(LeftBlockPiece.x,LeftBlockPiece.y)<Grid(piece.x,piece.y):
                                                LeftBlockPiece=piece
                                        LeftTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])>Grid(LeftBlockPiece.x,LeftBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(LeftBlockPiece.x,LeftBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if LeftBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        LeftBlockPiece.x=700
                                                        LeftBlockPiece.y=525
                        if LeftTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
    ##Right                    
    RightTempConst=0
    if IsSelected:
        for Rook in RookUList:
            if SelectedInfo.item==Rook:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==1*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==1*(i+1):
                                        if RightTempConst==0:
                                            RightBlockPiece=piece
                                        else:
                                            if Grid(RightBlockPiece.x,RightBlockPiece.y)>Grid(piece.x,piece.y):
                                                RightBlockPiece=piece
                                        RightTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])<Grid(RightBlockPiece.x,RightBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(RightBlockPiece.x,RightBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if RightBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        RightBlockPiece.x=700
                                                        RightBlockPiece.y=525
                        if RightTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]

    #################################Queeeeeeeeeeen
    ###topleft
    TopLeftTempConst=0
    if IsSelected:
        for Queen in QueenUList:
            if SelectedInfo.item==Queen:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==-11*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==-11*(i+1):
                                        if TopLeftTempConst==0:
                                            TopLeftBlockPiece=piece
                                        else:
                                            if Grid(TopLeftBlockPiece.x,TopLeftBlockPiece.y)<Grid(piece.x,piece.y):
                                                TopLeftBlockPiece=piece
                                        TopLeftTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])>Grid(TopLeftBlockPiece.x,TopLeftBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(TopLeftBlockPiece.x,TopLeftBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if TopLeftBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        TopLeftBlockPiece.x=700
                                                        TopLeftBlockPiece.y=525
                        if TopLeftTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]

    ###topRight
    TopRightTempConst=0
    if IsSelected:
        for Queen in QueenUList:
            if SelectedInfo.item==Queen:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==-9*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==-9*(i+1):
                                        if TopRightTempConst==0:
                                            TopRightBlockPiece=piece
                                        else:
                                            if Grid(TopRightBlockPiece.x,TopRightBlockPiece.y)<Grid(piece.x,piece.y):
                                                TopRightBlockPiece=piece
                                        TopRightTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])>Grid(TopRightBlockPiece.x,TopRightBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(TopRightBlockPiece.x,TopRightBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if TopRightBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        TopRightBlockPiece.x=700
                                                        TopRightBlockPiece.y=525
                        if TopRightTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
    ###Bottomleft
    BottomLeftTempConst=0
    if IsSelected:
        for Queen in QueenUList:
            if SelectedInfo.item==Queen:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==9*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==9*(i+1):
                                        if BottomLeftTempConst==0:
                                            BottomLeftBlockPiece=piece
                                        else:
                                            if Grid(BottomLeftBlockPiece.x,BottomLeftBlockPiece.y)>Grid(piece.x,piece.y):
                                                BottomLeftBlockPiece=piece
                                        BottomLeftTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])<Grid(BottomLeftBlockPiece.x,BottomLeftBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(BottomLeftBlockPiece.x,BottomLeftBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if BottomLeftBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        BottomLeftBlockPiece.x=700
                                                        BottomLeftBlockPiece.y=525
                        if BottomLeftTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]

    ####BottomRight
    BottomRightTempConst=0
    if IsSelected:
        for Queen in QueenUList:
            if SelectedInfo.item==Queen:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==11*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==11*(i+1):
                                        if BottomRightTempConst==0:
                                            BottomRightBlockPiece=piece
                                        else:
                                            if Grid(BottomRightBlockPiece.x,BottomRightBlockPiece.y)>Grid(piece.x,piece.y):
                                                BottomRightBlockPiece=piece
                                        BottomRightTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])<Grid(BottomRightBlockPiece.x,BottomRightBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(BottomRightBlockPiece.x,BottomRightBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if BottomRightBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        BottomRightBlockPiece.x=700
                                                        BottomRightBlockPiece.y=525
                        if BottomRightTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
    ##############Roook
    ##bottom
    BottomTempConst=0
    if IsSelected:
        for Queen in QueenUList:
            if SelectedInfo.item==Queen:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==10*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==10*(i+1):
                                        if BottomTempConst==0:
                                            BottomBlockPiece=piece
                                        else:
                                            if Grid(BottomBlockPiece.x,BottomBlockPiece.y)>Grid(piece.x,piece.y):
                                                BottomBlockPiece=piece
                                        BottomTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])<Grid(BottomBlockPiece.x,BottomBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(BottomBlockPiece.x,BottomBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if BottomBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        BottomBlockPiece.x=700
                                                        BottomBlockPiece.y=525
                        if BottomTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
    ##Top
    TopTempConst=0
    if IsSelected:
        for Queen in QueenUList:
            if SelectedInfo.item==Queen:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==-10*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==-10*(i+1):
                                        if TopTempConst==0:
                                            TopBlockPiece=piece
                                        else:
                                            if Grid(TopBlockPiece.x,TopBlockPiece.y)<Grid(piece.x,piece.y):
                                                TopBlockPiece=piece
                                        TopTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])>Grid(TopBlockPiece.x,TopBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(TopBlockPiece.x,TopBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if TopBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        TopBlockPiece.x=700
                                                        TopBlockPiece.y=525
                        if TopTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                             
    ###Left
    LeftTempConst=0
    if IsSelected:
        for Queen in QueenUList:
            if SelectedInfo.item==Queen:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==-1*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==-1*(i+1):
                                        if LeftTempConst==0:
                                            LeftBlockPiece=piece
                                        else:
                                            if Grid(LeftBlockPiece.x,LeftBlockPiece.y)<Grid(piece.x,piece.y):
                                                LeftBlockPiece=piece
                                        LeftTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])>Grid(LeftBlockPiece.x,LeftBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(LeftBlockPiece.x,LeftBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if LeftBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        LeftBlockPiece.x=700
                                                        LeftBlockPiece.y=525
                        if LeftTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
    ##Right                    
    RightTempConst=0
    if IsSelected:
        for Queen in QueenUList:
            if SelectedInfo.item==Queen:
                for i in range(7):
                    if Grid(MousePosition[0],MousePosition[1])-SelectedInfo.Grid==1*(i+1):##Checking whether the seleced 
                        for i in range(7):
                            for lists in AllPieceList:
                                for piece in lists:
                                    if Grid(piece.x,piece.y)-SelectedInfo.Grid==1*(i+1):
                                        if RightTempConst==0:
                                            RightBlockPiece=piece
                                        else:
                                            if Grid(RightBlockPiece.x,RightBlockPiece.y)>Grid(piece.x,piece.y):
                                                RightBlockPiece=piece
                                        RightTempConst+=1
                                        if Grid(MousePosition[0],MousePosition[1])<Grid(RightBlockPiece.x,RightBlockPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                        elif Grid(MousePosition[0],MousePosition[1])==Grid(RightBlockPiece.x,RightBlockPiece.y):
                                            for DownPieces in DownPieceList:
                                                for DownPiece in DownPieces:
                                                    if RightBlockPiece==DownPiece:
                                                        SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                                        SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                                        RightBlockPiece.x=700
                                                        RightBlockPiece.y=525
                        if RightTempConst==0:
                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
    ##King
    if IsSelected:
        if SelectedInfo.item==KingUList[0]:
            for pieces in AllPieceList:
                for piece in pieces:
                    if Grid(piece.x,piece.y)!=Grid(MousePosition[0],MousePosition[1]):
                        KingDiff=Grid(MousePosition[0],MousePosition[1])-Grid(KingDList[0].x,KingDList[0].y)
                        if ((KingDiff==-11 or KingDiff==-10) or (KingDiff==-9 or KingDiff==-1))or((KingDiff==1 or KingDiff==9)or (KingDiff==10 or KingDiff==11)):
                            pass
                        else:
                            KingDiff2=Grid(MousePosition[0],MousePosition[1])-Grid(KingUList[0].x,KingUList[0].y)
                            for DownPieces in DownPieceList:
                                for DownPiece in DownPieces:
                                    if ((KingDiff2==-11 or KingDiff2==-10) or (KingDiff2==-9 or KingDiff2==-1))or((KingDiff2==1 or KingDiff2==9)or (KingDiff2==10 or KingDiff2==11)):
                                        if Grid(MousePosition[0],MousePosition[1])==Grid(DownPiece.x,DownPiece.y):
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                            DownPiece.x=700
                                            DownPiece.y=525
                                            KingMotionNum+=1
                                        else:
                                            SelectedInfo.item.x=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[0]
                                            SelectedInfo.item.y=GridToCordinates(Grid(MousePosition[0],MousePosition[1]))[1]
                                            KingMotionNum+=1
                        
    pygame.display.update()