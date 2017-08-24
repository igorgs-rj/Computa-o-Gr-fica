int centrox,centroy,raiocir; 
int raiopie; 
 
 
void setup() 
{ 
 size(600,600); 
 background(200,200,200); 
 centrox=width/2; 
 centroy=height/2; 
 raiocir=min(width,height)/2; 
 ellipse(centrox,centroy ,raiocir, raiocir); 
 raiopie=raiocir/2;
 
} 
 
void draw() 
{ 
      
      float ang1=0;
      String qtd = javax.swing.JOptionPane.showInputDialog("Com quantos valores deseja inserir na piechart ?:");
      int par=int(qtd);
      float[] valores=new float[par]; 
      float somatorio = 0;
      for(int i=0;i<par;i++) 
      { 
          String numero = javax.swing.JOptionPane.showInputDialog("Entre com o valor ?:");
          valores[i]= float(numero);
          somatorio=somatorio+valores[i];
      } 
      
      for(int i=0;i<par;i++) 
      { 
          ang1=(ang1+(valores[i]/somatorio)*2*PI);  
          stroke(64,64,255);
          line(centrox,centroy,centrox+raiopie*cos(ang1),centroy+raiopie*sin(ang1)); 
      }

} 
   
   
  