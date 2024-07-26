const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let wallLst = [];
class Bird{
    constructor(x, y){
        this.x = x;
        this.y = y;
        this.velocity = -20;
        this.acceleration = 1;
    }
    update(){
        this.velocity += this.acceleration;
        this.y += this.velocity;
    }
    jump(){
        this.velocity = -17;
        this.y -= 10;
    }
    draw(){
        ctx.fillStyle = "red";
        ctx.fillRect(this.x , this.y , 30 , 30);
    }
}

const bird = new Bird(300 , 300);
class Wall{
    constructor(x , y , side){
        this.width = 100;
        this.side = side;
        this.leftX = x;
        this.rightX = x + this.width;
        this.y = y;
    }
    update(){
        this.leftX -= 2;
        this.rightX -= 2;
    }
    draw(){
        if (this.side == "up"){
            ctx.fillStyle = "green";
            ctx.fillRect(this.leftX , 0 , this.width , this.y);
        }else{
            ctx.fillStyle = "green";
            ctx.fillRect(this.leftX , this.y , this.width , innerHeight - this.y);
        }
    }
}

addEventListener("keydown" , (event) => {
    if (event.code == "Space"){
        bird.jump();
    }
});
addEventListener( "ontouchstart" , () =>{
    bird.jump();
});

function createWall(){
    setInterval(() => {
        let y = Math.floor(Math.random() * (innerHeight - 400)) + 201;
        wallLst.push(new Wall(innerWidth , y - 150 , "up"));
        wallLst.push(new Wall(innerWidth , y + 150 , "down"))
    }, 2000);
}
createWall()
let animationId;

function animate(){
    animationId = requestAnimationFrame(animate);
    ctx.fillStyle = "white";
    ctx.fillRect(0 , 0, innerWidth , innerHeight);
    wallLst.forEach((wall) => {
        wall.update();
        wall.draw();
        if (wall.x < -100){
            wallLst.splice(wallLst.indexOf(wall) , 1)
        }
    })
    bird.update();
    bird.draw();
}

animate();