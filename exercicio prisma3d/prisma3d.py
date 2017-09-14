from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import*

r=1.0
h=3.0


n=input("Qual o numero de lados da base do prisma?")


ang=(2*pi)/n

vertices=[]
linhas=[]
faces=[]
aux1=[]
aux2=[]

for i in range(0,n):
    c0 = r * cos(ang * i)
    c1 = r * sin(ang * i)
    vertices += [[c0, -h / 2, c1]]
    vertices += [[c0, h, c1]]
linhas += [[0,(n*2)-2]]
linhas += [[1,(n*2)-1]]
y=0
for i in range(1,n):
    linhas += [[y, y+1]]
    linhas += [[y, y+2]]
    linhas += [[y+1, y + 3]]
    y+=2
c=0
for i in range(1,n):
    faces += [[c, c+1, c+2,c+3]]
    c+=2
faces+=[[0,1,(n*2)-1,(n*2)-2]]
a=0
b=1
for i in range(1,n):
    aux1 += [a]
    aux2 += [b]
    a+=2
    b+=2

faces += [aux1]
faces += [aux2]


#print(vertices)
#print(linhas)
#print(faces)

def keyPressed(tecla, x, y):
    global n
    if tecla == '3' or tecla == '4'or tecla == '5'or tecla == '6'or tecla == '7'or tecla == '8'or tecla == '9':
        n=int(tecla)

cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5),(1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5),(1, 0, 0), (1, 1, 0),(1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1),(1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1))




def Pol():
    glBegin(GL_QUAD_STRIP)
    i = 0
    for face in faces:
        #glColor3fv(cores[i])   # cor para cada face
        for vertex in face:
            glColor3fv(cores[vertex])   #cor para cada vertice
            glVertex3fv(vertices[vertex])
        i = i + 1
    glEnd()

    glColor3fv((0, 0.5, 0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(5, 1, 3, 0) #rota o cubo quanto esta rotando(2) em relacao ao vetor 130
    Pol()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay() #redesenha a janela
    glutTimerFunc(50, timer, 1) #ao passar esse tempo


# PROGRAMA PRINCIPAL

glutInit(sys.argv)
glutKeyboardFunc(keyPressed)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600) #define a dimensao do janela
glutCreateWindow("Pol")  #nome da janela
glutDisplayFunc(display)  #funcao de callback para repintar a tela
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0 / 600.0, 0.1, 50.0) #modifica a pespectiva
glTranslatef(0.0, 0.0, -10) #translacao da cena no eixo x ,y ,z
glRotatef(45, 1, 1, 1)       #
glutKeyboardFunc(keyPressed)
glutTimerFunc(50, timer, 1) #redesenha a janela ao chamar a funcao timer

glutMainLoop()
