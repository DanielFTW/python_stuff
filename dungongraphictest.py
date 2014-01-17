
class Level(object):
    def __init__(self,txt):
        self.lines=len(txt.splitlines())
        self.colls=len(txt.splitlines()[1])
        self.txt=txt
    def check(self, x, y):
        """
        check if this is a valid space
        """
        char=self.txt.splitlines()[y][x]
        return char
levels=[]
players=[]
#level0
levels.append(Level("""
################>>>################################
###########                 #########  7 MMM      #
############              ############# MMMMMMMMM #
###    ######        ###############              #
###  8 #######    O    #####################      #
###    ########      O         #############      #
###  ###########             ##################|||#
###  #########                                    #
###      ####                                     #
#######      #####                                #
###########      |                         ########
##################        B            s          #
##################| ||||||||||||||||||||||||||||||#
##################                                #
##################                        l       #
#                            D                    #
#                                T                #
#                                                 #
#                                                 #  
###################################################                                              
"""))
#T=Troll / G=Goblin / D=DarkElv / B=Bat / O=Ork / M=Mice
#|=breakable wall / #=unbreakable wall
#8=full health potion / 7=super big backpack / s=sword / l=leather helmet


#level1
levels.append(Level("""
################<<<###############################
#                  #       #                     #       
#    ###############   #   #       ###############
#                      #   #  MMM  #             #
########################   # O     #             #                         
#              O           #       #       O     #  
#       D                  #   T   #             #            
#                  MMMM    #       #             #             
#    #######################       #      ##### ##                                          
#     #     #                      #      #      #           
#      #     #     #################      #      #                                         
#       #     #     #                     #      #                                               
##       #     #     #             ########      #             
# #       #     #     #            #      #      #                                       
#  #       #     #     #           #  G   #      #                           
#   #   B   #     #     #          #      #      #                              
#  #         #   #     #           #      #      #                                     
# #         #   #     ######### ####      #      #                                    
##   B     #   #     #             #      #      #                                      
#        #    #     #              #      #      #                                          
#                                  #      #      #             
#############################################>>>##
"""))


mylevel=0


class Player(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y

players.append(Player(3,19))

def main():
    mylevel=0
    while True:
        x=0
        y=0

        for line in levels[mylevel].txt.splitlines():
            textline=""
            x=0
            for char in line:
                for player in players:
                    if player.x==x and player.y==y:
                        textline+="@"
                    else:
                        textline+=char
                    x+=1
                
            print(textline)
            y+=1
        print("Enter W , A , S , D to move")
        print("Enter Q to quit")
        command=input(">>>").lower()
        if command=="w":
            if players[0].y>1:
                newchar=levels[mylevel].check(players[0].x, players[0].y-1)
                if newchar in "#|":
                    print("You cant go walk here")
                elif newchar==">":
                    mylevel+=1
                else:
                    players[0].y-=1
        if command=="s":
            if players[0].y< levels[mylevel].lines-1:
                newchar=levels[mylevel].check(players[0].x, players[0].y+1)
                if newchar in "#|":
                    print("You cant go walk here")
                else:
                    players[0].y+=1
        if command=="a":
            if players[0].x>0:
                print("you will walk into :{}".format(
                     levels[mylevel].check(players[0].x-1, players[0].y)))
                newchar=levels[mylevel].check(players[0].x-1, players[0].y)
                if newchar in "#|":
                    print("You cant go walk here")
                else:
                    players[0].x-=1
        if command=="d":
            if players[0].x< levels[mylevel].colls-1:
                newchar=levels[mylevel].check(players[0].x+1, players[0].y)
                if newchar in "#|":
                    print("You cant go walk here")
                else:
                    players[0].x+=1
        if command=="q":
            break

main()

    

