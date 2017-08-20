float p2x, p2y, p3x, p3y,p4x,p4y,p5x,p5y;
float p1x,p1y;
int n=1;


void setup()
{
          size(600,600);
          frameRate(5);
          background(200,200,200);
          
          p1x=300;
          p1y=300;
          
          p2x=400;
          p2y=300;
            
          p4x=450;
          p4y=300;
          
          fill(255,200,64);  
          ellipse(p1x,p1y ,50, 50);
            
          fill(64,64,255);     
          ellipse(p2x,p2y ,25, 25);
            
          fill(192,192,180);  
          ellipse(p4x,p4y ,10, 10);
            
          p3x = p1x + ((p2x-p1x)*cos(n*PI/180)) + ((p2y-p1y)*sin(n*PI/180)); 
          p3y = p1y - ((p2x-p1x)*sin(n*PI/180)) + ((p2y-p1y)*cos(n*PI/180));
          p4x += (p3x-p2x);
          p4y += (p3y-p2y);
          p2x=p3x;
          p2y=p3y;
            
          p5x = p2x + ((p4x-p2x)*cos(25*PI/180)) + ((p4y-p2y)*sin(25*PI/180)); 
          p5y = p2y - ((p4x-p2x)*sin(25*PI/180)) + ((p4y-p2y)*cos(25*PI/180));
          p4x=p5x;
          p4y=p5y;
          n++;
  
}


void draw()
{
            background(200,200,200);    
            fill(255,200,64); 
            ellipse(p1x,p1y ,50, 50); 
            
            fill(64,64,255);    
            ellipse(p2x,p2y ,25, 25); 
            
            fill(192,192,180);  
            ellipse(p4x,p4y ,10, 10);
       
            p3x = p1x + ((p2x-p1x)*cos(n*PI/180)) + ((p2y-p1y)*sin(n*PI/180)); 
            p3y = p1y - ((p2x-p1x)*sin(n*PI/180)) + ((p2y-p1y)*cos(n*PI/180));
      
            p4x += (p3x-p2x);
            p4y += (p3y-p2y);
            p2x=p3x;
            p2y=p3y;
          
            p5x = p2x + ((p4x-p2x)*cos(25*PI/180)) + ((p4y-p2y)*sin(25*PI/180)); 
            p5y = p2y - ((p4x-p2x)*sin(25*PI/180)) + ((p4y-p2y)*cos(25*PI/180));
            p4x=p5x;
            p4y=p5y;
  
}