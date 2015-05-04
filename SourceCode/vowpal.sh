#!/usr/bin/env bash
#All 23

vw train.vw -f avazu.model.vw --loss_function=logistic --hash strings -b 26 --learning_rate=0.6 --compressed --ftrl --ftrl_alpha=0.1 --ftrl_beta=1.0 --nn=10
vw test.vw -t -i avazu.model.vw -p avazu.preds.txt

#All 23
vw train.vw -f avazu.model.vw --loss_function logistic
vw test.vw -t -i avazu.model.vw -p avazu.preds.txt


vw testOriginal.vw -t -i ./train/avazu.model.vw -p ./test/avazu.predsfrills.txt

vw reducedTrain.vw -f ./train/avazu.modelreduced.vw --loss_function=logistic --hash strings -b 26 --learning_rate=0.6 --compressed --ftrl --ftrl_alpha=0.1 --ftrl_beta=1.0 --nn=10
vw test.vw -t -i avazu.modelreduced.vw -p avazu.predsreduced.txt