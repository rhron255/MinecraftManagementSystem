# MinecraftManagementSystem
The goal of this system is essentially to allow easy server creation on the fly, on an underlying kubernetes cluster (with stateful sets), with a simple yet comprehensive UI.
After supporting vanilla servers, the next goal would be to create forge server support, with droppable mods through the UI.

## Tech Stack
In an attempt to broaden my knowledge, I decided to build the frontend in React and Next.js. As for the backend, I'm debating between Java\Spring to make this easier, or to learn something new like go or rust, or maybe play aroudn with django in python.
As for the infrastructure, the idea I had was to build an image on demand for each version requested by the user, so I can experiment with a docker builder image, creating jobs and setting up a docker repository inside the cluster (maybe).