import random

class DDZ:

    def __init__(self):
    
        # ID for every card
        # Will be used in one-hot encode
        self.total_cards_id = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,  
                19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,  
                36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53]

        # Dictionary for Card ID
        self.card_dic=dict([(0,'方片3'),(1,'梅花3'),(2,'红桃3'),(3,'黑桃3'),  
               (4,'方片4'),(5,'梅花4'),(6,'红桃4'),(7,'黑桃4'),  
               (8,'方片5'),(9,'梅花5'),(10,'红桃5'),(11,'黑桃5'),  
               (12,'方片6'),(13,'梅花6'),(14,'红桃6'),(15,'黑桃6'),  
               (16,'方片7'),(17,'梅花7'),(18,'红桃7'),(19,'黑桃7'),  
               (20,'方片8'),(21,'梅花8'),(22,'红桃8'),(23,'黑桃8'),  
               (24,'方片9'),(25,'梅花9'),(26,'红桃9'),(27,'黑桃9'),  
               (28,'方片10'),(29,'梅花10'),(30,'红桃10'),(31,'黑桃10'),  
               (32,'方片J'),(33,'梅花J'),(34,'红桃J'),(35,'黑桃J'),  
               (36,'方片Q'),(37,'梅花Q'),(38,'红桃Q'),(39,'黑桃Q'),  
               (40,'方片K'),(41,'梅花K'),(42,'红桃K'),(43,'黑桃K'),  
               (44,'方片A'),(45,'梅花A'),(46,'红桃A'),(47,'黑桃A'),  
               (48,'方片2'),(49,'梅花2'),(50,'红桃2'),(51,'黑桃2'),  
               (52,'BlackJoker'),(53,'RedJoker')])

        # Previous Round Cards
        self.prev_hand = []
        self.prev_player = ''

        # status = 0 when still gaming
        # status = 1 when the lord win
        # status = -1 when the farmer win
        self.status = 0

        #Shuffle Cards
        random.shuffle(self.total_cards_id)

        self.alpha_cards = self.total_cards_id[:20]
        self.beta_cards = self.total_cards_id[20:37]
        self.gamma_cards = self.total_cards_id[37:] 

    def cards_type(self, group):
        # Sort the group of cards
        group.sort()

        # CONDITIONS BEGIN
        if len(group) == 1:
            return 'single'

        elif len(group) == 2:
            if group[0] == group[1]:
                return 'double'

            elif group[0] == 'bj' or group[0] == 'rj':
                return 'kbomb'

            else:
                return 'false'

        elif len(group) == 3:
            if group[0] == group[1] == group[2]:
                return 'triple'
            
            else:
                return 'false'

        elif len(group) == 4:
            if group[0] == group[1] == group[2] == group[3]:
                return 'bomb'

            elif group[0] == group[1] == group[2] != group[3] or group[1] == group[2] == group[3] != group[0]:
                return 'triple+1'
            
            else:
                return 'false'

        elif len(group) == 5:
            if group[4] == group[3] + 1 == group[2] + 2 == group[1] + 3 == group[0] + 4:
                return 'shunzi*5'
            
            elif group[0] == group[1] == group[2] != group[3] == group[4] or group[2] == group[3] == group[4] != group[0] == group[1]:
                return 'triple+2'

            else:
                return 'false'

        elif len(group) == 6:
            if group[5] == group[4] + 1 == group[3] + 2 == group[2] + 3 == group[1] + 4 == group[0] + 5:
                return 'shunzi*6'

            elif group[0] == group[1] == group[2] == group[3] != group[4] == group[5] or group[2] == group[3] == group[4] == group[5] != group[0] == group[1]:
                return 'four+2'
                
            else:
                return 'false'
        
        # CONDITIONS END
        else:
            return 'false'
                
                


    # CARDS POLICIES
    def filter(self, prev_cards, holded_cards):

        groups = {
            '0':'3', '1':'3', '2':'3', '3':'3',
            '4':'4', '5':'4', '6':'4', '7':'4',
            '8':'5', '9':'5', '10':'5', '11':'5',
            '12':'6', '13':'6', '14':'6', '15':'6',
            '16':'7', '17':'7', '18':'7', '19':'7',
            '20':'8', '21':'8', '22':'8', '23':'8',
            '24':'9', '25':'9', '26':'9', '27':'9',
            '28':'10', '29':'10', '30':'10', '31':'10',
            '32':'11', '33':'11', '34':'11', '35':'11',
            '36':'12', '37':'12', '38':'12', '39':'12',
            '40':'13', '41':'13', '42':'13', '43':'13',
            '44':'1', '45':'1', '46':'1', '47':'1',
            '48':'2', '49':'2', '50':'2', '51':'2',
            '52':'bj','53':'rj'
        }

        # Single Card
        if len(prev_cards) == 1:
            group = groups[prev_cards]
            #TODO ADD POLICY HERE
            #available_actions = 
        
        #TODO ADD CONDITIONS HERE


    # Discard Function for all players
    def discard(self, cards_id, player):
        for index,cards in enumerate(self.cards):
            if cards in cards_id:
                del self.cards[index]
  
        # Update the Previous Round Cards
        self.prev_hand = cards_id

        # Update the Previous Round Player
        self.prev_player = player
    
# alpha is the lord
class alpha(DDZ):
    def __init__(self):
        self.cards = DDZ().alpha_cards
    
    def status_check(self):
        if len(self.cards) == 0:
            self.status = 1


# beta is the player after the lord
class beta(DDZ):
    def __init__(self):
        self.cards = DDZ().beta_cards

    def status_check(self):
        if len(self.cards) == 0:
            self.status = -1
            


# gamma is the player before the lord
class gamma(DDZ):
    def __init__(self):
        self.cards = DDZ().gamma_cards
    
    def status_check(self):
        if len(self.cards) == 0:
            self.status = -1
