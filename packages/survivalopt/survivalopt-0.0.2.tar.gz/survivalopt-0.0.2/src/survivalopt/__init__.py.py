import numpy as np
import pandas as pd
import pickle

import os.path

import matplotlib.pyplot as plt

from sklearn.preprocessing import OrdinalEncoder

from scipy import stats
from scipy.stats import qmc

import random

import itertools

#FROM 2023 FEB 22 

# Variable Transformers

def VarTra_log10(inp, inverse = False): 
    return np.log10(inp) if inverse == False else 10**inp

# Metrics

def MeanError(inp1, inp2, weights = None, expo = 2, inverse = False): 
    #inp1,inp2,weights = (np.array(n) for n in [inp1,inp2,weights])
    if weights is None: weights = 1
    e = abs(inp1-inp2)
    me = (weights*(e**expo)).mean()
    return me if inverse == False else 1/me 

def Correlation(inp1, inp2, weights = None, inverse = False): 
    if weights is None: weights = 1
    if isinstance(weights, int): cor = np.corrcoef(inp1,inp2)[0, 1]
    else: 
        def m(inp1, weights): return np.sum(inp1 * weights) / np.sum(weights)
        def cov(inp1, inp2, weights): return np.sum(weights * (inp1 - m(inp1, weights)) * (inp2 - m(inp2, weights))) / np.sum(weights)
        cor = cov(inp1, inp2, weights) / np.sqrt(cov(inp1, inp1, weights) * cov(inp2, inp2, weights))
    return cor if inverse == False else 1/cor

# Bin Metrics

def BinMetrics(inp1, inp2, weights = None, metrics_mode = [MeanError, {'expo': 2}], 
               categorical = False, bins = 10, quantile = True): 
    
    r = [inp1,inp2] if weights is None else [inp1,inp2,weights]
    
    inp1, inp2 = (np.array(x) for x in [inp1,inp2])
    idx = np.arange(len(inp1))
    sort = np.argsort(inp1)
    inp1, inp2 = (x[sort] for x in [inp1, inp2])
    if weights is not None: weights = weights[sort]
    
    if categorical is True: 
        uni = np.unique(inp1)
        par = [np.where(inp1 == u)[0] for u in uni]
    else:
        uni = np.arange(bins)
        if quantile is True: 
            par = np.array_split(idx, bins)
        else: 
            v = np.linspace(np.min(inp1), np.max(inp1), bins + 1)
            par = [np.where(np.logical_and(v[b+1]>=inp1, inp1>=v[b]))[0] for b in np.arange(bins)]
    
    lps, mets = [], []
    for p in par: 
        lps.append(len(p))
        mets.append(metrics_mode[0](*[g[p] for g in r], **metrics_mode[1]))
    
    return [uni, mets, lps]

# Tide

def Tide(inp1, inp2, weights = None, bins = 10, quantile = True, ordinal = False, metrics_mode = [MeanError, {'expo':2}]): 
    
    inp1, inp2 = (np.array(x) for x in [inp1,inp2])
    idx = np.arange(len(inp1))
    sort = np.argsort(inp1)
    inp1, inp2 = (x[sort] for x in [inp1, inp2])
    
    if ordinal == True: 
        inp1, inp2 = (x.reshape(-1,1) for x in [inp1,inp2])
        enc = OrdinalEncoder().fit(inp1)
        inp1 = enc.transform(inp1).astype(int).reshape(-1)
        inp2 = enc.transform(inp2).astype(int).reshape(-1)
    
    if weights is not None: 
        weights = weights[sort]
        m = metrics_mode[0](inp1, inp2, weights, **metrics_mode[1])
    else: m = metrics_mode[0](inp1, inp2, **metrics_mode[1])
    
    if ordinal == True: 
        uni = np.unique(inp1)
        par = [np.where(inp1 == t)[0] for t in uni]
        bins = len(uni)
    else: 
        if quantile == True:
            par = np.array_split(idx, bins)
        else: 
            v = np.linspace(np.min(inp1), np.max(inp1), bins + 1)
            par = [np.where(np.logical_and(v[b+1]>=inp1, inp1>=v[b]))[0] for b in np.arange(bins)]

    RT, FT = [], []
    
    rds, fds = [], []
    for b in np.arange(bins-1): 
        ridx = np.hstack(par[:b+1])
        fidx = idx[np.isin(idx, ridx, invert = True)]
        rds.append(ridx), fds.append(fidx)
        if weights is not None: 
            r, f = (metrics_mode[0](inp1[y], inp2[y], weights[y], **metrics_mode[1]) for y in [ridx, fidx]) 
        else: r, f = (metrics_mode[0](inp1[y], inp2[y], **metrics_mode[1]) for y in [ridx, fidx])
        RT.append(r), FT.append(f)
    #RT, FT = RT + [m], [m] + FT
    RT, FT = (np.array(tt) for tt in [RT, FT])
    
    return [RT, FT]


