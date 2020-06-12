# Recommendation_System-PyTorch
Prodcution-level implementations of recommender system Full Pytorch Implementation

#### Title
Implementations of various recommender systems in PyTorch

## Data
- MovieLens Data 100k & 1M ([download](https://grouplens.org/datasets/movielens/))
- Data files are in "data" folder

#### Recommendation-System Common Architecture
![image](./img/PersonalizedRecoSystems.png)

## Model Zoo
| Model    | Paper                                                                         |
|------------------|-----------------------------------------------------------------------|
| BPRMF            | [Link](https://arxiv.org/pdf/1205.2618) |
| ItemKNN          | [Link](http://web4.cs.ucl.ac.uk/staff/jun.wang/papers/2006-sigir06-unifycf.pdf) |
| SLIM             | [Link](http://glaros.dtc.umn.edu/gkhome/fetch/papers/SLIM2011icdm.pdf) |
| MultVAE          | [Link](https://arxiv.org/pdf/1802.05814) |


## Training 
    $ python main.py 
                --model YOUR MODEL (default: SLIM)
                --data_dir [YOUR DIRECTORY]
                --save_dir [YOUR SAVE DIRECTORY]
                --conf_dir [YOUR CONFIGURATION DIRECTORY] \ (i.e. './drive/My Drive/Python/Recommendation_System-PyTorch/config' 
                --seed YOUR SEED 

## Create your own model
1. Create 'Yourmodel.py' that inherits 'BaseModel.py'
2. Create 'YourModel.json' file in 'config' folder
3. Implement necessary class and add additional methods if you want.
4. Add your model in 'ModelBuilder.py'
5. Run 'main.py' with edited parameters

## Reference
- Facebook Group [Link](https://www.facebook.com/groups/2611614312273351)
- Facebook Group [Link](https://www.facebook.com/groups/PyTorchKR)
- Recommendation in Pytorch [github](https://github.com/yoongi0428/RecSys_PyTorch/blob/master/README.md) - util.py / Tools.py
- RecSys 2019 [github](https://github.com/MaurizioFD/RecSys2019_DeepLearning_Evaluation) - util.py / Tools.py
- NeuRec [github](https://github.com/wubinzzu/NeuRec)
