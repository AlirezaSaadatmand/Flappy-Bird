const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let wallLst = [];
class Bird{
    constructor(x, y){
        this.x = x;
        this.y = y;
        this.velocity = 0;
        this.acceleration = 0;
    }
    update(){
        this.velocity += this.acceleration;
        this.y += this.velocity;
    }
    draw(){

    }
}

let bird = Bird(300 , 300);
class Wall{
    constructor(x , y , side){
        this.width = 40;
        this.side = side;
        this.leftX = x;
        this.rightX = x + this.width;
    }
    update(){
        this.x -= 2;
    }
    draw(){

    }

}
function draw(){
    wallLst.forEach((wall) => {
        wall.update();
        wall.draw();
    })
    bird.update();
    bird.draw();
}
let = animationId;

function animate(){
    animationId = requestAnimationFrame(animate);

}