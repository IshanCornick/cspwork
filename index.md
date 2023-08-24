---
layout: default
title: Student Blog
---


## About me: Ishan Cornick 
Hello welcome to my blog! My name is Ishan Cornick and I am 15 years old. I enjoy spending time with my friends, playing video games and golfing. I just started to learn coding and I hope I can learn more.

![Alt text](<images/Screenshot 2023-08-23 at 12.14.52 PM.png>)

## Fun Facts about me
1: I have a younger brother that is 2 years younger.

![Alt text](<images/Screenshot 2023-08-23 at 8.07.15 PM.png>)

2: My favorite food is steak.

<div class="tenor-gif-embed" data-postid="22080224" data-share-method="host" data-aspect-ratio="1" data-width="100%"><a href="https://tenor.com/view/dj-khaled-food-meat-beating-funny-gif-22080224">Dj Khaled Food GIF</a>from <a href="https://tenor.com/search/dj+khaled-gifs">Dj Khaled GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>

3: I lived in Masschusetts but moved here when I was 9.

![Alt text](<images/e12150731430c8a8d25cdd2eb540dd4c-cc_ft_960.jpg>)

4: My mom is Indian and my dad is American and European.

![Alt text](<images/Screenshot 2023-08-23 at 8.05.20 PM.png>)

5: My favorite celebrity is DJ Khaled.

<div class="tenor-gif-embed" data-postid="21764359" data-share-method="host" data-aspect-ratio="0.99375" data-width="80%"><a href="https://tenor.com/view/dj-khaled-dancing-dance-gif-21764359">Dj Khaled GIF</a>from <a href="https://tenor.com/search/dj-gifs">Dj GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>

6: My favorite youtuber. He helps me decompress and relax with laughter.

<iframe width="560" height="315" src="https://www.youtube.com/embed/9_KeFKnhGqU?si=2l-nJsYCqYsgawQb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## HACKS

During my time setting up my wesbite/blog there were somethings that I wished I knew before I started.


## Doodle Jump