# REPEATS

def ReduceRepeats(scores, func = np.min, num_can = None, repeats = None): 
    #repeatsfunc is a numpy function with an axis argument. Examples include np.average, np.maximum, np.minimum
    
    scores = np.array(scores)
    scores = scores.reshape(num_can, -1) if num_can is not None else scores.reshape(-1, repeats)
    
    return func(scores, axis = -1)

# WEIGHTING

def MinMax(scores, smallest = True): 
    
    scores = np.array(scores)
    mi, ma = (j(scores) for j in [np.min, np.max])
    mami = ma-mi
    weights = (scores-mi) / mami
    if smallest == True: weights = 1-weights
    
    return weights

def Rank(scores, smallest = True): 
    
    scores = np.array(scores)
    g = -1 if smallest == True else 1
    weights = (g*scores).argsort().argsort()
    
    return weights 

# SELECTION

def Truncation(scores, survive = 0.7, equal = False, smallest = False): 
    
    v = np.array(scores)
    sel = np.round(len(v) * survive).astype(int)
    
    k = 1 if smallest == True else -1
    
    nonsel = np.argsort(v)[::k][sel:]
    v[nonsel] = 0
    
    if equal is True: v = np.greater(v, 0)*1 
    
    return v 

def RouletteWheel(scores, survive = 0.7, equal = False, smallest = False): 
    
    v = np.array(scores) 
    ls = len(scores)
    si = np.arange(ls)
    sel = np.round(ls * survive).astype(int)
    
    p = v / np.sum(scores)
    if smallest == True: p = 1-p 
    resamps = np.random.choice(si, size = sel, replace = False, p = p)
    nonsel = [s for s in si if s not in resamps]
    v[nonsel] = 0
    
    if equal is True: v = np.greater(v, 0)*1 
    
    return v

# DISTRIBUTION CREATORS AND SELECTORS 

def KDELimiter(init_bounds, used_vars, num_can, weights = None): 
    
    mi,ma = init_bounds[0][0], init_bounds[0][1]
    
    if len(init_bounds) > 2: used_vars = init_bounds[2](used_vars)
    
    d = stats.gaussian_kde(used_vars.astype(float), weights = weights, bw_method = 'silverman')
    
    resamps = []
    while len(resamps) < num_can:  
        r = d.resample(1)[0][0]
        if len(init_bounds) > 2: r = init_bounds[2](r, inverse = True)
        if init_bounds[1] == 'int': r = np.round(r).astype(int)
        if ma >= r >= mi: resamps.append(r)
    
    return np.array(resamps)
    
def NormalLimiter(init_bounds, used_vars, num_can, weights = None, limit_std = 1): 
    
    mi,ma = init_bounds[0][0], init_bounds[0][1]
    
    if len(init_bounds) > 2: used_vars = init_bounds[2](used_vars)
    
    meanpui = np.average(used_vars.astype(float), weights=weights)
    scalepui = np.sqrt(np.cov(used_vars.astype(float), aweights=weights))
    
    resamps = []
    while len(resamps) < num_can:  
        r = stats.truncnorm.rvs(-limit_std, limit_std, loc=meanpui, scale=scalepui, size=1)[0]
        if len(init_bounds) > 2: r = init_bounds[2](r, inverse = True)
        if init_bounds[1] == 'int': r = np.round(r).astype(int)
        if ma >= r >= mi: resamps.append(r)
    
    return np.array(resamps)

