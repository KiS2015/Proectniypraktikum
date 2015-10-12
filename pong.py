import simpleguitk as simplegui
import random, math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
PAD_WIDTH = 8
PAD_HEIGHT = 80
BALL_RADIUS = 10

# helper function that spawns a ball by updating the ball's position vector
# and velocity vector if right is True, the ball's velocity is upper right, else upper left
def ball_init(right=True):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [random.randrange(2,5),random.randrange(-2,4)]


def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    c.draw_text(str(score1),(20,100),40, "Red")
    c.draw_text(str(score2),(WIDTH-50,100),40, "Red")
    ball_pos[0]+= ball_vel[0]
    ball_pos[1]+= ball_vel[1]

    if abs(HEIGHT-ball_pos[1])<=BALL_RADIUS:
        ball_vel[1]*=-1
    elif abs(ball_pos[1])<=BALL_RADIUS:
        ball_vel[1]*=-1.2

    elif ball_pos[0]<=BALL_RADIUS+PAD_WIDTH/2:
        if paddle1_pos-PAD_HEIGHT/2<=ball_pos[1]<=paddle1_pos+PAD_HEIGHT/2:
            ball_vel[0]*=-1
        else:
            score2+=1
            ball_init(True)

    elif abs(ball_pos[0])>=WIDTH-PAD_WIDTH-BALL_RADIUS:
        if paddle2_pos-PAD_HEIGHT/2<=ball_pos[1]<=paddle2_pos+PAD_HEIGHT/2:
            ball_vel[0]*=-1.2
        else:
            score1+=1
            ball_init(False)




    paddle1_pos += paddle1_vel
    if (paddle1_pos-(PAD_HEIGHT/2))<0:
        paddle1_pos =PAD_HEIGHT/2
    elif (paddle1_pos+(PAD_HEIGHT/2))>HEIGHT:
        paddle1_pos =HEIGHT-PAD_HEIGHT/2

    paddle2_pos += paddle2_vel
    if (paddle2_pos-(PAD_HEIGHT/2))<0:
        paddle2_pos =PAD_HEIGHT/2
    elif (paddle2_pos+(PAD_HEIGHT/2))>HEIGHT:
        paddle2_pos =HEIGHT-PAD_HEIGHT/2

    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")

    c.draw_line([(PAD_WIDTH/2),(paddle1_pos)+(PAD_HEIGHT/2)],[(PAD_WIDTH/2),(paddle1_pos)-(PAD_HEIGHT/2)], PAD_WIDTH, "White")
    c.draw_line([WIDTH,(paddle2_pos)+(PAD_HEIGHT/2)],[WIDTH,(paddle2_pos)-(PAD_HEIGHT/2)], PAD_WIDTH, "White")

    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "Blue")
    c.draw_line([WIDTH-PAD_WIDTH, 0],[WIDTH-PAD_WIDTH, HEIGHT], 1, "Green")

    # draw paddles

    # update ball

    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 0.1, "White", "Red")

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP['W']:
        paddle1_vel=-5
    elif key==simplegui.KEY_MAP['S']:
        paddle1_vel=5

    elif key==simplegui.KEY_MAP['Up']:
        paddle2_vel=-5
    elif key==simplegui.KEY_MAP['Down']:
        paddle2_vel=5


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP['W']:
        paddle1_vel=0
    elif key==simplegui.KEY_MAP['S']:
        paddle1_vel=0

    elif key==simplegui.KEY_MAP['Up']:
        paddle2_vel=0
    elif key==simplegui.KEY_MAP['Down']:
        paddle2_vel=0

def restart():
    global score1, score2
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global side
    paddle1_vel = 0
    paddle2_vel = 0

    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2

    score1, score2 = 0, 0

    ball_init()


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)

score1, score2 = 0, 0
restart()

# start frame
frame.start()