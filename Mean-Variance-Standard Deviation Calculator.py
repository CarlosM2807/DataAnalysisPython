import numpy as np
def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    matriz = np.array(list).reshape(3,3)
    matriz

    medias = []
    medias.append(np.mean(matriz, axis=0).tolist())
    medias.append(np.mean(matriz, axis=1).tolist())
    medias.append(np.mean(matriz))

    var = []
    var.append(np.var(matriz, axis=0).tolist())
    var.append(np.var(matriz, axis=1).tolist())
    var.append(np.var(matriz).tolist())

    des = []
    des.append(np.std(matriz, axis=0).tolist())
    des.append(np.std(matriz, axis=1).tolist())
    des.append(np.std(matriz).tolist())

    mini = []
    mini.append(np.min(matriz, axis=0).tolist())
    mini.append(np.min(matriz, axis=1).tolist())
    mini.append(np.min(matriz).tolist())

    maxi = []
    maxi.append(np.max(matriz, axis=0).tolist())
    maxi.append(np.max(matriz, axis=1).tolist())
    maxi.append(np.max(matriz).tolist())

    suma = []
    suma.append(np.sum(matriz, axis=0).tolist())
    suma.append(np.sum(matriz, axis=1).tolist())
    suma.append(np.sum(matriz).tolist())

    calculations = {}
    calculations["mean"] = medias
    calculations["variance"] = var
    calculations["standard deviation"] = des
    calculations["max"] = maxi
    calculations["min"] = mini
    calculations["sum"] = suma

    return calculations