def RangeLimiter(init_bounds, used_vars, num_can, weights = None, limit_range = 0.7, current_round = 1):
    
    mi,ma = init_bounds[0][0], init_bounds[0][1]
    
    if len(init_bounds) > 2: 
        used_vars = init_bounds[2](used_vars)
        mi,ma = (init_bounds[2](b) for b in init_bounds[0])
    meanpui = np.average(used_vars.astype(float), weights=weights)
    rangepui = (limit_range**current_round) * (ma - mi)
    
    up, down = (meanpui-(rangepui/2), meanpui+(rangepui/2)) 
    if up > ma: up = ma
    if down < mi: down = mi
    
    resamps = np.random.uniform(up, down, size=num_can)
    if len(init_bounds) > 2: resamps = init_bounds[2](resamps , inverse = True)
    if init_bounds[1] == 'int': resamps = np.round(resamps).astype(int)
    
    return resamps

# CANDIDATE GENERATION

def RandomCanGen(VarDict, num_can, LHC = False, LHC_args = {}): 
    
    NewCanDict = {} 
    for i in range(num_can): NewCanDict[i] = {}
    
    if LHC == True: 
        sample = qmc.LatinHypercube(d = len(VarDict), **LHC_args).random(n = num_can)
    else: sample = np.random.uniform(size = (num_can, len(VarDict)))
    
    for ik, key in enumerate(VarDict): 
        if VarDict[key][1] == 'cat':
            if LHC == True: 
                ord_enc = OrdinalEncoder()
                oe = ord_enc.fit_transform(np.array(VarDict[key][0]).reshape(-1,1)).reshape(-1)
                g = np.round(sample[:, ik] * np.max(oe))
                r = ord_enc.inverse_transform(g.reshape(-1,1)).reshape(-1)
            else: 
                lvk = len(VarDict[key][0])
                c = np.random.choice(range(lvk), size = num_can)
                r = [VarDict[key][0][u] for u in c]
                
        else: 
            n,m = VarDict[key][0][0], VarDict[key][0][1]
            if len(VarDict[key]) > 2: n,m = (VarDict[key][2](q) for q in (n,m))
            g = sample[:, ik] * (m - n) + n
            if len(VarDict[key]) > 2: n,m = (VarDict[key][2](q, reverse = True) for q in (n,m))
            r = np.round(g).astype(int) if VarDict[key][1] == 'int' else g
            
        for i in range(num_can): NewCanDict[i][key] = r[i]
        
    return NewCanDict

def SurvivedCanGen(VarDict, CanDict, weights, num_can, mode = [KDELimiter, {}]): 
    
    weights = np.array(weights) / np.sum(weights)
    
    pdict = pd.DataFrame.from_dict(CanDict)
    
    r = len(weights) // len(CanDict)
    if r > 1: pdict = pdict.iloc[np.arange(len(pdict)).repeat(r)].reset_index(drop = True) 
        
    NewCanDict = {} 
    for i in range(num_can): NewCanDict[i] = {} 

    for key in VarDict:
        
        used_vars = pdict.T[key].to_numpy()
        
        if VarDict[key][1] == 'cat': 
            resamps = random.choices(used_vars, weights = weights, k = num_can)
        else: 
            resamps = mode[0](VarDict[key], used_vars, num_can, weights = weights, **mode[1])
        
        for i in range(num_can): NewCanDict[i][key] = resamps[i]
    
    return NewCanDict

# CANDIDATE SCORERS 

