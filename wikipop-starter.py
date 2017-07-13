"""
 Sample code for SI 507 Waiver Assignment
 University of Michigan School of Information

 Based on "Pygame base template for opening a window" 
     Sample Python/Pygame Programs
     Simpson College Computer Science
     http://programarcadegames.com/
     http://simpson.edu/computer-science/
 
See README for the assignment for instructions to complete and submit this.
"""
 
import pygame
import wikipedia
import nltk 
from nltk.tag import *
import sys
import requests
import json
import re
import random

#accepting command line arguments
query_terms_list = sys.argv[1:]
query_terms = ''.join(query_terms_list)

#create url
def create_url(baseurl, params_d):
	res = []
	for k in params_d:
			res.append("{}={}".format(k, params_d[k]))
	return baseurl + "&".join(res)

#cache 
CACHE_FNAME = "C:/Users/user/Workspaces/python/SI506waiver/waiver_cached_data.json"
try:
	cache_file = open(CACHE_FNAME, 'r')
	cache_contents = cache_file.read()
	CACHE_DICTION = json.loads(cache_contents)
	cache_file.close()
except: # But if anything doesn't work,
	CACHE_DICTION = {}

#get query result
def get_query_result(queryterms):
	baseurl = "https://en.wikipedia.org/w/api.php?"
	query_url={}
	query_url['action']="query"
	query_url['generator']="search"
	query_url['prop']="extracts"
	query_url['rvprop']="content"
	query_url['gsrsearch']= query_terms
	query_url['gsrnamespace']=0
	query_url['gsrlimit']=5
	query_url['exintro']= 1
	query_url['redirects']= 1
	query_url['format']= "json"
	unique_ident = create_url(baseurl,query_url)
	if unique_ident in CACHE_DICTION:
		print("Getting cached data...")
		return CACHE_DICTION[unique_ident]
	else:
		print("Making a request for new data...")
		# Make the request and cache the new data
		resp = requests.get(baseurl, query_url)
		CACHE_DICTION[unique_ident] = json.loads(resp.text)
		dumped_json_cache = json.dumps(CACHE_DICTION)
		fw = open(CACHE_FNAME,"w")
		fw.write(dumped_json_cache)
		fw.close() # Close the open file
		return CACHE_DICTION[unique_ident]

#remove html tags 
#############################################################################################################################
#get the filter_tags and replaceCharEntity from https://gist.github.com/dervn/859717/15b69ef75a04489f3a517b3d4f70c7e97b39d2ec
#############################################################################################################################
def filter_tags(htmlstr):
    re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) 
    re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)
    re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)
    re_br=re.compile('<br\s*?/?>')
    re_h=re.compile('</?\w+[^>]*>')
    re_comment=re.compile('<!--[^>]*-->')
    s=re_cdata.sub('',htmlstr)
    s=re_script.sub('',s) 
    s=re_style.sub('',s)
    s=re_br.sub('\n',s)
    s=re_h.sub('',s) 
    s=re_comment.sub('',s)
    blank_line=re.compile('\n+')
    s=blank_line.sub('\n',s)
    s=replaceCharEntity(s)
    return s


def replaceCharEntity(htmlstr):
    CHAR_ENTITIES={'nbsp':' ','160':' ',
                'lt':'<','60':'<',
                'gt':'>','62':'>',
                'amp':'&','38':'&',
                'quot':'"','34':'"',}
    
    re_charEntity=re.compile(r'&#?(?P<name>\w+);')
    sz=re_charEntity.search(htmlstr)
    while sz:
        entity=sz.group()#entity全称，如&gt;
        key=sz.group('name')#去除&;后entity,如&gt;为gt
        try:
            htmlstr=re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1)
            sz=re_charEntity.search(htmlstr)
        except KeyError:
            #以空串代替
            htmlstr=re_charEntity.sub('',htmlstr,1)
            sz=re_charEntity.search(htmlstr)
    return htmlstr

def repalce(s,re_exp,repl_string):
    return re_exp.sub(repl_string,s)
##################################################################################################################################   

