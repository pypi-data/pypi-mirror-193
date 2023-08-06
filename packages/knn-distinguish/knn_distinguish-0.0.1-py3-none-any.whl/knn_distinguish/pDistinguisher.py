import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from scipy.special import erf
from sklearn.preprocessing import MinMaxScaler

class knn_distinguish():
    def __init__(self, data, data_origin, predicted_class) -> None:
        self.arctan_popt = {}
        self.logistic_popt = {}
        self.tanh_popt = {}
        self.arc_popt = {}
        self.gd_popt = {}
        self.ERF_popt = {}
        self.algebra_popt = {}
        self.Gompertz_popt = {}
        self.data = data
        self.data_origin = data_origin
        self.predicted_class = predicted_class
        # self.data_location = data_location
        # self.data_ori_location = data_ori_location

    def combine_data(self, data_list, classes):
        df_comb = pd.DataFrame()
        i = 0
        for df in data_list:
            df['class'] = classes[i]
            df_comb = pd.concat([df, df_comb])
            i += 1
        return df_comb
    
    def data_process(self, dataframe, class_name):
        return dataframe[dataframe['class']==class_name].drop("class",axis=1).to_numpy()

    def data_distance(self, data):
        '''
        calculating empirical data's shortest(NN) distance 
        real data is high-dimensional data points
        '''
        shortest_distance = [0]*len(data)
        for i in range(len(data)):
            x = np.delete(data,i,0)
            temp = (x-data[i])**2
            d = np.sqrt(np.sum(temp,axis=1))
            shortest_distance[i] = d.min()
        
        return np.array(shortest_distance)   # return an array of real data's NN distance
    
    def empirical_CDF(self, data, title):
        '''
        return x,y data of CDF 
        '''    
        sort_data = np.sort(data)
        #print("data len: ",len(sort_data))
        x = np.concatenate(([0],sort_data))
        #print("x len : ",len(x))
        #print("first: ", x[0], "\nlast: ",x[-1])
        
        y = np.zeros((x.shape))
        for i in range(1,len(x)):
            y[i] = i/len(x)
        #print(plt.show())
        return x,y
    
    def auto_curve_fit(self, data_NN, x, y, x_scale_factor, func, s, p_control=None):
        '''
        data_NN: array empirical data_distance for calculating median
        x,y: from CDF
        s: sigma in curve_fit(), for weighting
        '''
        # print(np.median(data_NN))
        if p_control == "Gompertz":
            p0 = [1,1]
        elif p_control == "Weight":
            p0 = [np.median(data_NN)/x_scale_factor,1,0.5]
        else:
            p0 = [np.median(data_NN)/x_scale_factor,1] # this is initial guess for sigmoid parameters
        
        popt, _ = curve_fit(f=func, xdata=x/x_scale_factor, ydata=y, p0=p0,method='lm')

        # parameters yielded by Curve_fit: x0, k
        #print("curve_fit parameter on "+str(func)[9:-22]+": ", popt)
        return popt
    
    def data_binning(self, data):
    
        x = np.sort(data) 
        N = len(x)                   # e.g N = 500, sqrt(500)=22.3
        lower = int(np.floor(np.sqrt(N))) # 22
        upper = int(np.ceil(np.sqrt(N)))  # 23 as total #of bin
        
        if lower*upper >= N:
            small_bin_num = int(lower*upper - N)  # 22*23 - 500 = 6
            small_bin_size = int(lower - 1)  # 21
            large_bin_size = lower
        else: # HGG -> sqrt(252) = 15.8
            small_bin_num = int(upper**2 - N) # 16*16-252 =4
            small_bin_size = lower  # 15
            large_bin_size = upper
        
        large_bin_num = int(upper - small_bin_num) # 23-6 = 17

        # small_bin_size*small_bin_num + lower*large_bin_num = N

        bin_count = [large_bin_size]*large_bin_num + [small_bin_size]*small_bin_num  # [22..*17, 21..*6,]
        #print("items in each bin: ", bin_count)
        binned_data = []
        i = 0
        for count in bin_count:
            binned_data.append(np.mean(x[i:i+count]))
            i += count
        
        return binned_data


    def binning_xy(self, binned_data):
        x = np.concatenate(([0],binned_data))
        y = np.zeros((x.shape))
        
        for i in range(1,len(x)):
            y[i] = i/len(x)
            
        return x,y
    
    
    def sigmoids_for_class(self, data, name, factor, func_list, binning=False): #removed color list here
        if binning:
            x,y = self.binning_xy(self.data_binning(data))
        else:
            x,y = self.empirical_CDF(data, name)
        
        # axis[0] = 1-y = p_value (on log space)
        # axis[1] = y = CDF
        # f,ax = plt.subplots(1,2,figsize=(16,6))
        # ax[0].set_title('1-y(p_value) of '+name)
        # ax[0].set_yscale('log')
        # ax[0].scatter(x,1-y, color='b',s=10)
        
        # ax[1].set_title('y of '+name)
        # ax[1].scatter(x,y, color='b',s=10)
        
        # print("For ",name," :")
        for i in range(len(func_list)):
            try:
                if i == 7:
                    p = self.auto_curve_fit(data,x,y,factor,func_list[i],s=y,p_control="Gompertz")
                elif i == 6:
                    p = self.auto_curve_fit(data,x,y,factor,func_list[i],s=y,p_control="Weight")
                else:
                    p = self.auto_curve_fit(data,x,y,factor,func_list[i],s=y)
            except RuntimeError:
                print("error in ",str(func_list[i])[9:-22])
                continue
            y2 = func_list[i](x/factor, *p)
            if func_list[i] == self.arctan_GD:
                self.arctan_popt[f"{name}"] = p
                # self.arctan_popt.append(self.arctan_GD)
            if func_list[i] == self.logistic:
                self.logistic_popt[f"{name}"] = p
                # self.logistic_popt.append(self.logistic)
            if func_list[i] == self.tanh:
                self.tanh_popt[f"{name}"] = p
                # self.tanh_popt.append(self.tanh)
            if func_list[i] == self.arctan:
                self.arc_popt[f"{name}"] = p
                # self.arc_popt.append(self.arctan)
            if func_list[i] == self.GD:
                self.gd_popt[f"{name}"] = p
                # self.gd_popt.append(self.GD)
            if func_list[i] == self.ERF:
                self.ERF_popt[f"{name}"] = p
                # self.ERF_popt.append(self.ERF)
            if func_list[i] == self.algebra:
                self.algebra_popt[f"{name}"] = p
                # self.algebra_popt.append(self.algebra)
            if func_list[i] == self.Gompertz:
                self.Gompertz_popt[f"{name}"] = p
                # self.Gompertz_popt.append(self.Gompertz)

            #ax[0].plot(x, 1-y2, color=color_list[i], label=str(func_list[i])[9:-22])
            # ax[1].plot(x, y2, color=color_list[i], label=str(func_list[i])[9:-22])
        
        # ax[0].legend(loc='lower left')
        # ax[1].legend(loc='lower left')
        # plt.show()


    def logistic(self, x,x0, k):
        m = (1/ (1 + np.exp(-k*(x-x0))))      
        return m

    def tanh(self, x, x0, k): 
        m = (1+np.tanh(k*(x-x0)))/2
        return m

    def arctan(self, x, x0, k):
        m = (1+(2/np.pi)*np.arctan(k*(x-x0)))/2
        return m

    def GD(self, x, x0, k):
        m = (1+(4/np.pi)*np.arctan(np.tanh(k*(x-x0))))/2
        return m

    def ERF(self, x, x0, k):
        m = (1+erf(k*(x-x0)))/2
        return m

    def algebra(self, x, x0, k):
        m = (1+x/((1+abs(x)**k)**(1/k)))/2
        return m

    def arctan_GD(self, x,x0,k, w):
        m = w*self.GD(x,x0,k)+(1-w)*self.arctan(x,x0,k)
        return m

    def Gompertz(self, x,b,c):
        m = np.e**(-np.e**(b-c*x))
        return m
    
    def euclid(self, origin, other):
        return np.sum((origin - other) ** 2)**(1/2)

    def NN_distance(self, ref_point, data):
        nearest_distance = 1e999
        for point in data:
            if self.euclid(ref_point, point) < nearest_distance: 
                nearest_distance = self.euclid(ref_point, point)
        return nearest_distance
    
    def getPvalue(self, if_binning=False):
        # df_comb = pd.DataFrame()
        # this_df = self.data
        # this_df["class"] = self.predicted_class
        # df_comb = pd.concat([this_df, df_comb])
        # this_origin = self.data_origin
        # this_origin["class"] = "Original"
        # df_comb = pd.concat([this_origin, df_comb])
        # print(df_comb.head)
        df_comb = self.combine_data([self.data, self.data_origin], [self.predicted_class, "Original"])
        df_class = df_comb['class']
        df_comb = df_comb.drop("class", axis = 1)
        # print(df_comb.head)
        df_comb = pd.DataFrame(MinMaxScaler().fit_transform(df_comb))
        df_comb['class'] = df_class.reset_index(drop = True)

        processed_data = self.data_distance(self.data_process(df_comb, self.predicted_class))
        # print(processed_data)

        if not np.any(processed_data):
            print(processed_data)
            return 0

        functions = [self.logistic, self.tanh, self.arctan, self.GD, self.ERF, self.algebra, self.arctan_GD, self.Gompertz]
        # processed_data = self.data_distance(self.data)
        original = df_comb[df_comb['class'] == 'Original']
        self.sigmoids_for_class(processed_data, self.predicted_class, np.mean(processed_data), functions, binning=if_binning)
        for target in self.arctan_popt:
            nearDis = self.NN_distance(original.drop(['class'], axis = 1).to_numpy(), df_comb[df_comb['class'] == f'{target}'].drop(['class'], axis = 1).to_numpy())
            arctan_GD_val = [self.arctan_GD(nearDis, *self.arctan_popt[f'{target}'])]
        
        for target in self.ERF_popt:
            nearDis = self.NN_distance(original.drop(['class'], axis = 1).to_numpy(), df_comb[df_comb['class'] == f'{target}'].drop(['class'], axis = 1).to_numpy())
            ERF_val = [self.ERF(nearDis, *self.ERF_popt[f'{target}'])]
        
        for target in self.arc_popt:
            nearDis = self.NN_distance(original.drop(['class'], axis = 1).to_numpy(), df_comb[df_comb['class'] == f'{target}'].drop(['class'], axis = 1).to_numpy())
            arctan_val = [self.arctan(nearDis, *self.arc_popt[f'{target}'])]
        
        for target in self.logistic_popt:
            nearDis = self.NN_distance(original.drop(['class'], axis = 1).to_numpy(), df_comb[df_comb['class'] == f'{target}'].drop(['class'], axis = 1).to_numpy())
            logistic_val = [self.logistic(nearDis, *self.logistic_popt[f'{target}'])]

        for target in self.tanh_popt:
            nearDis = self.NN_distance(original.drop(['class'], axis = 1).to_numpy(), df_comb[df_comb['class'] == f'{target}'].drop(['class'], axis = 1).to_numpy())
            tanh_val = [self.tanh(nearDis, *self.tanh_popt[f'{target}'])]

        for target in self.gd_popt:
            nearDis = self.NN_distance(original.drop(['class'], axis = 1).to_numpy(), df_comb[df_comb['class'] == f'{target}'].drop(['class'], axis = 1).to_numpy())
            GD_val = [self.GD(nearDis, *self.gd_popt[f'{target}'])]

        for target in self.algebra_popt:
            nearDis = self.NN_distance(original.drop(['class'], axis = 1).to_numpy(), df_comb[df_comb['class'] == f'{target}'].drop(['class'], axis = 1).to_numpy())
            algebra_val = [self.algebra(nearDis, *self.algebra_popt[f'{target}'])]

        for target in self.Gompertz_popt:
            nearDis = self.NN_distance(original.drop(['class'], axis = 1).to_numpy(), df_comb[df_comb['class'] == f'{target}'].drop(['class'], axis = 1).to_numpy())
            Gompertz_val = [self.Gompertz(nearDis, *self.Gompertz_popt[f'{target}'])]
        
        #outer_list = [arctan_GD_val, ERF_val, arctan_val, logistic_val, tanh_val, GD_val, algebra_val, Gompertz_val]
        # print(np.array(self.data_origin))
        use = np.delete(np.array(self.data_origin), -1, 1)
        # print(use.dtype)
        # print("\n")
        # print(np.array(arctan_GD_val[0]))
        dict = {}
        rmse1 = np.sqrt((np.mean(use - np.array(arctan_GD_val[0]))**2))
        dict[rmse1] = [arctan_GD_val[0], "using arctan_GD"]
        rmse2 = np.sqrt((np.mean(use - np.array(ERF_val[0]))**2))
        dict[rmse2] = [ERF_val[0], "using ERF"]
        rmse3 = np.sqrt((np.mean(use - np.array(arctan_val[0]))**2))
        dict[rmse3] = [arctan_val[0], "using arctan"]
        rmse4 = np.sqrt((np.mean(use - np.array(logistic_val[0]))**2))
        dict[rmse4] = [logistic_val[0], "using logistic"]
        rmse5 = np.sqrt((np.mean(use - np.array(tanh_val[0]))**2))
        dict[rmse5] = [tanh_val[0], "using tanh"]
        rmse6 = np.sqrt((np.mean(use - np.array(GD_val[0]))**2))
        dict[rmse6] = [GD_val[0], "using GD"]
        rmse7 = np.sqrt((np.mean(use - np.array(algebra_val[0]))**2))
        dict[rmse7] = [algebra_val[0], "using algebra"]
        rmse8 = np.sqrt((np.mean(use - np.array(Gompertz_val[0]))**2))
        dict[rmse8] = [Gompertz_val[0], "using Gompertz"]
        # lst = [rmse1, rmse2, rmse3, rmse4, rmse5, rmse6, rmse7, rmse8]
        res = 0
        keys = list(dict.keys())
        keys.sort()
        # print(keys)
        #return arctan_GD_val[0]
        for i in keys:
            # if dict[i] < 0:
            # print(dict[i])
            if dict[i][0] < 1:
                res = dict[i]
                # print(res)
                break
        return 1-res[0], res[1]