def StandardCanScorer(algo, algo_args, data, metrics_mode, add_metrics_modes = None, 
                     pathname = None, returnmodel = False): 

    #add_metrics_mode is optional but if specified is a list of functions and a list of their respective arguments. 
    
    m = algo(**algo_args)
    m.fit(*data[0])
    y_hat = m.predict(data[1][0])
    score = metrics_mode[0](y_hat, *data[1][1:], **metrics_mode[1])
    
    if pathname is not None: pickle.dump(m, open(pathname + '.p', 'wb'))
    
    add_scores = []
    if add_metrics_modes is not None: 
        lamm = len(add_metrics_modes) // 2
        for amm in range(lamm): 
            add_scores.append(add_metrics_modes[amm](y_hat, *data[1][1:], **metrics_mode[amm+lamm]))
        
        score = [score, add_scores]
        
    return score if returnmodel is False else (score, m)  


def BasicScorer(func, func_args, data, pathname = None, idx = None): 
    
    #func returns score
    #pathname is path for saving models and is optional. 
    if pathname is not None: 
        score = func(data, pathname = pathname, **func_args)
    else: 
        score = func(data, **func_args)
    
    if isinstance(idx, int): score = score[idx]
    
    return score 


# CANDIDATE EVALUATORS

def CanEvaluator(algo, CanDict, data, Splits = None, repeats = 1, 
                 CS_mode = [StandardCanScorer, {'metrics_mode': [MeanError, {'expo': 2}]}], CS_vars = None, 
                 pickup = False, statusprints = True, pathname = None, savemodels = False): 
    
    metrics = pickle.load(open(pathname + '_SurvOptMet.p', 'rb')) if pickup == True else [] 
        
    lmd = len(CanDict.keys())
    
    CSDict = {} 
    for i in range(lmd): 
        CSDict[i] = CS_mode[1]
        if CS_vars is not None: 
            x = {v: CanDict[i][v] for v in CS_vars}
            CSDict[i].update(x)
            for v in CS_vars: 
                del CanDict[i][v]
    
    if Splits is not None: 
        if isinstance(Splits, list): Splits = [Splits]
        lsp = len(Splits) 
        
    else: lsp = len(data) if type(data) is dict else 1
    
    modelcombos = []
    for i in range(lmd): 
        for s in range(lsp):
            for r in range(repeats):
                modelcombos.append([i, s, r])
    
    savepath = None
    
    for c in modelcombos[len(metrics):]: 
        i, s, r = c
        
        if Splits is not None: dataz = [[d[Splits[s][t]] for d in data] for t in [0,1]]
        else: dataz = data[data.keys[s]] if type(data) is dict else data
        
        if statusprints == True: 
            if r == 0 and s == 0: 
                print(f' Model {i+1} of {lmd}: {CanDict[i].items()}')
            print(f' cross val {s+1} of {lsp}, Repeat {r+1} of {repeats}')
        
        if pathname is not None and savemodels == True: 
            savepath = pathname + '_' + str(i) + '_' + str(s) + '_' + str(r) + '_SurvOptMod'
        
        score = CS_mode[0](algo, CanDict[i], dataz, pathname = savepath, **CSDict[i])

        metrics.append(score)
        
        if statusprints == True: 
            #print(f"{CS_mode[1]['metrics_mode']} {score}")
            print(f"{score}")
        
        if pathname is not None: pickle.dump(metrics, open(pathname + '_SurvOptMet.p', 'wb'))
        
    return np.array(metrics)
    
# SURVIVAL OPTIMISATION

