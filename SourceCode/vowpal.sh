#All 23

vazu.model.vw --loss_function=logistic --hash strings -b 26 --learning_rate=0.6 --compressed --ftrl --ftrl_alpha=0.1 --ftrl_beta=1.0 --nn=10
vw test.vw -t -i avazu.model.vw -p avazu.preds.txt