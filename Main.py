import pgzrun
import random

#add test comment

box_size = 32
border_height = 16
border_width = 16
planet = []
WIDTH = box_size * border_width
HEIGHT = box_size * border_height

mod = "menu" 

computer = Actor("computer")
generator = Actor("generator")
menu = Actor("screen")
research = Actor("researchfon")
energy_icon = Actor("energy", pos = (115, 170))
heat_icon = Actor("heatlevel", pos = (115, 240))
start = Actor("start", pos = (256, 300))
radar_icon = Actor("radaricon", pos = (300, 300))
back_arrow = Actor("back", pos = (390, 170))
generator_research = Actor("generator", pos = (50, 256))
generator_research2 = Actor("generator", pos = (450, 256))
solar_panel_research = Actor("solarpanel", pos = (200, 256))
wire_research = Actor("wires", pos = (200, 306))
circut_research = Actor("circut", pos = (200, 356))
energy_box_research = Actor("energybox", pos = (200, 206))
battery_research = Actor("battery", pos = (200, 156))
battery_research_test = Actor("radar", pos = (200, 156))
green_choice_research = Actor("radar", pos = (325, 256))

research_list = [Actor("radar", pos = (200, 156)), 
                 Actor("radar", pos = (200, 156)), 
                 Actor("radar", pos = (200, 156)), 
                 Actor("radar", pos = (200, 156)), 
                 Actor("radar", pos = (200, 156))]

research_cell = ["researchdownload1", "researchdownload2", "researchdownload1", "researchdownload2"]

computer.left = 0
computer.top = (border_height - 3) * box_size
generator.left = 7 * 32
generator.top = 7 * 32

heat_waves = random.randint(20, 70)
heat_random = random.randint(-150, 150)
asteroid = random.randint(2, 10)
virus = random.randint(30, 120)

max_heat = 1000
heat = 100
max_energy = 60
energy = 60
radar_unlocked = True
max_radar = 20
radar = 0
research_cell_gone = True

def research_window():
    screen.draw.filled_rect(Rect((170, 156), (5, 200)), (0,0,0))
    screen.draw.filled_rect(Rect((225, 156), (5, 200)), (0,0,0))
    screen.draw.filled_rect(Rect((270, 206), (5, 100)), (0,0,0))
    screen.draw.filled_rect(Rect((370, 206), (5, 105)), (0,0,0))
    screen.draw.filled_rect(Rect((50, 256), (150, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((170, 156), (60, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((170, 206), (60, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((170, 256), (100, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((170, 306), (60, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((170, 356), (60, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((270, 206), (100, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((270, 306), (100, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((370, 256), (50, 5)), (0,0,0))

    generator_research.draw()
    generator_research2.draw()
    solar_panel_research.draw()
    wire_research.draw()
    circut_research.draw()
    energy_box_research.draw()
    battery_research.draw()
    green_choice_research.draw()

    for i in range(len(research_list)):
        if research_true[i] == True:    
            research_list[i].draw()


research_time = [8, 12, 12, 20, 20]
research_names = ["battery", "energy_box", "solar_panel", "wires", "circut"]
research_true = [False, False, False, False, False]
research_level = "green"
research_status = False
research_number = -1
research_timer_amount = 0


def create_map():
    for i in range(border_height):
        row = []
        for j in range(border_width):
            row.append("rocktexture")
        planet.append(row)

create_map()
print(planet)

def heat_time():
    global heat
    heat += 50

clock.schedule_interval(heat_time, 60)

def draw_map():
    for i in range(border_height):
        for j in range(border_width):
            box = Actor(planet[i][j])
            box.left = i * box_size
            box.top = j * box_size
            box.draw()

def draw_energy():
    global energy, max_energy

    cost = max_energy // 20
    energy_icon.draw()
    for i in range(20):
        emptycell = Actor("emptycell", pos = (115 + 31 + 11 * i, 170))
        emptycell.draw()
    for i in range(int(energy) // cost):
        cell = Actor("cell", pos = (115 + 31 + 11 * i, 170))
        cell.draw()

def draw_heat():
    global max_heat, heat_waves, heat_random, heat
    cost = max_heat // 20
    heat_icon.draw()
    for i in range(20):
        emptycell = Actor("emptycell", pos = (115 + 31 + 11 * i, 240))
        emptycell.draw()
    heat_temp = min(heat + heat_random, max_heat)
    for i in range(int(heat_temp) // cost):
        cell = Actor("cell", pos = (115 + 31 + 11 * i, 240))
        cell.draw()
    
def draw_radar():
    global radar, radar_unlocked, radar_icon

    if radar_unlocked == True:
        cost = max_radar // 20
        radar_icon.draw()
        for i in range(20):
            emptycell = Actor("emptycell", pos = (115 + 31 + 11 * i, 240))
            emptycell.draw()
        for i in range(int(heat) // cost):
            cell = Actor("cell", pos = (115 + 31 + 11 * i, 240))
            cell.draw()

def draw_research_process():
    global research_timer_amount, research_number

    cost =  research_time[research_number] // 4
    research_count = research_timer_amount // cost
    for i in range(research_count):
        cell = Actor(research_cell[i], pos = (188 + i * 8,156 + research_number * 50 ))
        cell.draw()

def draw():
    global mod, research_status

    if mod == "game":
        draw_map()
        computer.draw()
        generator.draw()
    elif mod == "menu":
        menu.draw()
        start.draw()
    elif mod == "screen":
        menu.draw()
        draw_energy()
        draw_heat()
        #draw_radar()
        back_arrow.draw()
    elif mod == "research":
        research.draw()
        back_arrow.draw()
        research_window()
        if research_status == True:
            draw_research_process()

def research_prosses():
    global research_number, research_status, research_timer_amount, research_cell_gone
    
    if research_cell_gone == False:
        research_status = False
        research_cell_gone = True
    print(research_timer_amount)
    if research_status == True:
        research_timer_amount += 1
        if research_timer_amount == research_time[research_number]:
            #research_status = False
            research_cell_gone = False
            research_true[research_number] = True

clock.schedule_interval(research_prosses, 1)

def research_update(button, pos):
    global research_number, research_status, research_timer_amount

    if battery_research.collidepoint(pos):  
        if research_number != 0:
            research_timer_amount = 0
        research_number = 0
        research_status = True
       
    elif energy_box_research.collidepoint(pos):
        if research_number != 1:
            research_timer_amount = 0
        research_number = 1
        research_status = True

def update(dt):
    pass

def on_mouse_down(button, pos):
    global mod

    if mod == "screen" and back_arrow.collidepoint(pos):
        mod = "game"
    
    if mod == "research" and back_arrow.collidepoint(pos):
        mod = "game"
    
    if mod == "research":
        research_update(button, pos)

    if mod == "menu" and start.collidepoint(pos):
        mod = "game"

    if mod == "game" and computer.collidepoint(pos):
        mod = "screen"

    if mod == "game" and generator.collidepoint(pos):
        mod = "research"

def on_colliderect():
    pass


pgzrun.go()