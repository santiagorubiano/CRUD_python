import random
def binary_search(data,target,low,hight):
    """
    If the target is not in the list, return False. 
    
    If the target is in the list, return True.
    
    :param data: the list of data to search through
    :param target: the value we're searching for
    :param low: the index of the first element in the array
    :param hight: the index of the last element in the list
    :return: the index of the target value.
    """
    if low > hight:
        return False
    mid = (low + hight)//2
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data,target,low,mid-1)
    
    else:
        return binary_search(data,target, mid+1,hight)

if __name__ =='__main__':
    # creamos una lista de numero alieatoria con 10 nuermos de 1 a 100
    data = [random.randint(0,100) for i in range(0,10)]
    # ordenamos la lista
    data.sort()
    
# Imprime la lista de numeros aleatorios
    print(data)
    
    target = int(input("elige el numero que quieres buscar "))
    found = binary_search(data,target,0,len(data)-1)

    print(found)