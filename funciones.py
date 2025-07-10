import os, time

def menu():
    menu="""----MENU----
1. Stock marca.
2. Busqueda por precio.
3. Listado de productos.
4. Salir"""

    while True:
        os.system('cls')
        print(menu)

        opc=input("Ingrese una opción: ")
        os.system('cls')

        if opc=='1':
            print("---STOCK---")
            if comprobar_lista()==False:
                break
            marca=comproba_marca()
            stock_marca(marca)
            
                

        elif opc=='2':
            print("---BUSQUEDA DE PRECIO---")
            p_min =None
            p_max=None
            busqueda_precio(p_min,p_max)

        elif opc=='3':
            print("---LISTADO DE PRODUCTOS---")
            ordenar_productos()
        elif opc=='4':
            print("PROGRAMA TERMINADO....")
            time.sleep(3)
        else:
            print("ERROR!!! opción incorrectaa...")
            time.sleep(2)

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def stock_marca(marca):
    cantidad=0
    for m in productos:
        if marca==productos[m][0]==marca:
            varia =productos[m][1]
            cantidad = cantidad + varia
        print(f"el stock es {cantidad}")
        break
    time.sleep(3)



def busqueda_precio(p_min, p_max):
    precio = 0
    valida=[]
    while True:
        try:
            p_min =int(input("Ingrese precio minimo:"))
            p_max=int(input("Ingrese precio maximo"))        
        except ValueError:
            print("Ingrese un número valido")   
            time.sleep(3) 
            break
        print(f"Los productos en ese rango son: {stock} ")
        for p in stock:
            precio= stock[p][1]
            if precio<p_max and precio>p_min:
                valida.append(p)
                print(f"({productos[p][0]-{p}})")
        if len(valida)==0:
            print("No hay productos a ese rango de precio")
            input("presione ENTER para continuar /n ")
            return

def ordenar_productos():
    print("Listado de productos: ")
    for p in productos:
        print(f"{productos[p][0], stock[p], productos[p][2], productos[p][4]}")




def comproba_marca():
    marca= input("Ingrese marca a consultar: ").strip().title()
    for m in productos:
        if productos[m][1]==marca:
            break
time.sleep(3)
            
def comprobar_lista():
    if len(productos)<0:
        print("No hay productos en la lista")
        return False
    return True
