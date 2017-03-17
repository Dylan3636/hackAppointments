def function train(X_train, y, day):
     vals = []
     for i in range(0, size(y_train, 0)):
        if (X_train.iloc[i, 3] == day and y_train.iloc[i] == y):
            vals.append(X_train.iloc[i, 1])

        mu = np.mean(vals)
        sig = np.cov(vals)
     return (mu, sig)