#make the query results looks like {"h": ["happy", "had"], "b": ["ball", "bat"]}
query_result= get_query_result(query_terms)
query_result_articleonly = []
for a_page in query_result['query']['pages']:
	query_result_articleonly.append(query_result['query']['pages'][a_page]['extract'])
results = filter_tags("".join(query_result_articleonly))

tagged_sent = pos_tag(results.split())
#print(tagged_sent)
adjs = [word for word,pos in tagged_sent if pos == 'JJ' or pos=='JJR' or pos=="JJS"]
#print(adjs)
freq_adjs=nltk.FreqDist(adjs)
freq_pair_list=freq_adjs.most_common(6)
freq_adj_list=[]
for a_freq_adj in freq_pair_list:
	freq_adj_list.append(a_freq_adj[0])
#print(freq_adj_list)
freq_adj_firs=[]
for a_fir in freq_adj_list:
	freq_adj_firs.append(a_fir[0])
freq_adj_firs=set(freq_adj_firs)
word_dict={}
for a_fir in freq_adj_firs:
	alist=[]
	for a_word in freq_adj_list:
		if a_fir==a_word[0]:
			alist.append(a_word)
			word_dict[a_fir]=alist


#pygame part			
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# The class that manages the balls shown on the screen in the game.
class BallManager:

    INIT_SPEED = 1
    current_index = 0

    def __init__(self):
        self.max_balls = 6
        self.active_balls = []
        for w in freq_adj_list: 
            self.active_balls.append(WordBall(w, self.INIT_SPEED))


    def create_ball(self, word):
        self.active_balls.append(WordBall(word, self.INIT_SPEED))
	
#write del_ball function
    def del_ball(self, word):
    	for b in self.active_balls:
    		if b.word==word:
    			self.active_balls.remove(b)
    	#self.active_balls.remove(WordBall(word, self.INIT_SPEED))

    def num_balls(self):
        return len(self.active_balls)

    def __str__(self):
        s = ''
        for b in self.active_balls:
            s += b.word + ", "
        return s


class WordBall:

    def __init__(self, word, speed):
        self.word = word
        self.x_pos = random.randint(0, pygame.display.Info().current_w)
        self.y_pos = 0
        self.height = 100
        self.width = 100
        self.speed = speed

    def move_ball(self):
        self.y_pos += self.speed
        if (self.y_pos > pygame.display.Info().current_h - self.height):
            self.y_pos = 0


# Initialize game
pygame.init()

size = (1000, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Type the first letters of words to win")
clock = pygame.time.Clock()

ball_manager = BallManager()
ball_font = pygame.font.Font(None, 36)
keys_font = pygame.font.Font(None, 60)
done = False
game_over = False
keys_typed = ''

# Main display loop
while not done:
    
    # Handle input events.
    key = ''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            key = event.unicode
            keys_typed += key
            if key in freq_adj_firs:
            	for i in list(range(0,len(word_dict[key]),1)):
            		ball_manager.del_ball(word_dict[key][i])


    if ball_manager.active_balls==[]:
    	done=True

    # Manipulate game objects.
    for b in ball_manager.active_balls:
        b.move_ball()


    # Blank the screen
    screen.fill(WHITE)

    # Render game objects
    for ball in ball_manager.active_balls:
        pygame.draw.ellipse(screen, RED, [ball.x_pos, ball.y_pos, ball.width, ball.height]) 
        text = ball_font.render(ball.word, 1, BLACK)
        textpos = text.get_rect()
        textpos.centerx = ball.x_pos + ball.width / 2
        textpos.centery = ball.y_pos + ball.height / 2
        screen.blit(text, textpos)

 
    text = keys_font.render('keys typed: ' + keys_typed, 1, GREEN)
    textpos = text.get_rect()
    textpos.centerx = pygame.display.Info().current_w / 2
    textpos.centery = pygame.display.Info().current_h - 30
    screen.blit(text, textpos)


    # Update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)


if done:
	screen.fill(BLACK)
	end_text=keys_font.render('Game Over', 1, RED)
	end_textpos = end_text.get_rect()
	screen.blit(end_text,end_textpos)
	pygame.display.flip()
	clock.tick(1)



# Close the window and quit.
#pygame.quit()   