# if __name__ == "__main__":
    # test my function
    # classes = ['ER', 'ERDD', 'GEO', 'GEOGD', 'HGG', 'SF', 'SFDD', 'Sticky', 'Original']
    # classes_pred = ['ER', 'ERDD', 'GEO', 'GEOGD', 'HGG', 'SF', 'SFDD', 'Sticky']
    # #data_locations = [r"/content/drive/MyDrive/random stuff/Adaptable-Sigmoids/data/AT"+c for c in classes]
    # data_locations = [r"/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/AT"+c for c in classes]
    # #data_locations_CE = [r"/content/drive/MyDrive/random stuff/Adaptable-Sigmoids/data/CE"+c for c in classes]
    # data_locations_CE = [r"/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/CE"+c for c in classes]
    # #prediction_p_value = "/content/drive/MyDrive/random stuff/Adaptable-Sigmoids/data/ATOriginal"
    # prediction_p_value = "Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/ATOriginal"

    # print("test AT")
    # df = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/ATER", header = None, sep = ' ')
    # df_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/ATOriginal", header = None, sep = ' ')
    # test_ER = knn_distinguish(df, df_origin, "ER")
    # print(test_ER.getPvalue())
    # # print(test_ER.getPvalue(if_binning=True))

    # print("----------------------")

    # df1 = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/ATERDD", header = None, sep = ' ')
    # test_ERDD = knn_distinguish(df1, df_origin, "ERDD")
    # print(test_ERDD.getPvalue())
    # # print(test_ERDD.getPvalue(if_binning=True))

    # print("----------------------")

    # df2 = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/ATGEO", header = None, sep = ' ')
    # test_GEO = knn_distinguish(df2, df_origin, "GEO")
    # print(test_GEO.getPvalue())
    # # print(test_GEO.getPvalue(if_binning=True))

    # print("----------------------")
    # print("test CE")
    # df3 = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/CEER", header=None, sep=' ')
    # df3_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/CEOriginal", header=None, sep=' ')
    # test_3ER = knn_distinguish(df3, df3_origin, "ER")
    # print(test_3ER.getPvalue())
   
    # print("----------------------")
    # print("test DM")
    # df4 = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/DMERDD", header=None, sep=' ')
    # df4_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/DMOriginal", header=None, sep=' ')
    # test_4ERDD = knn_distinguish(df4, df4_origin, "ERDD")
    # print(test_4ERDD.getPvalue())

    # print("----------------------")
    # print("test EC")
    # df5 = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/ECHGG", header=None, sep=' ')
    # df5_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/ECOriginal", header=None, sep=' ')
    # test_5HGG = knn_distinguish(df5, df5_origin, "HGG")
    # print(test_5HGG.getPvalue())

    # print("----------------------")
    # print("test HS")
    # df6 = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/HSSticky", header=None, sep=' ')
    # df6_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/HSOriginal", header=None, sep=' ')
    # test_6sticky = knn_distinguish(df6, df6_origin, "Sticky")
    # print(test_6sticky.getPvalue())

    # print("----------------------")
    # print("test MM")
    # df7 = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/MMGEO", header=None, sep=' ')
    # df7_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/MMOriginal", header=None, sep=' ')
    # test_7sticky = knn_distinguish(df7, df7_origin, "GEO")
    # print(test_7sticky.getPvalue())

    # print("----------------------")
    # print("test RN")
    # df8 = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/RNSF", header=None, sep=' ')
    # df8_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/RNOriginal", header=None, sep=' ')
    # test_8sticky = knn_distinguish(df8, df8_origin, "SF")
    # print(test_8sticky.getPvalue())

    # print("-----------------")
    # classes = ['ER', 'ERDD', 'GEO', 'GEOGD', 'HGG', 'SF', 'SFDD', 'Sticky']
    # data_locations = [r"/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/AT"+c for c in classes]
    # df_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/ATOriginal", header=None, sep=' ')
    # for i, v in enumerate(data_locations):
    #     pd_i = pd.read_csv(v, header=None, sep=' ')
    #     print("testing AT" + classes[i])
    #     test_allAT = knn_distinguish(pd_i, df_origin, classes[i])
    #     # print("1")
    #     print(test_allAT.getPvalue())



    # print("-----------------")
    # classes = ['ER', 'ERDD', 'GEO', 'GEOGD', 'HGG', 'SF', 'SFDD', 'Sticky']
    # data_locations = [r"/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/CE"+c for c in classes]
    # df_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/CEOriginal", header=None, sep=' ')
    # for i, v in enumerate(data_locations):
    #     pd_i = pd.read_csv(v, header=None, sep=' ')
    #     print("testing CE" + classes[i])
    #     test_allCE = knn_distinguish(pd_i, df_origin, classes[i])
    #     # print("1")
    #     print(test_allCE.getPvalue())


    # print("-----------------")
    # classes = ['ER', 'ERDD', 'GEO', 'GEOGD', 'HGG', 'SF', 'SFDD', 'Sticky']
    # data_locations = [r"/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/DM"+c for c in classes]
    # df_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/DMOriginal", header=None, sep=' ')
    # for i, v in enumerate(data_locations):
    #     pd_i = pd.read_csv(v, header=None, sep=' ')
    #     print("testing DM" + classes[i])
    #     test_allDM = knn_distinguish(pd_i, df_origin, classes[i])
    #     # print("1")
    #     print(test_allDM.getPvalue())

    # print("-----------------")
    # classes = ['ER', 'ERDD', 'GEO', 'GEOGD', 'HGG', 'SF', 'SFDD', 'Sticky']
    # data_locations = [r"/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/EC"+c for c in classes]
    # df_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/ECOriginal", header=None, sep=' ')
    # for i, v in enumerate(data_locations):
    #     pd_i = pd.read_csv(v, header=None, sep=' ')
    #     print("testing EC" + classes[i])
    #     test_allEC = knn_distinguish(pd_i, df_origin, classes[i])
    #     # print("1")
    #     # if i == 4:
    #     print(test_allEC.getPvalue())


    # print("-----------------")
    # classes = ['ER', 'ERDD', 'GEO', 'GEOGD', 'HGG', 'SF', 'SFDD', 'Sticky']
    # data_locations = [r"/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/HS"+c for c in classes]
    # df_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/HSOriginal", header=None, sep=' ')
    # for i, v in enumerate(data_locations):
    #     pd_i = pd.read_csv(v, header=None, sep=' ')
    #     print("testing HS" + classes[i])
    #     test_allHS = knn_distinguish(pd_i, df_origin, classes[i])
    #     # print("1")
    #     print(test_allHS.getPvalue())

    
    # print("-----------------")
    # classes = ['ER', 'ERDD', 'GEO', 'GEOGD', 'HGG', 'SF', 'SFDD', 'Sticky']
    # data_locations = [r"/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/MM"+c for c in classes]
    # df_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/MMOriginal", header=None, sep=' ')
    # for i, v in enumerate(data_locations):
    #     pd_i = pd.read_csv(v, header=None, sep=' ')
    #     print("testing MM" + classes[i])
    #     test_allMM = knn_distinguish(pd_i, df_origin, classes[i])
    #     # print("1")
    #     print(test_allMM.getPvalue())


    # print("-----------------")
    # classes = ['ER', 'ERDD', 'GEO', 'GEOGD', 'HGG', 'SF', 'SFDD', 'Sticky']
    # data_locations = [r"/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/RN"+c for c in classes]
    # df_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/RNOriginal", header=None, sep=' ')
    # for i, v in enumerate(data_locations):
    #     pd_i = pd.read_csv(v, header=None, sep=' ')
    #     print("testing RN" + classes[i])
    #     test_allRN = knn_distinguish(pd_i, df_origin, classes[i])
    #     # print("1")
    #     print(test_allRN.getPvalue())

    
    # print("-----------------")
    # classes = ['ER', 'ERDD', 'GEO', 'GEOGD', 'HGG', 'SF', 'SFDD', 'Sticky']
    # data_locations = [r"/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/SC"+c for c in classes]
    # df_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/SCOriginal", header=None, sep=' ')
    # for i, v in enumerate(data_locations):
    #     pd_i = pd.read_csv(v, header=None, sep=' ')
    #     print("testing SC" + classes[i])
    #     test_allSC = knn_distinguish(pd_i, df_origin, classes[i])
    #     # print("1")
    #     print(test_allSC.getPvalue())

    
    # print("-----------------")
    # classes = ['ER', 'ERDD', 'GEO', 'GEOGD', 'HGG', 'SF', 'SFDD', 'Sticky']
    # data_locations = [r"/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/SP"+c for c in classes]
    # df_origin = pd.read_csv("/Users/lizongli/Desktop/knn research/Adaptable-Sigmoids/data/SPOriginal", header=None, sep=' ')
    # for i, v in enumerate(data_locations):
    #     pd_i = pd.read_csv(v, header=None, sep=' ')
    #     print("testing SP" + classes[i])
    #     test_allSP = knn_distinguish(pd_i, df_origin, classes[i])
    #     # print("1")
    #     print(test_allSP.getPvalue())






