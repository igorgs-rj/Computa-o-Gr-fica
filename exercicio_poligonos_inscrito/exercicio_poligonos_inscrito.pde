float  p3x, p3y;
int n;
float p1x=300;
float p1y=300;
float p2x=560;
float p2y=300;



void setup()
{
  size(600,600);
  n=3;
 
  
}


void draw()
{ 

  background(200,200,200);
  ellipse(300,300,560,560);
  int a=0;
  switch (n){
    
          case 3:

          p2x=580;
          p2y=300;
          while(a<3)
          {
               p1x=300;
               p1y=300;
               p3x = p1x + ((p2x-p1x)*cos((360/n)*PI/180)) + ((p2y-p1y)*sin((360/n)*PI/180)); 
               p3y = p1y - ((p2x-p1x)*sin((360/n)*PI/180)) + ((p2y-p1y)*cos((360/n)*PI/180)); 
               line(p2x, p2y, p3x, p3y);
               p2x=p3x;
               p2y=p3y;
               a++;
          }
  
          case 4:
            
          p2x=580;
          p2y=300;
          while(a<4)
          {
               p1x=300;
               p1y=300;
               p3x = p1x + ((p2x-p1x)*cos((360/n)*PI/180)) + ((p2y-p1y)*sin((360/n)*PI/180)); 
               p3y = p1y - ((p2x-p1x)*sin((360/n)*PI/180)) + ((p2y-p1y)*cos((360/n)*PI/180)); 
               line(p2x, p2y, p3x, p3y);
               p2x=p3x;
               p2y=p3y;
               a++;
          }
          case 5:
            
          p2x=580;
          p2y=300;
          while(a<5)
          {
               p1x=300;
               p1y=300;
               p3x = p1x + ((p2x-p1x)*cos((360/n)*PI/180)) + ((p2y-p1y)*sin((360/n)*PI/180)); 
               p3y = p1y - ((p2x-p1x)*sin((360/n)*PI/180)) + ((p2y-p1y)*cos((360/n)*PI/180)); 
               line(p2x, p2y, p3x, p3y);
               p2x=p3x;
               p2y=p3y;
               a++;
          }
          case 6:
            
          p2x=580;
          p2y=300;
          while(a<6)
          {
               p1x=300;
               p1y=300;
               p3x = p1x + ((p2x-p1x)*cos((360/n)*PI/180)) + ((p2y-p1y)*sin((360/n)*PI/180)); 
               p3y = p1y - ((p2x-p1x)*sin((360/n)*PI/180)) + ((p2y-p1y)*cos((360/n)*PI/180)); 
               line(p2x, p2y, p3x, p3y);
               p2x=p3x;
               p2y=p3y;
               a++;
          }
          case 7:
            
          p2x=580;
          p2y=300;
          while(a<7)
          {
               p1x=300;
               p1y=300;
               p3x = p1x + ((p2x-p1x)*cos((360/n)*PI/180)) + ((p2y-p1y)*sin((360/n)*PI/180)); 
               p3y = p1y - ((p2x-p1x)*sin((360/n)*PI/180)) + ((p2y-p1y)*cos((360/n)*PI/180)); 
               line(p2x, p2y, p3x, p3y);
               p2x=p3x;
               p2y=p3y;
               a++;
          }
       
          case 8:
            
          p2x=580;
          p2y=300;
          while(a<8)
          {
               p1x=300;
               p1y=300;
               p3x = p1x + ((p2x-p1x)*cos((360/n)*PI/180)) + ((p2y-p1y)*sin((360/n)*PI/180)); 
               p3y = p1y - ((p2x-p1x)*sin((360/n)*PI/180)) + ((p2y-p1y)*cos((360/n)*PI/180)); 
               line(p2x, p2y, p3x, p3y);
               p2x=p3x;
               p2y=p3y;
               a++;
          }
          case 9:
            
          p2x=580;
          p2y=300;
          while(a<9)
          {
               p1x=300;
               p1y=300;
               p3x = p1x + ((p2x-p1x)*cos((360/n)*PI/180)) + ((p2y-p1y)*sin((360/n)*PI/180)); 
               p3y = p1y - ((p2x-p1x)*sin((360/n)*PI/180)) + ((p2y-p1y)*cos((360/n)*PI/180)); 
               line(p2x, p2y, p3x, p3y);
               p2x=p3x;
               p2y=p3y;
               a++;
          }

          break;
          default:
} 
  
  
  
  
  
  
  
}



void keyPressed() {
  n = int(key);
  n = n - 48;
  if(n >= 0 && n <= 9)
  {
     println("Valid digit: " + n);
  }
  else 
  {
     println("Invalid you pressed " + key);
  }
} 