def SurvivalOpt(algo, VarDict, data, Splits = None, 
                rounds = [50,10,1], repeats = 1, survive = 0.7,
                CS_mode = [StandardCanScorer, {'metrics_mode': [MeanError, {'expo': 2}]}], CS_vars = None,
                RMG_args = {},
                R_func = np.min,
                W_mode = [MinMax, {'smallest': True}], 
                S_mode = [Truncation, {'equal': False}], 
                SMG_mode = [KDELimiter, {}], 
                pickup = False, statusprints = True, pathname = None, savemodels = False): 
    
    # Train is  0 and Test is 1 in Splits[i]
    # You specify a list of candidates per round. e.g. rounds = np.linspace(init, out, rounds, dtype = int)
    
    if pickup == False: 
        allCanDict, roundsused, allmetrics, allweights = {}, 0, [], []
        allCanDict[0] = RandomCanGen(VarDict, rounds[0], **RMG_args)
        
    elif pickup == True: 
        allCanDict, allmetrics, allweights = pickle.load(open(pathname + '_SurvOptOut.p', 'rb'))
        roundsused = len(allmetrics)
    
    for ro in range(len(rounds))[roundsused:]: 
        
        print(f'Round {ro + 1} of {len(rounds)}')
        
        pn = pathname + '_' + str(ro) if pathname is not None else None
        
        metrics = CanEvaluator(algo, allCanDict[ro], data, Splits = Splits, repeats = repeats, CS_vars = CS_vars, CS_mode = CS_mode, 
                               pickup = pickup, statusprints = statusprints, pathname = pn, savemodels = savemodels)
        
        
        if R_func is not None: metrics = ReduceRepeats(metrics, R_func, num_can = len(allCanDict[ro]), repeats = None)
        
        allmetrics.append(metrics) 

        if W_mode is not None: metrics = W_mode[0](metrics, **W_mode[1])
        
        allweights.append(metrics)
        
        if pathname is not None: pickle.dump([allCanDict, allmetrics, allweights], open(pathname + '_SurvOptOut.p', 'wb'))

        if ro < (len(rounds) - 1): 
            
            metrics = S_mode[0](metrics, **S_mode[1])
            
            if SMG_mode[0] == RangeLimiter: 
                if ro == 0: SMG_mode[1]['round'] = 1
                else: SMG_mode[1]['round'] += 1

            allCanDict[ro + 1] = SurvivedCanGen(VarDict, allCanDict[ro], metrics, rounds[ro + 1], mode = SMG_mode)
        
        allweights[ro] = metrics
        
    return allCanDict, allmetrics, allweights

def BestCan(SurvOptOut, smallest = True, num_splits = 1, 
            savemodels = False):
    
    #Atleast one round needs to be complete
        
    allCanDict, allmetrics, allweights = pickle.load(open(SurvOptOut + '_SurvOptOut.p', 'rb')) if isinstance(SurvOptOut, str) else SurvOptOut
    allrepeats = len(allmetrics[0]) // len(allCanDict[0])
    repeats = allrepeats // num_splits
    
    if len(allCanDict) > len(allmetrics) and isinstance(x, str): 
        v = x + '_SurvOptMet.p'
        if os.path.exists(v): 
            allmetrics.append(pickle.load(open(v, 'rb')))
        
    f = np.nanargmin if smallest == True else np.nanargmax
    bestidx = [f(m) for m in allmetrics]
    bestscores = [m[b] for m,b in zip(allmetrics, bestidx)] 
    bestround = f(bestscores) 
    bestmodel = bestidx[bestround] // allrepeats
    
    bestdict = allCanDict[bestround][bestmodel]
    
    allreps = list(itertools.product(np.arange(num_splits), np.arange(repeats)))
    bestsplit, bestrep = allreps[bestidx[bestround] % allrepeats]
    
    print(f'''Best at: 
    round {bestround+1},
    model {bestmodel+1}, 
    split {bestsplit+1}, 
    repeat {bestrep+1}, 
    with score {bestscores[bestround]}''')
    
    if savemodels is not False: 
        pn = SurvOptOut if isinstance(SurvOptOut, str) else savemodels
        pathname = pn + '_' + str(bestround) + '_' + str(bestmodel) + '_' + str(bestsplit) + '_' + str(bestrep) + '_' + 'SurvOptMod' 
    
    return (bestdict, pathname) if savemodels is not False else bestdict

