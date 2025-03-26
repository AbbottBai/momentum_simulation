import pygame, time
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def user_input():
    missing_field = ["N/A", 0, "N/A"]
    time.sleep(1)
    print("\nPLEASE LEAVE FIELD BLANK IF VALUE IS UNKNOWN\n")
    time.sleep(1.5)
    print("Otherwise please enter NUMBERS ONLY for the specified field\n")
    time.sleep(1)
    print("PLEASE LEAVE NO MORE THAN 1 BLANK FIELD\n")
    time.sleep(1)

    print("Please enter the mass of the bullet (kg)")
    try:
        bullet_mass = float(input(">"))
    except:
        bullet_mass = -90.09

    print("\nPlease enter the velocity of the bullet (m/s)")
    try:
        bullet_velocity = float(input(">"))
    except:
        bullet_velocity = -90.09

    print("\nPlease enter the mass of the trolley ONLY (kg), excluding the bullet")
    try:
        trolley_mass = float(input(">"))
    except:
        trolley_mass = -90.09

    print("\nPlease enter the final velocity of the trolley and bullet after collision (m/s)")
    try:
        final_velocity = float(input(">"))
    except:
        final_velocity = -90.09

    time.sleep(1)
    print("\nIF THIS IS LEFT BLANK THEN FRICTION WILL BE SET TO 0")
    time.sleep(1)
    print("""\nIF THE TROLLEY DOESNT MOVE ON SCREEN AFTER COLLISION 
    THEN THE COEFFICIENT OF FRICTION IS TOO LARGE""")
    print("\nPlease enter the coefficient of friction")
    try:
        R = float(input(">"))
    except:
        R = 0

    time.sleep(1)
    print("\nPRESS SPACE IN GRAPHICAL WINDOW IF YOU WANT TO SEE YOUR OWN INPUTS")

    # Conservation of momentum being applied here!
    if bullet_mass == -90.09:
        bullet_mass = (final_velocity * trolley_mass) / (bullet_velocity - final_velocity)
        missing_field = ["bullet mass", bullet_mass, "kg"]
    elif bullet_velocity == -90.09:
        bullet_velocity = ((trolley_mass + bullet_mass) * final_velocity) / bullet_mass
        missing_field = ["bullet velocity", bullet_velocity, "m/s"]
    elif trolley_mass == -90.09:
        trolley_mass = ((bullet_mass * bullet_velocity) / final_velocity) - bullet_mass
        missing_field = ["trolley mass", trolley_mass, "kg"]
    elif final_velocity == -90.09:
        final_velocity = (bullet_mass * bullet_velocity) / (trolley_mass + bullet_mass)
        missing_field = ["final velocity", final_velocity, "m/s"]

    f_max = 9.8 * (trolley_mass + bullet_mass) * R
    all_values = [bullet_mass, bullet_velocity, trolley_mass, final_velocity, R]

    return bullet_mass, bullet_velocity, trolley_mass, final_velocity, missing_field, f_max, all_values

bullet_mass, bullet_velocity, trolley_mass, final_velocity, missing_field,f_max, all_values = user_input()

dec = f_max/(bullet_mass + trolley_mass)

pygame.init()

clock = pygame.time.Clock()

window_size = (1200,300)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Momentum Simulation")

