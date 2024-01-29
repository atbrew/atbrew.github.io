---
layout: post
title:  "Push yourself outside your comfort zone"
date:   2024-01-24 10:00:40
blurb: "Pushing yourself beyond your boundaries"
og_image: /assets/img/content/chess/chess_wide.png
published: true
---

<img src="{{ "/assets/img/content/chess/chess_wide.png" | absolute_url }}" alt="Liffey swim" class="post-pic"/>
<br />
<br />

One of [my goals](/about/#my-goals) for 2024 is to blog 4 blog worthy projects. This is to stretch myself beyond my comfort zone and to learn something fun along the way. I've also always had an itch to "build something" real, tangible and touchable that uses software. The stars have beeb alligning for this project I feel. A spanish colleague before Christmas, convinced me that what (ahem) my kids needed was a 3-d printer.  

The lego set I loved the most as a child was obviously lego technic, and of the sets I recall most vividly was probably the simplist to build; a 2d plotter. I'm also always looking for projects where I can get the kids involed and excited. Now comes the last bit of the puzzle. My eldest son Ryan has got a fondness for chess, to the point I just don't have a hope at beating him.

This leads me to my first project codenamed "Daddy". I'm going to try to build an automated chess board inspired by [square off](https://amzn.to/3SayIak). I intend to print component parts (I might end up buying them) to build a 2d plotter that will be controlled by a raspberry pi. On the arm instead of a pen I will put an electromagnet that will operate the chess peices from the underside of the board. Ive heard of hall efect transistors that will be able to identify where the pieces are lifted and placed down.

Now Ryan will be able to play against Daddy, and should I play against him I will have a button aptly named "what would Daddy do" to help me play the best move given my current position. 

# Ask the Robot overlorsd for a plan!
Let's use chat GPT to help me come up with a project plan 

```
I want to build an automated chess board like the one at square off grand kingdom set https://squareoffnow.com/product/gks 

I have the following 
- a raspberry pi 5 
- a anycubic photon 3d printer 

My plan is to build a 2d plotter with an electromagnet that will move the chess peices rom under to board. The postion of the magnets on the board will be determined using what I think are efred to as hall effect transistors. 

I'm happy to buy some parts, like linear rails, servos and belts, but would like to print as much as I can. 

My knowledge is light on the following 
- controlling electronics with a raspberry pi 
- compouter aided design for printing 3d parts 
- I need a refresher on electronics 

I want to build a plan, that I can do this as a side project. 

I would like to have a goal for each week one by one (i.e. week 1 : don X week 2 do Y).  

I can devote 8-10 hours per week building and coding. 
I want like each individual weeks goal to be something clear and specific. 

For example "learn the fundaments required to to build the electric circuit that will be used to programtically power the motors". 

All the weekly goals should group up towards completeing the overall project. 

Using the above please ask me any clarifying questions and then formulate a plan we can revise

``` 
It asked me some follow-up questions and then came up with this plan

### Chat GPT Plan 

Based on your responses, I'll craft a structured plan that balances learning and hands-on work, and is suitable for blogging about your progress. Given your goals and the time you can devote each week, I'll outline a 12-week plan. This plan assumes a progressive learning curve, starting with basics and moving towards more complex tasks.

# Week 1: Introduction to Raspberry Pi GPIO and Basic Electronics
- **Goal:** Learn the basics of Raspberry Pi GPIO (General Purpose Input Output) pins and basic electronics concepts.
- **Tasks:**
  - Study Raspberry Pi GPIO pin layout and basic usage.
  - Refresh basic electronics knowledge, focusing on concepts like current, voltage, resistance, and how transistors work (especially MOSFETs for your electromagnet control).
- **Resources:** Raspberry Pi documentation, online electronics tutorials.

# Week 2: Exploring Servos and Stepper Motors
- **Goal:** Understand different types of motors and how to control them with Raspberry Pi.
- **Tasks:**
  - Learn about servos and stepper motors, including how they are controlled.
  - Experiment with a simple motor circuit using Raspberry Pi.
- **Resources:** Online tutorials, Raspberry Pi motor control projects.

# Week 3: Introduction to CAD for 3D Printing
- **Goal:** Get familiar with Computer-Aided Design (CAD) for 3D printing.
- **Tasks:**
  - Choose and learn the basics of a CAD software (like Fusion 360 or Tinkercad).
  - Design a simple object to 3D print.
- **Resources:** Online CAD tutorials, 3D printing forums.

# Week 4: Hall Effect Sensors and Electronics Integration
- **Goal:** Learn about Hall effect sensors and start integrating electronics.
- **Tasks:**
  - Study Hall effect sensors and their usage in detecting magnetic fields.
  - Experiment with a Hall effect sensor circuit with the Raspberry Pi.
- **Resources:** Sensor datasheets, Raspberry Pi sensor project guides.

# Week 5: Designing 2D Plotter Components
- **Goal:** Start designing parts for the 2D plotter.
- **Tasks:**
  - Create a basic design for the plotter's frame and moving parts.
  - Consider how the electromagnet will be integrated.
- **Resources:** Online CAD resources, existing 2D plotter designs.

# Week 6: Basic Plotter Assembly and Testing
- **Goal:** Begin assembling and testing the plotter.
- **Tasks:**
  - Print and assemble the basic frame and moving parts.
  - Test the plotter movement without the electromagnet.
- **Resources:** 3D printing communities, DIY plotter project guides.

# Week 7: Electromagnet Integration and Control
- **Goal:** Integrate the electromagnet into the plotter.
- **Tasks:**
  - Attach the electromagnet to the plotter.
  - Program the Raspberry Pi to control the electromagnet based on plotter position.
- **Resources:** Online tutorials on electromagnet control, Raspberry Pi forums.

# Week 8: Chess Piece Movement Mechanics
- **Goal:** Develop a system for moving chess pieces.
- **Tasks:**
  - Test moving a chess piece with the electromagnet.
  - Adjust the plotter and electromagnet strength as needed.
- **Resources:** Experimentation, online resources on magnetic chess sets.

# Week 9: Building a Custom Chess Board
- **Goal:** Create a chess board suitable for the project.
- **Tasks:**
  - Design and create a chess board with space underneath for the plotter.
  - Integrate Hall effect sensors into the board (if needed for position tracking).
- **Resources:** DIY chess board designs, woodworking or 3D printing resources.

# Week 10: Software Development for Chess Logic
- **Goal:** Develop software to control chess piece movement.
- **Tasks:**
  - Write a program for basic chess piece movement and rules.
  - Integrate this software with the plotter control system.
- **Resources:** Chess algorithms, Python programming resources.

# Week 11: Testing and Refining
- **Goal:** Test the entire system and refine.
- **Tasks:**
  - Conduct extensive testing of the chess board, plotter, and software.
  - Make necessary adjustments and refinements.
- **Resources:** Testing methodologies, online forums for troubleshooting.

# Week 12: Final Assembly and Documentation
- **Goal:** Complete final assembly and document the project.
- **Tasks:**
  - Assemble all parts into a final product.
  - Document the process, challenges, and solutions for your blog.
- **Resources:** Project documentation best practices, blogging platforms.

This plan should give you a structured approach to your project. Each week's goal is achievable within 8-10 hours, allowing time for both hands-on work and learning. Remember, flexibility is key; some tasks may take longer than anticipated. Good luck with your project, and enjoy the process!

Thank you AI overlord, onwards with learning!