def StandardFitter(algo, algo_args, data, Split = None, repeats = 3, 
                   CS_mode = [StandardCanScorer, {'metrics_mode': [MeanError, {'expo': 2}]}],
                   smallest = True, statusprints = True,
                   pathname = None): 
    
    if Split is not None: data = [[d[Split[t]] for d in data] for t in [0,1]]
    
    if repeats is None or repeats == 0: repeats = 1
    
    pn = pathname
    
    mets = []
    mods = []
    for r in range(repeats): 
        if pathname is not None: 
            if repeats > 1: pn = pathname + '_' + str(r)
            pn = pathname + '_' + str(r) if repeats > 1 else pathname
        csout = CS_mode[0](algo, algo_args, data, pathname = pn, returnmodel = True, **CS_mode[1])
        mets.append(csout[0]), mods.append(csout[1])
        
        if statusprints is True: 
            print(f'Repeat {r}, Score: {mets[-1]}') if repeats > 1 else print(f'Score: {mets[-1]}')
        
    f = np.nanargmin if smallest == True else np.nanargmax
    bm = f(mets)
    if repeats > 1: 
        print(f'Best at repeat {bm}')
        if pathname is not None: pn = pathname + '_' + str(bm)
    
    return mods[bm] if pathname is None else (mods[bm], pn)

def StandardPredictor(model, Xdatas, onlyidx = None): 
    
    #If onlyidx is not None, then the datas are in divided format. 
    
    if isinstance(Xdatas, list) == False: Xdatas = [Xdatas]
    
    preds = [] 
    for x in Xdatas:  
        if onlyidx is not None: 
            for ij, j in enumerate(x):
                if ij in onlyidx: 
                    preds.append(model.predict(j))
        else: preds.append(model.predict(x))
        
    if isinstance(Xdatas, list) == True: preds = preds[0]
   
    return preds

# VISUALS 

def SurvivalOptPlot(SurvOptOut, 
                    only_var = None, only_round = None, 
                    metricname = 'pear', pointsize = (10,20), 
                    figsize = (30,5), fontsize = 13, sharey = True):
    
    plt.rc('font', size=fontsize)
    titlesize = int(fontsize + fontsize * 0.2)
    
    allCanDict, allmetrics, allweights = pickle.load(open(SurvOptOut + '_SurvOptOut.p', 'rb')) if isinstance(SurvOptOut, str) else SurvOptOut
    
    if only_var is None: only_var = allCanDict[0][0].keys()
    if only_round is None: only_round = np.arange(len(allCanDict))
    
    pdicts = {}
    for iro, ro in enumerate(only_round): 
        pdict = pd.DataFrame.from_dict(allCanDict[ro])
        reps = len(allmetrics[iro]) // len(allCanDict[ro])
        if reps > 1: pdict = pdict.iloc[np.arange(len(pdict)).repeat(reps)].reset_index(drop = True) 
        pdicts[ro] = pdict
    
    lh, lr = (len(x) for x in [only_var, only_round]) 
    
    fig, axs = plt.subplots(lr, lh, figsize = figsize, sharex = 'col', sharey = sharey)
    
    for iro, ro in enumerate(only_round): 
        
        w = allweights[ro]
        
        if pointsize is not None: 
            colors = ['red' if x == 0 else 'purple' for x in w]
            ma = np.max(w)
            w = (w / ma) * (pointsize[1] - pointsize[0]) + pointsize[0]
        
        
        else: colors = None
        
        for ih, h in enumerate(only_var): 

            used_vars = pdicts[ro].T[h].to_numpy()
            
            p = axs[iro, ih] if len(only_round) > 1 else axs[ih]
            
            p.scatter(used_vars, allmetrics[ro], s = w, c = colors)
            
            if iro == 0: p.set_title(h, fontsize = titlesize, fontweight='bold')
            if ih == 0: 
                j = 'Round ' + str(ro + 1) 
                if metricname is not None: j = j + '\n' + metricname
                p.set_ylabel(j, fontsize = titlesize, fontweight='bold')
        
    fig.tight_layout()
   
    return 


    
# DEFAULT HPS

