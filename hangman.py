#hangman
import random
import turtle
def main():

    n=0
    while n==0:
        wordList=["mechanical","shimmering","photograph","companions","sprinkling","suppertime","amputation","electronic","omnipotent","triumphant","demolition","acclimated","bridesmaid","confounded","accredited","operations","silverback","assessment","succeeding","windowsill","gentleness","contrition","battleship","salamander","commentary","allocation","attributes","lighthouse","forbearing","saturation","transplant","accidental","chessboard","infighting","irrational","roadrunner","fluttering","anticipate","compromise","processing","conduction","processing","intolerant","decapitate","conditions","blistering","biophysics","flamboyant","foreseeing","lightening","exhaustion","congestion","discovered","apologetic","fraternity","satisfying","deactivate","worthiness","profession","alienation","bedazzling","gettysburg","turbulence","shattering","inflatable","absolutely","protractor","earmarking","journalist","lumberjack","antibiotic","scriptures","activating","witnessing","collection","habitation","adventures","astounding","naturalist","gradualism","projectile","submissive","settlement","federation","digression","detonation","subculture","mayonnaise","bolstering","accomplice","goldilocks","dilatation","boringness","waterproof","thickening","abominably","fellowship","energizing","projection","suggesting","speciality","crossroads","promptness","dishwasher","apparently","compatible","compelling","footballer","tumbleweed","destroying","concession","contestant","protruding","automation","estimation","assignable","navigation","deliberate","vegetation","remodeling","snickering","daydreamer","bewildered","millennium","nutcracker","harassment","dreamworld","conspiracy","proportion","irritation","babysitter","levitation","unyielding","hemisphere","accumulate","underwater","terminator","aboriginal","choiceless","occupation","wildebeest","madagascar","motherless","ecotourism","woodcutter","temperance","complexity","rottweiler","bratislava","equivalent","smothering","montgomery","acrobatics","artificial","biological","bareheaded","astonished","hereditary","rhinoceros","succession","acrophobia","kidnapping","enthusiasm","positivity","possessive","initiation","excavation","portuguese","prometheus","mainstream","disability","shopaholic","themselves","acquainted","translator","precaution","repentance","indication","motherland","escalating","interwoven","supermodel","sweltering","distortion","interested","upbringing","investment","definition","democratic","equestrian","aspiration","employment","blubbering","coronation","outlandish","paranormal","grapefruit","applesauce","footprints","adjustment","politician","seamstress","typewriter","exhibition","penetrator","interstate","compassion","locomotion","vulnerable","impeccable","dependable","properties","opposition","brilliance","blabbering","conceiving","auditorium","infidelity","psychology","completion","insatiable","thoughtful","wonderland","missionary","impressive","percussion","moderation","cantaloupe","allegation","identifier","fatherless","anesthesia","flatulence","compliance","enthusiast","chandelier","redemption","belongings","accessible","commercial","incredible","blackberry","attendance","crocheting","hesitation","misleading","backbiting","poinsettia","changeling","liveliness","binoculars","cardiology","linebacker","phenomenon","icebreaker","impediment","penicillin","courageous","impossible","playwright","confection","simulation","antisocial","outrageous","recreation","impression","plantation","semicircle","consistent","vegetarian","stalagmite","dehydrated","healthcare","conviction","centimeter","remembered","aggravator","microphone","aquamarine","blackbeard","irrigation","absorption","calculator","arithmetic","resentment","discomfort","aftershock","abbreviate","wheelchair","commission","astronomer","impressive","brokenness","convincing","determined","discretion","engagement","loveliness","respectful","slobbering","blacksmith","relentless","slithering","believable","flashlight","motionless","guillotine","chimpanzee","plagiarism","staggering","transition","simplicity","mysterious","discussion","conclusion","peacefully","prevention","misfortune","confession","ammunition","challenger","suggestion","initiative","starstruck","disrespect","effortless","locomotive","compulsion","dedication","heartbreak","industrial","immaculate","tenderness","perception","camouflage","roundabout","scoreboard"," admiration","pocahontas","expedition","microscope","toothbrush","liberation","meditation","waterspout","internally","production","inequality","laboratory"," vocabulary","aggressive","reflection","apotheosis","resistance","prediction","infectious","fundraiser","department","sanitation","directions","patriotism","forgetting","acceptance","evaluation","comparison","motorcycle","undeniable","evacuation","excellence","attraction","gracefully","allegiance","playground","aggravated","possession","creativity","annihilate","brightness","contagious","invitation","acceptable","hypothesis","cleverness","remarkable","attractive","victorious","disneyland","prosperity","bitterness","experience","submission","accusation","aggression","oppression","generosity","experiment","corruption","foundation","atmosphere","practicing","historical","medication","bottomless","temptation","republican","statistics","sweetheart","tournament","automobile","invincible","apostrophe","separation","revelation","infinitive","weatherman","appetizing","cheesecake","connection","snorkeling","graduation","disturbing","chalkboard","convention","apprentice","endangered","counseling","threatened","wilderness","motivation","management","rainforest","girlfriend","trampoline","resolution","vegetables","accountant","expression","earthquake","protection"," individual","innovation","gymnastics","excitement","elementary","conference","accomplish","accounting","speechless","compliment","appearance","difference","accelerate","everywhere","breathless","disposable","technology","watermelon","appreciate","relaxation","government","abominable","strawberry","friendship","punishment","loneliness","university","cinderella","confidence","restaurant","blackboard","discipline","helicopter","generation","skateboard","understand","leadership","california","everything","basketball","weathering","characters","literature","perfection","volleyball","wilderness","relinquish","decoration","expression","television","excitement","assessment","generation","instrument","revolution","corruption","excavation","retirement","conspiracy","dictionary","pedestrian"]
        specialWord=(wordList[random.randint(0,len(wordList))])
        guessedList=["_","_","_","_","_","_","_","_","_","_"]
        goodbyesList=["Bye","See you later","Toodles","So long","Thanks for playing"]
        playAgainList=["Great!","Awesome!","OK let's play again","Ready for another round?","Let's play!"]
        winList=["Great Job!","Nice!","Congrats!","Awesome Job","Terrific!"]
        loseList=["Better luck next time.","Aw man.","Tough luck.","That's unfortunate.","You lose."]
        againList=["Do you want to play again? ","Are you up for one more try? ","Want to give it another go? ","Another puzzle? ","Want to go another game? "]
        letterList=[]
        x=0
        y=0
        z=0
        print(" ".join(guessedList))
        while x<=9:
            letter=input("What is the  #"+str(y+1)+" letter you want to guess? You have already guessed "+", ".join(letterList)+" (all lowercase) ")
            y=y+1
            letterList.append(letter)
            if letter in specialWord:
                pass
            else:
                z=z+1
                print("There is no "+letter+" in this word")
            if letter==specialWord[0]:
                print("The first letter is "+letter)
                x=x+1
                guessedList[0]=letter
            if letter==specialWord[1]:
                print("The second letter is "+letter)
                x=x+1
                guessedList[1]=letter
            if letter==specialWord[2]:
                print("The third letter is "+letter)
                x=x+1
                guessedList[2]=letter
            if letter==specialWord[3]:
                print("The fourth letter is "+letter)
                x=x+1
                guessedList[3]=letter
            if letter==specialWord[4]:
                print("The fifth letter is "+letter)
                x=x+1
                guessedList[4]=letter
            if letter==specialWord[5]:
                print("The sixth letter is "+letter)
                x=x+1
                guessedList[5]=letter
            if letter==specialWord[6]:
                print("The seventh letter is "+letter)
                x=x+1
                guessedList[6]=letter
            if letter==specialWord[7]:
                print("The eighth letter is "+letter)
                x=x+1
                guessedList[7]=letter
            if letter==specialWord[8]:
                print("The ninth letter is "+letter)
                x=x+1
                guessedList[8]=letter
            if letter==specialWord[9]:
                print("The tenth letter is "+letter)
                x=x+1
                guessedList[9]=letter
            if z==0:
                print(" _____    ")
                print("|     |   ")
                print("|         ")
                print("|         ")
                print("|         ")
                print("|         ")
                print("|         ")
                print("|         ")
                print("|         ")
                print("|         ")
                print("|         ")
                print("|         ")
                print("|_________")
            elif z==1:
                print(" _____    ")
                print("|    _|   ")
                print("|   / \   ")
                print("|  |   |  ")
                print("|   \_/   ")
                print("|         ")
                print("|         ")
                print("|         ")
                print("|         ")
                print("|         ")
                print("|         ")
                print("|         ")
                print("|_________")
            elif z==2:
                print(" _____   ")
                print("|    _|  ")
                print("|   / \  ")
                print("|  |   | ")
                print("|   \_/  ")
                print("|    |   ")
                print("|    |   ")
                print("|    |   ")
                print("|    |   ")
                print("|    |   ")
                print("|        ")
                print("|        ")
                print("|_______ ")
            elif z==3:
                print(" _____   ")
                print("|    _|  ")
                print("|   / \  ")
                print("|  |   | ")
                print("|   \_/  ")
                print("|    |  /")
                print("|    | / ")
                print("|    |/  ")
                print("|    |   ")
                print("|    |   ")
                print("|        ")
                print("|        ")
                print("|_______ ")
            elif z==4:
                print(" _____   ")
                print("|    _|  ")
                print("|   / \  ")
                print("|  |   | ")
                print("|   \_/  ")
                print("| \  |  /")
                print("|  \ | / ")
                print("|   \|/  ")
                print("|    |   ")
                print("|    |   ")
                print("|        ")
                print("|        ")
                print("|_______ ")
            elif z==5:
                print(" _____   ")
                print("|    _|  ")
                print("|   / \  ")
                print("|  |   | ")
                print("|   \_/  ")
                print("| \  |  /")
                print("|  \ | / ")
                print("|   \|/  ")
                print("|    |   ")
                print("|    |   ")
                print("|     \  ")
                print("|      \ ")
                print("|_______\ ")
                      
            elif z==6:
                print(" _____   ")
                print("|    _|  ")
                print("|   / \  ")
                print("|  |   | ")
                print("|   \_/  ")
                print("| \  |  /")
                print("|  \ | / ")
                print("|   \|/  ")
                print("|    |   ")
                print("|    |   ")
                print("|   / \  ")
                print("|  /   \ ")
                print("|_/_____\ ")
            print(" ".join(guessedList))
            if x==10:
                print(winList[random.randint(0,4)]+" You win! The word was "+specialWord)
                again=input("Do you want to play again? ")
                if again=="no":
                    n=1
                    print(goodbyesList[random.randint(0,4)])
                else:
                    n=0
                    print(playAgainList[random.randint(0,4)])
            elif z==6:
                x=20
                print(loseList[random.randint(0,4)]+" The word was "+specialWord)
                again=input(againList[random.randint(0,4)])
                if again=="no":
                    n=1
                    print(goodbyesList[random.randint(0,4)])
                else:
                    n=0
                    print(playAgainList[random.randint(0,4)])
                    
main()
