#!/usr/bin/env python3

### Data Loader file for Myo Armband Gesture Data - Edited By Allan Garcia


import torch
from torch.utils import data
import numpy as np
from scipy.io import loadmat
from statistics import mode
import csv
import argparse, sys
import json




class SEMG_Dataset(data.Dataset):
    '''Custom pytorch dataset class, used to iterate through dataset when used with DataLoaders'''
    def __init__(self,path,mode,fold):
        '''ARGS: path: dir/file of dataset to load
                 mode: Set to create datasets for training, validation, and testing
                 fold: only used for k fold testing, sets current fold out of set number of folds'''
        all_data = np.load(path+'.npy',allow_pickle='True').item()
        if len(all_data) == 3:
            self.data = all_data[mode]
        else:
            num_folds = 5
            rng = int(len(all_data['train'])/num_folds)
            self.val_data = all_data['train'][rng*fold:rng*(fold+1)]
            self.train_data = all_data['train']
            del self.train_data[rng*fold:rng*(fold+1)]
            self.test_data = all_data['test']

            if mode == 'train':
                self.data = self.train_data[:]
            elif mode == 'test':
                self.data = self.test_data[:]
            elif mode == 'val':
                self.data = self.val_data[:]

    def __len__(self):
        '''Returns length of the data set'''
        return len(self.data)


    def __getitem__(self,index):
        '''Iterater that pulls a sample from the dataset. Behavior (random, in order) depends on DataLoader
        ARGS: index: provided by DataLoader to pull a sample'''
        samp = torch.from_numpy(self.data[index][0]).float()
        label = torch.from_numpy(self.data[index][1])
        samp = samp.view(1,samp.shape[0],samp.shape[1])
        return samp, label


