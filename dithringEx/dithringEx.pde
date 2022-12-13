PImage input;

void setup() {
  size(1024, 800);
  input = loadImage("9vSlQkP88A-04j_RjL5GFHSArCQ.jpg");
  
  input.resize(width,height);
  //input.filter(GRAY);
  input = floydSteinberg(input);
  
  passToBlue();
  
  input.save("out.png");
}



void draw() {
  image(input, 0, 0);
}


void passToBlue(){
  for (int i = 0; i < input.pixels.length; i++){
    //println(hex(input.pixels[i]));
    if(input.pixels[i] == 0xFF000000){
      input.pixels[i] = 0xFF0000FF;
    }else{
      //input.pixels[i] = 0xFFFFFF00;
    }
  }
  input.updatePixels();
}
