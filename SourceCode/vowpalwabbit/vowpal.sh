#!/usr/bin/env bash
#All 23

vw train.vw -f avazu.model.vw --loss_function=logistic --hash strings -b 26 --learning_rate=0.6 --compressed --ftrl --ftrl_alpha=0.1 --ftrl_beta=1.0 --nn=10
vw test.vw -t -i avazu.model.vw -p avazu.preds.txt

#All 23
vw train.vw -f avazu.model.vw --loss_function logistic
vw test.vw -t -i avazu.model.vw -p avazu.preds.txt


vw reducedTrain.vw -f ./train/avazu.modelreduced.vw --loss_function=logistic --hash strings -b 26 --learning_rate=0.6 --compressed --ftrl --ftrl_alpha=0.1 --ftrl_beta=1.0 --nn=10
vw reducedtest.vw -t -i ./train/avazu.modelreduced.vw -p ./test/avazu.predsreduced.txt

vw reducedTrain.vw -f ./train/avazu.modelnofrillsreduced.vw --loss_function logistic
vw reducedtest.vw -t -i ./train/avazu.modelnofrillsreduced.vw -p ./test/avazu.predsnofrillsreduced.txt

awk -F, 'NR > 1 {print ($2*2)-1, "|a", "a_"$4, "|b", "b_"$5, "|c", "c_"$6, "|d", "d_"$7, "|e", "e_"$8, "|f", "f_"$9, "|g", "g_"$10, "|h", "h_"$11, "|i", "i_"$12, "|j", "j_"$13, "|k", "k_"$14, "|l", "l_"$15, "|m", "m_"$16, "|n", "n_"$17, "|o", "o_"$18, "|p", "p_"$19, "|q", "q_"$20, "|r", "r_"$21, "|s", "s_"$22, "|t", "t_"$23, "|u", "u_"$24, "|v", "v_"substr($3, 7, 2)}' Data/train_clean.csv > Vowpal/train.vw

vw -d Vowpal/train.vw -f Vowpal/model_sub3.vw --loss_function logistic -l 0.07 -c -k --passes 4 -b 25 --holdout_after 32377421 --hash all --l1 1e-8 --l2 1e-8 -q d: -q f: -q bk --cubic bdk --cubic bfk --ignore l --ignore v


vw lesserTrain.vw -f ./train/avazu.modellesser.vw --loss_function=logistic --hash strings -b 26 --learning_rate=0.6 --compressed --ftrl --ftrl_alpha=0.1 --ftrl_beta=1.0 --nn=10
vw lessertest.vw -t -i ./train/avazu.modellesser.vw -p ./test/avazu.predsreduced.txt