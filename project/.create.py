import os

names = []
for i in os.listdir("project"):
    i = i.split("-", 1)[-1].replace("-", " ")
    y = ''
    for x in i.split():
        y += x.capitalize() + " "
    y = y.strip()
    if "." not in y:
        names.append(y)

# 01-expanding-cards
# 02-progress-steps
# 03-rotating-navigation
# 04-hidden-search-widget
# 05-blurry-loading
# 06-scroll-animation
# 07-split-landing-page
# 08-form-wave-animation
# 09-sound-board
# 10-dad-jokes
# 11-event-keycodes
# 12-faq-collapse
# 13-random-choice-picker
# 14-animated-navigation
# 15-incrementing-counter
# 16-drink-water
# 17-movie-app
# 18-background-slider
# 19-theme-clock
# 20-button-ripple-effect
# 21-drag-n-drop
# 22-drawing-app
# 23-content-placeholder
# 24-kinetic-loader
# 25-sticky-navigation
# 26-double-vertical-slider
# 27-toast-notification
# 28-github-profiles
# 29-double-click-heart
# 30-auto-text-effect
# 31-password-generator
# 32-good-cheap-fast
# 33-notes-app
# 34-animated-countdown
# 35-image-carousel
# 36-hoverboard
# 37-pokedex
# 38-mobile-tab-navigation
# 39-password-strength-background
# 40-3d-boxes-background
# 41-verify-account-ui
# 42-live-user-filter
# 43-feedback-ui-design
# 44-custom-range-slider
# 45-netflix-mobile-navigation
# 46-quiz-app
# 47-testimonial-box-switcher
# 48-random-image-generator
# 49-todo-list
# 50-insect-catch-game

# Expanding Cards
# Progress Steps
# Rotating Navigation
# Hidden Search Widget
# Blurry Loading
# Scroll Animation
# Split Landing Page
# Form Wave Animation
# Sound Board
# Dad Jokes
# Event Keycodes
# Faq Collapse
# Random Choice Picker
# Animated Navigation
# Incrementing Counter
# Drink Water
# Movie App
# Background Slider
# Theme Clock
# Button Ripple Effect
# Drag N Drop
# Drawing App
# Content Placeholder
# Kinetic Loader
# Sticky Navigation
# Double Vertical Slider
# Toast Notification
# Github Profiles
# Double Click Heart
# Auto Text Effect
# Password Generator
# Good Cheap Fast
# Notes App
# Animated Countdown
# Image Carousel
# Hoverboard
# Pokedex
# Mobile Tab Navigation
# Password Strength Background
# 3d Boxes Background
# Verify Account Ui
# Live User Filter
# Feedback Ui Design
# Custom Range Slider
# Netflix Mobile Navigation
# Quiz App
# Testimonial Box Switcher
# Random Image Generator
# Todo List
# Insect Catch Game

with open('project/temp.html') as f:
    t = f.read()
index = 0
# times = 0
text = ""
for i in t.split("\n"):
    if ">Project</a" in i:
        i = i.replace("Project", names[index])
        # print(i)
        index += 1
        # times += 1
    text += i+"\n"

print(text)

# print(times)
# print(len(names))
