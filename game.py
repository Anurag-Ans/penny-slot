import random
x= 0
bet = 100
while x == 0   :
    def start() :
        code = [random.randint(1,5),random.randint(1,5)-1,random.randint(1,5)-2]
        if bet ==33:
            code[0] = 33
            code [1] = code[0] 
            code[2] = code[1]
            
        return code

    ans = start()
    print "Penny Slot Game"
    print "Do you want to begin the game (Y/N)"
    choice = raw_input()
    if choice=="Y" :
        
        print "You have got  amount in your pocket . "
        print bet
        on_bet = input("How much do you want to bet ??")
        if on_bet == 0:
            print " Sorry you just can't bet a zero , you cheater , get out !!!"
            break
        bet = bet - on_bet 
        

        print "Let's Roll !!!"
        print ans
        if ans[0]==ans[1]==ans[2]:
            print "You have won !!!!"
            bet = bet + (on_bet*2)
            print "Now your pocket holds - "
            print bet
        else:
            print"Sorry you loose !!!"
        if bet == 0 :
            print "Sorry you have been ruined , Get out from here , this place is for people with money . !!!!"
            break
        ch = raw_input("Do you want to play again ?(Y/N)")
        if ch == "N":
            break
        

    elif choice=="N":
        print "Ok Bye"
        break
    



    