<https://gist.github.com/straker/b96a4a68bd6d79cf75a833d98a2b654f>
<html>
<head>
  <title>Basic Doodle Jump HTML Game</title>
  <meta charset="UTF-8">
  <style>
  html, body {
    height: 100%;
    margin: 0;
  }

  body {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  canvas {
    border: 1px solid black;
  }
  </style>
</head>
<body>
<canvas width="375" height="667" id="game"></canvas>
<script>
const canvas = document.getElementById('game');
const context = canvas.getContext('2d');

// width and height of each platform and where platforms start
const platformWidth = 65;
const platformHeight = 20;
const platformStart = canvas.height - 50;

// player physics
const gravity = 0.33;
const drag = 0.3;
const bounceVelocity = -12.5;

// minimum and maximum vertical space between each platform
let minPlatformSpace = 15;
let maxPlatformSpace = 20;

// information about each platform. the first platform starts in the
// bottom middle of the screen
let platforms = [{
  x: canvas.width / 2 - platformWidth / 2,
  y: platformStart
}];

// get a random number between the min (inclusive) and max (exclusive)
function random(min, max) {
  return Math.random() * (max - min) + min;
}

// fill the initial screen with platforms
let y = platformStart;
while (y > 0) {
  // the next platform can be placed above the previous one with a space
  // somewhere between the min and max space
  y -= platformHeight + random(minPlatformSpace, maxPlatformSpace);

  // a platform can be placed anywhere 25px from the left edge of the canvas
  // and 25px from the right edge of the canvas (taking into account platform
  // width).
  // however the first few platforms cannot be placed in the center so
  // that the player will bounce up and down without going up the screen
  // until they are ready to move
  let x;
  do {
    x = random(25, canvas.width - 25 - platformWidth);
  } while (
    y > canvas.height / 2 &&
    x > canvas.width / 2 - platformWidth * 1.5 &&
    x < canvas.width / 2 + platformWidth / 2
  );

  platforms.push({ x, y });
}

// the doodle jumper
const doodle = {
  width: 40,
  height: 60,
  x: canvas.width / 2 - 20,
  y: platformStart - 60,

  // velocity
  dx: 0,
  dy: 0
};

// keep track of player direction and actions
let playerDir = 0;
let keydown = false;
let prevDoodleY = doodle.y;

// game loop
function loop() {
  requestAnimationFrame(loop);
  context.clearRect(0,0,canvas.width,canvas.height);

  // apply gravity to doodle
  doodle.dy += gravity;

  // if doodle reaches the middle of the screen, move the platforms down
  // instead of doodle up to make it look like doodle is going up
  if (doodle.y < canvas.height / 2 && doodle.dy < 0) {
    platforms.forEach(function(platform) {
      platform.y += -doodle.dy;
    });

    // add more platforms to the top of the screen as doodle moves up
    while (platforms[platforms.length - 1].y > 0) {
      platforms.push({
        x: random(25, canvas.width - 25 - platformWidth),
        y: platforms[platforms.length - 1].y - (platformHeight + random(minPlatformSpace, maxPlatformSpace))
      })

      // add a bit to the min/max platform space as the player goes up
      minPlatformSpace += 0.5;
      maxPlatformSpace += 0.5;

      // cap max space
      maxPlatformSpace = Math.min(maxPlatformSpace, canvas.height / 2);
    }
  }
  else {
    doodle.y += doodle.dy;
  }

  // only apply drag to horizontal movement if key is not pressed
  if (!keydown) {
    if (playerDir < 0) {
      doodle.dx += drag;

      // don't let dx go above 0
      if (doodle.dx > 0) {
        doodle.dx = 0;
        playerDir = 0;
      }
    }
    else if (playerDir > 0) {
      doodle.dx -= drag;

      if (doodle.dx < 0) {
        doodle.dx = 0;
        playerDir = 0;
      }
    }
  }

  doodle.x += doodle.dx;

  // make doodle wrap the screen
  if (doodle.x + doodle.width < 0) {
    doodle.x = canvas.width;
  }
  else if (doodle.x > canvas.width) {
    doodle.x = -doodle.width;
  }

  // draw platforms
  context.fillStyle = 'green';
  platforms.forEach(function(platform) {
    context.fillRect(platform.x, platform.y, platformWidth, platformHeight);

    // make doodle jump if it collides with a platform from above
    if (
      // doodle is falling
      doodle.dy > 0 &&

      // doodle was previous above the platform
      prevDoodleY + doodle.height <= platform.y &&

      // doodle collides with platform
      // (Axis Aligned Bounding Box [AABB] collision check)
      doodle.x < platform.x + platformWidth &&
      doodle.x + doodle.width > platform.x &&
      doodle.y < platform.y + platformHeight &&
      doodle.y + doodle.height > platform.y
    ) {
      // reset doodle position so it's on top of the platform
      doodle.y = platform.y - doodle.height;
      doodle.dy = bounceVelocity;
    }
  });

  // draw doodle
  context.fillStyle = 'yellow';
  context.fillRect(doodle.x, doodle.y, doodle.width, doodle.height);

  prevDoodleY = doodle.y;

  // remove any platforms that have gone offscreen
  platforms = platforms.filter(function(platform) {
    return platform.y < canvas.height;
  })
}

// listen to keyboard events to move doodle
document.addEventListener('keydown', function(e) {
  // left arrow key
  if (e.which === 37) {
    keydown = true;
    playerDir = -1;
    doodle.dx = -3;

  }
  // right arrow key
  else if (e.which === 39) {
    keydown = true;
    playerDir = 1;
    doodle.dx = 3;
  }
});

document.addEventListener('keyup', function(e) {
  keydown = false;
});

// start the game
requestAnimationFrame(loop);
</script>
</body>
</html>