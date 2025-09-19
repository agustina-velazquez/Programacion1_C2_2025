def buscar_numero(vector:list, numero:int)->int:
    for i in range(len(vector)):
        if vector[i] == numero:
            return i
    
    return -1
        
print(buscar_numero([1,2,3,4],0))

            
        

    

            
        
        
