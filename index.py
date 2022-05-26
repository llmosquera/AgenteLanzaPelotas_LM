from random import choice, randrange

#Se va a definir una clase que va contener la funcionalidad de lanzador de pelotas
class lanzadorPelotas():
    def __init__(self):
        #Asignaremos la variable para saber el costo de trabajo
        self.costo=0
        #Asignaremos la variable para asignar la posicion de las areas
        self.valor=1
        #Asignaremos la variable para guardar cada una de las areas como un libro
        self.diccionario_areas={}
        #Asignaremos la variable para saber donde se encuentra el lanzador
        self.posicion_lanza_pelotas=''
    
    
    #En este metodo se establecera la informacion del libro para su uso
    def Informacion(self):
        #Estableceremos una variable aleatoria para simular un sensor de camara
        tierrasEncontradas=randrange(5)+1
            
        print('La camara encontró '+ str(tierrasEncontradas)+' posiciones para lanzar')
        while(True):
            
            
            if(self.valor<=tierrasEncontradas):
                area=choice(['Tenis', 'Futbol', 'Beisbol'])
                areaEstado = input("Se encontro una zona de: "+area+" Ingrese el estado de esa area: ")
                self.diccionario_areas[str(self.valor)] = [areaEstado,area]
                self.valor+=1
            else:
                break
        
        self.posicion_lanza_pelotas = input("Digite la zona en que se encuentra el lanza pelotas: ")
    
    #En este metodo se identificara las areas sin pelotas
    def identificarArea(self):
        self.areasVaciasEncontradas=[]
        for key in self.diccionario_areas:
            if((self.diccionario_areas[key])[0]=='1'):
                self.areasVaciasEncontradas.append(key)
        
        
                
    
    #En este metodo se identificara si lanzar o no a un area para optmizar trabajo
    def containZona(self, numero):
        keys = list(self.diccionario_areas.keys())
        
        for x in self.areasVaciasEncontradas:
            if(str(numero)==str(x)):
                print('Lanzando pelota a la zona: que es una zona de '+str((self.diccionario_areas[x])[1]))
                return True
            
        return False
    
    #En este metodo se permitira mover la posicion al primer elemento del libro
    def redirigirPrimero(self):
        #si no hay areas vacias se terminara el programa
        if( not(not self.areasVaciasEncontradas)):
            #si la posicion del lanza pelota es la misma no se necesitara de movimientos extras
            if(self.posicion_lanza_pelotas==self.areasVaciasEncontradas[0]):
                pass
            else:
                #Se movera nuestro lanza pelotas a la posicion inicial de nuestro libro
                for i in range(int(self.posicion_lanza_pelotas),int(self.areasVaciasEncontradas[0]),-1):
                    print('girando de zona '+str(i)+' a posicion '+str(i-1))
                    self.costo+=1
                    
                self.posicion_lanza_pelotas=self.areasVaciasEncontradas[0]
          
    
    #En este metodo se establecera toda la logica de manera que usaremos los demás metodos
    def lanzamientoPelotas(self):
        self.Informacion()
        self.identificarArea()
        self.redirigirPrimero()
        #si no hay areas vacias se terminara el programa
        if( not(not self.areasVaciasEncontradas)):
            #Se buscara las areas para lanzar la pelota
            for i in range(int(self.posicion_lanza_pelotas) ,int(self.areasVaciasEncontradas[len(self.areasVaciasEncontradas)-1])+1,+1):
                #Comprobara si la pelota debe ser lanzada
                if(self.containZona(i)):
                    self.costo+=2
                    print('Girando...')
                else:
                    self.costo+=1
                    print('Girando...')
        
        print('Ya no hay areas que lanzar ')
        print('El costo seria '+str(self.costo))

limpiadorplatos= lanzadorPelotas()
limpiadorplatos.lanzamientoPelotas()