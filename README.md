# Forest Run
  ## Video URL
  https://youtu.be/67AeMoJtoAo

  ## GitHub URL
  https://github.com/EliaPham/Forest-run/tree/main
  
  ## Short Description
  In this game you try to survive the longest you can. If you hit one of the many obstacles, then you will be restarted to the beginning. Be careful though! Some of the objects require a double jump to pass over it. The speed will increase as the game keeps going and adventuring the forest and the game becomes harder to do. With the increasing difficulty, it will all in all provide one with an option to restart this adventure once again.
  
  ## design considerations
  For this game consited of my very own made graphics. I used procreate to draw these graphics and experimented with pixel art to create this game. I wanted it to give off the vibe of a free indie game that you could find off of steam, and I would like to say that I think I pulled it off. I chose to go more for vibrant colors with a more blue and green undertone to more give off the bright, yet crowded forest adventure atmosphere. Also while going through the project I had realized that the obstacles I put into the game should be a very different color from what is going on in the background to ensure that the user knows what is an obstacle and what is not.
  
  ## Repositoy
  Before anything, I imported the gaming libraries I would need then I added in all of my graphics (having to resize it as well) and implemented the creen height and width. For my repositories, I used the class systems to implement my graphics into the game. The Girl class has the most controls as it it the "main character". The small log, large log, extra large log, and snail class are ground/jumping obstacles, and the vine and bird class were the air/ducking obstacles. My "Pixel_collision" function's pourpose is to provide a smaller hitbox of the collision of the girl and the objects because when resizing my graphics, it increased their hitboxes very high. In my main function, I put together everything like the score(how long the player lasts in their run), the background and foreground (which procvided the setting for which the game takes place in), and the while loop that randomizes which obstacle is to come next as well as print it out. In my menu function, it displays the instruction on how to start (by pressing any key) and also after the first play it shows the option to play aganin (with the score the player just recieved from their run).

  
  ## Areas of imporvements
  Some places Where I would like to improve would be in knowing pygame more. The project was time consuming because of the un learned stuff I have yet to learn in our class yet, but at the same time it was fun learning it. I leared how to do the pygame mask option on an image, and also how to use the pygame.transform.scale that I had not known of before. But with more practice in the future, and with the practice I got in using pygame, it will make future projects easier.
  