HPS_defaults = {
    
    'Ada_reg': {'learning_rate': ([0.01, 2.0], 'float'), 
               'max_depth': ([1, 10], 'int'), 
               'n_estimators': ([10, 200], 'int'),
               'loss': (['linear', 'square', 'exponential'], 'cat') }, 
    
    'Ada_clf': {'learning_rate': ([0.01, 2.0], 'float'), 
               'max_depth': ([1, 10], 'int'), 
               'n_estimators': ([10, 200], 'int'),
               'algorithm': (['SAMME', 'SAMME.R'], 'cat') },
    
    'DT': {'min_samples_split': ([2, 60], 'int'), 
          'max_depth': ([1, 100], 'int'), 
          'min_samples_leaf': ([1, 60], 'int'), 
          'ccp_alpha': ([0, 1], 'float') },
    
    'ElNet_reg': {'alpha': ([0.01, 10], 'float'),
                 'l1_ratio': ([0, 1], 'float'),
                 'tol': ([1e-6, 1e-2], 'float'),
                 'max_iter': ([100, 2000], 'int'),
                 'fit_intercept': ([True, False], 'cat'), 
                 'normalize': ([True, False], 'cat'), 
                 'positive': ([True, False], 'cat'), 
                 'selection': (['cyclic', 'random'], 'cat') }, 
    
    'KNN': {'n_neighbors': ([1, 100], 'int'), 
           'leaf_size': ([1, 60], 'int'), 
           'p': ([1, 2], 'int'), 
           'weights': (['uniform', 'distance'], 'cat'), 
           'algorithm': (['auto', 'ball_tree', 'kd_tree', 'brute'], 'cat') }, 
    
    'Lin_reg': {'fit_intercept': ([True, False], 'cat'), 
               'normalize': ([True, False], 'cat') }, 
    
    'LGB': {'num_leaves': ([2, 256], 'int'), 
           'min_data_in_leaf': ([20,1000], 'int'),
           'max_depth': ([-1, 100], 'int'),
           'feature_fraction': ([0.3, 1], 'float'), 
           'bagging_fraction': ([0.3, 1], 'float') }, 
    
    'Log_reg': {'tol': ([1e-6, 1e-2], 'float'), 
               'C': ([0.1, 4.0], 'float'), 
               'intercept_scaling': ([0.1, 4.0], 'float'),
               'max_iter': ([50, 150], 'int'),
               'fit_intercept': ([True, False], 'cat'), 
               'solver': (['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'], 'cat') },
    
    'MLP': {'n_hidden_layers': ([0, 4], 'int'),
           'hidden_layer_size': ([10, 100], 'int'),
           'activation': (['identity', 'logistic', 'tanh', 'relu'], 'cat'),
           'learning_rate': (['constant', 'invscaling', 'adaptive'], 'cat') }, 
    
    'NB': {'var_smoothing': ([0, 1], 'float') }, 
    
    'RF_reg': {'min_samples_leaf': ([1, 20], 'int'),
              'min_samples_split': ([2, 20], 'int'),
              'n_estimators': ([10, 200], 'int'),
              'max_features': ([0.1, 1.0], 'float'),
              'bootstrap': ([True, False], 'cat') }, 
    
    'RF_clf': {'min_samples_leaf': ([1, 20], 'int'),
              'min_samples_split': ([2, 20], 'int'),
              'n_estimators': ([10, 200], 'int'),
              'max_features': ([0.1, 1.0], 'float'),
              'bootstrap': ([True, False], 'cat'), 
              'criterion': (['entropy', 'gini'], 'cat') }, 
    
    'SVM': {'C': ([2**-5, 2**15], 'float', VarTra_log10),
           'gamma': ([2**-15, 2**3], 'float', VarTra_log10),
           'tol': ([1e-5, 1e-1], 'float', VarTra_log10),
           'kernel': (['sigmoid', 'rbf'], 'cat') }, 
    
    'XGB': {'eta': ([0, 1.0], 'float'),
           'subsample': ([0.1, 1.0], 'float'),
           'min_child_weight': ([1.0, 128.0], 'float', VarTra_log10),
           'colsample_bytree': ([0, 1.0], 'float'), 
           'colsample_bylevel': ([0, 1.0], 'float'), 
           'lambda': ([0, 5], 'float'), 
           'alpha': ([0, 5], 'float'), 
           'max_depth': ([1, 15], 'int'),
           'booster': (['gbtree', 'gblinear', 'dart'], 'cat') }
    
}
