import tkinter as tk
import random
import math

root = tk.Tk()
root.title("AI Listening and Speaking Animation")
root.geometry("800x600")

canvas = tk.Canvas(root, width=800, height=600, bg="black")
canvas.pack()

circle_radius = 150
circle_pos = (400, 300)
pulse_speed = 0.1
angle = 0
scale_factor = 1.0

bubbles = []
num_bubbles = 50

particles = []
num_particles_listening = 100
num_particles_speaking = 300

is_speaking = False

class Bubble:
    def __init__(self):
        self.angle = random.uniform(0, 2 * math.pi)
        self.size = random.randint(5, 10)
        self.speed = random.uniform(0.02, 0.05)
        self.color = random.choice(["#0066ff", "#00ccff", "#ffffff"])

    def move(self):
        self.angle += self.speed

    def draw(self):
        radius = circle_radius * scale_factor
        x = circle_pos[0] + radius * math.cos(self.angle)
        y = circle_pos[1] + radius * math.sin(self.angle)
        canvas.create_oval(
            x - self.size, y - self.size,
            x + self.size, y + self.size,
            fill=self.color, outline=""
        )

class Particle:
    def __init__(self):
        self.x = circle_pos[0]
        self.y = circle_pos[1]
        self.size = random.randint(2, 5)
        self.color = random.choice(["#0066ff", "#00ccff"])
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 3)

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.size -= 0.1

    def draw(self):
        canvas.create_oval(
            self.x - self.size, self.y - self.size,
            self.x + self.size, self.y + self.size,
            fill=self.color, outline=""
        )

def draw_animated_circle():
    global angle, bubbles, particles, is_speaking, scale_factor

    canvas.delete("all")

    if is_speaking:
        scale_factor = 1 + 0.1 * math.sin(angle)
        angle += pulse_speed
    else:
        scale_factor = 1.0

    canvas.create_oval(
        circle_pos[0] - circle_radius, circle_pos[1] - circle_radius,
        circle_pos[0] + circle_radius, circle_pos[1] + circle_radius,
        outline="", width=2, fill=""
    )

    if len(bubbles) < num_bubbles:
        bubbles.append(Bubble())

    for bubble in bubbles[:]:
        bubble.move()
        bubble.draw()

    num_particles = num_particles_speaking if is_speaking else num_particles_listening
    if len(particles) < num_particles:
        particles.append(Particle())

    for particle in particles[:]:
        particle.move()
        particle.draw()
        if particle.size <= 0:
            particles.remove(particle)

    mode_text = "Speaking Mode" if is_speaking else "Listening Mode"
    canvas.create_text(
        400, 50, text=mode_text, font=("Arial", 24), fill="white"
    )

    root.after(20, draw_animated_circle)

def toggle_speaking_mode():
    global is_speaking
    is_speaking = not is_speaking
    print("Speaking Mode:", is_speaking)

toggle_button = tk.Button(root, text="Toggle Speaking Mode", command=toggle_speaking_mode)
toggle_button.pack()

draw_animated_circle()

root.mainloop()