font = pygame.font.SysFont("Arial", 50, bold=True)
small_font = pygame.font.SysFont("Arial", 25, bold=False)
init_text_surface = font.render("Press any button to begin simulation!", True, (255, 0, 0))
init_text_rect = init_text_surface.get_rect(center=(window_size[0]//2, window_size[1]//1.2))

final_text_surface = font.render(f"The calculated {missing_field[0]} is {round(missing_field[1],5)} {missing_field[2]}", True, (0, 0, 0))
final_text_rect = final_text_surface.get_rect(center=(window_size[0]//2, window_size[1]//5.2))

if missing_field[0] == "bullet mass":
    userinput_text_surface = small_font.render(f"You entered: bullet_velocity = {bullet_velocity}, trolley mass = {trolley_mass}, final velocity = {final_velocity}, R = {all_values[4]}", True, (0, 0, 0))
    userinput_text_rect = userinput_text_surface.get_rect(center=(window_size[0] / 2, window_size[1] // 1.3))

elif missing_field[0] == "bullet velocity":
    userinput_text_surface = small_font.render(f"You entered: bullet mass = {bullet_mass}, trolley mass = {trolley_mass}, final velocity = {final_velocity}, R = {all_values[4]}", True, (0, 0, 0))
    userinput_text_rect = userinput_text_surface.get_rect(center=(window_size[0] / 2, window_size[1] // 1.3))

elif missing_field[0] == "trolley mass":
    userinput_text_surface = small_font.render(f"You entered: bullet mass = {bullet_mass}, bullet_velocity = {bullet_velocity}, final velocity = {final_velocity}, R = {all_values[4]}", True, (0, 0, 0))
    userinput_text_rect = userinput_text_surface.get_rect(center=(window_size[0] / 2, window_size[1]//1.3))

elif missing_field[0] == "final velocity":
    userinput_text_surface = small_font.render(f"You entered: bullet mass = {bullet_mass}, bullet_velocity = {bullet_velocity}, trolley mass = {trolley_mass}, R = {all_values[4]}", True, (0, 0, 0))
    userinput_text_rect = userinput_text_surface.get_rect(center=(window_size[0]/2, window_size[1]//1.3))

else:
    userinput_text_surface = small_font.render(f"You entered: bullet mass = {bullet_mass}, bullet_velocity = {bullet_velocity}, trolley mass = {trolley_mass}, final velocity = {final_velocity}, R = {all_values[4]}", True, (0, 0, 0))
    userinput_text_rect = final_text_surface.get_rect(center=(window_size[0]//3, window_size[1]//1.3))

gun_img = pygame.image.load(resource_path("gun.jpg"))
gun_size = (window_size[0]//6, (window_size[0]//6) // 3.929)
gun_img = pygame.transform.scale(gun_img, gun_size)
gun_coords = [window_size[0]//20, (window_size[1]//2) - gun_size[1]//2]

trolley_img = pygame.image.load(resource_path("trolley.jpg"))
trolley_size = (window_size[0]//6, (window_size[0]//6) // 1.394)
trolley_img = pygame.transform.scale(trolley_img, trolley_size)
trolley_coords = [window_size[0]//1.8, (window_size[1]//2) - trolley_size[1]//2]

bullet_img = pygame.image.load(resource_path("bullet.png"))
bullet_size = (window_size[0]//25, (window_size[0]//25) // 1.047)
bullet_img = pygame.transform.scale(bullet_img, bullet_size)
bullet_coords = [gun_coords[0]+gun_size[0]-15, gun_coords[1] - gun_size[1]//2 +18]

i = 61
key_pressed = False
display_userinput = False
collided = False
run = True
final_velocity += 5
bullet_velocity -= 40
trolley_velocity = final_velocity
while run:
    i += 1
    clock.tick(60)
    #print(trolley_velocity, dec)
    #print(trolley_velocity)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            key_pressed = True
            if event.key == pygame.K_SPACE and display_userinput == False:
                display_userinput = True
            elif event.key == pygame.K_SPACE and display_userinput == True:
                display_userinput = False

    window.fill((255, 255, 255))

    window.blit(gun_img, gun_coords)
    window.blit(trolley_img, trolley_coords)
    if key_pressed:
        window.blit(bullet_img, bullet_coords)
        if bullet_coords[0] + bullet_size[0] >= trolley_coords[0]+15:
            collided = True
            trolley_velocity -= dec / 60
            if display_userinput:
                window.blit(userinput_text_surface, userinput_text_rect)
            if trolley_velocity >= 0:
                bullet_coords[0] += trolley_velocity
                trolley_coords[0] += trolley_velocity
            if missing_field[0] != "N/A":
                window.blit(final_text_surface, final_text_rect)
        else:
            bullet_coords[0] += int(bullet_velocity)

    else:
        if i >= 60:
            i = -60
        elif i <= 0:
            window.blit(init_text_surface, init_text_rect)

    pygame.display.update()

pygame.quit()