class GenData():
    def __init__(self,exercises=None, gestures=None):
        self.exercises = exercises
        self.gestures = gestures
        self.remapped_gestures = []


    def window_data(self,data_array,labels,save_path,label_map,normalize=True):
        '''Takes emg data and splits it into windowed samples.
        ARGS: data_array: emg data
            labels: class labels for data_array
            save_path: dir/file to save windowed data
            label_map: list of tuples containing int class number and corresponding list with zeros and a 1 designating the correct class (Ex:with 5 classes total, [(0,[1,0,0,0,0]),(1, [0,1,0,0,0]), etc..])
            normalize: (default=True) Normalize data'''

        ## Initialize sampling parameters
        ## Want a 260ms window (52 samples) of all eight channels as inputs with 235ms overlap (from paper)
        window_size = 52 #samples, 260ms
        overlap = 47 #sample, 235ms
        step = window_size - overlap
        i = 0
        data = {'train':[],'val':[],'test':[]}
        mean_emg = np.mean(data_array)
        std_emg = np.std(data_array)

        f = open(save_path+'_stats.txt','w')
        f.write('{},'.format(mean_emg))
        f.write('{}'.format(std_emg))

        ## Sort and label it for training/validation
        while i < len(data_array)-window_size:
            # Split all data into either training(80%), validation(10%), or testing(10%)
            if np.random.randint(1,11) < 9:
                if np.random.randint(1,11) < 9:
                    set = 'train'
                else:
                    set = 'val'
            else:
                set = 'test'
            try:
                label = mode(list(labels[i:i+window_size]))
            except:
                i += step
                continue
            ## Normalize Data
            emg_win = data_array[i:i+window_size,:8]
            if normalize:
                emg_win = (emg_win - mean_emg)/(std_emg)

            if label == 0:
                if np.random.randint(10) == 1: #only save about 10th of the rest states
                    data[set].append([emg_win,np.array([1,0,0,0,0,0,0])])
            else:
                for act, new in label_map:
                    if label == act:
                        data[set].append([emg_win,new])
            i += step
    
        np.save(save_path+".npy",data)


    def checkDuplicates(self,val,dup_list, prev,new):
  
        if val in dup_list:
            if prev!= val and prev!=0:
                new+=1
                # dup_list.pop(0)
            prev=val
        return new, prev


    def genFromTwo(self):

        keys=self.exercises
        vals=self.gestures

        x = loadmat('ninapro_data/s1/S1_'+keys[0]+'_A1.mat') #Exercise 1. 12 hand gestures included gestures of interest, USING E3 NOW FOR GRASPS
        x['emg'][0] = 0
        x['restimulus'][0] = 0
        emg_data=x['emg'][0] #first 8 columns are from myo closest to elbow, next 8 are from second myo rotated 22 degs
        restim = x['restimulus'][0] #restimulus and rerepetition are the corrected indexes for the movements
        val_set0=set(vals[0])
        val_set1=set(vals[1])

        for i in range(1,11):
            # print('Starting file: S'+str(i)+'_'+keys[0]+'_A1.mat')
            print('Starting files for sample S'+str(i)+'')
            x = loadmat('ninapro_data/s'+str(i)+'/S'+str(i)+'_'+keys[0]+'_A1.mat') #Exercise 1. 12 hand gestures included gestures of interest, USING E3 NOW FOR GRASPS
        
            emg_data = np.vstack((emg_data,x['emg']))
            restim = np.vstack((restim,x['restimulus']))

            y = loadmat('ninapro_data/s'+str(i)+'/S'+str(i)+'_'+keys[1]+'_A1.mat')
            # print('S'+str(i)+'_'+keys[1]+'_A1.mat')
            e2 = y['emg']
            e2_res = y['restimulus']
    

            duplicates = [e for i, e in enumerate(val_set1) if e in np.unique(x['restimulus'])]
            prev_val=0
            new_val = 30
            
            prev_label=0
            for j, e in enumerate(e2_res.flatten()):
                if e in val_set1:
                    emg_data = np.vstack((emg_data,e2[j]))
                    if len(duplicates)>0:
                        new_val, prev_val= self.checkDuplicates(e2_res[j],duplicates,prev_val, new_val)
                        restim = np.vstack((restim,new_val))
                    else:
                        restim = np.vstack((restim,e2_res[j]))

                if i == 2:
                    if new_val!=prev_label:
                        self.remapped_gestures.append(new_val)
                        prev_label = new_val

            print("Finished files for S"+str(i)+ "\n")

        print("Writing Files to CSV.. \n")
        if len(duplicates)>0:
            for index,k in enumerate(duplicates):
                print("Found duplicate gesture values across exercises - remapped exercise {} gesture number {} to {}".format(str(key_list[1]),k,self.remapped_gestures[index]))
        all_emg_path = 'nina_data/combined_emg_data_argtest1.csv'
        all_ges_path = 'nina_data/combined_gest_data_argtest1.csv'
        with open(all_emg_path,mode='w') as comb_emg, open(all_ges_path,mode='w') as comb_ges:
            emg_writer = csv.writer(comb_emg, delimiter=',')
            emg_gesture_writer = csv.writer(comb_ges, delimiter=',')
            for row in emg_data:
                emg_writer.writerow(row)

            for row in restim:
                emg_gesture_writer.writerow(row)

        print("Finished Writing to CSV")

    def createLabelMap(self):
        vals=self.gestures
        label_map=[]
        all_vals  = vals[0] + self.remapped_gestures
        gesture_list = np.unique(all_vals)
     
        for index,label in enumerate(gesture_list):
            remap= np.zeros(len(all_vals)+1, dtype=int)
            remap[index+1]+=1
            if index>0:
                remap[index-1] =0 
            label_pair = (label, remap)
            label_map.append(label_pair)
           
        print("Generated Label Map: \n" ,label_map)
            
        return label_map




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gen_data','-g',help='((True or true or t)/False) Generate dataset from raw data or calculate sampling stats of dataset')
    parser.add_argument('--window','-w',help='((True or true or t)/False) Set to true to sample existing dataset or false to generate dataset')
    parser.add_argument('--gest_dict', '-gestures', type=str)
    parser.add_argument('--csv_path', '-c', type=str)
    parser.add_argument('--npy_path', '-n', type=str)
     ### ./data_loader.py -g t -gestures '{"E1": [0,2,3], "E2": [4,5]}' ###
    args = parser.parse_args()
    data = json.loads(args.gest_dict)
    key_list = list(data.keys())
    val_list = list(data.values())

    generate_data=GenData(key_list,val_list)
    

    if args.gen_data == 'True' or args.gen_data == 'true' or args.gen_data == 't':
        gen_data = True
    else:
        gen_data = False

    if args.window == 'True' or args.window == 'true' or args.window == 't':
        win = True
    else:
        win = False


    if gen_data:
        if len(key_list) == 2:
            print("Generating data from two exercises")
            generate_data.genFromTwo()

        if win:
            emg_data = np.genfromtxt('nina_data/combined_emg_data_argtest1.csv',delimiter=',')
            restim = np.genfromtxt('nina_data/combined_gest_data_argtest1.csv',delimiter=',')
            path = 'nina_data/all_data_combined_argtest1' #### 2 is for new grasp data, 1 was with original finger gestures. 
            label_map = generate_data.createLabelMap()
            generate_data.window_data(np.abs(emg_data),restim,path,label_map,normalize=True)
    else:
        ## Test distribution of dataset
        path = "nina_data/all_data_combined"
        f = open(path+'.txt','w')
        modes = ['train','val','test']
        tot = []
        data_len = 0
        for phase in modes:
            dataset = SEMG_Dataset(path,phase,0)
            data_len += len(dataset)
            params = {'batch_size': 1000, 'shuffle': True,'num_workers': 4}
            train_loader = data.DataLoader(dataset, **params)
            test = [0,1,2,3,4,5,6]
            c1 = c2 = c3 = c4 = c5 = c6 = c7 = 0
            for input, label in train_loader:
                c1 += (torch.argmax(label,dim=1) == test[0]).sum().item()
                c2 += (torch.argmax(label,dim=1) == test[1]).sum().item()
                c3 += (torch.argmax(label,dim=1) == test[2]).sum().item()
                c4 += (torch.argmax(label,dim=1) == test[3]).sum().item()
                c5 += (torch.argmax(label,dim=1) == test[4]).sum().item()
                c6 += (torch.argmax(label,dim=1) == test[5]).sum().item()
                c7 += (torch.argmax(label,dim=1) == test[6]).sum().item()
            res = [c1,c2,c3,c4,c5,c6,c7]
            for c in test:
                print("Class {} has {} samples".format(c+1,res[c]))
                f.write("Class {} has {} samples\n".format(c+1,res[c]))
            tot.append(c1+c2+c3+c4+c5+c6+c7)

        print('Total training samples: {}, {:.4f}%'.format(tot[0],(tot[0]/data_len)*100))
        f.write('Total training samples: {}, {:.4f}%'.format(tot[0],(tot[0]/data_len)*100))
        print('Total testing samples: {}, {:.4f}%'.format(tot[2],(tot[2]/data_len)*100))
        f.write('Total testing samples: {}, {:.4f}%'.format(tot[2],(tot[2]/data_len)*100))
        f.close()
