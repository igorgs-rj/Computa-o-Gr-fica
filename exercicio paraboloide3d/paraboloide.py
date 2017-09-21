from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import*

malha = []
color=[]
a=1
b=0
c=0
x0=-2
xf=2
y0=-2
yf=2
n=20.0
m=20.0
r0=0
rf=1
b0=0
bf=1
xdel=((xf-x0)/n)
ydel=((yf-y0)/m)
funcaoAtual=0


def f(x,y,p):
    if p==1:
        return x ** 2 + y ** 2
    elif p==2:
        return x ** 2 - y ** 2
    elif p == 3:
        return x ** 3 - 3*x*y ** 2
    elif p == 4:
        return sin(x ** 2 + y ** 2)
    elif p == 5:
        return cos(x ** 2 + y ** 2)
    elif p == 6:
        v= (x**2+ y**2)-1
        if(v>0):
            return sqrt(v)
        else:
            return -sqrt(-v)
    elif p == 7:
        v= (x**2+ y**2)
        if(v>0):
            return sqrt(v)
        else:
            return -sqrt(-v)



print malha


cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5),(1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5),(1, 0, 0), (1, 1, 0),(1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1),(1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1))

def keyPressed(tecla, x, y):
    global a
    print(tecla)
    if tecla == '1' or tecla == '2' or tecla == '3' or tecla == '4' or tecla == '5' or tecla == '6'or tecla == '7':
        Red(int(tecla))
    if tecla == 'x':
        a=1
        b=0
        c=0
    if tecla == 'y':
        a = 0
        b = 1
        c = 0



def Red(p):
    global malha,x0,y0,xf,yf,xdel,ydel, funcaoAtual,color
    if p == funcaoAtual:
        return
    print "criando malha para", p
    funcaoAtual = p
    malha = []
    y=y0
    while y < yf:
        linhas = []
        x = x0
        b=b0
        r=r0
        while x < xf:
            r=(((y-y0)*(rf-r0))+r0)/float(yf-y0)
            b=(((y-y0)*(bf-b0))+b0)/float(yf-y0)
            color.append((r,0,b))
            z = f(x, y,p)
            linhas.append((x, y, z))
            z = f(x, y + ydel,p)
            linhas.append((x, y + ydel, z))
            x += xdel
        malha.append(linhas)
        y += ydel



def Pol():

    j = 0
    for l in malha:
        glBegin(GL_QUAD_STRIP)
        i = 0
        for u in l:
            r = u[2] / 8.0
            glColor3f(r,1-r, 0)  # cor para cada vertice
            glVertex3fv(u)
            i += 1
        glEnd()
        j += 1
    '''
    for l in malha:
        glBegin(GL_QUAD_STRIP)
        i = 0
        for u in l:
            glColor3fv(cores[i%len(cores)])  # cor para cada vertice
            glVertex3fv((u[0],u[1],-u[2]))
            i += 1
        glEnd()
    '''




def display():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(5, a, b, c) #100 roda em torna do x 110 roda em torno do y
    Pol()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay() #redesenha a janela
    glutTimerFunc(50, timer, 1) #ao passar esse tempo


# PROGRAMA PRINCIPAL

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600) #define a dimensao do janela
Red(1)
glutCreateWindow("Pol")  #nome da janela
glutDisplayFunc(display)  #funcao de callback para repintar a tela
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
gluPerspective(45, 800.0 / 600.0, 0.1, 50.0) #modifica a pespectiva
glTranslatef(0.0, 0.0, -10) #translacao da cena no eixo x ,y ,z
#glRotatef(45, 1, 1, 1)       #
glutKeyboardFunc(keyPressed)
glutTimerFunc(50, timer, 1) #redesenha a janela ao chamar a funcao timer
glutMainLoop()
