# Recommendation_System-PyTorch
Prodcution-level implementations of recommender system Full Pytorch Implementation

#### Title
Implementations of various recommender systems in PyTorch

#### Data
- MovieLens Data 100k & 1M ([download](https://grouplens.org/datasets/movielens/))
- Data files are in "data" folder

#### Recommendation-System Common Architecture
![image](./img/PersonalizedRecoSystems.png)

## Model Zoo
| Model    | Paper                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------|
| BPRMF            | Steffen Rendle et al., BPR: Bayesian Personalized Ranking from Implicit Feedback. UAI 2009. [Link](https://arxiv.org/pdf/1205.2618) |
| ItemKNN          | Jun Wang et al., Unifying user-based and item-based collaborative filtering approaches by similarity fusion. SIGIR 2006. [Link](http://web4.cs.ucl.ac.uk/staff/jun.wang/papers/2006-sigir06-unifycf.pdf) |
| SLIM             | Xia Ning et al., SLIM: Sparse Linear Methods for Top-N Recommender Systems. ICDM 2011. [Link](http://glaros.dtc.umn.edu/gkhome/fetch/papers/SLIM2011icdm.pdf) |
| MultVAE          | Dawen Liang et al., Variational Autoencoders for Collaborative Filtering. WWW 2018. [Link](https://arxiv.org/pdf/1802.05814) |


## How to run
1. Choose RecSys model and edit configurations in main.py
2. Edit configurations of the model you choose in 'conf'
3. run 'main.py'

## Implement your own model
You can add your own model into the framework if:

1. Your model inherits 'BaseModel' class in 'models/BaseModel.py'
2. Implement necessary methods and add additional methods if you want.
3. Make 'YourModel.conf' file in 'conf'
4. Add your model in 'utils.ModelBuilder.py'

# Reference
- Facebook Group [Link](https://www.facebook.com/groups/2611614312273351)
- Facebook Group [Link](https://www.facebook.com/groups/PyTorchKR)
- Recommendation in Pytorch [github](https://github.com/yoongi0428/RecSys_PyTorch/blob/master/README.md)
- RecSys 2019 [github](https://github.com/MaurizioFD/RecSys2019_DeepLearning_Evaluation)
- NeuRec [github](https://github.com/wubinzzu/NeuRec)
