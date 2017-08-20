int centrox,centroy,raiorel;
int raioseg,raiomin,raiohor;

float angseg,angmin,anghor;



void setup()
{
  size(600,600);
  background(200,200,200);
  stroke(255);
 centrox=width/2;
 centroy=height/2;
 raiorel=min(width,height)/2;
 raioseg=raiorel/3;
 raiomin=raiorel/4;
 raiohor=raiorel/5;
}


void draw()
{
  background(0);
  
  float s = second();  
  float m = minute(); 
  float h = hour();
  if(h>12){
    h=(h%12);
  }

   
  angseg=((((2*PI)*s)/60))-(PI/2);
  angmin=((((2*PI)*m)/60))-(PI/2);
  anghor=(((2*PI)*(h+(m/60)))/12)-(PI/2);
  ellipse(centrox,centroy ,raiorel, raiorel); 
  
  stroke(64,64,255);
  line(centrox,centroy,centrox+raioseg*cos(angseg),centroy+raioseg*sin(angseg));
  stroke(255,200,64);
  line(centrox,centroy,centrox+raiomin*cos(angmin),centroy+raiomin*sin(angmin));
  stroke(192,192,180);
  line(centrox,centroy,centrox+raiohor*cos(anghor),centroy+raiohor*sin(anghor));
  
  strokeWeight(2);
  beginShape(POINTS);
  for (int a = 0; a < 360; a+=6) {
    float angle = radians(a);
    float x = centrox + cos(angle) * raioseg;
    float y = centroy + sin(angle) * raioseg;
    vertex(x, y);
  }
  endShape();
 
  
}