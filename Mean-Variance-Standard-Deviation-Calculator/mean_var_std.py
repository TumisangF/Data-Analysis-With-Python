import numpy as np

def calculate(list):
    mean = []
    var = []
    std_d = []
    max = []
    min = []
    sum = []

    if len(list) < 9:
      raise ValueError ('List must contain nine numbers.')
    else:
        a = np.reshape(list,(3,3))
    
        mean.append(np.mean(a, axis=0).tolist())
        mean.append(np.mean(a, axis=1).tolist()) 
        mean.append(np.mean(a).tolist())
        
        var.append(np.var(a, axis=0).tolist())
        var.append(np.var(a, axis=1).tolist())
        var.append(np.var(a).tolist())

        std_d.append(np.std(a, axis=0).tolist()) 
        std_d.append(np.std(a, axis=1).tolist())
        std_d.append(np.std(a).tolist())

        max.append(np.max(a, axis=0).tolist()) 
        max.append(np.max(a, axis=1).tolist())
        max.append(np.max(a).tolist())

        min.append(np.min(a, axis=0).tolist())
        min.append(np.min(a, axis=1).tolist())
        min.append(np.min(a).tolist())

        sum.append(np.sum(a, axis=0).tolist())
        sum.append(np.sum(a, axis=1).tolist())
        sum.append(np.sum(a).tolist())
        
        calculations = {'mean': mean,
                        'variance': var,
                        'standard deviation': std_d,
                        'max': max,
                        'min': min,
                        'sum': sum}
                        
    return calculations